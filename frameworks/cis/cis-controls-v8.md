# CIS Controls v8

**Framework**: Center for Internet Security Critical Security Controls
**Version**: 8 (released May 2021)
**Publisher**: Center for Internet Security (CIS)
**Controls**: 18 CIS Controls, 153 Safeguards

---

## Overview

CIS Controls v8 reorganizes the controls around activities rather than who manages devices. Controls are mapped to Implementation Groups (IGs) to allow prioritization based on organizational maturity.

## Implementation Groups

| Group | Profile | Description |
|---|---|---|
| IG1 | Basic | Small businesses, limited IT resources, limited cybersecurity expertise |
| IG2 | Foundational | Organizations with some IT staff, handles sensitive client/company data |
| IG3 | Advanced | Organizations with significant security expertise, processes sensitive data |

---

## The 18 CIS Controls

### CIS Control 1: Inventory and Control of Enterprise Assets
**Why**: Actively manage all hardware assets to accurately know which are authorized and which need to be tracked, corrected, or removed.

| Safeguard | Description | IG |
|---|---|---|
| 1.1 | Establish and maintain detailed enterprise asset inventory | IG1 |
| 1.2 | Address unauthorized assets | IG1 |
| 1.3 | Utilize DHCP logging to update enterprise asset inventory | IG2 |
| 1.4 | Use dynamic host configuration protocol (DHCP) logging | IG2 |
| 1.5 | Use a passive asset discovery tool | IG3 |

### CIS Control 2: Inventory and Control of Software Assets
**Why**: Actively manage all software assets to accurately know which are authorized and tracked.

| Safeguard | Description | IG |
|---|---|---|
| 2.1 | Establish and maintain a software inventory | IG1 |
| 2.2 | Ensure authorized software is currently supported | IG1 |
| 2.3 | Address unauthorized software | IG1 |
| 2.4 | Utilize automated software inventory tools | IG2 |
| 2.5 | Allowlist authorized software | IG2 |
| 2.6 | Allowlist authorized libraries | IG2 |
| 2.7 | Allowlist authorized scripts | IG3 |

### CIS Control 3: Data Protection
**Why**: Develop processes and controls to identify, classify, securely handle, retain, and dispose of data.

| Safeguard | Description | IG |
|---|---|---|
| 3.1 | Establish and maintain a data management process | IG1 |
| 3.2 | Establish and maintain a data inventory | IG1 |
| 3.3 | Configure data access control lists | IG1 |
| 3.4 | Enforce data retention | IG1 |
| 3.5 | Securely dispose of data | IG1 |
| 3.6 | Encrypt data on end-user devices | IG1 |
| 3.7 | Establish and maintain a data classification scheme | IG2 |
| 3.8 | Document data flows | IG2 |
| 3.9 | Encrypt data on removable media | IG2 |
| 3.10 | Encrypt sensitive data in transit | IG2 |
| 3.11 | Encrypt sensitive data at rest | IG2 |
| 3.12 | Segment data processing and storage based on sensitivity | IG3 |
| 3.13 | Deploy a Data Loss Prevention solution | IG3 |
| 3.14 | Log sensitive data access | IG3 |

### CIS Control 4: Secure Configuration of Enterprise Assets and Software
**Why**: Establish and maintain the secure configuration of enterprise assets and software.

| Safeguard | Description | IG |
|---|---|---|
| 4.1 | Establish and maintain a secure configuration process | IG1 |
| 4.2 | Establish and maintain a secure configuration process for network infrastructure | IG1 |
| 4.3 | Configure automatic session locking on enterprise assets | IG1 |
| 4.4 | Implement and manage a firewall on servers | IG1 |
| 4.5 | Implement and manage a firewall on end-user devices | IG1 |
| 4.6 | Securely manage enterprise assets and software | IG2 |
| 4.7 | Manage default accounts on enterprise assets and software | IG1 |
| 4.8 | Uninstall or disable unnecessary services | IG2 |
| 4.9 | Configure trusted DNS servers on enterprise assets | IG2 |
| 4.10 | Enforce automatic device lockout on portable end-user devices | IG2 |
| 4.11 | Enforce remote wipe capability on portable end-user devices | IG2 |
| 4.12 | Separate enterprise workspaces on mobile end-user devices | IG3 |

### CIS Control 5: Account Management

| Safeguard | Description | IG |
|---|---|---|
| 5.1 | Establish and maintain an inventory of accounts | IG1 |
| 5.2 | Use unique passwords | IG1 |
| 5.3 | Disable dormant accounts | IG1 |
| 5.4 | Restrict administrator privileges to dedicated administrator accounts | IG1 |
| 5.5 | Establish and maintain an inventory of service accounts | IG2 |
| 5.6 | Centralize account management | IG2 |

### CIS Control 6: Access Control Management

| Safeguard | Description | IG |
|---|---|---|
| 6.1 | Establish an access granting process | IG1 |
| 6.2 | Establish an access revoking process | IG1 |
| 6.3 | Require MFA for externally-exposed applications | IG1 |
| 6.4 | Require MFA for remote network access | IG1 |
| 6.5 | Require MFA for administrative access | IG2 |
| 6.6 | Establish and maintain an inventory of authentication systems | IG2 |
| 6.7 | Centralize access control | IG3 |
| 6.8 | Define and maintain role-based access control | IG3 |

### CIS Controls 7-18 Summary

| Control | Name | IG |
|---|---|---|
| 7 | Continuous Vulnerability Management | IG1-3 |
| 8 | Audit Log Management | IG1-3 |
| 9 | Email and Web Browser Protections | IG1-3 |
| 10 | Malware Defenses | IG1-3 |
| 11 | Data Recovery | IG1-3 |
| 12 | Network Infrastructure Management | IG1-3 |
| 13 | Network Monitoring and Defense | IG2-3 |
| 14 | Security Awareness and Skills Training | IG1-3 |
| 15 | Service Provider Management | IG1-3 |
| 16 | Application Software Security | IG2-3 |
| 17 | Incident Response Management | IG1-3 |
| 18 | Penetration Testing | IG3 |

## References

- [CIS Controls v8 Download](https://www.cisecurity.org/controls/v8)
- [CIS Controls Assessment Specification](https://www.cisecurity.org/controls/cis-controls-assessment-specification)
