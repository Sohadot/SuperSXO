# SuperSXO — Technical Standard

## Core Philosophy

The project follows a **static-first architecture** unless a later approved decision introduces backend functionality.

Every technical decision must be justified against the asset thesis: a sovereign-grade digital asset that is fast, indexable, accessible, and acquisition-ready.

---

## Approved Technical Direction

The technical implementation must prioritize:

- semantic HTML
- controlled CSS
- lightweight JavaScript
- fast loading
- indexable content
- accessible interfaces
- deterministic routing
- validator-based quality control

---

## Prohibited Technical Patterns

The following are prohibited unless explicitly justified and logged in `DECISION_LOG.md`:

- unnecessary dependencies
- unnecessary third-party scripts
- CMS lock-in
- databases in the initial phase
- login systems in the initial phase
- server-side rendering without documented justification
- client-side routing that breaks canonical URLs

---

## Static-First Rule

The site must remain:

- readable without JavaScript
- navigable without JavaScript
- meaningful without JavaScript

Spatial or VR-inspired effects are **progressive enhancements only**.

They must not be the core content delivery mechanism.

---

## SEO Technical Requirements

Every indexable page must have:

- a unique canonical URL
- a controlled `<title>` tag
- a controlled `<meta name="description">`
- one clear `<h1>`
- logical heading structure: H1 → H2 → H3
- structured data where appropriate
- a valid sitemap entry
- a correct robots directive

---

## Performance Standard

The technical implementation must:

- pass Core Web Vitals on mobile and desktop
- achieve minimal Largest Contentful Paint (LCP)
- avoid layout shift from uncontrolled assets
- avoid render-blocking scripts
- avoid excessive image sizes
- avoid unnecessary font loading

Performance budgets must be defined before any public launch and enforced in the quality gate.

---

## Dependency Governance

No new dependency may be added without:

1. A stated justification
2. A review of the dependency's bundle size and risk surface
3. A log entry in `DECISION_LOG.md`

---

## Build Tooling

Build tooling decisions must be:

- documented
- reversible
- appropriate to the static-first requirement
- not introducing hidden server-side complexity

No deployment should introduce undocumented infrastructure.

---

## Repository Hygiene Enforcement

The following are prohibited until explicitly approved through route governance and a logged decision in `DECISION_LOG.md`:

- public HTML output (`index.html`, `output/`, `public/`, `dist/`)
- JavaScript files (`.js`) anywhere in the repository
- inline event handlers in HTML templates (`onclick=`, `onload=`, etc.)
- external script tags (`<script src="http...">`)
- third-party libraries (Three.js, WebGL-only rendering, canvas-only content)
- analytics or tracking scripts (Google Analytics, Google Tag Manager, etc.)
- payment scripts (Stripe, PayPal, or equivalent)
- affiliate links or monetization scripts outside approved routes
- external dependencies (`requirements.txt`, `package.json`, etc.)
- `.env` files or committed secrets of any kind

These prohibitions are machine-enforced by `scripts/validate_repository_hygiene.py` which runs on every push as part of the sovereign quality gate.

---

## Deployment

- Cloudflare Pages is the approved deployment target
- GitHub is the source of truth
- No build output may be committed to the repository
- No deployment secrets may be stored in the repository
- Deployment configuration must be documented in `DECISION_LOG.md`
