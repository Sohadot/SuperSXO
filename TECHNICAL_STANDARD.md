# SuperSXO — Technical Standard

## Core Philosophy

The project follows a **static-first architecture** unless a later approved decision introduces backend functionality.

Every technical decision must be justified against the asset thesis: a sovereign-grade digital asset that is fast, indexable, accessible, and acquisition-ready.

---

## Approved Technical Direction

The technical implementation must prioritize:

- semantic HTML
- controlled CSS
- lightweight, governed JavaScript
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

JavaScript effects are **progressive enhancements only**.

They must not be the core content delivery mechanism.

---

## First-Party JavaScript Governance

First-party JavaScript is approved under the following governance model:

**Approval registry:** `data/approved-scripts.json` — each approved script must declare its purpose, allowed APIs, and forbidden APIs.

**Validator:** `scripts/validate_approved_scripts.py` — runs on every push. Verifies that only approved scripts exist, that no forbidden APIs appear in any script, and that base.html references approved scripts with `defer`.

**Currently approved scripts:**

| File | Purpose |
|---|---|
| `static/js/interface-state.js` | IntersectionObserver station active state for the SXO diagnostic environment |
| `static/js/theme-toggle.js` | Session-only display mode toggle — Option A (no storage, no network calls) |

**Allowed APIs:** querySelector, querySelectorAll, classList, dataset, IntersectionObserver, getAttribute, setAttribute, addEventListener

**Forbidden APIs:** eval, innerHTML, document.write, fetch, XMLHttpRequest, localStorage, sessionStorage, document.cookie, import, external script loading

Any additional first-party script requires:
1. A new entry in `data/approved-scripts.json`
2. Validation passage
3. A log entry in `DECISION_LOG.md`

---

## Source Template Governance

The build pipeline uses a two-path rendering model:

**Homepage route ("/"):**  
`scripts/build.py` calls `render_homepage()`, which loads `templates/home.html` as the layout template and assembles four source components:

| Template | Component | Function |
|---|---|---|
| `templates/home.html` | Layout | Placeholder template for 4 components |
| `templates/components/opening-chamber.html` | Opening Chamber | Case intake hero |
| `templates/components/examination-record.html` | Examination Record | Seven-layer case sheets |
| `templates/components/assessment-entry.html` | Assessment Entry | Diagnostic entry CTAs |
| `templates/components/doctrine-statement.html` | Doctrine Statement | Canonical authority |

`output/index.html` is a **generated file**. It must not be manually authored. The source of truth is `templates/home.html` and the four components above.

**Inner page routes (all except "/"):**  
`scripts/build.py` calls `render_full_page()` using `templates/page.html` and `templates/components/sxo-diagnostic-environment.html`.

**Shared components (all routes):**  
`templates/components/header.html` and `templates/components/footer.html` are rendered into `templates/base.html` via `render_header()` and `render_footer()`.

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

All approved JS must use the `defer` attribute to avoid render-blocking.

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

The following are prohibited unless explicitly approved through route governance and a logged decision in `DECISION_LOG.md`:

- public HTML output (`index.html`, `output/`, `public/`, `dist/`)
- JavaScript files (`.js`) not registered in `data/approved-scripts.json`
- inline event handlers in HTML templates (`onclick=`, `onload=`, etc.)
- external script tags (`<script src="http...">`)
- third-party libraries (Three.js, WebGL-only rendering, canvas-only content)
- analytics or tracking scripts (Google Analytics, Google Tag Manager, etc.)
- payment scripts (Stripe, PayPal, or equivalent)
- affiliate links or monetization scripts outside approved routes
- external dependencies (`requirements.txt`, `package.json`, etc.)
- `.env` files or committed secrets of any kind

**Exception:** Two first-party scripts are approved and governed by `data/approved-scripts.json`:
- `static/js/interface-state.js` — IntersectionObserver station active state
- `static/js/theme-toggle.js` — Session-only display mode toggle (Option A)

Both are validated by `scripts/validate_approved_scripts.py` on every push as part of the sovereign quality gate.

---

## Deployment

- GitHub Pages (via GitHub Actions) is the active deployment target
- GitHub is the source of truth
- No build output may be committed to the repository
- No deployment secrets may be stored in the repository
- Deployment configuration must be documented in `DECISION_LOG.md`
