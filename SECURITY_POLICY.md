# SuperSXO — Security Policy

## Security Baseline Enforcement

Security controls are enforced through machine-readable governance and automated validators. The following files form the security enforcement layer:

- `SECURITY_BASELINE.md` — human-readable baseline covering threat model, policies, and incident response
- `TECHNICAL_RISK_REGISTER.md` — technical risk register with severity, prevention, detection, and response for each known risk
- `data/security-baseline.json` — machine-readable security controls for nine governance areas
- `data/technical-risk-register.json` — machine-readable risk entries with `blocks_publication` enforcement
- `scripts/validate_security_baseline.py` — validates control groups and risk entries against governance rules
- `scripts/validate_repository_hygiene.py` — scans the repository for secrets, forbidden directories, JavaScript violations, external scripts, and prohibited patterns

These validators run as part of the sovereign quality gate on every push.

---

## Core Principle

This asset must be built with a **low attack surface**.

Security is not a feature to be added later. It is an architectural constraint from the beginning.

---

## Initial Version Restrictions

The following must be absent from the initial version:

- user accounts
- login systems
- databases
- file uploads
- admin panels
- untrusted user-generated content
- unnecessary third-party scripts
- exposed API keys
- payment processing inside the repository
- secrets committed to GitHub

---

## Repository Security Requirements

The repository must at all times:

- contain no secrets
- contain no `.env` files
- contain no API tokens
- contain no unsafe inline scripts without review
- contain no `eval`
- contain no unescaped user input
- contain no uncontrolled redirects
- contain no dependency bloat
- contain no tracking scripts without approval
- contain no monetization scripts without approval

---

## Deployment Security Headers

Future deployment must support strong security headers:

| Header | Purpose |
|---|---|
| `Content-Security-Policy` | Controls script, style, and resource origins |
| `Strict-Transport-Security` | Forces HTTPS |
| `X-Content-Type-Options` | Prevents MIME sniffing |
| `Referrer-Policy` | Controls referrer information |
| `Permissions-Policy` | Restricts browser feature access |
| Frame restrictions | Via CSP or equivalent frame-control controls |

---

## Cloudflare Security Layer

Cloudflare is the approved edge-governance layer.

It may support:

- DNS and nameserver delegation
- TLS / HTTPS enforcement
- security posture and WAF
- caching and performance
- Cloudflare Pages deployment

Cloudflare must not:

- create hidden deployment paths
- store or request credentials from AI agents
- produce undocumented operational state

GitHub remains the single source of truth.

All Cloudflare operations are governed by the Sovereign Asset System cloudflare governance rules.

---

## Third-Party Script Policy

No third-party script may be added without:

1. A documented justification
2. A review of what data the script accesses
3. A Content-Security-Policy update
4. A log entry in `DECISION_LOG.md`

---

## Security Violation Classification

Any of the following constitutes a security violation:

| Violation | Severity |
|---|---|
| Secret committed to repository | Critical |
| Unreviewed third-party script injection | High |
| User data collected without consent | High |
| Payment logic added without approval | High |
| Admin functionality without authentication design | Medium |
| Dependency added without review | Medium |

Security violations must be:

1. Reported in `DECISION_LOG.md`
2. Resolved before any public deployment proceeds
3. Reviewed to determine whether rollback is required
