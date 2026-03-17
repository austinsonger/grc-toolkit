# GRC-Toolkit

> A comprehensive, scalable, and operational Governance, Risk, and Compliance (GRC) platform — not just a static reference library.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Frameworks](https://img.shields.io/badge/Frameworks-SOC2%20%7C%20ISO27001%20%7C%20NIST%20%7C%20FedRAMP%20%7C%20CIS-blue)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Purpose

GRC-Toolkit is a community-driven repository that centralizes governance, risk, and compliance knowledge for security practitioners, auditors, compliance engineers, and GRC program managers. It goes beyond static documentation to provide:

- **Normalized control structures** across major frameworks (NIST, ISO 27001, SOC 2, FedRAMP, CIS)
- **Automation and compliance-as-code** examples for cloud environments
- **Control mappings and crosswalks** between frameworks
- **Risk libraries** with likelihood/impact scoring
- **Policy templates** ready for organizational use
- **Evidence collection** scripts and artifact examples
- **Audit programs** and gap analysis templates

---

## Target Audience

| Role | How to Use This Repo |
|---|---|
| GRC Engineers | Use controls/, mappings/, and automation/ to build compliance programs |
| Security Auditors | Use audits/, checklists/, and evidence/ for audit execution |
| Compliance Managers | Use policies/, ssp/, and assessments/ to manage compliance programs |
| Cloud Security Teams | Use implementation-guides/ and automation/ for cloud-native compliance |
| Risk Managers | Use risk-library/ to build and maintain risk registers |

---

## Repository Structure

```
GRC-Toolkit/
├── regulations/          # Global regulatory requirements (HIPAA, GDPR, CCPA, etc.)
├── laws/                 # Applicable laws by jurisdiction
├── frameworks/           # Security frameworks (NIST, ISO, SOC 2, FedRAMP, CIS)
├── controls/             # Normalized control library with mappings
├── risk-library/         # Risk register templates and scenarios
├── audits/               # Audit programs, methodologies, checklists
├── evidence/             # Example audit evidence and artifacts
├── implementation-guides/ # Cloud-specific implementation guidance
├── responsibility-matrix/ # Shared responsibility models (SaaS/PaaS/IaaS)
├── mappings/             # Cross-framework control mappings
├── policies/             # Policy templates and modular policy components
├── ssp/                  # System Security Plan templates
├── assessments/          # Gap analysis and maturity scoring
├── automation/           # Scripts, compliance-as-code, detection rules
├── threat-mapping/       # MITRE ATT&CK and control alignment
├── data/                 # Machine-readable JSON data files
├── schemas/              # JSON schemas for data validation
├── playbooks/            # Incident response and compliance playbooks
├── integrations/         # GRC tool integrations (Jira, ServiceNow)
├── changelog/            # Framework and regulation change tracking
├── best-practices/       # Implementation best practices
├── anti-patterns/        # Common GRC anti-patterns to avoid
└── lessons-learned/      # Real-world lessons from compliance programs
```

---

## Quick Start

### 1. Find Controls for Your Framework

```bash
# Browse normalized controls
cat controls/normalized/unified-control-set.md

# View NIST to ISO 27001 mapping
cat mappings/nist-to-iso/nist-800-53-to-iso-27001.md
```

### 2. Use Machine-Readable Data

```bash
# Load all controls
cat data/controls.json | jq '.controls[] | select(.framework == "NIST-800-53")'

# Find risk-to-control mappings
cat data/mappings.json | jq '.mappings[] | select(.source_framework == "SOC2")'
```

### 3. Run Compliance Automation

```bash
# AWS evidence collection
python automation/scripts/aws-evidence-collector.py --profile default --output ./evidence/output

# Check S3 bucket compliance
python automation/scripts/aws-s3-compliance-check.py
```

### 4. Use Policy Templates

Copy and customize templates from `policies/templates/` for your organization. Each template includes:
- Purpose and scope
- Policy statements
- Roles and responsibilities
- Exceptions process
- Review cadence

---

## Supported Frameworks

| Framework | Version | Status |
|---|---|---|
| NIST SP 800-53 | Rev 5 | ✅ Complete |
| NIST CSF | 2.0 | ✅ Complete |
| ISO/IEC 27001 | 2022 | ✅ Complete |
| SOC 2 | 2017 TSC | ✅ Complete |
| FedRAMP | Rev 5 | ✅ Complete |
| CIS Controls | v8 | ✅ Complete |
| HIPAA | Current | 🔄 In Progress |
| PCI DSS | v4.0 | 🔄 In Progress |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Adding new frameworks
- Submitting control mappings
- Contributing automation scripts
- Reporting errors or outdated content

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

## Maintainers

This repository is maintained by the GRC community. See [CONTRIBUTING.md](CONTRIBUTING.md) to get involved.