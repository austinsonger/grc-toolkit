# SSP Component: AU-2 Event Logging

The system generates and centrally aggregates security audit logs from identity, compute, network, and application layers.

Implementation details:
- Organization-wide CloudTrail with log validation
- SIEM ingestion for near-real-time analytics
- Log retention: 365 days hot, 7 years archive

Evidence references:
- `evidence/artifacts/cloudtrail-retention.json`
- `automation/scripts/aws_collect_evidence.sh`
