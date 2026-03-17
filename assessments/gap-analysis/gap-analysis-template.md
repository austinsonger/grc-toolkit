# GRC Gap Analysis Template

**Organization**: [Organization Name]  
**Framework**: [Target Framework – e.g., SOC 2, ISO 27001, NIST CSF]  
**Assessment Date**: [YYYY-MM-DD]  
**Assessor**: [Name/Team]  
**Scope**: [Systems, services, or organizational units in scope]

---

## Executive Summary

| Metric | Value |
|---|---|
| Total Controls Assessed | [N] |
| Fully Implemented | [N] (X%) |
| Partially Implemented | [N] (X%) |
| Not Implemented | [N] (X%) |
| Not Applicable | [N] (X%) |
| Overall Maturity Score | [X.X / 5.0] |

**Risk Summary**: [High-level narrative of most significant gaps and their risk implications]

---

## Maturity Scale

| Level | Score | Description |
|---|---|---|
| Not Implemented | 0 | Control does not exist |
| Initial | 1 | Ad hoc, reactive, undocumented |
| Developing | 2 | Partially implemented, not consistently applied |
| Defined | 3 | Documented, implemented consistently |
| Managed | 4 | Monitored, measured, reviewed regularly |
| Optimizing | 5 | Continuously improving, proactively managed |

---

## Gap Analysis Results

### Domain: Access Control

| Control ID | Control Name | Current State | Target State | Gap | Priority | Remediation Action | Owner | Due Date |
|---|---|---|---|---|---|---|---|---|
| CC6.1 / AC-2 | Account Management | 2 – Developing | 4 – Managed | Partial | High | Implement automated provisioning via IGA tool; conduct quarterly access reviews | IT/IAM | Q2 2024 |
| CC6.1 / IA-2 | Multi-Factor Authentication | 3 – Defined | 4 – Managed | Minor | High | Enable MFA for all users; enforce phishing-resistant MFA for privileged accounts | IT Security | Q1 2024 |
| CC6.3 / AC-2(3) | Account Termination | 1 – Initial | 3 – Defined | Significant | Critical | Automate account disable on HR termination trigger; establish 4-hour SLA | IT/HR | Q1 2024 |
| CC6.6 / AC-17 | Remote Access | 3 – Defined | 4 – Managed | Minor | Medium | Implement ZTNA solution; enforce device compliance checks | Network Team | Q3 2024 |

### Domain: Audit Logging

| Control ID | Control Name | Current State | Target State | Gap | Priority | Remediation Action | Owner | Due Date |
|---|---|---|---|---|---|---|---|---|
| CC7.2 / AU-2 | Audit Log Configuration | 2 – Developing | 4 – Managed | Partial | High | Centralize logging to SIEM; define and implement log requirements per system | SIEM Team | Q2 2024 |
| CC7.2 / AU-11 | Log Retention | 1 – Initial | 3 – Defined | Significant | High | Implement 90-day hot/1-year archive retention policy; configure log archival | IT Ops | Q1 2024 |

### Domain: Vulnerability Management

| Control ID | Control Name | Current State | Target State | Gap | Priority | Remediation Action | Owner | Due Date |
|---|---|---|---|---|---|---|---|---|
| CC7.1 / RA-5 | Vulnerability Scanning | 2 – Developing | 4 – Managed | Partial | High | Deploy continuous scanning; establish remediation SLAs; track in ticket system | SecOps | Q2 2024 |
| CC7.1 / SI-2 | Patch Management | 2 – Developing | 3 – Defined | Partial | High | Implement automated patching for OS/middleware; track patch compliance | IT Ops | Q2 2024 |

### Domain: Incident Response

| Control ID | Control Name | Current State | Target State | Gap | Priority | Remediation Action | Owner | Due Date |
|---|---|---|---|---|---|---|---|---|
| CC7.4 / IR-4 | Incident Handling | 2 – Developing | 4 – Managed | Partial | High | Document incident response playbooks; assign IR team roles; test quarterly | SecOps | Q2 2024 |
| CC7.5 / CP-10 | Incident Recovery | 1 – Initial | 3 – Defined | Significant | High | Test DR procedures; document recovery runbooks; validate RTO/RPO | IT Ops | Q3 2024 |

### Domain: Vendor Management

| Control ID | Control Name | Current State | Target State | Gap | Priority | Remediation Action | Owner | Due Date |
|---|---|---|---|---|---|---|---|---|
| CC9.2 / SA-9 | Vendor Risk Management | 1 – Initial | 3 – Defined | Significant | Medium | Implement vendor risk assessment process; include security requirements in MSAs | Procurement/Legal | Q3 2024 |

---

## Prioritized Remediation Roadmap

### Critical (Complete within 30 days)
1. **Account Termination Automation** – Automate disable on HR termination notification
2. **MFA Enforcement** – Enable MFA for all cloud console access

### High (Complete within 90 days)
3. **SIEM/Log Centralization** – Centralize logs from all in-scope systems
4. **Log Retention Policy** – Implement retention per policy requirements
5. **Vulnerability Scanning** – Deploy continuous scanning with SLA tracking
6. **IR Plan Documentation** – Document and tabletop test IR procedures

### Medium (Complete within 180 days)
7. **Vendor Risk Program** – Establish formal vendor assessment process
8. **ZTNA Implementation** – Deploy Zero Trust Network Access for remote workers
9. **IGA Tool Deployment** – Automate provisioning and access reviews

---

## Evidence Required for Next Assessment

| Domain | Evidence Needed |
|---|---|
| Access Control | User access reports, quarterly review records, termination records |
| Logging | SIEM configuration, log samples, retention policy |
| Vulnerability Mgmt | Scan reports, remediation tickets, patch reports |
| Incident Response | IR plan document, tabletop exercise results |
| Vendor Management | Vendor inventory, assessment questionnaires, MSA security clauses |
