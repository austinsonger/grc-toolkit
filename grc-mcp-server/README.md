# GRC MCP Server

MCP (Model Context Protocol) server providing structured data access for the GRC Toolkit.

## Tools

| Tool | Description |
|------|-------------|
| `grc_lookup_control` | Look up control by ID (GOV-01, CTRL-AC-001) |
| `grc_search_controls` | Full-text search with domain/CSF/cadence filters |
| `grc_list_controls_by_domain` | List controls in a domain |
| `grc_lookup_risk` | Look up risk by ID |
| `grc_search_risks` | Search risks by keyword or mapped control |
| `grc_lookup_threat` | Look up threat by ID |
| `grc_map_control` | Cross-framework control mapping |
| `grc_reverse_map` | Reverse mapping lookup |
| `grc_coverage_report` | Coverage analysis between frameworks |
| `grc_get_oscal_control` | Extract OSCAL control (NIST/FedRAMP) |
| `grc_search_oscal` | Search OSCAL control prose |
| `grc_list_fetchers` | List evidence fetchers by platform |
| `grc_run_fetcher` | Execute an evidence fetcher script |

## Installation

```bash
pip install -e grc-mcp-server/
```

## Usage

```bash
# Run directly
grc-mcp-server

# Or as a module
python -m grc_mcp_server
```

## Configuration

Set `GRC_REPO_ROOT` to the repository root if running from a non-standard location.
Defaults to auto-detection relative to the package location.
