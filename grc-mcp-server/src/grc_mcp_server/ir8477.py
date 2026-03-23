"""NIST IR 8477 Set-Theory Relationship Mapping (STRM) methodology.

Implements the mapping relationships defined in NIST IR 8477 for
cross-framework control alignment using set-theory semantics.

Terminology (per IR 8477):
  - Focal Document Element (FDE): The control/requirement being mapped FROM
  - Reference Document Element (RDE): The control/requirement being mapped TO
  - Relationship: The set-theory relation between FDE and RDE
  - Rationale: The basis for the relationship (syntactic, semantic, functional)

Relationship Types:
  - equal:          FDE and RDE express identical requirements (A = B)
  - subset_of:      FDE requirements are entirely contained within RDE (A ⊂ B)
  - superset_of:    FDE requirements entirely contain RDE (A ⊃ B)
  - intersects_with: FDE and RDE partially overlap (A ∩ B ≠ ∅, A ⊄ B, B ⊄ A)
  - not_related:    No meaningful overlap between FDE and RDE (A ∩ B = ∅)

Rationale Types:
  - syntactic:   Relationship based on wording/textual similarity
  - semantic:    Relationship based on meaning/intent similarity
  - functional:  Relationship based on outcome/result similarity
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any


class RelationType(str, Enum):
    """IR 8477 set-theory relationship types between document elements."""

    EQUAL = "equal"
    SUBSET_OF = "subset_of"
    SUPERSET_OF = "superset_of"
    INTERSECTS_WITH = "intersects_with"
    NOT_RELATED = "not_related"

    @classmethod
    def from_legacy(cls, value: str) -> "RelationType":
        """Resolve legacy aliases to canonical IR 8477 values."""
        aliases = {
            "equivalent": cls.EQUAL,
            "subset": cls.SUBSET_OF,
            "superset": cls.SUPERSET_OF,
            "intersection": cls.INTERSECTS_WITH,
            "overlap": cls.INTERSECTS_WITH,
            "no_relationship": cls.NOT_RELATED,
            "disjoint": cls.NOT_RELATED,
        }
        try:
            return cls(value)
        except ValueError:
            return aliases.get(value.lower(), cls.NOT_RELATED)


class RationaleType(str, Enum):
    """IR 8477 rationale types explaining why a relationship holds."""

    SYNTACTIC = "syntactic"
    SEMANTIC = "semantic"
    FUNCTIONAL = "functional"


class Confidence(str, Enum):
    """Confidence level for a mapping relationship."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Scope(str, Enum):
    """Scope categories for FDE/RDE document elements in set-theory relations."""

    FRAMEWORK_CONTROL_SET = "framework_control_set"
    NORMALIZED_CONTROL_SET = "normalized_control_set"
    CONTROL_REQUIREMENT_SET = "control_requirement_set"
    RISK_SCENARIO_SET = "risk_scenario_set"
    IMPLEMENTATION_EVIDENCE_SET = "implementation_evidence_set"


@dataclass
class SetTheoryRelationship:
    """A single IR 8477 set-theory relationship between two document elements."""

    relation: RelationType
    source_scope: Scope
    target_scope: Scope
    rationale: RationaleType = RationaleType.SEMANTIC
    confidence_alignment: Confidence = Confidence.MEDIUM
    strength: int | None = None  # Optional 1-10 STRM strength score

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "relation": self.relation.value,
            "source_scope": self.source_scope.value,
            "target_scope": self.target_scope.value,
            "rationale": self.rationale.value,
            "confidence_alignment": self.confidence_alignment.value,
        }
        if self.strength is not None:
            d["strength"] = self.strength
        return d

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SetTheoryRelationship":
        return cls(
            relation=RelationType.from_legacy(data.get("relation", "not_related")),
            source_scope=Scope(data.get("source_scope", "control_requirement_set")),
            target_scope=Scope(data.get("target_scope", "control_requirement_set")),
            rationale=RationaleType(data.get("rationale", "semantic")),
            confidence_alignment=Confidence(data.get("confidence_alignment", "medium")),
            strength=data.get("strength"),
        )


