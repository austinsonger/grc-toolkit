# MITRE ATT&CK to Security Controls Mapping

**Source**: MITRE ATT&CK Framework v14.1  
**Target**: NIST SP 800-53 Rev 5, ISO 27001:2022, SOC 2 TSC  
**Last Updated**: 2024-01

---

## Overview

Maps MITRE ATT&CK tactics and techniques to security controls, enabling organizations to validate control coverage against known adversary behaviors.

## Mapping by Tactic

### TA0001 – Initial Access

| Technique | ID | NIST SP 800-53 | ISO 27001 | SOC 2 | Detection |
|---|---|---|---|---|---|
| Phishing | T1566 | AT-2, AT-3, SI-3 | A.6.3, A.8.7 | CC6.8 | Email gateway logs |
| Phishing: Spearphishing Attachment | T1566.001 | SI-3, SC-7 | A.8.7 | CC6.8 | Email sandbox alerts |
| Phishing: Spearphishing Link | T1566.002 | SC-7, SI-3 | A.8.7, A.8.23 | CC6.8 | Proxy/DNS logs |
| Valid Accounts | T1078 | AC-2, IA-2, IA-5 | A.5.15, A.5.16 | CC6.1, CC6.2 | Failed login alerts |
| Valid Accounts: Cloud Accounts | T1078.004 | AC-2, IA-2(1) | A.5.16, A.8.5 | CC6.1 | CloudTrail ConsoleLogin |
| Exploit Public-Facing Application | T1190 | RA-5, SI-2, SI-10 | A.8.8, A.8.26 | CC7.1 | WAF logs |
| External Remote Services | T1133 | AC-17, IA-2 | A.6.7, A.8.5 | CC6.6 | VPN/RDP logs |

### TA0004 – Privilege Escalation

| Technique | ID | NIST SP 800-53 | ISO 27001 | SOC 2 | Detection |
|---|---|---|---|---|---|
| Abuse Elevation Control Mechanism | T1548 | AC-6, AU-12 | A.8.2 | CC6.1 | Sudo/UAC logs |
| Access Token Manipulation | T1134 | AC-6, AU-12 | A.8.2 | CC6.1 | Token manipulation alerts |
| Exploitation for Privilege Escalation | T1068 | RA-5, SI-2 | A.8.8 | CC7.1 | Exploit alerts |

### TA0005 – Defense Evasion

| Technique | ID | NIST SP 800-53 | ISO 27001 | SOC 2 | Detection |
|---|---|---|---|---|---|
| Indicator Removal | T1070 | AU-9, SI-7 | A.8.15 | CC7.1 | Log tampering alerts |
| Impair Defenses | T1562 | CM-7, SI-4 | A.8.16 | CC7.2 | Security tool health |
| Disable or Modify Cloud Logs | T1562.008 | AU-9, CM-3 | A.8.15 | CC7.1 | CloudTrail tampering |

### TA0006 – Credential Access

| Technique | ID | NIST SP 800-53 | ISO 27001 | SOC 2 | Detection |
|---|---|---|---|---|---|
| Brute Force | T1110 | AC-7, IA-2 | A.8.5 | CC6.1 | Failed auth rate monitoring |
| Credential Dumping | T1003 | AC-6, IA-5 | A.8.2, A.5.17 | CC6.1 | EDR/AV, LSASS protection |
| Unsecured Credentials | T1552 | IA-5, SC-28 | A.5.17, A.8.24 | CC6.7 | Secret scanner |
| Credentials in Files | T1552.001 | SC-28, SA-15 | A.8.24 | CC6.7 | SAST/DAST |

### TA0010 – Exfiltration

| Technique | ID | NIST SP 800-53 | ISO 27001 | SOC 2 | Detection |
|---|---|---|---|---|---|
| Exfiltration Over C2 Channel | T1041 | SC-7, SI-4 | A.8.20, A.8.16 | CC7.2 | DLP, network monitoring |
| Exfiltration to Cloud Storage | T1567 | SC-7, AC-3 | A.8.12, A.8.20 | CC6.7 | DLP, cloud API monitoring |
| Transfer Data to Cloud Account | T1537 | AC-3, SC-7 | A.8.12 | CC6.7 | Cloud transfer anomalies |

### TA0040 – Impact

| Technique | ID | NIST SP 800-53 | ISO 27001 | SOC 2 | Detection |
|---|---|---|---|---|---|
| Data Encrypted for Impact (Ransomware) | T1486 | CP-9, SC-28 | A.8.13, A.8.24 | A1.2 | File activity monitoring |
| Account Access Removal | T1531 | AC-2, CP-2 | A.5.16 | A1.2 | Account lockout monitoring |
| Service Stop | T1489 | CP-2, SI-4 | A.5.29 | A1.2 | Service health monitoring |

## Control Coverage Heatmap

| ATT&CK Tactic | Key Controls | Coverage Status |
|---|---|---|
| Initial Access | AC-2, IA-2, SI-3, SC-7 | [Assess] |
| Execution | CM-7, AU-12, SI-3 | [Assess] |
| Persistence | AC-2, AU-12, CM-7 | [Assess] |
| Privilege Escalation | AC-6, IA-2(1), RA-5 | [Assess] |
| Defense Evasion | AU-9, SI-7, CM-3 | [Assess] |
| Credential Access | AC-7, IA-5, SC-28 | [Assess] |
| Exfiltration | SC-7, SI-4, AC-3 | [Assess] |
| Impact | CP-9, CP-2, SI-7 | [Assess] |

## References

- [MITRE ATT&CK Framework](https://attack.mitre.org)
- [NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/)
