---
name: frmr-analysis
description: Analyzes FedRAMP FRMR documents to extract control mappings, KSI entries, and version changes. Use when the user asks about FedRAMP requirements, control mappings, compliance data, or needs to understand FRMR document content.
---

When analyzing FRMR documents:

1. Identify the document type (KSI, MAS, VDR, SCN, FRD, ADS, CCM, FSI, ICP, PVA, SCG, UCM)
2. Extract control mappings between NIST SP 800-53 and FedRAMP requirements
3. Identify Key Security Indicators (KSI) when relevant
4. Highlight significant changes between document versions
5. Map controls to specific compliance requirements
6. Provide citations to specific FRMR sections and item IDs

## MCP Tools

When the `grc-mcp-server` is available, prefer these tools:

| MCP Tool | Use For |
|----------|---------|
| `grc_map_control` | Map NIST controls to FedRAMP and other frameworks |
| `grc_strm_analyze` | IR 8477 STRM analysis of a mapping (relation, rationale, strength) |
| `grc_transitive_map` | Derive cross-framework mappings via an intermediary |
| `grc_lookup_control` | Look up control catalog entries by ID |
| `grc_search_controls` | Search controls by keyword |
| `grc_get_oscal_control` | Extract full OSCAL control data (statement, params, assessment) |
| `grc_coverage_report` | Analyze coverage between frameworks |

**Fallback**: If MCP tools are unavailable, read knowledge files from `grc-pro/knowledge/frameworks/` and `grc-pro/knowledge/mappings/`.
