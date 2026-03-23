"""OSCAL control access MCP tools."""

from __future__ import annotations

import json
from typing import Any


def register_oscal_tools(mcp_server: Any, data_loader: Any) -> None:
    """Register OSCAL access tools with the MCP server."""

    @mcp_server.tool()
    async def grc_get_oscal_control(catalog: str, control_id: str) -> str:
        """Extract a full OSCAL control record including statement, parameters, guidance, assessment objectives, and assessment methods.

        Args:
            catalog: OSCAL catalog name - either "nist-800-53-rev5" or "fedramp-moderate-rev5"
            control_id: Control ID (e.g., "ac-2", "AC-2", "ac-2.1", "AC-2(1)")
        """
        valid_catalogs = ["nist-800-53-rev5", "fedramp-moderate-rev5"]
        if catalog not in valid_catalogs:
            return json.dumps({
                "error": f"Invalid catalog '{catalog}'",
                "valid_catalogs": valid_catalogs,
            })

        ctrl = data_loader.get_oscal_control(catalog, control_id)
        if not ctrl:
            return json.dumps({"error": f"Control '{control_id}' not found in catalog '{catalog}'"})
        return json.dumps(ctrl, indent=2, default=str)

    @mcp_server.tool()
    async def grc_search_oscal(
        catalog: str,
        query: str,
        limit: int = 15,
    ) -> str:
        """Search OSCAL controls by keyword across prose, parameters, and guidance.

        Args:
            catalog: OSCAL catalog name - either "nist-800-53-rev5" or "fedramp-moderate-rev5"
            query: Search keywords (e.g., "encryption", "multi-factor", "audit log")
            limit: Maximum results to return (default 15)
        """
        valid_catalogs = ["nist-800-53-rev5", "fedramp-moderate-rev5"]
        if catalog not in valid_catalogs:
            return json.dumps({
                "error": f"Invalid catalog '{catalog}'",
                "valid_catalogs": valid_catalogs,
            })

        results = data_loader.search_oscal(catalog, query, limit)
        return json.dumps({"count": len(results), "query": query, "catalog": catalog, "results": results}, indent=2)
