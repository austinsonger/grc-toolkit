# Unified Control Set (UCS)

> Version: 1.0 | Last Updated: 2024-01  
> A normalized control library mapping controls across major security frameworks.

---

## Overview

The Unified Control Set (UCS) provides a vendor-neutral, framework-agnostic control taxonomy. Each control includes a unique UCS ID, description, and mappings to major frameworks.

## Control Schema

| Field | Description |
|---|---|
| UCS-ID | Unique identifier in format UCS-[Domain]-[Number] |
| Name | Short control name |
| Description | What the control requires |
| Risk Addressed | The risk category this control mitigates |
| NIST SP 800-53 | Mapped NIST control(s) |
| ISO 27001:2022 | Mapped ISO control(s) |
| SOC 2 (TSC) | Mapped SOC 2 criterion |
| CIS v8 | Mapped CIS Safeguard(s) |
| FedRAMP | Applicable at which FedRAMP baseline |

---

## Domain: Access Control (AC)

### UCS-AC-001 – User Account Lifecycle Management

| Field | Value |
|---|---|
| **UCS-ID** | UCS-AC-001 |
| **Name** | User Account Lifecycle Management |
| **Description** | Establish a formal process for creating, modifying, reviewing, and disabling user accounts. Accounts must be provisioned based on the principle of least privilege and business need. |
| **Risk Addressed** | Unauthorized access via stale or overprivileged accounts |
| **NIST SP 800-53** | AC-2, AC-2(1), AC-2(3) |
| **ISO 27001:2022** | A.5.15, A.5.16, A.5.18 |
| **SOC 2 (TSC)** | CC6.1, CC6.2, CC6.3 |
| **CIS v8** | 5.1, 5.3, 6.1, 6.2 |
| **FedRAMP** | Low, Moderate, High |

**Implementation Notes**:
- Automated account provisioning through HR system integration reduces manual errors
- Quarterly access reviews minimum; monthly for privileged accounts
- Immediate revocation upon termination (same-day business requirement)

---

### UCS-AC-002 – Multi-Factor Authentication

| Field | Value |
|---|---|
| **UCS-ID** | UCS-AC-002 |
| **Name** | Multi-Factor Authentication (MFA) |
| **Description** | Require multi-factor authentication for all users accessing information systems, with elevated requirements for privileged and remote access. |
| **Risk Addressed** | Account compromise through credential theft or phishing |
| **NIST SP 800-53** | IA-2, IA-2(1), IA-2(2), IA-2(6) |
| **ISO 27001:2022** | A.8.5 |
| **SOC 2 (TSC)** | CC6.1 |
| **CIS v8** | 6.3, 6.4, 6.5 |
| **FedRAMP** | Moderate, High |

**Implementation Notes**:
- Hardware tokens (FIDO2/WebAuthn) preferred over SMS for high-sensitivity systems
- Push notification MFA with number matching reduces MFA fatigue attacks
- Phishing-resistant MFA required for privileged access in high-security environments

---

### UCS-AC-003 – Privileged Access Management

| Field | Value |
|---|---|
| **UCS-ID** | UCS-AC-003 |
| **Name** | Privileged Access Management |
| **Description** | Manage and control privileged access to systems and data through just-in-time access, session recording, and strict approval workflows. |
| **Risk Addressed** | Insider threat and external attacker lateral movement using privileged credentials |
| **NIST SP 800-53** | AC-2(7), AC-6, AC-6(1), AC-6(2), AC-6(5) |
| **ISO 27001:2022** | A.8.2 |
| **SOC 2 (TSC)** | CC6.1, CC6.3 |
| **CIS v8** | 5.4, 6.8 |
| **FedRAMP** | Moderate, High |

---

### UCS-AC-004 – Remote Access Controls

| Field | Value |
|---|---|
| **UCS-ID** | UCS-AC-004 |
| **Name** | Remote Access Controls |
| **Description** | Implement secure remote access with encrypted connections, MFA, device compliance verification, and activity logging. |
| **Risk Addressed** | Unauthorized access and data exfiltration via remote connections |
| **NIST SP 800-53** | AC-17, AC-17(1), AC-17(2) |
| **ISO 27001:2022** | A.6.7, A.8.20 |
| **SOC 2 (TSC)** | CC6.6, CC6.7 |
| **CIS v8** | 6.4, 12.7 |
| **FedRAMP** | Low, Moderate, High |

---

## Domain: Audit and Logging (AL)

### UCS-AL-001 – Audit Log Configuration

| Field | Value |
|---|---|
| **UCS-ID** | UCS-AL-001 |
| **Name** | Audit Log Configuration |
| **Description** | Configure systems to generate audit logs for security-relevant events including authentication, authorization, privileged operations, and configuration changes. |
| **Risk Addressed** | Inability to detect or investigate security incidents |
| **NIST SP 800-53** | AU-2, AU-3, AU-12 |
| **ISO 27001:2022** | A.8.15 |
| **SOC 2 (TSC)** | CC7.2 |
| **CIS v8** | 8.1, 8.2, 8.5 |
| **FedRAMP** | Low, Moderate, High |

