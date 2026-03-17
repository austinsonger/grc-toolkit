# Implementing AU Controls on AWS (AU-2, AU-6, AU-11, AU-12)

## Objective
Implement centralized logging aligned to `CTRL-AU-001` with defensible audit evidence.

## Architecture
- Enable AWS CloudTrail organization trail (all accounts, all regions)
- Route CloudTrail, VPC Flow Logs, and CloudWatch Logs to central log archive account
- Stream selected detections to SIEM
- Apply immutable retention for high-value logs

## Implementation Steps
1. Create organization trail with log file validation enabled.
2. Configure S3 bucket with Object Lock (compliance mode) and KMS encryption.
3. Configure CloudWatch metric filters for authentication failures and root usage.
4. Send log events to SIEM connector and validate ingestion latency.
5. Define retention schedules:
   - Security events: 365 days online, 7 years archive
   - Debug logs: 30 days online

## Evidence to Collect
- `aws cloudtrail describe-trails`
- S3 bucket retention and object lock config
- SIEM ingestion dashboard snapshot
- Quarterly log access review records

## Example Validation Commands
```bash
aws cloudtrail describe-trails --trail-name-list org-security-trail
aws logs describe-metric-filters --log-group-name /aws/cloudtrail/security
aws s3api get-object-lock-configuration --bucket sanitized-security-logs
```
