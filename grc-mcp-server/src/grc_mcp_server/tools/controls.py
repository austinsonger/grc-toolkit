"""Control catalog MCP tools."""

from __future__ import annotations

import json
from typing import Any


def register_control_tools(mcp_server: Any, data_loader: Any) -> None:
    """Register control catalog tools with the MCP server."""

    @mcp_server.tool()
    async def grc_lookup_control(control_id: str) -> str:
        """Look up a GRC Toolkit control by ID.

        Args:
            control_id: Control ID such as GOV-01, GOV-01.1, CTRL-AC-001
        """
        ctrl = data_loader.lookup_control(control_id)
        if not ctrl:
            return json.dumps({"error": f"Control '{control_id}' not found"})
        return json.dumps(ctrl, indent=2, default=str)

    @mcp_server.tool()
    async def grc_search_controls(
        query: str,
        domain: str = "",
        nist_csf_function: str = "",
        cadence: str = "",
        applicability: str = "",
        limit: int = 20,
    ) -> str:
        """Search GRC Toolkit controls by keyword with optional filters.

        Args:
            query: Search keywords (e.g., "encryption", "access control")
            domain: Filter by control domain (e.g., "Cybersecurity & Data Protection Governance")
            nist_csf_function: Filter by NIST CSF function (Govern, Identify, Protect, Detect, Respond, Recover)
            cadence: Filter by cadence (Annual, Quarterly, Semi-Annual)
            applicability: Filter by applicability (Data, Facility, People, Process, Technology)
            limit: Maximum results to return (default 20)
        """
        results = data_loader.search_controls(
            query=query,
            domain=domain or None,
            nist_csf_function=nist_csf_function or None,
            cadence=cadence or None,
            applicability=applicability or None,
            limit=limit,
        )
        summary = []
        for ctrl in results:
            summary.append({
                "control_id": ctrl.get("control_id"),
                "control_name": ctrl.get("control_name"),
                "control_domain": ctrl.get("control_domain"),
                "cadence": ctrl.get("cadence"),
                "nist_csf_function_grouping": ctrl.get("nist_csf_function_grouping"),
            })
        return json.dumps({"count": len(summary), "results": summary}, indent=2)

    @mcp_server.tool()
    async def grc_list_controls_by_domain(domain: str) -> str:
        """List all GRC Toolkit controls within a specific domain.

        Args:
            domain: Domain name or partial match (e.g., "Access Control", "Governance")
        """
        results = data_loader.list_controls_by_domain(domain)
        if not results:
            domains = data_loader.list_domains()
            return json.dumps({
                "error": f"No controls found for domain '{domain}'",
                "available_domains": domains,
            }, indent=2)
        summary = []
        for ctrl in results:
            summary.append({
                "control_id": ctrl.get("control_id"),
                "control_name": ctrl.get("control_name"),
                "cadence": ctrl.get("cadence"),
            })
        return json.dumps({"domain": domain, "count": len(summary), "controls": summary}, indent=2)
