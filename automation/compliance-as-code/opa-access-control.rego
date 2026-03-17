package grc.access_control

default deny = []

# Example input contract:
# {
#   "user": {"id": "u-123", "roles": ["developer"]},
#   "resource": {"environment": "production", "classification": "confidential"},
#   "action": "write"
# }

deny[msg] {
  input.resource.environment == "production"
  not has_prod_role
  msg := "write access to production requires approved production role"
}

has_prod_role {
  some role
  role := input.user.roles[_]
  role == "prod-admin"
}

# Control alignment:
# - CTRL-AC-001
# - NIST AC-2/AC-3, SOC2 CC6.1
