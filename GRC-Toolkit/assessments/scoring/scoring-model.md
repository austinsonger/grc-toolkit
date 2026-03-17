# Compliance Scoring Model

## Scale
- 0: Not implemented
- 1: Ad hoc
- 2: Partially implemented
- 3: Implemented
- 4: Implemented and measured
- 5: Optimized and continuously improved

## Formula
`control_score = implementation_score * evidence_quality_multiplier`

Where:
- `implementation_score` = 0..5
- `evidence_quality_multiplier` = 0.8 (weak), 1.0 (adequate), 1.2 (strong)

## Program KPI
`program_maturity = average(control_score) / 5 * 100`
