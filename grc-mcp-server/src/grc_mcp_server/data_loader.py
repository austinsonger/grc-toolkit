"""Data loader for GRC Toolkit JSON datasets.

Loads controls, risks, threats, mappings, and OSCAL data into memory
with dictionary indexes for fast lookup.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any

from .utils import resolve_repo_root, tokenize
from .ir8477 import (
    ControlMapping,
    RelationType,
    RationaleType,
    Confidence,
    SetTheoryRelationship,
    infer_inverse_relation,
    derive_transitive_relation,
    compute_mapping_strength,
)

logger = logging.getLogger(__name__)

# Framework name aliases for user-friendly lookups
_FRAMEWORK_ALIASES: dict[str, str] = {
    "NIST-800-53": "NIST SP 800-53 REV.5",
    "NIST 800-53": "NIST SP 800-53 REV.5",
    "NIST": "NIST SP 800-53 REV.5",
    "800-53": "NIST SP 800-53 REV.5",
    "ISO-27001": "ISO/IEC 27001:2022",
    "ISO27001": "ISO/IEC 27001:2022",
    "ISO 27001": "ISO/IEC 27001:2022",
    "ISO": "ISO/IEC 27001:2022",
    "SOC2": "SOC 2",
    "SOC-2": "SOC 2",
    "PCI-DSS": "PCI DSS V4.0.1",
    "PCI": "PCI DSS V4.0.1",
    "HIPAA": "HIPAA",
    "CIS": "CIS CONTROLS V8.1",
    "CIS-CONTROLS": "CIS CONTROLS V8.1",
    "CMMC": "CMMC 2.0",
    "CMMC-2": "CMMC 2.0",
    "800-171": "NIST SP 800-171 REV.2",
    "NIST-800-171": "NIST SP 800-171 REV.2",
    "COBIT": "COBIT 2019",
    "CSA-CCM": "CSA CCM V4",
    "CCM": "CSA CCM V4",
    "GDPR": "GDPR",
    "FEDRAMP": "FEDRAMP",
}


class DataLoader:
    """Loads and indexes GRC Toolkit JSON data for fast queries."""

    def __init__(self) -> None:
        self._repo_root = Path(os.environ.get("GRC_REPO_ROOT", str(resolve_repo_root())))
        self._data_dir = self._repo_root / "data"
        self._grc_pro_dir = self._repo_root / "grc-pro"

        # Control catalog
        self._controls_by_id: dict[str, dict] = {}
        self._controls_by_domain: dict[str, list[dict]] = {}
        self._controls_list: list[dict] = []

        # Risks and threats
        self._risks_by_id: dict[str, dict] = {}
        self._risks_list: list[dict] = []
        self._threats_by_id: dict[str, dict] = {}
        self._threats_list: list[dict] = []

        # Mappings
        self._mappings: list[dict] = []
        self._mappings_by_source: dict[str, list[dict]] = {}
        self._mappings_by_target: dict[str, list[dict]] = {}
        self._typed_mappings: list[ControlMapping] = []

        # OSCAL (lazy loaded)
        self._oscal_cache: dict[str, dict] = {}

        self._loaded = False

    def load_all(self) -> None:
        """Load all JSON datasets into memory."""
        if self._loaded:
            return

        self._load_controls()
        self._load_risks()
        self._load_threats()
        self._load_mappings()
        self._loaded = True
        logger.info(
            "Data loaded: %d controls, %d risks, %d threats, %d mappings",
            len(self._controls_by_id),
            len(self._risks_by_id),
            len(self._threats_by_id),
            len(self._mappings),
        )

    def _load_controls(self) -> None:
        """Load controls.json and build indexes."""
        path = self._data_dir / "controls.json"
        if not path.exists():
            logger.warning("controls.json not found at %s", path)
            return

        data = json.loads(path.read_text(encoding="utf-8"))

        # Index grctoolkit_controls
        for ctrl in data.get("grctoolkit_controls", []):
            cid = ctrl.get("control_id", "").upper()
            if cid:
                self._controls_by_id[cid] = ctrl
                self._controls_list.append(ctrl)
                domain = ctrl.get("control_domain", "Unknown")
                self._controls_by_domain.setdefault(domain, []).append(ctrl)

        # Index canonical controls
        for ctrl in data.get("controls", []):
            cid = ctrl.get("control_id", "").upper()
            if cid:
                self._controls_by_id[cid] = ctrl
                self._controls_list.append(ctrl)

    def _load_risks(self) -> None:
        """Load risks.json and build index."""
        path = self._data_dir / "risks.json"
        if not path.exists():
            logger.warning("risks.json not found at %s", path)
            return

        data = json.loads(path.read_text(encoding="utf-8"))
        for risk in data.get("risks", []):
            rid = risk.get("risk_id", "")
            if rid:
                self._risks_by_id[rid] = risk
                self._risks_list.append(risk)

    def _load_threats(self) -> None:
        """Load threats.json and build index."""
        path = self._data_dir / "threats.json"
        if not path.exists():
            logger.warning("threats.json not found at %s", path)
            return

        data = json.loads(path.read_text(encoding="utf-8"))
        for threat in data.get("threats", []):
            tid = threat.get("threat_id", "")
            if tid:
                self._threats_by_id[tid] = threat
                self._threats_list.append(threat)

    def _load_mappings(self) -> None:
        """Load all mapping JSON files from data/mappings/."""
        mappings_dir = self._data_dir / "mappings"
        if not mappings_dir.exists():
            logger.warning("mappings directory not found at %s", mappings_dir)
            return

        for json_file in mappings_dir.rglob("*.json"):
            try:
                data = json.loads(json_file.read_text(encoding="utf-8"))
                for m in data.get("mappings", []):
                    self._mappings.append(m)
                    self._typed_mappings.append(ControlMapping.from_dict(m))
                    src_key = f"{m.get('source_framework', '')}::{m.get('source_control', '')}".upper()
                    tgt_key = f"{m.get('target_framework', '')}::{m.get('target_control', '')}".upper()
                    self._mappings_by_source.setdefault(src_key, []).append(m)
                    self._mappings_by_target.setdefault(tgt_key, []).append(m)
            except (json.JSONDecodeError, OSError) as e:
                logger.warning("Failed to load mapping file %s: %s", json_file, e)

    @staticmethod
    def _resolve_framework(name: str) -> str:
        """Resolve a framework alias to the canonical name used in mapping data."""
        return _FRAMEWORK_ALIASES.get(name.upper(), name.upper())

    # ── Control queries ──────────────────────────────────────────────

    def lookup_control(self, control_id: str) -> dict | None:
        """Look up a control by ID (case-insensitive)."""
        return self._controls_by_id.get(control_id.upper())

    def search_controls(
        self,
        query: str,
        domain: str | None = None,
        nist_csf_function: str | None = None,
        cadence: str | None = None,
        applicability: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """Full-text search across controls with optional filters."""
        results: list[dict] = []
        for ctrl in self._controls_list:
            # Apply filters
            if domain and ctrl.get("control_domain", "").lower() != domain.lower():
                continue
            if nist_csf_function and ctrl.get("nist_csf_function_grouping", "").lower() != nist_csf_function.lower():
                continue
            if cadence and ctrl.get("cadence", "").lower() != cadence.lower():
                continue
            if applicability and ctrl.get("applicability", "").lower() != applicability.lower():
                continue

            # Text search across name, description, domain
            searchable = " ".join([
                ctrl.get("control_id", ""),
                ctrl.get("control_name", ""),
                ctrl.get("control_description", ""),
                ctrl.get("control_domain", ""),
            ])
            query_tokens = tokenize(query)
            searchable_lower = searchable.lower()
            if all(t in searchable_lower for t in query_tokens):
                results.append(ctrl)
                if len(results) >= limit:
                    break

        return results

    def list_controls_by_domain(self, domain: str) -> list[dict]:
        """List all controls in a domain."""
        # Try exact match first
        if domain in self._controls_by_domain:
            return self._controls_by_domain[domain]
        # Try case-insensitive partial match
        domain_lower = domain.lower()
        for key, ctrls in self._controls_by_domain.items():
            if domain_lower in key.lower():
                return ctrls
        return []

    def list_domains(self) -> list[str]:
        """List all control domains."""
        return sorted(self._controls_by_domain.keys())

    # ── Risk queries ─────────────────────────────────────────────────

    def lookup_risk(self, risk_id: str) -> dict | None:
        """Look up a risk by ID."""
        return self._risks_by_id.get(risk_id.upper())

    def search_risks(
        self,
        query: str | None = None,
        mapped_control: str | None = None,
        limit: int = 20,
    ) -> list[dict]:
        """Search risks by keyword or mapped control ID."""
        results: list[dict] = []
        for risk in self._risks_list:
            if mapped_control:
                mapped = [c.upper() for c in risk.get("mapped_controls", [])]
                if mapped_control.upper() not in mapped:
                    continue
            if query:
                searchable = " ".join([
                    risk.get("risk_id", ""),
                    risk.get("title", ""),
                    risk.get("description", ""),
                ])
                query_tokens = tokenize(query)
                if not all(t in searchable.lower() for t in query_tokens):
                    continue
            results.append(risk)
            if len(results) >= limit:
                break
        return results

    # ── Threat queries ───────────────────────────────────────────────

    def lookup_threat(self, threat_id: str) -> dict | None:
        """Look up a threat by ID."""
        return self._threats_by_id.get(threat_id.upper())

    # ── Mapping queries ──────────────────────────────────────────────

    def map_control(
        self,
        source_framework: str,
        source_control: str,
        target_framework: str | None = None,
    ) -> list[dict]:
        """Map a source control to target framework(s)."""
        fw = self._resolve_framework(source_framework)
        key = f"{fw}::{source_control}".upper()
        results = self._mappings_by_source.get(key, [])
        if target_framework:
            tgt_fw = self._resolve_framework(target_framework)
            results = [m for m in results if m.get("target_framework", "").upper() == tgt_fw]
        return results

    def reverse_map(
        self,
        target_framework: str,
        target_control: str,
    ) -> list[dict]:
        """Find all source mappings for a target control."""
        fw = self._resolve_framework(target_framework)
        key = f"{fw}::{target_control}".upper()
        return self._mappings_by_target.get(key, [])

    def coverage_report(
        self,
        source_framework: str,
        source_controls: list[str],
        target_framework: str,
    ) -> dict:
        """Compute coverage of source controls against a target framework."""
        covered = 0
        uncovered: list[str] = []
        details: list[dict] = []

        for ctrl in source_controls:
            mappings = self.map_control(source_framework, ctrl, target_framework)
            if mappings:
                covered += 1
                details.append({
                    "source_control": ctrl,
                    "mapped": True,
                    "target_controls": [m.get("target_control") for m in mappings],
                })
            else:
                uncovered.append(ctrl)
                details.append({"source_control": ctrl, "mapped": False, "target_controls": []})

        total = len(source_controls)
        return {
            "source_framework": source_framework,
            "target_framework": target_framework,
            "total_controls": total,
            "covered": covered,
            "uncovered_count": len(uncovered),
            "coverage_percentage": round((covered / total * 100) if total > 0 else 0, 1),
            "uncovered_controls": uncovered,
            "details": details,
        }

    # ── IR 8477 STRM queries ─────────────────────────────────────────

    def get_mapping_relationships(
        self,
        source_framework: str,
        source_control: str,
        target_framework: str | None = None,
    ) -> list[dict]:
        """Get IR 8477 set-theory relationships for a control mapping.

        Returns enriched mapping data with STRM analysis including
        relation type, rationale, confidence, and computed strength score.
        """
        raw = self.map_control(source_framework, source_control, target_framework)
        results = []
        for m in raw:
            cm = ControlMapping.from_dict(m)
            strength = compute_mapping_strength(cm)
            results.append({
                **m,
                "ir8477": {
                    "primary_relation": cm.primary_relation.value,
                    "primary_rationale": cm.primary_rationale.value,
                    "strength_score": strength,
                    "inverse_relation": infer_inverse_relation(cm.primary_relation).value,
                    "set_theory_relationships": [r.to_dict() for r in cm.set_theory_relationships],
                },
            })
        return results

    def find_transitive_mappings(
        self,
        source_framework: str,
        source_control: str,
        target_framework: str,
        via_framework: str | None = None,
    ) -> list[dict]:
        """Find transitive mappings from source to target through an intermediary.

        Uses IR 8477 set-theory transitivity rules to derive A→C from A→B and B→C.
        If via_framework is not specified, tries all frameworks with data for source.
        """
        a_to_b_list = self.map_control(source_framework, source_control)
        if not a_to_b_list:
            return []

        results = []
        seen: set[str] = set()

        for a_to_b_raw in a_to_b_list:
            intermediate_fw = a_to_b_raw.get("target_framework", "")
            intermediate_ctrl = a_to_b_raw.get("target_control", "")

            if via_framework:
                resolved_via = self._resolve_framework(via_framework)
                if intermediate_fw.upper() != resolved_via:
                    continue

            b_to_c_list = self.map_control(intermediate_fw, intermediate_ctrl, target_framework)
            a_to_b = ControlMapping.from_dict(a_to_b_raw)

            for b_to_c_raw in b_to_c_list:
                b_to_c = ControlMapping.from_dict(b_to_c_raw)
                final_ctrl = b_to_c.target_control
                dedup_key = f"{final_ctrl}::{intermediate_fw}::{intermediate_ctrl}"
                if dedup_key in seen:
                    continue
                seen.add(dedup_key)

                derived = derive_transitive_relation(
                    a_to_b.primary_relation,
                    b_to_c.primary_relation,
                )

                # Use lowest confidence of the chain
                conf_order = ["low", "medium", "high"]
                a_conf = conf_order.index(a_to_b.confidence) if a_to_b.confidence in conf_order else 0
                b_conf = conf_order.index(b_to_c.confidence) if b_to_c.confidence in conf_order else 0
                chain_confidence = conf_order[min(a_conf, b_conf)]

                results.append({
                    "source_framework": source_framework,
                    "source_control": source_control,
                    "target_framework": target_framework,
                    "target_control": final_ctrl,
                    "via_framework": intermediate_fw,
                    "via_control": intermediate_ctrl,
                    "ir8477": {
                        "leg1_relation": a_to_b.primary_relation.value,
                        "leg2_relation": b_to_c.primary_relation.value,
                        "derived_relation": derived.value if derived else "indeterminate",
                        "chain_confidence": chain_confidence,
                        "is_definitive": derived is not None,
                    },
                })

        return results

    def strm_summary(self) -> dict:
        """Return an IR 8477 STRM summary of all loaded mappings."""
        relation_counts: dict[str, int] = {}
        rationale_counts: dict[str, int] = {}
        confidence_counts: dict[str, int] = {}
        frameworks: set[str] = set()

        for cm in self._typed_mappings:
            rel = cm.primary_relation.value
            rat = cm.primary_rationale.value
            relation_counts[rel] = relation_counts.get(rel, 0) + 1
            rationale_counts[rat] = rationale_counts.get(rat, 0) + 1
            confidence_counts[cm.confidence] = confidence_counts.get(cm.confidence, 0) + 1
            frameworks.add(cm.source_framework)
            frameworks.add(cm.target_framework)

        return {
            "total_mappings": len(self._typed_mappings),
            "frameworks": sorted(frameworks),
            "relation_distribution": relation_counts,
            "rationale_distribution": rationale_counts,
            "confidence_distribution": confidence_counts,
            "methodology": "NIST IR 8477 Set-Theory Relationship Mapping (STRM)",
        }

    # ── OSCAL queries ────────────────────────────────────────────────

    # Catalog aliases: short name → directory name under grc-pro/knowledge/oscal/
    _CATALOG_ALIASES: dict[str, str] = {
        "nist": "nist-800-53-rev5",
        "nist-800-53": "nist-800-53-rev5",
        "800-53": "nist-800-53-rev5",
        "fedramp": "fedramp-moderate-rev5",
        "fedramp-moderate": "fedramp-moderate-rev5",
    }

    def _resolve_catalog(self, catalog: str) -> str:
        """Resolve a catalog alias to the actual directory name."""
        return self._CATALOG_ALIASES.get(catalog.lower(), catalog)

    def _load_oscal_family(self, catalog: str, family: str) -> dict | None:
        """Lazy-load an OSCAL family JSON file."""
        resolved = self._resolve_catalog(catalog)
        cache_key = f"{resolved}::{family}"
        if cache_key in self._oscal_cache:
            return self._oscal_cache[cache_key]

        oscal_dir = self._grc_pro_dir / "knowledge" / "oscal" / resolved
        family_file = oscal_dir / f"{family.lower()}.json"

        if not family_file.exists():
            return None

        try:
            data = json.loads(family_file.read_text(encoding="utf-8"))
            self._oscal_cache[cache_key] = data
            return data
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("Failed to load OSCAL file %s: %s", family_file, e)
            return None

    def get_oscal_control(self, catalog: str, control_id: str) -> dict | None:
        """Extract a full control record from OSCAL JSON.

        Args:
            catalog: "nist-800-53-rev5" or "fedramp-moderate-rev5"
            control_id: e.g., "ac-2", "AC-2", "ac-2.1", "AC-2(1)"
        """
        from .utils import normalize_control_id, extract_family_from_control_id

        normalized = normalize_control_id(control_id)
        family = extract_family_from_control_id(normalized)
        if not family:
            return None

        data = self._load_oscal_family(catalog, family)
        if not data:
            return None

        # Check if it's an enhancement (has a dot)
        if "." in normalized:
            base_id = normalized.split(".")[0]
            return self._find_control_in_list(data.get("controls", []), base_id, normalized)
        else:
            return self._find_control_in_list(data.get("controls", []), normalized, None)

    def _find_control_in_list(
        self, controls: list[dict], target_id: str, enhancement_id: str | None
    ) -> dict | None:
        """Find a control or enhancement in a controls list."""
        for ctrl in controls:
            if ctrl.get("id") == target_id:
                if enhancement_id is None:
                    return ctrl
                # Look for enhancement in nested controls
                for enh in ctrl.get("controls", []):
                    if enh.get("id") == enhancement_id:
                        return enh
                return None
        return None

    def search_oscal(self, catalog: str, query: str, limit: int = 15) -> list[dict]:
        """Keyword search across OSCAL control prose in a catalog."""
        resolved = self._resolve_catalog(catalog)
        oscal_dir = self._grc_pro_dir / "knowledge" / "oscal" / resolved
        if not oscal_dir.exists():
            return []

        results: list[dict] = []
        query_tokens = tokenize(query)

        for json_file in sorted(oscal_dir.glob("*.json")):
            if json_file.name == "metadata.json":
                continue

            data = self._load_oscal_family(resolved, json_file.stem)
            if not data:
                continue

            for ctrl in data.get("controls", []):
                if self._oscal_control_matches(ctrl, query_tokens):
                    results.append({
                        "id": ctrl.get("id"),
                        "title": ctrl.get("title"),
                        "family": data.get("title"),
                    })
                    if len(results) >= limit:
                        return results

                # Also search enhancements
                for enh in ctrl.get("controls", []):
                    if self._oscal_control_matches(enh, query_tokens):
                        results.append({
                            "id": enh.get("id"),
                            "title": enh.get("title"),
                            "family": data.get("title"),
                            "parent": ctrl.get("id"),
                        })
                        if len(results) >= limit:
                            return results

        return results

    def _oscal_control_matches(self, ctrl: dict, query_tokens: list[str]) -> bool:
        """Check if an OSCAL control matches query tokens."""
        searchable_parts: list[str] = [
            ctrl.get("id", ""),
            ctrl.get("title", ""),
        ]
        for part in ctrl.get("parts", []):
            if "prose" in part:
                searchable_parts.append(part["prose"])
            for sub in part.get("parts", []):
                if "prose" in sub:
                    searchable_parts.append(sub["prose"])
        for param in ctrl.get("params", []):
            if "label" in param:
                searchable_parts.append(param["label"])

        combined = " ".join(searchable_parts).lower()
        return all(t in combined for t in query_tokens)

    # ── Fetcher queries ──────────────────────────────────────────────

    def list_fetchers(self) -> dict[str, list[dict]]:
        """List available fetchers grouped by platform."""
        fetchers_dir = self._grc_pro_dir / "fetchers"
        if not fetchers_dir.exists():
            return {}

        result: dict[str, list[dict]] = {}
        skip_dirs = {"common", "logos"}

        for platform_dir in sorted(fetchers_dir.iterdir()):
            if not platform_dir.is_dir() or platform_dir.name in skip_dirs:
                continue

            scripts: list[dict] = []
            for script in sorted(platform_dir.iterdir()):
                if script.suffix in (".sh", ".py") and not script.name.startswith("__"):
                    scripts.append({
                        "name": script.name,
                        "path": str(script.relative_to(self._grc_pro_dir)),
                        "type": "shell" if script.suffix == ".sh" else "python",
                    })

            if scripts:
                result[platform_dir.name] = scripts

        return result

    def get_fetcher_path(self, platform: str, script_name: str) -> Path | None:
        """Get the full path to a fetcher script."""
        fetcher_path = self._grc_pro_dir / "fetchers" / platform / script_name
        if fetcher_path.exists():
            return fetcher_path
        return None
