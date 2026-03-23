---
name: control-mapping
description: Maps controls across cybersecurity frameworks using NIST IR 8477 Set-Theory Relationship Mapping (STRM). Use when helping with control implementation, compliance mapping, cross-framework alignment, or understanding control relationships.
---

When mapping controls:

1. Cross-reference NIST SP 800-53 control definitions with target frameworks
2. Identify baseline control families (AC, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, RA, SA, SC, SI, SR)
3. Use IR 8477 set-theory relationships to characterize mappings (equal, subset_of, superset_of, intersects_with, not_related)
4. Flag any control gaps or special framework-specific considerations
5. Provide implementation examples and rationale (syntactic, semantic, functional)
6. Include control enhancements and strength scores (1-10 STRM scale)

## NIST IR 8477 Methodology

Mappings follow IR 8477 Set-Theory Relationship Mapping (STRM):

- **Focal Document Element (FDE)**: The source control being mapped FROM
- **Reference Document Element (RDE)**: The target control being mapped TO
- **Relationship types**: equal (A=B), subset_of (A subset B), superset_of (A superset B), intersects_with (partial overlap), not_related (disjoint)
- **Rationale types**: syntactic (wording), semantic (meaning), functional (outcome)
- **Strength score**: 1-10 computed from relation type, confidence, and rationale
- **Transitivity**: Derive A to C from A to B and B to C chains using set-theory rules

## MCP Tools

When the `grc-mcp-server` is available, prefer these tools:

| MCP Tool | Use For |
|----------|---------|
| `grc_map_control` | Map controls between frameworks with IR 8477 set-theory relationships |
| `grc_strm_analyze` | Detailed IR 8477 STRM analysis (relation, rationale, strength, inverse) |
| `grc_transitive_map` | Derive transitive mappings using set-theory transitivity rules |
| `grc_strm_summary` | Distribution of relation/rationale/confidence across all mappings |
| `grc_reverse_map` | Find all source mappings for a target control |
| `grc_coverage_report` | Coverage percentage between source and target frameworks |
| `grc_get_oscal_control` | Extract full NIST/FedRAMP control details (statement, params, assessment) |
| `grc_lookup_control` | Control catalog lookup by ID |
| `grc_search_controls` | Full-text search across control catalog |

**Fallback**: If MCP tools are unavailable, read mapping files from `grc-pro/knowledge/mappings/` and OSCAL data from `grc-pro/knowledge/oscal/`.
