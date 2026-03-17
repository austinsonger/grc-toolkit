#!/usr/bin/env python3
"""
AWS Evidence Collector for GRC/Compliance Audits
================================================
Collects compliance evidence from AWS accounts for SOC 2, ISO 27001, and FedRAMP audits.

Usage:
    python aws-evidence-collector.py --profile default --output ./evidence/output
    python aws-evidence-collector.py --regions us-east-1 us-west-2 --output ./evidence

Requirements:
    pip install boto3 botocore

Author: GRC-Toolkit Contributors
Version: 1.0.0
"""

import boto3
import json
import os
import sys
import argparse
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_boto3_session(profile: str, region: str) -> boto3.Session:
    """Create a boto3 session with the specified profile and region."""
    try:
        session = boto3.Session(profile_name=profile, region_name=region)
        # Validate credentials
        sts = session.client('sts')
        identity = sts.get_caller_identity()
        logger.info(f"Authenticated as: {identity['Arn']}")
        return session
    except Exception as e:
        logger.error(f"Failed to create AWS session: {e}")
        sys.exit(1)


def collect_iam_evidence(session: boto3.Session, output_dir: Path) -> Dict:
    """
    Collect IAM evidence for access control requirements.
    Maps to: NIST AC-2, AC-6, IA-2 | SOC 2 CC6.1, CC6.2, CC6.3 | ISO A.5.15-5.18
    """
    logger.info("Collecting IAM evidence...")
    iam = session.client('iam')
    evidence = {}

    # Password policy
    try:
        password_policy = iam.get_account_password_policy()['PasswordPolicy']
        evidence['password_policy'] = password_policy
        logger.info("✓ Collected password policy")
    except iam.exceptions.NoSuchEntityException:
        evidence['password_policy'] = {"error": "No password policy configured"}
        logger.warning("✗ No IAM password policy configured")

    # MFA summary
    try:
        users = []
        paginator = iam.get_paginator('list_users')
        for page in paginator.paginate():
            users.extend(page['Users'])

        mfa_summary = {
            'total_users': len(users),
            'users_with_mfa': 0,
            'users_without_mfa': [],
            'root_mfa_enabled': False
        }

        for user in users:
            mfa_devices = iam.list_mfa_devices(UserName=user['UserName'])['MFADevices']
            if mfa_devices:
                mfa_summary['users_with_mfa'] += 1
            else:
                # Check if user has console access
                try:
                    iam.get_login_profile(UserName=user['UserName'])
                    mfa_summary['users_without_mfa'].append(user['UserName'])
                except iam.exceptions.NoSuchEntityException:
                    pass  # No console access

        # Check root MFA
        account_summary = iam.get_account_summary()['SummaryMap']
        mfa_summary['root_mfa_enabled'] = bool(account_summary.get('AccountMFAEnabled', 0))

        evidence['mfa_summary'] = mfa_summary
        logger.info(f"✓ MFA: {mfa_summary['users_with_mfa']}/{mfa_summary['total_users']} users have MFA")
    except Exception as e:
        logger.error(f"Error collecting MFA data: {e}")

    # IAM roles with admin access
    try:
        admin_principals = []
        paginator = iam.get_paginator('list_policies')
        for page in paginator.paginate(Scope='Local'):
            for policy in page['Policies']:
                if 'admin' in policy['PolicyName'].lower():
                    entities = iam.list_entities_for_policy(PolicyArn=policy['Arn'])
                    admin_principals.append({
                        'policy': policy['PolicyName'],
                        'users': [u['UserName'] for u in entities.get('PolicyUsers', [])],
                        'roles': [r['RoleName'] for r in entities.get('PolicyRoles', [])],
                        'groups': [g['GroupName'] for g in entities.get('PolicyGroups', [])]
                    })
        evidence['admin_access'] = admin_principals
        logger.info("✓ Collected admin access information")
    except Exception as e:
        logger.error(f"Error collecting admin access: {e}")

    # Access keys age (for key rotation evidence)
    try:
        old_keys = []
        for user in users:
            keys = iam.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
            for key in keys:
                if key['Status'] == 'Active':
                    age_days = (datetime.now(timezone.utc) - key['CreateDate']).days
                    if age_days > 90:
                        old_keys.append({
                            'user': user['UserName'],
                            'key_id': key['AccessKeyId'][:8] + '...',
                            'age_days': age_days
                        })
        evidence['access_keys_over_90_days'] = old_keys
        logger.info(f"✓ Found {len(old_keys)} access keys older than 90 days")
    except Exception as e:
        logger.error(f"Error collecting access key ages: {e}")

    # Save evidence
    output_file = output_dir / 'iam-evidence.json'
    with open(output_file, 'w') as f:
        json.dump(evidence, f, indent=2, default=str)
    logger.info(f"IAM evidence saved to {output_file}")

    return evidence