@dataclass
class ControlMapping:
    """A complete IR 8477-compliant control mapping (FDE → RDE).

    Attributes:
        mapping_id: Unique identifier for this mapping
        source_framework: FDE framework name (Focal Document)
        source_control: FDE control ID
        target_framework: RDE framework name (Reference Document)
        target_control: RDE control ID
        normalized_control_id: Canonical control ID in the GRC toolkit
        relationship: Legacy compatibility field (equivalent/overlap/partial)
        confidence: Overall mapping confidence
        rationale_text: Human-readable explanation of the mapping
        set_theory_relationships: IR 8477 STRM relationships
        source_control_parts: Optional FDE sub-parts (enhancements, statement items)
        target_control_parts: Optional RDE sub-parts
        parameters: Framework-specific parameter values
    """

    mapping_id: str
    source_framework: str
    source_control: str
    target_framework: str
    target_control: str
    normalized_control_id: str = ""
    relationship: str = ""  # legacy compat
    confidence: str = "medium"
    rationale_text: str = ""
    set_theory_relationships: list[SetTheoryRelationship] = field(default_factory=list)
    source_control_parts: list[str] = field(default_factory=list)
    target_control_parts: list[str] = field(default_factory=list)
    parameters: dict[str, Any] = field(default_factory=dict)

    @property
    def primary_relation(self) -> RelationType:
        """Return the primary (first) set-theory relation, or derive from legacy."""
        if self.set_theory_relationships:
            return self.set_theory_relationships[0].relation
        return RelationType.from_legacy(self.relationship)

    @property
    def primary_rationale(self) -> RationaleType:
        """Return the primary rationale type."""
        if self.set_theory_relationships:
            return self.set_theory_relationships[0].rationale
        return RationaleType.SEMANTIC

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "mapping_id": self.mapping_id,
            "source_framework": self.source_framework,
            "source_control": self.source_control,
            "target_framework": self.target_framework,
            "target_control": self.target_control,
            "normalized_control_id": self.normalized_control_id,
            "relationship": self.relationship,
            "confidence": self.confidence,
            "rationale": self.rationale_text,
            "set_theory_relationships": [r.to_dict() for r in self.set_theory_relationships],
            "source_control_parts": self.source_control_parts,
            "target_control_parts": self.target_control_parts,
            "parameter": self.parameters,
        }
        return d

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ControlMapping":
        str_list = data.get("set_theory_relationships", [])
        return cls(
            mapping_id=data.get("mapping_id", ""),
            source_framework=data.get("source_framework", ""),
            source_control=data.get("source_control", ""),
            target_framework=data.get("target_framework", ""),
            target_control=data.get("target_control", ""),
            normalized_control_id=data.get("normalized_control_id", ""),
            relationship=data.get("relationship", ""),
            confidence=data.get("confidence", "medium"),
            rationale_text=data.get("rationale", ""),
            set_theory_relationships=[SetTheoryRelationship.from_dict(r) for r in str_list],
            source_control_parts=data.get("source_control_parts", []),
            target_control_parts=data.get("target_control_parts", []),
            parameters=data.get("parameter", {}),
        )


def infer_inverse_relation(relation: RelationType) -> RelationType:
    """Return the inverse of a set-theory relationship.

    Per IR 8477: if FDE ⊂ RDE then RDE ⊃ FDE.
    """
    inverse_map = {
        RelationType.EQUAL: RelationType.EQUAL,
        RelationType.SUBSET_OF: RelationType.SUPERSET_OF,
        RelationType.SUPERSET_OF: RelationType.SUBSET_OF,
        RelationType.INTERSECTS_WITH: RelationType.INTERSECTS_WITH,
        RelationType.NOT_RELATED: RelationType.NOT_RELATED,
    }
    return inverse_map[relation]


def derive_transitive_relation(
    a_to_b: RelationType,
    b_to_c: RelationType,
) -> RelationType | None:
    """Derive A→C relationship from A→B and B→C using set-theory transitivity.

    Returns None if the transitive relation cannot be definitively determined.

    Transitivity rules:
      equal + equal         = equal
      equal + X             = X
      subset + subset       = subset
      subset + equal        = subset
      superset + superset   = superset
      superset + equal      = superset
      intersects + anything = None (indeterminate without further analysis)
      not_related + anything = not_related (if A∩B=∅, no transitive path)
    """
    if a_to_b == RelationType.NOT_RELATED or b_to_c == RelationType.NOT_RELATED:
        return RelationType.NOT_RELATED

    if a_to_b == RelationType.EQUAL:
        return b_to_c
    if b_to_c == RelationType.EQUAL:
        return a_to_b

    if a_to_b == RelationType.SUBSET_OF and b_to_c == RelationType.SUBSET_OF:
        return RelationType.SUBSET_OF
    if a_to_b == RelationType.SUPERSET_OF and b_to_c == RelationType.SUPERSET_OF:
        return RelationType.SUPERSET_OF

    # All other combinations are indeterminate
    return None


def compute_mapping_strength(mapping: ControlMapping) -> int:
    """Compute 1-10 STRM strength score for a mapping.

    Score composition:
      - Relation type:  equal=10, subset/superset=7, intersects=4, not_related=0
      - Confidence:     high=+0, medium=-1, low=-2
      - Rationale:      functional=+0, semantic=-0, syntactic=-1

    Result is clamped to [1, 10].
    """
    rel = mapping.primary_relation
    base_scores = {
        RelationType.EQUAL: 10,
        RelationType.SUBSET_OF: 7,
        RelationType.SUPERSET_OF: 7,
        RelationType.INTERSECTS_WITH: 4,
        RelationType.NOT_RELATED: 0,
    }
    score = base_scores.get(rel, 4)

    confidence_adj = {"high": 0, "medium": -1, "low": -2}
    score += confidence_adj.get(mapping.confidence, -1)

    rationale = mapping.primary_rationale
    rationale_adj = {
        RationaleType.FUNCTIONAL: 0,
        RationaleType.SEMANTIC: 0,
        RationaleType.SYNTACTIC: -1,
    }
    score += rationale_adj.get(rationale, 0)

    return max(1, min(10, score))
