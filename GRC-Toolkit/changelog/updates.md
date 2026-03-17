# Repository Update Log

## 2026-03-17
- Added normalized control catalog and baseline mappings.
- Added machine-readable datasets and JSON schemas.
- Added AWS logging implementation guide and evidence automation scripts.
- Added shared responsibility matrices and MITRE ATT&CK alignment examples.
- Extended controls, mappings, and risks schemas with optional set-theory relationship mapping fields aligned to NIST IR 8477 concepts (`equivalent`, `subset`, `superset`, `intersection`, `disjoint`) while preserving legacy relationship compatibility.
- Replaced monolithic `data/mappings.json` with framework-pair mapping datasets (`data/*_mappings.json`) and updated validation tooling accordingly.
- Added optional mapping fields for control sub-parts (`source_control_parts`, `target_control_parts`) and framework parameters (`parameter.source`, `parameter.target`).
- Added SCF-derived threats dataset (`data/threats.json`) and `schemas/threats.schema.json` for natural and man-made threat cataloging.