def collect_cloudtrail_evidence(session: boto3.Session, output_dir: Path, region: str) -> Dict:
    """
    Collect CloudTrail configuration evidence.
    Maps to: NIST AU-2, AU-3, AU-12 | SOC 2 CC7.2 | ISO A.8.15
    """
    logger.info("Collecting CloudTrail evidence...")
    ct = session.client('cloudtrail', region_name=region)
    evidence = {}

    try:
        trails = ct.describe_trails(includeShadowTrails=False)['trailList']
        trail_details = []

        for trail in trails:
            status = ct.get_trail_status(Name=trail['TrailARN'])
            trail_info = {
                'name': trail['Name'],
                'is_multi_region': trail.get('IsMultiRegionTrail', False),
                'is_logging': status.get('IsLogging', False),
                'include_management_events': True,
                'log_file_validation_enabled': trail.get('LogFileValidationEnabled', False),
                's3_bucket': trail.get('S3BucketName', 'N/A'),
                'cloudwatch_logs_enabled': bool(trail.get('CloudWatchLogsLogGroupArn')),
                'kms_key_id': trail.get('KMSKeyId', 'Not encrypted')
            }

            # Get event selectors
            try:
                selectors = ct.get_event_selectors(TrailName=trail['TrailARN'])
                trail_info['event_selectors'] = selectors.get('EventSelectors', [])
            except Exception:
                pass

            trail_details.append(trail_info)

        evidence['trails'] = trail_details
        evidence['trail_count'] = len(trails)
        evidence['multi_region_trails'] = sum(1 for t in trail_details if t['is_multi_region'])
        evidence['all_trails_logging'] = all(t['is_logging'] for t in trail_details)

        logger.info(f"✓ Found {len(trails)} CloudTrail trail(s)")
    except Exception as e:
        logger.error(f"Error collecting CloudTrail evidence: {e}")
        evidence['error'] = str(e)

    output_file = output_dir / 'cloudtrail-evidence.json'
    with open(output_file, 'w') as f:
        json.dump(evidence, f, indent=2, default=str)
    logger.info(f"CloudTrail evidence saved to {output_file}")

    return evidence


