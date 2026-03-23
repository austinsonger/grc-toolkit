---
name: audit-assess
description: "Audit preparation, evidence checklists, assessment simulation, gap analysis, and maturity scoring."
---

# Audit & Assessment

Prepare for audits, generate evidence checklists, simulate 3PAO assessments, conduct gap analyses, and score organizational maturity.

## Commands

| Command | Description |
|---------|-------------|
| `/grc:audit-prep` | Audit preparation guidance by framework |
| `/grc:evidence-checklist` | Generate evidence requirement checklists by control |
| `/grc:evidence-examples` | Evidence examples by control |
| `/grc:3pao-dryrun` | Simulate a FedRAMP 3PAO assessment |
| `/grc:pmo-review` | PMO review templates |
| `/grc:isora-assess` | ISORA assessment guidance |
| `/grc:score-maturity` | Maturity scoring on 0-5 scale |
| `/grc:gap-analysis` | Structured gap analysis by framework and scope |

## When to Use

Use this skill when the user needs to:
- Prepare for an upcoming audit (FedRAMP, SOC 2, ISO, PCI)
- Generate evidence checklists for specific controls
- Simulate a 3PAO assessment dry run
- Conduct a gap analysis against a framework baseline
- Score maturity of their compliance program

## Knowledge Files

- `grc-pro/knowledge/audits/*.md` — All audit guidance (3PAO, SOC 2, ISO, PCI QSA, internal, gap analysis)
- `grc-pro/knowledge/audits/narrative-quality-criteria.md` — Maturity scoring rubric
- `grc-pro/knowledge/frameworks/*.md` — Framework requirements context
- `grc-pro/config/guardrails.md` — Operational principles

## MCP Tools

When the `grc-mcp-server` is available:

| MCP Tool | Use For |
|----------|---------|
| `grc_get_oscal_control` | Extract assessment objectives and methods for evidence checklists |
| `grc_lookup_risk` | Risk context for gap analysis |
| `grc_search_risks` | Find risks related to specific controls |
| `grc_coverage_report` | Coverage analysis between frameworks |
| `grc_strm_analyze` | IR 8477 STRM analysis to understand mapping strength and gaps |
| `grc_map_control` | Cross-framework mapping for multi-framework audits |
