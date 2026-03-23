---
name: control-ops
description: "Control lookup, cross-framework mapping, search, and coverage analysis across 15 compliance frameworks."
---

# Control Operations

Search, look up, map, and analyze controls across NIST 800-53, FedRAMP, SOC 2, ISO 27001, PCI DSS, HIPAA, CIS Controls, CMMC, COBIT, CSA CCM, and GDPR.

## Commands

| Command | Description |
|---------|-------------|
| `/grc:control-lookup` | Look up controls by framework and ID or keyword |
| `/grc:map-controls` | Cross-framework control mapping (NIST as hub) |
| `/grc:list-controls` | List NIST controls from FRMR documents |
| `/grc:control-coverage` | Analyze control coverage across baselines |
| `/grc:control-requirements` | Get detailed control requirement info |
| `/grc:get-requirement` | Retrieve a specific requirement by ID |
| `/grc:filter-impact` | Filter controls by impact level |
| `/grc:list-ksi` | List FedRAMP Key Security Indicators |
| `/grc:theme-summary` | Summarize controls by framework theme |
| `/grc:search` | Search FedRAMP documentation |
| `/grc:search-definitions` | Search control definitions |
| `/grc:list-documents` | List compliance documents |

## When to Use

Use this skill when the user needs to:
- Find a specific control by ID (e.g., AC-2, CC6.1, A.8.1)
- Search for controls related to a topic (e.g., "encryption", "logging")
- Map controls between frameworks (e.g., NIST AC-2 to ISO 27001)
- Understand control requirements, assessment objectives, and methods
- Analyze coverage or gaps in control implementation

## Knowledge Files

- `grc-pro/knowledge/frameworks/*.md` — Framework reference files
- `grc-pro/knowledge/mappings/*.md` — Cross-framework mapping tables
- `grc-pro/knowledge/oscal/nist-800-53-rev5/*.json` — NIST 800-53 OSCAL data
- `grc-pro/knowledge/oscal/fedramp-moderate-rev5/*.json` — FedRAMP OSCAL data
- `grc-pro/config/control-families.json` — Control family metadata

## MCP Tools

When the `grc-mcp-server` is available, prefer these MCP tools over direct file reading:

| MCP Tool | Use For |
|----------|---------|
| `grc_get_oscal_control` | NIST/FedRAMP control lookups (statement, params, assessment objectives/methods) |
| `grc_lookup_control` | Control catalog lookups by ID (GOV-01, CTRL-AC-001) |
| `grc_search_controls` | Full-text search across control catalog |
| `grc_map_control` | Cross-framework mapping with IR 8477 set-theory relationships |
| `grc_strm_analyze` | Detailed IR 8477 STRM analysis (relation type, rationale, strength score) |
| `grc_transitive_map` | Derive indirect mappings through an intermediary framework |
| `grc_strm_summary` | Distribution of STRM relationship types across all mappings |
| `grc_reverse_map` | Find all source mappings for a target control |
| `grc_search_oscal` | Keyword search across OSCAL control prose |

**Fallback**: If MCP tools are unavailable, read the OSCAL JSON files directly from `grc-pro/knowledge/oscal/` using offset/limit for large files.
