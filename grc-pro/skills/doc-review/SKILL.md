---
name: doc-review
description: "Review SSPs, narratives, POA&Ms, policies, and CRMs for structural completeness and quality."
---

# Document Review

Review compliance documents for structural completeness, quality, and adherence to framework requirements. All reviews focus on structure, not security — assessing whether documents say enough, not whether described systems are secure.

## Commands

| Command | Description |
|---------|-------------|
| `/grc:review-ssp` | Validate SSP structure, section completeness, diagrams, appendices |
| `/grc:review-narrative` | Control narrative quality review (Five W's: What, Who, How, When, Where) |
| `/grc:review-poam` | POA&M document review |
| `/grc:review-policy` | Policy document review |
| `/grc:review-crm` | Customer Responsibility Matrix review |

## When to Use

Use this skill when the user shares a compliance document and wants feedback on:
- Whether required sections are present and complete
- Narrative quality against the Five W's rubric
- POA&M formatting and milestone tracking
- Policy structure and coverage
- CRM completeness and clarity

## Redaction Notice

All document review commands MUST display this notice at the top of every response:

> **Before sharing GRC artifacts**: Consider replacing real system names, IP addresses, personnel names, agency names, and CVE IDs with generic placeholders (e.g., "[Agency Name]", "[System Name]", "10.x.x.x"). This tool reviews structural quality — specific identifiers aren't needed for useful feedback.

## Review Principles

1. **Structural focus** — Assess whether the document says enough, not whether the described system is secure
2. **No content judgment** — Never evaluate whether described security measures are adequate
3. **Safe to share** — Generic narratives, outlines, policy language, and templates are safe to review
4. **Redact before sharing** — Real CVEs, IPs, agency names, boundaries, and personnel names should be replaced

## Knowledge Files

- `grc-pro/knowledge/audits/narrative-quality-criteria.md` — Five W's rubric + maturity 0-5 scale
- `grc-pro/knowledge/audits/document-section-requirements.md` — SSP, POA&M, policy, CRM structure
- `grc-pro/knowledge/audits/sar-response-patterns.md` — SAR response quality checklist
- `grc-pro/config/guardrails.md` — Operational principles

## MCP Tools

When the `grc-mcp-server` is available:

| MCP Tool | Use For |
|----------|---------|
| `grc_get_oscal_control` | Look up control statement text when reviewing narrative completeness |
| `grc_lookup_control` | Get control metadata for context during reviews |
| `grc_search_controls` | Find related controls when a narrative references multiple controls |
| `grc_lookup_risk` | Risk context when reviewing POA&M entries |

**Fallback**: If MCP tools are unavailable, read knowledge files directly from `grc-pro/knowledge/audits/`.
