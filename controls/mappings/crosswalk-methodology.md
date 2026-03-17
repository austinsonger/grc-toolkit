# Crosswalk Methodology

1. Normalize controls into capability statements (actor, action, scope, outcome).
2. Preserve source framework identifiers and revision metadata.
3. Map with confidence (`high`, `medium`, `low`) and rationale.
4. Record one-to-many relationships explicitly.
5. Validate with implementation evidence requirements.

## Mapping Confidence Guide
- `high`: semantic equivalence and comparable assurance intent
- `medium`: overlapping intent but different depth/scope
- `low`: indirect relationship; requires compensating controls

## Set-Theory Mapping Guidance
- Use canonical IR 8477 relation values when possible: `equal`, `subset_of`, `superset_of`, `intersects_with`, `no_relationship`.
- Record rationale context as one of: `syntactic`, `semantic`, `functional`.
- Legacy aliases may appear for compatibility in historical datasets, but new mappings should prefer canonical values.

## Sub-Part and Parameter Guidance
- Populate `source_control_parts` and `target_control_parts` when a control references sub-parts (for example NIST SP 800-53 control enhancements like `(1)`, `(2)`).
- Populate `parameter.source` and `parameter.target` when mappings depend on parameterized language (for example review frequency, retention period, or sampling cadence).
- Use empty arrays/objects when no sub-parts or parameters are required so data shape remains consistent.
