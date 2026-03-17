# GRC-Toolkit

A comprehensive, scalable, and operational Governance, Risk, and Compliance (GRC) platform repository designed for engineering teams, auditors, and compliance operators.

This repository is not a static reference library. It is structured for day-to-day compliance execution, including:
- Cross-framework control normalization (SOC 2, ISO 27001, NIST, FedRAMP, CIS)
- Risk-to-control mapping
- Audit planning and evidence collection
- Implementation guidance for cloud environments
- Compliance-as-code and detection engineering

## Target Audience
- GRC engineers building and operating compliance programs
- Internal and external auditors performing assessments
- Security engineering teams implementing controls
- Compliance program managers maintaining continuous readiness

## Core Capabilities
- Centralized regulations, laws, frameworks, and updates
- Normalized control catalog with machine-readable data models
- Mappings and crosswalks between major frameworks
- Risk library tied directly to control implementation
- Evidence and audit artifacts designed for repeatable assessments
- Automation scripts and policy-as-code guardrails

## Repository Structure

- `regulations/`: Regulatory obligations by geography
- `laws/`: Legal requirements and statutory references
- `frameworks/`: Canonical control framework source material
- `controls/`: Unified control taxonomy, baselines, enhancements, mappings
- `risk-library/`: Risk scenarios and risk-to-control relationships
- `audits/`: Methodologies, checklists, and audit programs
- `evidence/`: Example artifacts and evidence handling patterns
- `implementation-guides/`: Practical implementation guidance by platform
- `responsibility-matrix/`: Shared responsibility models across SaaS/PaaS/IaaS
- `mappings/`: Cross-framework mapping packs
- `policies/`: Reusable policy templates and modular policy components
- `ssp/`: System Security Plan templates and reusable sections
- `assessments/`: Gap analysis templates and scoring models
- `automation/`: Scripts, compliance-as-code, and detections
- `threat-mapping/`: ATT&CK-to-control and threat-control alignment
- `data/`: Machine-readable datasets (`controls.json`, `*_mappings.json`, `risks.json`, `threats.json`)
- `schemas/`: JSON schemas for data quality and automation pipelines
- `playbooks/`: Operational playbooks for evidence and incident response support
- `integrations/`: Jira/ServiceNow integration examples
- `changelog/`: Time-based updates for framework/regulation changes
- `best-practices/`, `anti-patterns/`, `lessons-learned/`: Program maturity guidance

## How To Use
1. Start with `controls/normalized/unified-controls.yaml` and `data/controls.json` as the source of truth.
2. Use `mappings/` and `data/*_mappings.json` files to build cross-framework coverage reports.
3. Use `risk-library/` and `data/risks.json` to prioritize implementation by risk.
4. Use `data/threats.json` to incorporate natural and man-made threat scenarios into risk and resilience analysis.
5. Implement controls using `implementation-guides/` and `automation/compliance-as-code/`.
6. Collect evidence using `automation/scripts/` and store outputs in `evidence/artifacts/`.
7. Run audits using checklists in `audits/` and templates in `assessments/`.

## Data Standards
- Control IDs use canonical form: `CTRL-<DOMAIN>-<NUMBER>` (example: `CTRL-AC-001`)
- Framework references use native IDs (example: `NIST SP 800-53 Rev.5 AC-2`, `ISO/IEC 27001:2022 A.5.15`)
- Risk IDs use `RISK-<DOMAIN>-<NUMBER>`
- Mappings are directional with rationale and confidence metadata

## Quick Start
```bash
cd GRC-Toolkit
jq . data/controls.json > /dev/null
jq . data/*_mappings.json > /dev/null
jq . data/risks.json > /dev/null
jq . data/threats.json > /dev/null
bash automation/scripts/aws_collect_evidence.sh --help
```

## License
This repository is released under the Apache-2.0 License.
