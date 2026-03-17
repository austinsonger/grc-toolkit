# Access Control Policy

**Document ID**: POL-SEC-001  
**Version**: 2.0  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Last Reviewed**: 2024-01  
**Next Review**: 2025-01  
**Approved By**: [Executive Sponsor]

---

## 1. Purpose

This policy establishes requirements for controlling access to [Organization Name]'s information systems, data, and facilities to ensure that only authorized individuals have access to resources appropriate for their role and responsibilities.

## 2. Scope

This policy applies to:
- All employees, contractors, consultants, and third-party users
- All information systems, applications, databases, and cloud services owned or operated by [Organization Name]
- All data classifications (Public, Internal, Confidential, Restricted)

## 3. Policy Statements

### 3.1 Account Management

**3.1.1** All users must have a unique account identifier. Shared accounts are prohibited except for service accounts approved by the CISO.

**3.1.2** User accounts must be provisioned based on a formal access request approved by the user's manager and the system/data owner.

**3.1.3** Access privileges must follow the principle of **least privilege** — users receive only the minimum access required to perform their job functions.

**3.1.4** User accounts must be reviewed at minimum:
- Quarterly for accounts with privileged access
- Semi-annually for standard user accounts
- Immediately upon role change or termination

**3.1.5** Accounts must be disabled within **4 business hours** of employee termination notification and removed within **30 days**.

### 3.2 Authentication Requirements

**3.2.1** All users must authenticate using unique credentials. Passwords or PINs alone are insufficient for systems processing Confidential or Restricted data.

**3.2.2** Multi-factor authentication (MFA) is required for:
- All remote access (VPN, remote desktop)
- All cloud service consoles (AWS, Azure, GCP)
- All systems processing Confidential or Restricted data
- All privileged/administrative accounts

**3.2.3** Password requirements:
| Account Type | Minimum Length | Complexity | Max Age | Lockout |
|---|---|---|---|---|
| Standard User | 12 characters | 3 of 4 character classes | 365 days | 10 failed attempts |
| Privileged User | 16 characters | 3 of 4 character classes | 90 days | 5 failed attempts |
| Service Account | 20+ characters | Random/managed by vault | Rotated annually | N/A |

**3.2.4** Passwords must not be shared, written down, or transmitted in cleartext.

### 3.3 Privileged Access

**3.3.1** Privileged accounts (domain admin, root, cloud admin) must be separate from standard user accounts.

**3.3.2** Privileged access must be obtained via a Privileged Access Management (PAM) solution with:
- Just-in-time (JIT) access provisioning
- Session recording for all privileged sessions
- Approval workflow for access requests

**3.3.3** Privileged access must not be used for general business activities (email, web browsing, etc.).

### 3.4 Remote Access

**3.4.1** Remote access to internal systems is permitted only through approved methods (corporate VPN, Zero Trust Network Access solution).

**3.4.2** Remote access connections must use MFA.

**3.4.3** Unmanaged personal devices must not be used to access systems processing Confidential or Restricted data without a virtual desktop or containerized solution.

**3.4.4** All remote access sessions must be automatically terminated after **60 minutes of inactivity**.

### 3.5 Third-Party Access

**3.5.1** Vendor and contractor access must be time-limited and specific to the systems required.

**3.5.2** Third-party access must be formally requested, approved by the system owner, and documented.

**3.5.3** All vendor/contractor accounts must be reviewed at minimum **quarterly** and disabled when no longer needed.

**3.5.4** Third parties must not have access to systems outside the scope of their contract.

### 3.6 Physical Access

**3.6.1** Physical access to data centers and secure areas requires badge authentication.

**3.6.2** Visitors must be escorted by authorized personnel at all times in restricted areas.

**3.6.3** Physical access logs must be retained for a minimum of 1 year.

## 4. Roles and Responsibilities

| Role | Responsibility |
|---|---|
| CISO | Owns this policy, approves exceptions, reviews annually |
| IT/IAM Team | Implements access controls, processes provisioning requests |
| Managers | Approves access requests for direct reports, notifies HR/IT of terminations |
| Data Owners | Approves access to data/systems they own |
| All Employees | Comply with this policy, report violations |
| Auditors | Conducts access reviews and compliance assessments |

## 5. Exceptions

Exceptions to this policy require:
1. Written request detailing the exception, business justification, and risk
2. Approval from the CISO
3. Compensating controls to reduce risk
4. Time-limited (max 90 days) with renewal process
5. Documentation in the exceptions register

## 6. Compliance and Enforcement

Violations of this policy may result in disciplinary action up to and including termination. Intentional circumvention of access controls may result in legal action.

## 7. Related Documents

- Password Management Procedure
- Privileged Access Management Procedure
- Identity and Access Management Standard
- User Termination Checklist
- Third-Party Access Agreement

## 8. Regulatory Mapping

| Requirement | Framework Reference |
|---|---|
| Access control policy | NIST AC-1, ISO 5.1, SOC 2 CC5.3 |
| Account management | NIST AC-2, ISO 5.15, SOC 2 CC6.2 |
| Least privilege | NIST AC-6, ISO 8.2, CIS 6.8 |
| MFA | NIST IA-2(1), ISO 8.5, SOC 2 CC6.1 |
| Privileged access | NIST AC-6(5), ISO 8.2, SOC 2 CC6.1 |
| Remote access | NIST AC-17, ISO 6.7, SOC 2 CC6.6 |
| Third-party access | NIST AC-20, ISO 5.19, SOC 2 CC9.2 |

## 9. Review History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2022-01 | [Author] | Initial version |
| 2.0 | 2024-01 | [Author] | Updated MFA requirements, added cloud requirements |
