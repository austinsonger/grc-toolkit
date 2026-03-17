# AWS Implementation Guide: Logging (AU Controls)

**Topic**: Audit Logging Implementation on AWS  
**Control Coverage**: NIST AU-2, AU-3, AU-6, AU-9, AU-11, AU-12  
**SOC 2 Coverage**: CC7.2, CC4.1  
**ISO 27001**: A.8.15, A.8.16, A.8.17  
**Last Updated**: 2024-01

---

## Overview

This guide covers implementing comprehensive audit logging on AWS to satisfy AU family controls from NIST SP 800-53 and equivalent requirements in SOC 2 and ISO 27001.

## Step 1: Enable AWS CloudTrail (AU-2, AU-12)

### Minimum Requirements
- Multi-region trail enabled
- Management events (read/write) logged
- S3 data events logged for sensitive buckets
- Log file validation enabled

### AWS CLI
```bash
aws s3 mb s3://cloudtrail-logs-$(aws sts get-caller-identity --query Account --output text)

aws s3api put-bucket-versioning \
  --bucket cloudtrail-logs-ACCOUNT_ID \
  --versioning-configuration Status=Enabled

aws cloudtrail create-trail \
  --name org-compliance-trail \
  --s3-bucket-name cloudtrail-logs-ACCOUNT_ID \
  --is-multi-region-trail \
  --enable-log-file-validation \
  --include-global-service-events

aws cloudtrail start-logging --name org-compliance-trail

aws cloudtrail put-event-selectors \
  --trail-name org-compliance-trail \
  --event-selectors '[{
    "ReadWriteType": "All",
    "IncludeManagementEvents": true,
    "DataResources": [
      {"Type": "AWS::S3::Object", "Values": ["arn:aws:s3:::"]},
      {"Type": "AWS::Lambda::Function", "Values": ["arn:aws:lambda"]}
    ]
  }]'
```

## Step 2: Configure VPC Flow Logs (AU-2, SC-7)

```bash
aws ec2 create-flow-logs \
  --resource-type VPC \
  --resource-ids vpc-XXXXXXXX \
  --traffic-type ALL \
  --log-destination-type cloud-watch-logs \
  --log-group-name /aws/vpc/flowlogs \
  --deliver-logs-permission-arn arn:aws:iam::ACCOUNT_ID:role/flowlogs-role
```

## Step 3: Enable AWS Config (CM-8, CM-6)

```bash
aws configservice put-configuration-recorder \
  --configuration-recorder name=default,roleARN=arn:aws:iam::ACCOUNT_ID:role/config-role \
  --recording-group allSupported=true,includeGlobalResourceTypes=true

aws configservice put-delivery-channel \
  --delivery-channel name=default,s3BucketName=aws-config-ACCOUNT_ID

aws configservice start-configuration-recorder --configuration-recorder-name default
```

## Step 4: Set Up Security Hub (SI-4, AU-6)

```bash
aws securityhub enable-security-hub

aws securityhub batch-enable-standards \
  --standards-subscription-requests '[{
    "StandardsArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.4.0"
  }]'
```

## Step 5: Log Retention Configuration (AU-11)

| Framework | Retention Required | AWS Implementation |
|---|---|---|
| FedRAMP Moderate | 90 days online + 1 year | S3 lifecycle: 90d → Glacier |
| HIPAA | 6 years | S3 lifecycle: 1y → Glacier → 6y delete |
| SOC 2 | Audit period + review | S3 + Glacier |
| PCI DSS | 1 year (3 months accessible) | S3 lifecycle policy |
| SOX | 7 years | S3 lifecycle + Glacier Deep Archive |

## Evidence Collection Checklist

- [ ] CloudTrail trail configuration screenshot/export
- [ ] S3 bucket policy and encryption settings
- [ ] Log retention lifecycle policy
- [ ] Sample CloudTrail logs (sanitized)
- [ ] CloudWatch Alarms configured for security events
- [ ] Log file validation verification command output
- [ ] Security Hub dashboard screenshot with compliance scores

## Common Findings and Remediation

| Finding | Remediation |
|---|---|
| CloudTrail not multi-region | Update trail to `is-multi-region-trail: true` |
| Log file validation disabled | Enable in trail settings |
| Logs not encrypted | Apply KMS encryption to S3 bucket and trail |
| No CloudWatch integration | Add CWL group and IAM role to trail |
| Log retention < requirement | Update S3 lifecycle policy |
| S3 bucket publicly accessible | Apply public access block configuration |