**Required Log Events**:
- Authentication: successes, failures, lockouts
- Authorization: access grants and denials
- Account management: creation, modification, deletion
- Privileged actions: sudo, admin operations
- System events: startup, shutdown, crashes
- Network: firewall blocks, VPN connections
- Data access: reads/writes to sensitive data repositories

---

### UCS-AL-002 – Log Retention and Protection

| Field | Value |
|---|---|
| **UCS-ID** | UCS-AL-002 |
| **Name** | Log Retention and Protection |
| **Description** | Retain audit logs for defined periods based on regulatory requirements and protect logs from unauthorized modification or deletion. |
| **Risk Addressed** | Loss of forensic evidence during incident investigations |
| **NIST SP 800-53** | AU-9, AU-11 |
| **ISO 27001:2022** | A.8.15 |
| **SOC 2 (TSC)** | CC7.2 |
| **CIS v8** | 8.3, 8.10 |
| **FedRAMP** | Moderate, High |

**Retention Requirements by Framework**:
| Framework | Minimum Retention |
|---|---|
| FedRAMP Moderate | 90 days online, 1 year archived |
| HIPAA | 6 years |
| SOX | 7 years |
| PCI DSS | 1 year (3 months online) |
| SOC 2 | Per audit period + 1 year |

---

## Domain: Configuration Management (CM)

### UCS-CM-001 – Secure Baseline Configuration

| Field | Value |
|---|---|
| **UCS-ID** | UCS-CM-001 |
| **Name** | Secure Baseline Configuration |
| **Description** | Establish, document, and maintain secure baseline configurations for all systems. Deviations require formal approval and documentation. |
| **Risk Addressed** | System compromise through misconfiguration |
| **NIST SP 800-53** | CM-2, CM-6, CM-6(1) |
| **ISO 27001:2022** | A.8.9 |
| **SOC 2 (TSC)** | CC7.1 |
| **CIS v8** | 4.1, 4.2 |
| **FedRAMP** | Low, Moderate, High |

**Reference Baselines**:
- CIS Benchmarks (OS, cloud platforms, applications)
- DISA STIGs (federal environments)
- AWS/Azure/GCP security foundations

---

### UCS-CM-002 – Vulnerability Management

| Field | Value |
|---|---|
| **UCS-ID** | UCS-CM-002 |
| **Name** | Vulnerability Management |
| **Description** | Identify, assess, prioritize, and remediate vulnerabilities in systems and applications within defined timeframes based on severity. |
| **Risk Addressed** | Exploitation of known vulnerabilities |
| **NIST SP 800-53** | RA-5, RA-5(2), SI-2 |
| **ISO 27001:2022** | A.8.8 |
| **SOC 2 (TSC)** | CC7.1 |
| **CIS v8** | 7.1, 7.2, 7.4, 7.6 |
| **FedRAMP** | Low, Moderate, High |

**Remediation SLAs**:
| Severity | CVSS Score | Remediation Timeline |
|---|---|---|
| Critical | 9.0-10.0 | 15 days |
| High | 7.0-8.9 | 30 days |
| Medium | 4.0-6.9 | 90 days |
| Low | 0.1-3.9 | 180 days |

---

## Domain: Incident Response (IR)

### UCS-IR-001 – Incident Response Plan

| Field | Value |
|---|---|
| **UCS-ID** | UCS-IR-001 |
| **Name** | Incident Response Plan |
| **Description** | Develop, maintain, and test a documented incident response plan covering preparation, identification, containment, eradication, recovery, and lessons learned. |
| **Risk Addressed** | Uncoordinated or inadequate response to security incidents |
| **NIST SP 800-53** | IR-4, IR-8 |
| **ISO 27001:2022** | A.5.24, A.5.26 |
| **SOC 2 (TSC)** | CC7.3, CC7.4, CC7.5 |
| **CIS v8** | 17.1, 17.2, 17.4 |
| **FedRAMP** | Low, Moderate, High |

---

## Domain: Data Protection (DP)

### UCS-DP-001 – Encryption at Rest

| Field | Value |
|---|---|
| **UCS-ID** | UCS-DP-001 |
| **Name** | Encryption at Rest |
| **Description** | Encrypt sensitive data at rest using approved cryptographic algorithms. Manage encryption keys securely with separate key management infrastructure. |
| **Risk Addressed** | Data exposure through storage media theft or unauthorized access |
| **NIST SP 800-53** | SC-28, SC-28(1) |
| **ISO 27001:2022** | A.8.24 |
| **SOC 2 (TSC)** | CC6.7 |
| **CIS v8** | 3.11 |
| **FedRAMP** | FIPS 140-2 validated modules required |

---

### UCS-DP-002 – Encryption in Transit

| Field | Value |
|---|---|
| **UCS-ID** | UCS-DP-002 |
| **Name** | Encryption in Transit |
| **Description** | Encrypt all data transmitted over networks using TLS 1.2 or higher. Disable weak cipher suites and insecure protocols. |
| **Risk Addressed** | Data interception and man-in-the-middle attacks |
| **NIST SP 800-53** | SC-8, SC-8(1) |
| **ISO 27001:2022** | A.8.24 |
| **SOC 2 (TSC)** | CC6.7 |
| **CIS v8** | 3.10 |
| **FedRAMP** | TLS 1.2 minimum, 1.3 preferred |
