# Access Control Audit Checklist

**Audit Area**: Logical Access Controls  
**Framework Coverage**: SOC 2 CC6.1-CC6.8, NIST AC, IA; ISO 27001 5.15-5.18, 8.2-8.5  
**Audit Type**: Annual audit / SOC 2 Type II / ISO 27001 Surveillance

---

## Pre-Audit Preparation

- [ ] Request user account list from all in-scope systems
- [ ] Request privileged account list (admin, root, service accounts)
- [ ] Request access review records (last 12 months)
- [ ] Request termination reports correlated with HR records
- [ ] Request authentication configuration documentation
- [ ] Request MFA enrollment reports

---

## Section 1: Account Management (CC6.1, CC6.2, CC6.3 / AC-2)

### 1.1 Account Provisioning
- [ ] Verify formal access request process exists and is documented
- [ ] Sample 25 users provisioned in the audit period – verify approval records exist for each
- [ ] Verify accounts were provisioned with least privilege
- [ ] Verify new accounts required manager and data owner approval

### 1.2 Account Reviews
- [ ] Verify quarterly access reviews were performed for privileged accounts
- [ ] Verify semi-annual reviews were performed for standard accounts
- [ ] Review access review documentation for completeness (who reviewed, date, actions taken)
- [ ] Verify that inappropriate access identified in reviews was revoked

### 1.3 Account Termination
- [ ] Sample 25 terminated employees from HR records
- [ ] Verify each account was disabled within SLA (4 business hours)
- [ ] Verify accounts were fully removed within 30 days
- [ ] Check for any terminated users with active accounts (exception finding if present)
- [ ] Verify physical access was revoked for terminated employees

### 1.4 Account Inventory
- [ ] Verify an accurate account inventory exists across all in-scope systems
- [ ] Check for orphaned accounts (no corresponding HR record)
- [ ] Check for shared/generic accounts (exception if present without CISO approval)
- [ ] Check for dormant accounts (no login > 90 days)

---

## Section 2: Authentication Controls (CC6.1 / IA-2, IA-5)

### 2.1 Password Policy
- [ ] Verify password policy meets requirements (length, complexity, age, lockout)
- [ ] Verify policy is enforced technically (not just documented)
- [ ] Check that password policy is applied to all in-scope systems

### 2.2 Multi-Factor Authentication
- [ ] Verify MFA is enabled for all remote access connections
- [ ] Verify MFA is enabled for all cloud service consoles
- [ ] Verify MFA is enabled for all privileged accounts
- [ ] Verify MFA enrollment rate (target: 100% for required users)
- [ ] Check for any MFA exceptions – verify compensating controls

### 2.3 Service Accounts
- [ ] Verify service accounts use long, complex passwords managed by a vault
- [ ] Verify service accounts are not used for interactive logins
- [ ] Verify service accounts have only required permissions
- [ ] Verify service account passwords are rotated at least annually

---

## Section 3: Privileged Access (CC6.1 / AC-6, AC-2(7))

### 3.1 Privileged Account Controls
- [ ] Verify privileged accounts are separate from standard user accounts
- [ ] Verify privileged accounts use just-in-time (JIT) access if PAM implemented
- [ ] Verify all privileged sessions are recorded
- [ ] Check that privileged access requires approval workflow
- [ ] Verify that privileged accounts are not used for email/web browsing

### 3.2 Privileged Access Reviews
- [ ] Verify privileged access reviews occur quarterly
- [ ] Verify least privilege is enforced for all privileged roles
- [ ] Check number of domain/global admins (flag if excessive)

---

## Section 4: Network and Remote Access (CC6.6 / AC-17)

### 4.1 Remote Access
- [ ] Verify VPN or ZTNA is the only method of remote access
- [ ] Verify MFA is required for all remote access
- [ ] Verify remote access sessions timeout after inactivity period
- [ ] Check for any split-tunneling configurations (flag if present)

### 4.2 Network Segmentation
- [ ] Verify production and non-production environments are segregated
- [ ] Verify firewalls implement default-deny rules
- [ ] Review firewall rule sets for overly permissive rules (any/any findings)

---

## Section 5: Third-Party Access (CC9.2 / AC-20, SA-9)

- [ ] Verify vendor/contractor access is documented and time-limited
- [ ] Verify vendor accounts are reviewed quarterly
- [ ] Check for any vendor accounts that should have been disabled
- [ ] Verify vendors are restricted to only necessary systems
- [ ] Verify security requirements are included in vendor contracts

---

## Audit Findings Log

| Finding ID | Control | Description | Severity | Recommendation | Management Response | Due Date |
|---|---|---|---|---|---|---|
| AF-001 | AC-2 | 3 terminated user accounts not disabled within SLA | High | Automate termination process, remediate immediately | Accounts disabled; automation project initiated | 30 days |
| AF-002 | IA-2 | MFA not enforced for 15% of cloud console users | High | Enforce MFA policy for all users | MFA enrollment campaign launched | 15 days |
| AF-003 | AC-2 | Access reviews not documented for Q3 | Medium | Implement GRC tool to track review completion | Reviews being conducted retroactively | 30 days |

---

## Audit Conclusion

**Overall Assessment**: [Pass / Pass with Exceptions / Fail]  
**Number of Findings**: [N]  
**Critical**: [N] | **High**: [N] | **Medium**: [N] | **Low**: [N]

**Auditor Signature**: ___________________  
**Date**: ___________________
