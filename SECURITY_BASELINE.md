# SuperSXO — Security Baseline

## Status

Sprint 6. Active.  
Machine-readable controls: `data/security-baseline.json`  
Validator: `scripts/validate_security_baseline.py`

---

## Threat Model

SuperSXO.com operates as a static-first informational and diagnostic asset. The current threat surface is low by design. Primary threat vectors at this stage are:

- accidental or unauthorized secret commitment to the repository
- unauthorized introduction of JavaScript before approval
- introduction of external scripts or tracking libraries
- premature publication of routes or generation of public output
- GitHub Actions workflow misuse or overly broad permissions
- dependency injection without review
- introduction of monetization, payment, or affiliate surfaces before approval

No backend, database, authentication system, user-generated content surface, or API endpoint exists. The attack surface is intentionally minimal.

---

## Static-First Security Posture

The asset must remain static until a deliberate, logged decision introduces server-side functionality. Static HTML with no JavaScript, no server-side logic, no database, no user inputs, and no third-party execution context represents the current lowest-risk posture.

Progressive enhancement is permitted when JavaScript is approved, but the asset must remain readable, navigable, and meaningful without it.

---

## Disallowed Attack Surfaces

The following attack surfaces are disallowed until explicitly approved through route governance and decision logging:

- user input forms of any kind
- database queries or connections
- server-side rendering with user-controlled variables
- login or authentication flows
- admin panels
- file uploads
- user-generated content
- exposed API endpoints
- webhook receivers
- client-side routing that breaks canonical URLs

---

## Repository Secret Policy

No secret may be committed to this repository. This includes:

- API keys (any service)
- access tokens
- private keys
- `.env` files of any kind (`.env`, `.env.local`, `.env.production`, etc.)
- Cloudflare tokens or API credentials
- GitHub tokens or personal access tokens
- any key-value pair where the value is a live credential

Secrets required for deployment must be managed through the deployment platform's environment variable system (e.g., Cloudflare Pages environment variables, GitHub Actions repository secrets) and never stored in repository files.

**Violation response:** any committed secret constitutes a critical security incident. The credential must be rotated immediately, removed from git history, and the incident logged in `DECISION_LOG.md`.

---

## JavaScript Restriction Policy

No JavaScript file (`.js`) may exist in this repository until JavaScript is explicitly approved through a logged decision. Current approval status: **not approved**.

When approved, JavaScript must:

- live exclusively in `static/js/`
- be reviewed for `eval()`, `innerHTML`, and `document.write` usage before merge
- not introduce third-party library loading without separate approval
- not introduce tracking or analytics behavior
- be referenced in `DECISION_LOG.md` with authorization date

JavaScript must remain a progressive enhancement layer. The asset must be readable, navigable, and meaningful without any JavaScript execution.

No inline event handlers (`onclick`, `onload`, `onerror`, `onmouseover`) may appear in HTML templates.

---

## Third-Party Script Restriction Policy

No third-party script tag (`<script src="...">`), tracking pixel, analytics snippet, CDN-loaded library, or external resource reference may be added to any HTML template without:

1. A documented justification in `DECISION_LOG.md`
2. A Content-Security-Policy update naming the permitted source
3. A review of what data the script accesses and transmits
4. Explicit approval from the asset operator

Current approval status: **no third-party scripts approved**.

---

## Dependency Restriction Policy

All validator scripts must use the Python standard library only. No `pip install`, `npm install`, `requirements.txt`, `package.json`, `pyproject.toml`, `poetry.lock`, or any other dependency manifest may be introduced without:

1. A stated justification
2. A review of the dependency's bundle size, maintenance status, and vulnerability surface
3. A log entry in `DECISION_LOG.md`

Current approval status: **no external dependencies approved**.

---

## GitHub Actions Least-Privilege Policy

The GitHub Actions workflow (`quality-gate.yml`) must use:

```yaml
permissions:
  contents: read
```

No additional permissions are required for running quality gate validators. Write permissions must not be granted unless a specific, logged action requires them.

No third-party GitHub Actions may be added beyond:

- `actions/checkout`
- `actions/setup-python`

Any additional action requires operator review and a decision log entry.

---

## Future Security Headers Target

When the asset is deployed, the following security headers must be present:

| Header | Purpose |
|---|---|
| `Content-Security-Policy` | Controls script, style, and resource origins. Must be restrictive. Default-src 'self'. |
| `Strict-Transport-Security` | Forces HTTPS on all connections. |
| `X-Content-Type-Options: nosniff` | Prevents MIME type sniffing. |
| `Referrer-Policy: no-referrer-when-downgrade` | Controls referrer information sent to external resources. |
| `Permissions-Policy` | Restricts browser feature access (camera, geolocation, payment, etc.). |
| Frame restrictions | Via `Content-Security-Policy: frame-ancestors 'none'` or equivalent. |

These headers must be configured at the Cloudflare edge layer or equivalent deployment platform and validated before any public route is published.

---

## Form, Payment, and Tracking Prohibition

The following are prohibited until explicitly approved through route governance and decision logging:

- contact forms, lead capture forms, email collection forms
- payment processing (Stripe, PayPal, or equivalent)
- affiliate links or referral tracking parameters
- analytics snippets (Google Analytics, GA4, Plausible, or equivalent)
- advertising scripts (Google AdSense, or equivalent)
- retargeting pixels or conversion tracking
- cookie consent banners (not needed until tracking is added)

No monetization surface may be introduced outside the routes where `monetization_allowed: true` in `data/routes.json`, and only after passing the monetization quality gate.

---

## Deployment Security Assumptions

Current deployment target: Cloudflare Pages.

Security assumptions:

- Cloudflare enforces TLS on all connections
- Repository secrets (Cloudflare API token) are stored in GitHub Actions repository secrets, not in repository files
- No build output is committed back to the repository
- All deployments are triggered through the approved CI/CD pipeline
- Cloudflare must not create hidden deployment paths or store credentials accessible to AI agents
- Deployment configuration is documented in `DECISION_LOG.md` before activation
- GitHub remains the single source of truth for all repository state

---

## Incident Logging Requirement

Any security incident, violation, or near-miss must be logged in `DECISION_LOG.md` immediately.

Minimum incident log entry must include:

- date and time of discovery
- nature of the violation (secret exposure, unauthorized script, unapproved dependency, etc.)
- affected files or surfaces
- immediate response taken
- whether credentials were exposed or rotated
- whether public users were affected
- remediation steps completed

No security incident may be silently resolved without a log entry.
