---
name: scanners
description: "Compliance code scanning for HIPAA, GDPR, AI, government enterprise, and multi-standard frameworks."
---

# Compliance Scanners

Run focused compliance scans against codebases to identify regulatory gaps, missing controls, and common deficiencies. Each scanner provides regex patterns, critical file checklists, common deficiency examples, and remediation guidance.

## Scanners

| Scanner | Trigger | Description |
|---------|---------|-------------|
| `ai-compliance` | AI/ML, LLM, model governance | AI system compliance checks |
| `gdpr-compliance` | GDPR, EU data, personal data | GDPR personal data handling |
| `gov-enterprise` | FedRAMP, federal, government | Federal enterprise compliance |
| `hipaa-compliance` | HIPAA, PHI, healthcare | Comprehensive HIPAA checks |
| `hipaa-hitrust` | HITRUST, HIPAA+HITRUST | HIPAA with HITRUST alignment |
| `hipaa-quick-scan` | Quick HIPAA check | Fast PHI detection reference |
| `multi-standard` | Multiple frameworks, SOC 2+ISO | Multi-framework scanning |

## When to Use

Use this skill when the user wants to:
- Scan a codebase for compliance issues against a specific framework
- Identify PHI/PII handling gaps
- Check for AI governance requirements
- Run a multi-standard compliance assessment
- Get remediation guidance for common deficiencies

## How to Route

Match the user's request to the appropriate scanner file:
- HIPAA mentions → Start with `hipaa-compliance.md`, use `hipaa-quick-scan.md` for fast checks
- GDPR/EU mentions → Use `gdpr-compliance.md`
- AI/ML/LLM mentions → Use `ai-compliance.md`
- Federal/FedRAMP mentions → Use `gov-enterprise.md`
- Multiple frameworks or SOC 2+ISO → Use `multi-standard.md`
- HITRUST mentions → Use `hipaa-hitrust.md`
