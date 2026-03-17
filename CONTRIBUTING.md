# Contributing to GRC-Toolkit

Thank you for your interest in contributing! This document outlines how to contribute effectively.

## Ways to Contribute

- **Add new frameworks**: Create a new directory under `frameworks/` with controls and documentation
- **Improve mappings**: Add or correct cross-framework control mappings in `mappings/`
- **Add automation scripts**: Contribute compliance-as-code in `automation/`
- **Update regulations**: Add new or updated regulatory requirements in `regulations/`
- **Fix errors**: Correct outdated or incorrect compliance information

## Contribution Guidelines

### File Naming Conventions

- Use lowercase with hyphens: `access-control-policy.md`
- Framework files: `{framework}-{version}-controls.md`
- Mapping files: `{source}-to-{target}-mapping.md`
- Scripts: `{platform}-{function}.py` or `{platform}-{function}.sh`

### Content Standards

1. **Be specific**: Reference exact control IDs (e.g., `NIST AC-2`, `ISO A.9.2.1`)
2. **Cite sources**: Link to official framework documentation
3. **Include versions**: Always specify framework version
4. **Keep it current**: Note the last-reviewed date

### Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/add-pci-dss-controls`
3. Make your changes following the naming conventions
4. Update the relevant README or index file
5. Submit a PR with a clear description of changes

### Quality Checklist

- [ ] Content is accurate and references official sources
- [ ] File naming follows conventions
- [ ] No sensitive or proprietary information included
- [ ] Mappings reference valid control IDs from both frameworks
- [ ] Scripts include error handling and documentation

## Code of Conduct

Be respectful and constructive. This is a community resource for security professionals.

## Questions?

Open an issue with the `question` label.
