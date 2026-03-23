"""Cross-framework mapping MCP tools with IR 8477 STRM support."""

from __future__ import annotations

import json
from typing import Any


def register_mapping_tools(mcp_server: Any, data_loader: Any) -> None:
    """Register cross-framework mapping tools with the MCP server."""

    @mcp_server.tool()
    async def grc_map_control(
        source_framework: str,
        source_control: str,
        target_framework: str = "",
    ) -> str:
        """Map a source control to target framework(s) with set-theory relationships.

        Returns mappings including IR 8477 STRM data: relation type, rationale,
        confidence, and computed strength score (1-10).

        Args:
            source_framework: Source framework (Focal Document). Accepts short names
                (nist, iso-27001, soc2, pci, hipaa, cis, cmmc, cobit, ccm, gdpr)
                or full names (e.g., "NIST SP 800-53 Rev.5").
            source_control: Source control ID (e.g., "AC-2")
            target_framework: Optional target framework (Reference Document) filter.
        """
        results = data_loader.get_mapping_relationships(
            source_framework=source_framework,
            source_control=source_control,
            target_framework=target_framework or None,
        )
        if not results:
            return json.dumps({
                "error": f"No mappings found for {source_framework} {source_control}",
                "hint": "Accepts short names (nist, iso-27001, soc2, pci, hipaa, cis, cmmc, cobit, ccm, gdpr) or full names.",
            })
        return json.dumps({"count": len(results), "mappings": results}, indent=2, default=str)

    @mcp_server.tool()
    async def grc_reverse_map(
        target_framework: str,
        target_control: str,
    ) -> str:
        """Find all source framework controls that map to a target control.

        Args:
            target_framework: Target framework (Reference Document). Accepts short
                or full names.
            target_control: Target control ID (e.g., "A.5.15")
        """
        results = data_loader.reverse_map(
            target_framework=target_framework,
            target_control=target_control,
        )
        if not results:
            return json.dumps({"error": f"No reverse mappings found for {target_framework} {target_control}"})
        return json.dumps({"count": len(results), "mappings": results}, indent=2, default=str)

    @mcp_server.tool()
    async def grc_coverage_report(
        source_framework: str,
        source_controls: list[str],
        target_framework: str,
    ) -> str:
        """Compute coverage of source controls against a target framework.

        Args:
            source_framework: Source framework name.
            source_controls: List of source control IDs (e.g., ["AC-2", "AU-6", "SC-7"])
            target_framework: Target framework to check coverage against.
        """
        report = data_loader.coverage_report(
            source_framework=source_framework,
            source_controls=source_controls,
            target_framework=target_framework,
        )
        return json.dumps(report, indent=2, default=str)

    @mcp_server.tool()
    async def grc_strm_analyze(
        source_framework: str,
        source_control: str,
        target_framework: str = "",
    ) -> str:
        """Analyze a control mapping using NIST IR 8477 Set-Theory Relationship Mapping.

        Returns detailed IR 8477 STRM analysis including:
        - Primary set-theory relation (equal, subset_of, superset_of, intersects_with, not_related)
        - Rationale type (syntactic, semantic, functional)
        - Strength score (1-10 scale)
        - Inverse relation (what the target maps back as)
        - All set-theory relationships on the mapping

        Args:
            source_framework: Source framework (Focal Document Element).
            source_control: Source control ID.
            target_framework: Optional target framework (Reference Document Element).
        """
        results = data_loader.get_mapping_relationships(
            source_framework=source_framework,
            source_control=source_control,
            target_framework=target_framework or None,
        )
        if not results:
            return json.dumps({
                "error": f"No STRM data for {source_framework} {source_control}",
                "hint": "Use grc_map_control first to check if a mapping exists.",
            })
        # Extract just the IR 8477 analysis
        analysis = []
        for r in results:
            analysis.append({
                "source": f"{r.get('source_framework')} {r.get('source_control')}",
                "target": f"{r.get('target_framework')} {r.get('target_control')}",
                **r.get("ir8477", {}),
            })
        return json.dumps({
            "methodology": "NIST IR 8477 Set-Theory Relationship Mapping (STRM)",
            "count": len(analysis),
            "analysis": analysis,
        }, indent=2, default=str)

    @mcp_server.tool()
    async def grc_transitive_map(
        source_framework: str,
        source_control: str,
        target_framework: str,
        via_framework: str = "",
    ) -> str:
        """Find transitive mappings using IR 8477 set-theory transitivity rules.

        Derives A->C mappings from A->B and B->C chains. Uses set-theory
        transitivity (e.g., subset + subset = subset) to compute the derived
        relationship. Reports when the result is indeterminate.

        Args:
            source_framework: Source framework (e.g., "soc2")
            source_control: Source control ID (e.g., "CC6.1")
            target_framework: Target framework (e.g., "iso-27001")
            via_framework: Optional intermediary framework (defaults to trying all)
        """
        results = data_loader.find_transitive_mappings(
            source_framework=source_framework,
            source_control=source_control,
            target_framework=target_framework,
            via_framework=via_framework or None,
        )
        if not results:
            return json.dumps({
                "error": f"No transitive path from {source_framework} {source_control} to {target_framework}",
                "hint": "A direct mapping may exist — try grc_map_control instead.",
            })
        return json.dumps({
            "methodology": "NIST IR 8477 transitive set-theory derivation",
            "count": len(results),
            "transitive_mappings": results,
        }, indent=2, default=str)

    @mcp_server.tool()
    async def grc_strm_summary() -> str:
        """Return an IR 8477 STRM summary of all loaded cross-framework mappings.

        Shows distribution of relationship types, rationale types, and confidence
        levels across all mapping data, plus the list of mapped frameworks.
        """
        summary = data_loader.strm_summary()
        return json.dumps(summary, indent=2, default=str)
