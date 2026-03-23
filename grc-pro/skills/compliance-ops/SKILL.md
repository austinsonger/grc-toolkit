---
name: compliance-ops
description: "Operational compliance workflows: continuous monitoring, calendaring, POA&M management, change management, and framework transitions."
---

# Compliance Operations

Manage day-to-day compliance operations including continuous monitoring, compliance calendaring, POA&M lifecycle, significant change analysis, deviation requests, and framework version transitions.

## Commands

| Command | Description |
|---------|-------------|
| `/grc:compliance-calendar` | Recurring compliance activities by framework and frequency |
| `/grc:conmon-guide` | Continuous monitoring guidance |
| `/grc:poam-help` | POA&M management guidance |
| `/grc:significant-change` | Significant change criteria analysis |
| `/grc:deviation-request` | Deviation request templates |
| `/grc:rev5-transition` | NIST Rev 4 to Rev 5 transition guide |

## When to Use

Use this skill when the user needs to:
- Plan monthly/quarterly/annual compliance activities
- Set up or improve continuous monitoring (ConMon) workflows
- Manage POA&M items (create, track, close, report)
- Determine if a change qualifies as "significant" under FedRAMP
- Draft deviation requests
- Transition from NIST Rev 4 to Rev 5

## Knowledge Files

- `grc-pro/knowledge/conmon/*.md` — ISCM lifecycle, monthly/annual deliverables, automated tooling
- `grc-pro/knowledge/conmon/compliance-calendar.md` — Consolidated compliance calendar
- `grc-pro/knowledge/conmon/poam-management.md` — POA&M lifecycle and severity timelines
- `grc-pro/knowledge/audits/significant-change-criteria.md` — FedRAMP significant change categories

## MCP Tools

When the `grc-mcp-server` is available:

| MCP Tool | Use For |
|----------|---------|
| `grc_lookup_control` | Control details for POA&M item context |
| `grc_lookup_risk` | Risk details when assessing POA&M severity |
| `grc_search_risks` | Find risks related to specific controls for change analysis |
| `grc_map_control` | Map controls across frameworks during transitions |
| `grc_list_fetchers` | List available evidence fetcher scripts for ConMon automation |
| `grc_run_fetcher` | Execute evidence collection scripts for ConMon deliverables |

**Fallback**: If MCP tools are unavailable, read knowledge files directly from `grc-pro/knowledge/conmon/`.
