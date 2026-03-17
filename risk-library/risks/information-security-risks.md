# Information Security Risk Library

> Version: 1.0 | Last Updated: 2024-01  
> Risk register entries for common information security risks.

## Risk Schema

| Field | Description |
|---|---|
| Risk ID | Unique identifier: RISK-[Domain]-[Number] |
| Risk Title | Short descriptive name |
| Description | Detailed risk description |
| Threat Source | Who or what could exploit this |
| Threat Event | What could happen |
| Vulnerability | Weakness that could be exploited |
| Likelihood | 1 (Very Low) – 5 (Very High) |
| Impact | 1 (Very Low) – 5 (Very High) |
| Risk Score | Likelihood × Impact |
| Risk Level | Low (1-4), Medium (5-9), High (10-16), Critical (17-25) |
| Mapped Controls | UCS or framework control IDs |

---

## RISK-IAM-001: Unauthorized Access via Compromised Credentials

| Field | Value |
|---|---|
| **Risk ID** | RISK-IAM-001 |
| **Risk Title** | Unauthorized Access via Compromised Credentials |
| **Description** | An attacker obtains valid user credentials through phishing, credential stuffing, or dark web purchase and uses them to gain unauthorized access to systems and data |
| **Threat Source** | External attacker, malicious insider |
| **Threat Event** | Account takeover leading to data breach or ransomware deployment |
| **Vulnerability** | Weak password policies, no MFA, credentials reuse |
| **Likelihood** | 4 (High) |
| **Impact** | 4 (High) |
| **Risk Score** | 16 |
| **Risk Level** | High |
| **Mapped Controls** | UCS-AC-001, UCS-AC-002, NIST IA-2, NIST IA-5, SOC 2 CC6.1 |

**Treatment Options**:
- Implement MFA (reduces likelihood to 2)
- Deploy password manager and enforce unique passwords
- Monitor for credential exposure on dark web
- Implement behavioral analytics for impossible travel detection

---

## RISK-IAM-002: Excessive Privileged Access

| Field | Value |
|---|---|
| **Risk ID** | RISK-IAM-002 |
| **Risk Title** | Excessive Privileged Access |
| **Description** | Users or service accounts have more access than required for their role, increasing the potential impact of account compromise or insider threat |
| **Threat Source** | Malicious insider, external attacker with compromised credentials |
| **Threat Event** | Data exfiltration, ransomware deployment, unauthorized configuration changes |
| **Vulnerability** | Lack of least privilege enforcement, no access reviews, role accumulation over time |
| **Likelihood** | 3 (Medium) |
| **Impact** | 5 (Very High) |
| **Risk Score** | 15 |
| **Risk Level** | High |
| **Mapped Controls** | UCS-AC-001, UCS-AC-003, NIST AC-2, NIST AC-6, SOC 2 CC6.3 |

**Treatment Options**:
- Implement quarterly access reviews
- Deploy just-in-time (JIT) privileged access
- Implement role-based access control (RBAC)
- Remove dormant accounts after 90 days

---

## RISK-DAT-001: Data Breach via Unencrypted Storage

| Field | Value |
|---|---|
| **Risk ID** | RISK-DAT-001 |
| **Risk Title** | Data Breach via Unencrypted Storage |
| **Description** | Sensitive data stored without encryption is exposed if storage media is lost, stolen, or accessed by unauthorized parties |
| **Threat Source** | External attacker, lost/stolen device, insider threat |
| **Threat Event** | Sensitive data exposure, regulatory violation, reputational damage |
| **Vulnerability** | Unencrypted databases, S3 buckets, EBS volumes, laptops |
| **Likelihood** | 3 (Medium) |
| **Impact** | 5 (Very High) |
| **Risk Score** | 15 |
| **Risk Level** | High |
| **Mapped Controls** | UCS-DP-001, NIST SC-28, ISO A.8.24, SOC 2 CC6.7 |

**Treatment Options**:
- Encrypt all databases using AES-256 (KMS-managed keys)
- Enable full-disk encryption on all endpoints
- Implement object storage encryption by default
- Conduct quarterly encryption coverage audits

---

## RISK-NET-001: Network Intrusion via Exposed Services

