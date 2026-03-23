"""Risk and threat MCP tools."""

from __future__ import annotations

import json
from typing import Any


def register_risk_tools(mcp_server: Any, data_loader: Any) -> None:
    """Register risk and threat tools with the MCP server."""

    @mcp_server.tool()
    async def grc_lookup_risk(risk_id: str) -> str:
        """Look up a risk scenario by ID.

        Args:
            risk_id: Risk ID such as RISK-AC-001, RISK-AU-002
        """
        risk = data_loader.lookup_risk(risk_id)
        if not risk:
            return json.dumps({"error": f"Risk '{risk_id}' not found"})
        return json.dumps(risk, indent=2, default=str)

    @mcp_server.tool()
    async def grc_search_risks(
        query: str = "",
        mapped_control: str = "",
        limit: int = 20,
    ) -> str:
        """Search risk scenarios by keyword or mapped control ID.

        Args:
            query: Search keywords (e.g., "privileged access", "data loss")
            mapped_control: Filter by mapped control ID (e.g., "CTRL-AC-001")
            limit: Maximum results to return (default 20)
        """
        results = data_loader.search_risks(
            query=query or None,
            mapped_control=mapped_control or None,
            limit=limit,
        )
        summary = []
        for risk in results:
            summary.append({
                "risk_id": risk.get("risk_id"),
                "title": risk.get("title"),
                "likelihood": risk.get("likelihood"),
                "impact": risk.get("impact"),
                "mapped_controls": risk.get("mapped_controls", []),
            })
        return json.dumps({"count": len(summary), "results": summary}, indent=2)

    @mcp_server.tool()
    async def grc_lookup_threat(threat_id: str) -> str:
        """Look up a threat scenario by ID.

        Args:
            threat_id: Threat ID such as THREAT-NT-001, THREAT-MT-002
        """
        threat = data_loader.lookup_threat(threat_id)
        if not threat:
            return json.dumps({"error": f"Threat '{threat_id}' not found"})
        return json.dumps(threat, indent=2, default=str)
