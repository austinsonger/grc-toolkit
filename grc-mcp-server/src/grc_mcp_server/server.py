"""GRC MCP Server - Main entry point.

Provides structured data access for the GRC Toolkit via the Model Context Protocol.
Exposes tools for control lookups, risk/threat queries, cross-framework mappings
with NIST IR 8477 STRM support, OSCAL control extraction, and evidence fetcher execution.
"""

from __future__ import annotations

import logging
from mcp.server.fastmcp import FastMCP

from .data_loader import DataLoader
from .tools.controls import register_control_tools
from .tools.risks import register_risk_tools
from .tools.mappings import register_mapping_tools
from .tools.oscal import register_oscal_tools
from .tools.fetchers import register_fetcher_tools

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def create_server() -> FastMCP:
    """Create and configure the GRC MCP server."""
    server = FastMCP(
        "grc-toolkit",
        instructions="GRC Toolkit MCP Server - Structured access to controls, risks, threats, OSCAL data, cross-framework mappings, and evidence fetchers.",
    )

    # Load data
    loader = DataLoader()
    loader.load_all()

    # Register all tool groups
    register_control_tools(server, loader)
    register_risk_tools(server, loader)
    register_mapping_tools(server, loader)
    register_oscal_tools(server, loader)
    register_fetcher_tools(server, loader)

    logger.info("GRC MCP Server ready with all tools registered")
    return server


def main() -> None:
    """Run the GRC MCP server."""
    server = create_server()
    server.run()


if __name__ == "__main__":
    main()