| Field | Value |
|---|---|
| **Risk ID** | RISK-NET-001 |
| **Risk Title** | Network Intrusion via Exposed Services |
| **Description** | Systems with unnecessary or misconfigured network services exposed to the internet provide attack surface for exploitation |
| **Threat Source** | External attacker, nation-state actor |
| **Threat Event** | Remote code execution, lateral movement, data exfiltration |
| **Vulnerability** | Unnecessary open ports, weak firewall rules, unpatched services |
| **Likelihood** | 3 (Medium) |
| **Impact** | 4 (High) |
| **Risk Score** | 12 |
| **Risk Level** | High |
| **Mapped Controls** | UCS-CM-001, NIST SC-7, NIST CM-7, ISO A.8.20, CIS 4.4 |

**Treatment Options**:
- Implement firewall default-deny rules
- Conduct quarterly port scans
- Use cloud security groups with minimum required access
- Implement network segmentation

---

## RISK-VUL-001: Exploitation of Unpatched Vulnerabilities

| Field | Value |
|---|---|
| **Risk ID** | RISK-VUL-001 |
| **Risk Title** | Exploitation of Known Unpatched Vulnerabilities |
| **Description** | Known vulnerabilities in operating systems, applications, or dependencies are exploited by attackers before patches are applied |
| **Threat Source** | External attacker, automated scanners, ransomware operators |
| **Threat Event** | System compromise, ransomware, data breach |
| **Vulnerability** | Delayed patching cycles, no vulnerability management program |
| **Likelihood** | 4 (High) |
| **Impact** | 4 (High) |
| **Risk Score** | 16 |
| **Risk Level** | High |
| **Mapped Controls** | UCS-CM-002, NIST RA-5, NIST SI-2, ISO A.8.8, CIS 7.1 |

**Remediation SLAs**:
| Severity | Timeline |
|---|---|
| Critical (CVSS 9-10) | 15 days |
| High (CVSS 7-8.9) | 30 days |
| Medium (CVSS 4-6.9) | 90 days |
| Low (CVSS 0.1-3.9) | 180 days |

---

## RISK-INC-001: Security Incident Without Formal Response Process

| Field | Value |
|---|---|
| **Risk ID** | RISK-INC-001 |
| **Risk Title** | Security Incident Without Formal Response Process |
| **Description** | Security incidents are not detected, contained, or remediated in a timely manner due to lack of formal incident response procedures |
| **Threat Source** | Any threat actor |
| **Threat Event** | Prolonged breach, regulatory violations (GDPR 72-hour notification), reputational damage |
| **Vulnerability** | No incident response plan, insufficient monitoring, unclear roles |
| **Likelihood** | 2 (Low) |
| **Impact** | 5 (Very High) |
| **Risk Score** | 10 |
| **Risk Level** | High |
| **Mapped Controls** | UCS-IR-001, NIST IR-4, NIST IR-8, ISO A.5.24, SOC 2 CC7.4 |

---

## RISK-VND-001: Third-Party Vendor Data Breach

| Field | Value |
|---|---|
| **Risk ID** | RISK-VND-001 |
| **Risk Title** | Third-Party Vendor Data Breach |
| **Description** | A vendor or supplier with access to the organization's systems or data experiences a breach, exposing organizational data |
| **Threat Source** | External attacker targeting vendor, malicious vendor employee |
| **Threat Event** | Data exposure, compliance violations, reputational harm |
| **Vulnerability** | Insufficient vendor due diligence, no security requirements in contracts, excessive vendor access |
| **Likelihood** | 3 (Medium) |
| **Impact** | 4 (High) |
| **Risk Score** | 12 |
| **Risk Level** | High |
| **Mapped Controls** | NIST SA-9, NIST SR-2, ISO A.5.19, SOC 2 CC9.2 |

**Treatment Options**:
- Annual vendor security assessments
- Include security requirements in MSAs
- Limit vendor access using least privilege
- Monitor vendor access via CASB or PAM solution

---

## Risk Score Reference

| Score | Level | Action Required |
|---|---|---|
| 17-25 | Critical | Immediate treatment, executive escalation |
| 10-16 | High | Treatment within 30 days, management notification |
| 5-9 | Medium | Treatment within 90 days, track in risk register |
| 1-4 | Low | Monitor, consider risk acceptance |
