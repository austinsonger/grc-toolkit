# Evidence Collection Playbook

## Trigger
- Quarterly control testing window
- Pre-audit readiness review
- Major incident post-event evidence pull

## Steps
1. Execute `automation/scripts/aws_collect_evidence.sh`.
2. Store outputs in `evidence/artifacts/aws/<period>/`.
3. Hash and sign artifacts where integrity proof is required.
4. Link artifacts to controls in audit workpapers.
