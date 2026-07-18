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

The asset must remain static until a deliberate, logged decision introduces server-side functionality. Static HTML with no server-side logic, no database, no data-transmitting inputs, and no third-party execution context represents the current lowest-risk posture.

First-party JavaScript is permitted only as a governed progressive enhancement under the JavaScript Governance Policy below. The asset must remain readable, navigable, and meaningful without any JavaScript execution.

---

## Disallowed Attack Surfaces

The following attack surfaces are disallowed until explicitly approved through route governance and decision logging:

- forms that transmit, store, or persist user input in any way (client-side-only instrument forms whose answers never leave browser memory — such as the SuperSXO Score — are permitted only when registered in `data/component-registry.json` and covered by a dedicated validator)
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

## JavaScript Governance Policy

First-party JavaScript is approved under strict governance. Current approval status: **approved, governed** (first authorization logged 2026-05-21; each script individually logged in `DECISION_LOG.md`).

`data/approved-scripts.json` is the **single source of truth** for all JavaScript. Every script must:

- be listed in `data/approved-scripts.json` with purpose, allowed APIs, forbidden APIs, `defer: true`, and `external_dependencies: false`
- live exclusively in `static/js/`
- contain none of the forbidden patterns: `eval(`, `innerHTML`, `document.write(`, `fetch(`, `XMLHttpRequest`, `localStorage`, `sessionStorage`, `document.cookie`, `import(`, or any external URL
- be loaded from `templates/base.html` with a per-tag `defer` attribute
- not introduce third-party library loading, tracking, or analytics behavior
- be referenced in `DECISION_LOG.md` with authorization date

Enforcement: `validate_approved_scripts` (list integrity, forbidden patterns, per-tag defer, no unapproved script tags, no executable inline scripts) and `validate_score_instrument` (instrument-specific governance). The build derives its script list from `data/approved-scripts.json` and never hardcodes script paths.

JavaScript must remain a progressive enhancement layer. The asset must be readable, navigable, and meaningful without any JavaScript execution.

No inline event handlers (`onclick`, `onload`, `onerror`, `onmouseover`) and no executable inline `<script>` blocks may appear in HTML templates. Non-executable `<script type="application/ld+json">` metadata blocks are permitted: they contain serialized data only, are emitted exclusively by the governed build from content sources, and are hardened against element breakout (`<` serialized as `<`).

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

Current deployment target: **GitHub Pages** via `.github/workflows/deploy-pages.yml`, governed by `DEPLOYMENT_POLICY.md`.

Security assumptions:

- GitHub Pages enforces TLS on all connections; the custom domain is pinned by the committed `CNAME`
- `output/` is the only deployable artifact; it is generated exclusively by `scripts/build.py`, committed to the repository, and validated by `validate_publication_readiness` and `validate_deploy_assets --strict` so no unpublished route can be deployed
- The deployment workflow uses least-privilege permissions (`contents: read`, `pages: write`, `id-token: write`) and no repository secrets
- No Cloudflare API token is used in the publishing workflow; Cloudflare, if adopted, is a DNS/edge layer only, never a deployment target
- All deployments are triggered through the approved CI/CD pipeline
- Deployment configuration changes are documented in `DECISION_LOG.md` before activation
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
