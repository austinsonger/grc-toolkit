# Incident Postmortem (Sanitized)

- Incident ID: IR-2026-02-14-01
- Detection Source: EDR + SIEM correlation rule
- Affected System: `payments-api`
- Root Cause: Compromised CI token with excessive permissions
- Corrective Actions:
  - Reduced token scope
  - Enforced OIDC short-lived credentials
  - Added pipeline secret scanning gate