def collect_s3_security_evidence(session: boto3.Session, output_dir: Path) -> Dict:
    """
    Collect S3 security configuration evidence.
    Maps to: NIST SC-28, AC-3 | SOC 2 CC6.1, CC6.7 | ISO A.8.24
    """
    logger.info("Collecting S3 security evidence...")
    s3 = session.client('s3')
    evidence = {'buckets': []}

    try:
        buckets = s3.list_buckets()['Buckets']

        for bucket in buckets:
            bucket_name = bucket['Name']
            bucket_info = {
                'name': bucket_name,
                'public_access_blocked': False,
                'versioning_enabled': False,
                'encryption_enabled': False,
                'encryption_type': None,
                'logging_enabled': False,
                'mfa_delete_enabled': False
            }

            # Public access block
            try:
                pab = s3.get_public_access_block(Bucket=bucket_name)['PublicAccessBlockConfiguration']
                bucket_info['public_access_blocked'] = all([
                    pab.get('BlockPublicAcls', False),
                    pab.get('IgnorePublicAcls', False),
                    pab.get('BlockPublicPolicy', False),
                    pab.get('RestrictPublicBuckets', False)
                ])
            except Exception:
                bucket_info['public_access_blocked'] = False

            # Versioning
            try:
                versioning = s3.get_bucket_versioning(Bucket=bucket_name)
                bucket_info['versioning_enabled'] = versioning.get('Status') == 'Enabled'
                bucket_info['mfa_delete_enabled'] = versioning.get('MFADelete') == 'Enabled'
            except Exception:
                pass

            # Encryption
            try:
                encryption = s3.get_bucket_encryption(Bucket=bucket_name)
                rules = encryption['ServerSideEncryptionConfiguration']['Rules']
                bucket_info['encryption_enabled'] = True
                bucket_info['encryption_type'] = rules[0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
            except s3.exceptions.ClientError:
                bucket_info['encryption_enabled'] = False

            # Logging
            try:
                logging_config = s3.get_bucket_logging(Bucket=bucket_name)
                bucket_info['logging_enabled'] = 'LoggingEnabled' in logging_config
            except Exception:
                pass

            evidence['buckets'].append(bucket_info)

        # Summary
        evidence['summary'] = {
            'total_buckets': len(buckets),
            'public_access_blocked': sum(1 for b in evidence['buckets'] if b['public_access_blocked']),
            'encrypted': sum(1 for b in evidence['buckets'] if b['encryption_enabled']),
            'versioning_enabled': sum(1 for b in evidence['buckets'] if b['versioning_enabled']),
            'logging_enabled': sum(1 for b in evidence['buckets'] if b['logging_enabled'])
        }

        logger.info(f"✓ Assessed {len(buckets)} S3 buckets")
    except Exception as e:
        logger.error(f"Error collecting S3 evidence: {e}")
        evidence['error'] = str(e)

    output_file = output_dir / 's3-security-evidence.json'
    with open(output_file, 'w') as f:
        json.dump(evidence, f, indent=2, default=str)
    logger.info(f"S3 evidence saved to {output_file}")

    return evidence


def collect_guardduty_evidence(session: boto3.Session, output_dir: Path, region: str) -> Dict:
    """
    Collect GuardDuty configuration and findings evidence.
    Maps to: NIST SI-4, IR-5 | SOC 2 CC7.2, CC7.3 | ISO A.8.16
    """
    logger.info("Collecting GuardDuty evidence...")
    gd = session.client('guardduty', region_name=region)
    evidence = {}

    try:
        detectors = gd.list_detectors()['DetectorIds']

        if not detectors:
            evidence['enabled'] = False
            evidence['message'] = 'GuardDuty not enabled in this region'
            logger.warning("✗ GuardDuty not enabled")
        else:
            detector_id = detectors[0]
            detector = gd.get_detector(DetectorId=detector_id)

            evidence['enabled'] = True
            evidence['detector_id'] = detector_id
            evidence['status'] = detector['Status']
            evidence['finding_publishing_frequency'] = detector.get('FindingPublishingFrequency', 'N/A')

            # Get high/critical findings count
            findings = gd.list_findings(
                DetectorId=detector_id,
                FindingCriteria={
                    'Criterion': {
                        'severity': {'Gte': 7}  # High and critical only
                    }
                }
            )
            evidence['high_critical_findings_count'] = len(findings.get('FindingIds', []))
            logger.info(f"✓ GuardDuty enabled, {evidence['high_critical_findings_count']} high/critical findings")

    except Exception as e:
        logger.error(f"Error collecting GuardDuty evidence: {e}")
        evidence['error'] = str(e)

    output_file = output_dir / 'guardduty-evidence.json'
    with open(output_file, 'w') as f:
        json.dump(evidence, f, indent=2, default=str)
    logger.info(f"GuardDuty evidence saved to {output_file}")

    return evidence


def generate_summary_report(evidence_results: Dict, output_dir: Path, account_id: str):
    """Generate a summary compliance report from collected evidence."""
    report = {
        'report_metadata': {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'aws_account_id': account_id,
            'report_type': 'AWS Compliance Evidence Summary'
        },
        'compliance_checks': [],
        'overall_score': 0
    }

    checks = []

    # IAM checks
    iam = evidence_results.get('iam', {})
    if iam:
        pp = iam.get('password_policy', {})
        checks.append({
            'check': 'IAM Password Policy Configured',
            'status': 'PASS' if 'error' not in pp else 'FAIL',
            'framework_mapping': 'NIST IA-5 | SOC2 CC6.1 | ISO A.5.17',
            'details': f"Min length: {pp.get('MinimumPasswordLength', 'N/A')}"
        })

        mfa = iam.get('mfa_summary', {})
        mfa_rate = mfa.get('users_with_mfa', 0) / max(mfa.get('total_users', 1), 1) * 100
        checks.append({
            'check': 'MFA Enabled for All Console Users',
            'status': 'PASS' if not mfa.get('users_without_mfa') else 'FAIL',
            'framework_mapping': 'NIST IA-2(1) | SOC2 CC6.1 | ISO A.8.5',
            'details': f"{mfa.get('users_with_mfa', 0)}/{mfa.get('total_users', 0)} users ({mfa_rate:.1f}%)"
        })

        checks.append({
            'check': 'Root Account MFA Enabled',
            'status': 'PASS' if mfa.get('root_mfa_enabled') else 'FAIL',
            'framework_mapping': 'NIST IA-2(1) | SOC2 CC6.1 | CIS 1.5',
            'details': 'Root MFA: ' + ('Enabled' if mfa.get('root_mfa_enabled') else 'DISABLED - CRITICAL')
        })

    # CloudTrail checks
    ct = evidence_results.get('cloudtrail', {})
    if ct:
        checks.append({
            'check': 'CloudTrail Multi-Region Logging Enabled',
            'status': 'PASS' if ct.get('multi_region_trails', 0) > 0 else 'FAIL',
            'framework_mapping': 'NIST AU-2, AU-12 | SOC2 CC7.2 | ISO A.8.15',
            'details': f"{ct.get('trail_count', 0)} trails, {ct.get('multi_region_trails', 0)} multi-region"
        })

    # S3 checks
    s3 = evidence_results.get('s3', {})
    if s3:
        summary = s3.get('summary', {})
        total = max(summary.get('total_buckets', 1), 1)
        checks.append({
            'check': 'S3 Public Access Blocked on All Buckets',
            'status': 'PASS' if summary.get('public_access_blocked', 0) == total else 'FAIL',
            'framework_mapping': 'NIST SC-7, AC-3 | SOC2 CC6.1 | ISO A.8.20',
            'details': f"{summary.get('public_access_blocked', 0)}/{total} buckets have public access blocked"
        })

        checks.append({
            'check': 'S3 Server-Side Encryption Enabled',
            'status': 'PASS' if summary.get('encrypted', 0) == total else 'FAIL',
            'framework_mapping': 'NIST SC-28 | SOC2 CC6.7 | ISO A.8.24',
            'details': f"{summary.get('encrypted', 0)}/{total} buckets encrypted"
        })

    report['compliance_checks'] = checks
    passing = sum(1 for c in checks if c['status'] == 'PASS')
    report['overall_score'] = f"{passing}/{len(checks)} checks passing ({passing/max(len(checks),1)*100:.1f}%)"

    output_file = output_dir / 'compliance-summary-report.json'
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)

    # Print summary to console
    print("\n" + "="*60)
    print("AWS COMPLIANCE EVIDENCE SUMMARY")
    print("="*60)
    print(f"Account: {account_id}")
    print(f"Generated: {report['report_metadata']['generated_at']}")
    print(f"Overall Score: {report['overall_score']}")
    print("-"*60)
    for check in checks:
        status_icon = "✅" if check['status'] == 'PASS' else "❌"
        print(f"{status_icon} {check['check']}")
        print(f"   {check['details']}")
        print(f"   Controls: {check['framework_mapping']}")
    print("="*60)
    print(f"Full evidence saved to: {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description='Collect AWS compliance evidence for GRC audits'
    )
    parser.add_argument('--profile', default='default', help='AWS profile name')
    parser.add_argument('--region', default='us-east-1', help='Primary AWS region')
    parser.add_argument('--output', default='./evidence/aws', help='Output directory for evidence')
    args = parser.parse_args()

    # Create output directory
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    run_dir = output_dir / f'run_{timestamp}'
    run_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Starting AWS evidence collection - output: {run_dir}")

    # Initialize session
    session = get_boto3_session(args.profile, args.region)
    sts = session.client('sts')
    account_id = sts.get_caller_identity()['Account']

    # Collect evidence
    evidence_results = {}
    evidence_results['iam'] = collect_iam_evidence(session, run_dir)
    evidence_results['cloudtrail'] = collect_cloudtrail_evidence(session, run_dir, args.region)
    evidence_results['s3'] = collect_s3_security_evidence(session, run_dir)
    evidence_results['guardduty'] = collect_guardduty_evidence(session, run_dir, args.region)

    # Generate summary
    generate_summary_report(evidence_results, run_dir, account_id)

    logger.info("Evidence collection complete!")


if __name__ == '__main__':
    main()
