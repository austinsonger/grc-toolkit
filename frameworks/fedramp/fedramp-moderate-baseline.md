# FedRAMP Moderate Baseline

**Program**: Federal Risk and Authorization Management Program (FedRAMP)
**Baseline**: Moderate Impact Level
**Based On**: NIST SP 800-53 Rev 5
**Applicable To**: Cloud Service Providers seeking FedRAMP authorization

---

## Overview

FedRAMP Moderate is appropriate for systems where the loss of confidentiality, integrity, or availability would have serious adverse effects on organizational operations, assets, or individuals.

## Control Summary by Family

| Family | Required Controls | Enhanced Controls | Total |
|---|---|---|---|
| AC | 20 | 15 | 35 |
| AT | 5 | 3 | 8 |
| AU | 12 | 6 | 18 |
| CA | 8 | 2 | 10 |
| CM | 11 | 8 | 19 |
| CP | 10 | 6 | 16 |
| IA | 11 | 8 | 19 |
| IR | 8 | 4 | 12 |
| MA | 6 | 2 | 8 |
| MP | 7 | 2 | 9 |
| PE | 17 | 4 | 21 |
| PL | 9 | 2 | 11 |
| PM | 16 | 0 | 16 |
| PS | 8 | 1 | 9 |
| PT | 8 | 0 | 8 |
| RA | 9 | 3 | 12 |
| SA | 22 | 3 | 25 |
| SC | 28 | 12 | 40 |
| SI | 16 | 7 | 23 |
| SR | 12 | 0 | 12 |

**Total: ~325 controls**

## Key FedRAMP-Specific Requirements

### Continuous Monitoring (ConMon)
- Monthly vulnerability scanning
- Annual penetration testing
- Real-time monitoring for critical controls
- Monthly reporting to AO

### Incident Response
- US-CERT reporting: 1 hour for CAT 1, 2 hours for CAT 2
- FedRAMP PMO notification within 1 hour for major incidents

### Cryptography
- FIPS 140-2/140-3 validated cryptographic modules required
- TLS 1.2+ for data in transit (TLS 1.3 preferred)
- AES-256 for data at rest

### Personnel Security
- US citizens or persons with lawful presence
- Background investigation: NACI minimum for Moderate
- PIV cards for federal employees accessing system

## Key Controls with FedRAMP Parameters

### AC-2 Account Management
**FedRAMP Requirement**: Account review at minimum every 60 days

### AC-17 Remote Access
**FedRAMP Requirement**: All remote connections must use multifactor authentication

### AU-2 Event Logging
**FedRAMP Requirement**: Mandatory events to log include:
- Authentication events (successes and failures)
- Account management events
- Access control events
- File integrity changes
- System administrator actions

### AU-11 Audit Record Retention
**FedRAMP Requirement**: Retain audit records for a minimum of 90 days online, 1 year archived

### IA-2 Multi-Factor Authentication
**FedRAMP Requirement**: MFA required for:
- All privileged accounts
- All non-privileged accounts with access to CUI
- Remote access for all users

### SC-28 Protection of Information at Rest
**FedRAMP Requirement**: FIPS 140-2 validated encryption for all data at rest

## Authorization Process

1. **Pre-Authorization**: Agency or FedRAMP PMO sponsorship
2. **Readiness Assessment**: Optional FedRAMP Ready designation
3. **Full Authorization**: 3PAO assessment, review by AO
4. **Continuous Monitoring**: Ongoing compliance

## References

- [FedRAMP Website](https://www.fedramp.gov)
- [FedRAMP Moderate Baseline Controls](https://www.fedramp.gov/documents/)
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
