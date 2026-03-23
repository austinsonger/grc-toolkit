---
name: trestle-commands
description: "OSCAL Compliance Trestle commands for workspace management, authoring, model operations, tasks, and end-to-end workflows."
---

# Trestle Commands

Command guidance for managing OSCAL compliance packages using Compliance Trestle (CNCF sandbox project). Commands are organized by operation type.

## Command Groups

### Workspace Management (`/trestle:workspace-*`)

| Command | Description |
|---------|-------------|
| `/trestle:workspace-init` | Initialize a trestle workspace |
| `/trestle:workspace-configure` | Configure workspace settings |
| `/trestle:workspace-status` | Show workspace status and inventory |
| `/trestle:workspace-validate` | Run full workspace validation |
| `/trestle:workspace-partial-validate` | Validate specific models |
| `/trestle:workspace-version` | Show trestle version info |
| `/trestle:workspace-href` | Manage OSCAL href references |

### Authoring (`/trestle:author-*`)

| Command | Description |
|---------|-------------|
| `/trestle:author-ssp-generate` | Generate SSP markdown from profile |
| `/trestle:author-ssp-assemble` | Assemble SSP markdown back to OSCAL JSON |
| `/trestle:author-ssp-filter` | Filter SSP by profile |
| `/trestle:author-profile-generate` | Generate profile markdown |
| `/trestle:author-profile-assemble` | Assemble profile from markdown |
| `/trestle:author-profile-resolve` | Resolve profile to flat catalog |
| `/trestle:author-profile-inherit` | Set up profile inheritance |
| `/trestle:author-catalog-generate` | Generate catalog markdown |
| `/trestle:author-catalog-assemble` | Assemble catalog from markdown |
| `/trestle:author-component-generate` | Generate component definition markdown |
| `/trestle:author-component-assemble` | Assemble component definition |
| `/trestle:author-docs` | Manage authored documents |
| `/trestle:author-folders` | Manage authoring folders |
| `/trestle:author-headers` | Manage YAML headers |
| `/trestle:author-jinja` | Jinja template rendering |

### Model Operations (`/trestle:model-*`)

| Command | Description |
|---------|-------------|
| `/trestle:model-import` | Import OSCAL models |
| `/trestle:model-create` | Create new OSCAL models |
| `/trestle:model-split` | Split models into parts |
| `/trestle:model-merge` | Merge model parts |
| `/trestle:model-replicate` | Copy existing models |
| `/trestle:model-remove` | Remove models |
| `/trestle:model-assemble` | Assemble models |
| `/trestle:model-describe` | Describe model structure |

### Tasks (`/trestle:task-*`)

| Command | Description |
|---------|-------------|
| `/trestle:task-list` | List available tasks |
| `/trestle:task-info` | Get task details |
| `/trestle:task-run` | Execute a task |

### Workflows (`/trestle:workflow-*`)

| Command | Description |
|---------|-------------|
| `/trestle:workflow-ssp-roundtrip` | End-to-end SSP authoring workflow |
| `/trestle:workflow-profile-roundtrip` | Profile authoring roundtrip |
| `/trestle:workflow-catalog-roundtrip` | Catalog authoring roundtrip |
| `/trestle:workflow-component-roundtrip` | Component definition roundtrip |
| `/trestle:workflow-assessment-roundtrip` | Assessment plan/results roundtrip |
| `/trestle:workflow-poam-roundtrip` | POA&M authoring roundtrip |
| `/trestle:workflow-data-import` | Data import workflow (CSV/XLSX/XCCDF) |
| `/trestle:workflow-governance-setup` | Governance and template setup |

## When to Use

Use this skill when the user is working with Compliance Trestle and needs guidance on specific trestle CLI commands or OSCAL workflows.

## Related Skills

- `trestle-workspace` — Workspace initialization and configuration details
- `trestle-authoring-workflow` — Generate/assemble roundtrip patterns
- `trestle-oscal-models` — OSCAL model type reference
- `trestle-control-implementation` — Writing SSP control responses
- `trestle-validation` — Validation and troubleshooting
- `trestle-task-system` — Data conversion tasks
