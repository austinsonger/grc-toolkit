---
name: authoring
description: "Draft SSP sections, SAR responses, boundary definitions, inheritance models, OSCAL guidance, and multi-framework coverage analyses."
---

# Document Authoring

Assist with writing and drafting compliance artifacts including SSP sections, SAR responses, authorization boundary definitions, control inheritance documentation, OSCAL guidance, and multi-framework coverage analyses.

## Commands

| Command | Description |
|---------|-------------|
| `/grc:ssp-section` | SSP section-by-section writing guidance |
| `/grc:sar-response` | SAR finding response patterns and templates |
| `/grc:boundary-guidance` | Authorization boundary definition and diagram requirements |
| `/grc:inheritance` | Control inheritance analysis by service model |
| `/grc:oscal-guide` | OSCAL model guidance and best practices |
| `/grc:multi-framework` | Multi-framework comparison and coverage analysis |

## When to Use

Use this skill when the user needs to:
- Write or improve specific SSP sections
- Respond to SAR findings with appropriate remediation plans
- Define or document an authorization boundary
- Document control inheritance across service models (IaaS/PaaS/SaaS)
- Understand OSCAL formats and how to use them
- Compare control coverage across multiple frameworks

## Knowledge Files

- `grc-pro/knowledge/audits/document-section-requirements.md` — SSP, POA&M, policy section structure
- `grc-pro/knowledge/audits/sar-response-patterns.md` — SAR response templates
- `grc-pro/knowledge/audits/boundary-guidance.md` — Authorization boundary requirements
- `grc-pro/knowledge/audits/control-inheritance.md` — Inheritance patterns by service model
- `grc-pro/knowledge/frameworks/oscal-reference.md` — OSCAL model reference
- `grc-pro/knowledge/frameworks/*.md` — Framework-specific requirements
- `grc-pro/knowledge/mappings/cross-framework-matrix.md` — Cross-framework family index

## MCP Tools

When the `grc-mcp-server` is available:

| MCP Tool | Use For |
|----------|---------|
| `grc_get_oscal_control` | Get authoritative control statement, params, and assessment objectives for SSP writing |
| `grc_search_oscal` | Find OSCAL controls by keyword for multi-control SSP sections |
| `grc_lookup_control` | Control metadata for authoring context |
| `grc_map_control` | Cross-framework mapping for multi-framework coverage analysis |
| `grc_strm_analyze` | IR 8477 STRM detail for documenting cross-framework alignment rationale |
| `grc_coverage_report` | Analyze coverage gaps between frameworks |
| `grc_lookup_risk` | Risk context for SAR response drafting |

**Fallback**: If MCP tools are unavailable, read OSCAL JSON files from `grc-pro/knowledge/oscal/` and knowledge files from `grc-pro/knowledge/`.
