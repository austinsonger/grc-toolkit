# HIPAA Quick Scan Reference Card

> Fast reference for common HIPAA compliance scans in Claude Code

---

## INSTANT SCAN COMMANDS

### 1. PHI Variable Names (30 seconds)
```
Search for these patterns in all source files:
ssn|social_security|mrn|medical_record|patient_name|patient_id|
member_id|dob|date_of_birth|diagnosis|medication|insurance_id|
health_plan|beneficiary|prescription
```

### 2. SSN Detection (10 seconds)
```regex
\b(?!000|666|9\d{2})\d{3}[-\s]?(?!00)\d{2}[-\s]?(?!0000)\d{4}\b
```

### 3. Hardcoded Credentials (20 seconds)
```regex
(?i)(password|api_key|secret|token)\s*[=:]\s*["'][^"']{8,}["']
```

### 4. PHI in Logs (15 seconds)
```regex
console\.(log|info|warn|error).*(?:patient|ssn|dob|diagnosis)
```

### 5. HTTP (Not HTTPS) (10 seconds)
```regex
http://(?!localhost|127\.0\.0\.1|10\.|192\.168\.)
```

---

## CRITICAL FILES TO CHECK

| Priority | Files | Check For |
|----------|-------|-----------|
| 1 | `.env*` | Hardcoded secrets, database credentials |
| 2 | `**/models/**` | PHI field definitions |
| 3 | `**/routes/**`, `**/controllers/**` | Missing auth on PHI endpoints |
| 4 | `**/*.log` | PHI in log files |
| 5 | `**/test/**`, `**/fixtures/**` | Real PHI in test data |
| 6 | `*.tf`, `*.yaml` (IaC) | Missing encryption configs |
| 7 | `docker-compose*` | Exposed secrets |

---

## RED FLAGS (Immediate Action)

| Pattern | Risk | Action |
|---------|------|--------|
| `\d{3}-\d{2}-\d{4}` in code | SSN exposure | Remove immediately |
| `password = "..."` | Hardcoded credential | Use secrets manager |
| `console.log(patient)` | PHI logging | Remove PHI from logs |
| `http://` for API calls | Unencrypted transmission | Switch to HTTPS |
| `localStorage.setItem(patient)` | Client-side PHI | Remove from browser storage |
| `SELECT * FROM patients` | Excessive data exposure | Select specific columns |
| Public S3/storage buckets | Data exposure | Set private ACL |
| Missing `@auth` decorator | Unprotected endpoint | Add authentication |

---

## 18 PHI IDENTIFIERS CHECKLIST

```
[ ] 1.  Names (first, last, full)
[ ] 2.  Geographic data (street, city, ZIP < state)
[ ] 3.  Dates (DOB, admission, discharge, death, age >89)
[ ] 4.  Phone numbers
[ ] 5.  Fax numbers
[ ] 6.  Email addresses
[ ] 7.  Social Security Numbers
[ ] 8.  Medical Record Numbers (MRN)
[ ] 9.  Health Plan Beneficiary Numbers
[ ] 10. Account numbers
[ ] 11. Certificate/license numbers
[ ] 12. Vehicle identifiers (VIN, plates)
[ ] 13. Device identifiers (serial, UDI)
[ ] 14. URLs
[ ] 15. IP addresses
[ ] 16. Biometric identifiers
[ ] 17. Full-face photographs
[ ] 18. Any other unique identifier
```

---

## ENCRYPTION REQUIREMENTS

| Data State | Minimum Standard | Recommended |
|------------|-----------------|-------------|
| At Rest | AES-128 | AES-256 |
| In Transit | TLS 1.2 | TLS 1.3 |
| Key Storage | Separate from data | HSM/KMS |

**Non-Compliant Patterns:**
- `TLS 1.0`, `TLS 1.1`, `SSL`
- `DES`, `RC4`, `MD5`, `SHA1` (without salt)
- Keys in source code or same location as data

---

## QUICK COMPLIANCE CHECKLIST

### Access Controls
- [ ] Unique user IDs (no shared accounts)
- [ ] Session timeouts (10-30 min)
- [ ] MFA enabled
- [ ] Automatic logoff

### Audit Logging
- [ ] All PHI access logged
- [ ] Logs include: who, when, what, where
- [ ] 6-year retention
- [ ] Logs do NOT contain PHI

### Encryption
- [ ] TLS 1.2+ for all traffic
- [ ] AES-256 for storage
- [ ] Keys in KMS/HSM

### Authentication
- [ ] All PHI endpoints require auth
- [ ] Strong password policy
- [ ] Account lockout

---

## SEVERITY GUIDE

| Level | Examples | Response |
|-------|----------|----------|
| **CRITICAL** | Plaintext SSN, public PHI endpoint, unencrypted DB | Fix NOW |
| **HIGH** | Missing auth, SQL injection, PHI in logs | Fix in 24h |
| **MEDIUM** | Weak encryption, missing rate limiting | Fix in 1 week |
| **LOW** | Missing comments, best practices | Sprint planning |

---

## SCAN TRIGGERS

Use full HIPAA scan when:
- New project setup
- Pre-deployment review
- After major changes
- Quarterly compliance check
- New team member review
- Security incident response

---

*Keep this card handy for quick compliance checks during development.*
