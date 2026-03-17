# Scenario: Ransomware Impacts Production Workloads

## Scenario Summary
A privileged credential is compromised, malicious encryption is launched across production instances, and backup integrity is uncertain.

## Preconditions
- Excessive standing admin access
- Incomplete endpoint telemetry
- Unverified backup restore tests

## Risk Response
- Trigger IR major incident process (`CTRL-IR-001`)
- Isolate affected assets and preserve forensic logs (`CTRL-AU-001`)
- Recover from immutable backups and validate RTO/RPO (`CTRL-CP-001`)
