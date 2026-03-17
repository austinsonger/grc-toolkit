# Shared Responsibility Model (CSP vs Customer)

## Legend
- `CSP`: Cloud Service Provider
- `Customer`: Tenant organization
- `Shared`: Both parties with defined boundaries

## Control Responsibility Snapshot
| Control | SaaS | PaaS | IaaS |
|---|---|---|---|
| Physical Security | CSP | CSP | CSP |
| Guest OS Patching | CSP | Shared | Customer |
| IAM Configuration | Shared | Customer | Customer |
| Network Segmentation | CSP | Shared | Customer |
| Encryption Key Management | Shared | Shared | Customer |
| Logging Configuration | Customer | Customer | Customer |
