# Sarbanes-Oxley Act (SOX) - IT Controls Overview

**Regulation**: Sarbanes-Oxley Act of 2002
**Authority**: Public Company Accounting Oversight Board (PCAOB)
**Jurisdiction**: United States
**Applicable To**: Public companies listed on US stock exchanges
**Key Sections**: Section 302, Section 404, Section 409

---

## Overview

SOX establishes requirements for financial reporting and internal controls for public companies. From an IT perspective, the most relevant sections are 302 and 404, which address internal controls over financial reporting (ICFR).

## IT General Controls (ITGCs)

### Access Management
- Segregation of duties for financial systems
- User access provisioning and de-provisioning
- Privileged access management
- Access reviews (quarterly minimum)
- Password policy enforcement

### Change Management
- Formal change control process for financial systems
- Testing requirements before production deployment
- Emergency change procedures with retroactive approval
- Change documentation and audit trails

### Computer Operations
- Job scheduling and monitoring
- Backup and recovery procedures
- Incident management for financial systems
- System availability monitoring

### Program Development
- SDLC requirements for financially significant systems
- Security testing integration
- Documentation standards

## Application Controls

- Input validation for financial data
- Processing controls and reconciliation
- Output controls and report integrity
- Interface controls between systems

## COBIT Mapping

| SOX Requirement | COBIT Process |
|---|---|
| Access Management | DSS05.04, APO13.01 |
| Change Management | BAI06.01, BAI06.02 |
| Incident Management | DSS02.01 |
| Backup/Recovery | DSS04.08 |

## References

- [PCAOB Auditing Standards](https://pcaobus.org/Standards/Auditing)
- [SEC Final Rule: Management's Report on ICFR](https://www.sec.gov/rules/final/33-8238.htm)
