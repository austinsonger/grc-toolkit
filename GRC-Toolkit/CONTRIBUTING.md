# Contributing Guidelines

## Contribution Principles
- Keep controls normalized and machine-readable.
- Preserve framework-native identifiers in all mappings.
- Include implementation and evidence implications for new controls.
- Validate JSON files against schemas before opening PRs.

## Branch and Commit Standards
- Branch format: `feat/<area>-<short-description>` or `fix/<area>-<short-description>`
- Commit format: `type(scope): summary`

Examples:
- `feat(controls): add baseline endpoint protection controls`
- `fix(mappings): correct nist-to-iso mapping for AC-2`

## Pull Request Checklist
- [ ] Updated relevant `data/*.json` file(s)
- [ ] Updated corresponding schema if model changed
- [ ] Added or updated mapping rationale
- [ ] Added implementation guidance or evidence impact notes
- [ ] Updated `changelog/updates.md`

## Validation Commands
```bash
jq . data/controls.json > /dev/null
jq . data/mappings.json > /dev/null
jq . data/risks.json > /dev/null
```

## Review Expectations
PRs are reviewed for:
- Control normalization quality
- Mapping correctness and traceability
- Operational implementability
- Audit defensibility
