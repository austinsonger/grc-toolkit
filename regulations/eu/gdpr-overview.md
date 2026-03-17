# General Data Protection Regulation (GDPR)

**Regulation**: EU General Data Protection Regulation
**Authority**: European Data Protection Board (EDPB)
**Regulation Number**: (EU) 2016/679
**Jurisdiction**: European Union (and EEA)
**Effective Date**: May 25, 2018
**Applicable To**: Organizations processing personal data of EU residents

---

## Overview

The GDPR is a comprehensive data protection regulation that governs how organizations collect, store, process, and transfer personal data of EU residents.

## Key Articles for Security Teams

### Article 5 – Principles of Processing
- Lawfulness, fairness, and transparency
- Purpose limitation
- Data minimization
- Accuracy
- Storage limitation
- **Integrity and confidentiality** (security requirement)
- Accountability

### Article 25 – Data Protection by Design and Default
Organizations must implement appropriate technical and organizational measures to implement data protection principles effectively.

### Article 32 – Security of Processing

Organizations must implement appropriate technical and organizational measures including:

| Measure | Description |
|---|---|
| Pseudonymization | De-identifying personal data where possible |
| Encryption | Encrypting personal data in transit and at rest |
| Confidentiality | Ensuring ongoing confidentiality of processing systems |
| Integrity | Maintaining integrity of processing systems |
| Availability | Ensuring availability and resilience of systems |
| Recovery | Ability to restore availability after incidents |
| Testing | Regular testing and evaluation of security measures |

### Article 33 – Breach Notification to Supervisory Authority
- Notification within **72 hours** of becoming aware of a breach
- Content requirements: nature, categories, approximate number of records
- Contact information for DPO
- Likely consequences of breach
- Measures taken or proposed

### Article 34 – Communication to Data Subjects
- Notification required when breach is "likely to result in high risk"
- Clear, plain language description of breach
- No undue delay

### Article 35 – Data Protection Impact Assessment (DPIA)
Required when processing is "likely to result in high risk", including:
- Systematic profiling
- Processing special categories of data at scale
- Systematic monitoring of publicly accessible areas

## NIST SP 800-53 Mapping

| GDPR Article | NIST SP 800-53 Controls |
|---|---|
| Art. 5(1)(f) - Integrity & Confidentiality | SC-8, SC-28, SI-7 |
| Art. 25 - Privacy by Design | PL-8, SA-8, SA-15 |
| Art. 32 - Security Measures | SC-8, SC-28, AU-2, IR-4 |
| Art. 33 - Breach Notification | IR-6, IR-8 |
| Art. 35 - DPIA | RA-3, RA-8, PL-2 |

## ISO 27001:2022 Mapping

| GDPR Article | ISO 27001:2022 Control |
|---|---|
| Art. 32 - Encryption | A.8.24 |
| Art. 32 - Access Control | A.8.3, A.5.15 |
| Art. 32 - Logging | A.8.15, A.8.16 |
| Art. 33 - Incident Response | A.5.24, A.5.26 |
| Art. 35 - Risk Assessment | A.8.8 |

## References

- [GDPR Full Text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)
- [EDPB Guidelines](https://edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en)
