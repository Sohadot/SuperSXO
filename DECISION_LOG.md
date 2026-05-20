# SuperSXO — Decision Log

## Purpose

This log records every significant architectural, strategic, technical, and governance decision made during the development of SuperSXO.com.

It exists to:

- prevent re-explanation of resolved decisions
- preserve reasoning for future operators and AI agents
- document any deviations from the standards defined in this repository
- track quality gate passages before publication
- log monetization approvals and changes
- record security incidents or violations

---

## Log Format

Each entry must follow this structure:

```
## [YYYY-MM-DD] — [Decision Title]

**Type:** architecture / security / monetization / route / content / quality / other
**Status:** decided / pending / reversed
**Decision:** [What was decided]
**Reasoning:** [Why this decision was made]
**Impact:** [What this decision affects]
**Logged by:** [operator / agent / both]
```

---

## Log Entries

---

## [2026-05-20] — Sovereign VR-Spatial Interface Upgrade Added

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 10 sovereign spatial interface upgrade: transformed public alpha from a conventional styled text site into a sovereign spatial search-experience control plane. Updated `templates/base.html` with `control-plane-shell` wrapper, `skip-link`, and `main-plane` main element. Updated `templates/page.html` with `page-command-panel`, `route-context-zone`, `page-signal-header`, `content-deck`, `journey-orbit-zone` (7-layer hardcoded static HTML, no dynamic placeholder), `related-routes-panel`, and `governed-cta-zone`. Updated `templates/components/header.html` with `spatial-header`, `authority-node`, `route-cluster`, and `action-node-cluster`. Updated `templates/components/route-context.html` with `route-telemetry-panel` (hidden by default via HTML `hidden` attribute). Updated `templates/components/spatial-map.html` with `journey-orbit` section and 7-layer `journey-plane`. Updated `static/css/tokens.css` with twelve new spatial tokens (deep-space surface, orbit surface, glass surface, command surface, signal blues, grid lines, depth shadows, perspective). Fully replaced `static/css/main.css` with spatial control plane styling: CSS grid background, `backdrop-filter` sticky header, spatial panel system, journey orbit zone with CSS-only radial glows, responsive mobile breakpoints. Added new approved patterns to `data/interface-patterns.json` (control_plane_shell, spatial_command_header, search_to_action_orbit, governed_action_nodes, route_telemetry_panel, content_deck, sovereign_signal_grid) and new prohibited patterns (conventional_blog_header, broken_mobile_nav, floating_cta_overflow, generic_dark_template, ungoverned_visual_decoration). Added seven new components to `data/component-registry.json` (spatial_header, route_cluster, action_node_cluster, journey_orbit, content_deck, page_command_panel, route_telemetry_panel). Created `scripts/validate_spatial_interface.py` checking CSS class presence, no external imports, no JS files, no external scripts in templates, no deferred routes hardcoded in published templates. Added `validate_spatial_interface` to `scripts/quality_gate.py` after `validate_build_boundaries` and before `validate_deploy_assets`.  
**Reasoning:** The public alpha was rendering as a readable but visually conventional styled text site — correct for MVP but insufficient for a sovereign-grade strategic digital asset. The upgrade establishes a CSS-only spatial search-experience control plane that signals authority through depth, structure, and visual language without introducing any external dependencies, JavaScript, analytics, tracking, forms, payment links, affiliate links, or deferred route publication. All legacy CSS classes are preserved for backward compatibility. The 7-layer journey map is embedded as static HTML in `page.html` to ensure it appears on every published route without changes to `build.py`. The validator `validate_spatial_interface.py` enforces the spatial architecture integrity in the quality gate before any future change can break it.  
**Impact:** All six published alpha routes will render with the sovereign spatial control plane interface after the next build and deployment. `static/css/main.css` and `static/css/tokens.css` were fully upgraded. Seven new components are registered in the component registry. Twelve new CSS tokens are governed. Five new approved interface patterns and five new prohibited patterns are machine-readable in `data/interface-patterns.json`. A new validator enforces spatial architecture integrity in the quality gate (14 validators total). No JavaScript was introduced. No external scripts, analytics, tracking, forms, payment links, affiliate links, or monetization scripts were added. No external fonts or dependencies were introduced. No WebGL, Three.js, canvas-only content, or heavy 3D was added. No new routes were created. No deferred routes (`/seo-vs-sxo/`, `/ai-search-experience/`, `/acquisition/`) were published or hardcoded in published templates. No validators were weakened. Sovereign quality gate passes before and after build.  
**Logged by:** agent

---

## [2026-05-20] — CNAME Copied to output/ for Custom Domain Stability

**Type:** architecture  
**Status:** decided  
**Decision:** Updated `scripts/build.py` to copy the repository root `CNAME` file into `output/CNAME` during every build, alongside the governed CSS assets. Updated `scripts/validate_deploy_assets.py` to verify `output/CNAME` exists in strict mode, and to include `CNAME` in the pre-build warning list. Root cause of the live site rendering README content instead of the built pages: GitHub Pages was configured to deploy from the branch root rather than from the GitHub Actions artifact. The code-side fix (CNAME in output/) ensures the custom domain `supersxo.com` is preserved across every GitHub Actions deployment once the operator switches Pages source to GitHub Actions.  
**Reasoning:** When GitHub Pages deploys from a GitHub Actions artifact, it serves exactly what is in the uploaded artifact. If `CNAME` is absent from `output/`, GitHub Pages drops the custom domain binding after each deployment and falls back to the `*.github.io` URL. Copying `CNAME` from the repository root (the single source of truth) into `output/` on every build prevents this regression without hardcoding the domain string anywhere in the build logic.  
**Impact:** `output/CNAME` is now generated on every build alongside `output/static/css/tokens.css` and `output/static/css/main.css`. The strict deploy asset validator enforces its presence before upload. The operator action required to restore correct deployment is: Settings → Pages → Source → GitHub Actions, then trigger or await the Deploy SuperSXO Public Alpha workflow on main. No JavaScript was introduced. No external scripts, analytics, tracking, forms, payment links, affiliate links, or heavy 3D were added. No routes were changed. No deferred routes were published.  
**Logged by:** agent

---

## [2026-05-20] — Deploy Asset Validation Context Fixed

**Type:** architecture  
**Status:** decided  
**Decision:** Added `--strict` flag support to `scripts/validate_deploy_assets.py` to separate pre-build and post-build validation contexts. Without `--strict` (default): if `output/` is absent the validator skips; if `output/` exists but CSS deploy assets are missing it prints a warning and exits 0, never blocking the pre-build quality gate. With `--strict`: full enforcement — requires `output/static/css/tokens.css` and `output/static/css/main.css`, verifies HTML references both, verifies no `.js` files deployed, verifies no external stylesheet or script references, verifies no deferred route output. Updated `.github/workflows/deploy-pages.yml` to run `python scripts/validate_deploy_assets.py --strict` after build and before upload. `scripts/quality_gate.py` is unchanged and continues to invoke the validator without `--strict`, so the push/PR quality gate passes safely in both pre-build and post-build states.  
**Reasoning:** The repository carries a committed `output/` directory from Sprint 8 (HTML only, no `output/static/css/`). The Sprint 9B validator introduced in the previous commit detected this state and failed the PR quality gate before build could run, blocking the fix from landing. The correct resolution is to make strict deploy asset enforcement a deployment-time concern, not a source governance concern. The pre-build quality gate governs source files; strict deploy asset enforcement governs the built artifact. Separating these contexts by flag preserves both without weakening either.  
**Impact:** The push/PR quality gate (`quality-gate.yml`) now passes with or without `output/static/css/` present. The deployment workflow (`deploy-pages.yml`) enforces strict deploy asset validation after build, blocking upload if CSS assets are absent or any governance violation is detected. No validators were weakened. No routes were changed. No JavaScript, external scripts, analytics, tracking, forms, payment links, affiliate links, or heavy 3D were introduced. Deferred routes remain unpublished. Sovereign quality gate passes before and after build.  
**Logged by:** agent

---

## [2026-05-20] — Static Asset Deployment Fixed

**Type:** architecture  
**Status:** decided  
**Decision:** Identified root cause of unstyled public alpha: `scripts/build.py` was generating HTML that referenced `/static/css/tokens.css` and `/static/css/main.css` via absolute paths, but was not copying those files into `output/static/css/`. GitHub Pages serves only `output/` as the artifact root, so the CSS paths 404'd on every page load. Fixed by adding `copy_static_assets()` to `build.py` which copies `static/css/tokens.css` and `static/css/main.css` into `output/static/css/` after HTML generation, failing clearly if either source file is missing. Created `scripts/validate_deploy_assets.py` to verify CSS files exist in `output/`, HTML references them, no `.js` files are deployed, no external stylesheet or script references are present, and no deferred route output exists; the validator skips safely when `output/` is absent (pre-build mode). Added `validate_deploy_assets` to `scripts/quality_gate.py` after `validate_build_boundaries`.  
**Reasoning:** The Sovereign Spatial Interface styling is governed by `static/css/tokens.css` and `static/css/main.css`. Deploying unstyled HTML undermines the sovereign asset positioning and signals an incomplete deployment pipeline. The fix is minimal, contained to the build script and a new post-build validator, and does not change any route, template, content source, or security control.  
**Impact:** `output/static/css/tokens.css` and `output/static/css/main.css` are now generated on every build. The public alpha at supersxo.com will render with the intended Sovereign Spatial Interface styling after the next deployment. The quality gate now validates deployed assets after build via `validate_deploy_assets`. No JavaScript was introduced. No external scripts, analytics, tracking, forms, payment links, affiliate links, or monetization scripts were added. No external fonts or dependencies were introduced. No WebGL, Three.js, or heavy 3D was added. No deferred routes (`/seo-vs-sxo/`, `/ai-search-experience/`, `/acquisition/`) were generated or deployed. Sovereign quality gate passes before and after build.  
**Logged by:** agent

---

## [2026-05-20] — GitHub Pages Deployment Workflow Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-9 GitHub Pages deployment workflow: `.github/workflows/deploy-pages.yml` (name: Deploy SuperSXO Public Alpha, triggers: push to main and workflow_dispatch, least-privilege permissions: contents: read / pages: write / id-token: write, concurrency group: pages). Created `DEPLOYMENT_POLICY.md` governing deployment method, deployable artifact, route publication requirements, quality gate enforcement, workflow permissions, and Cloudflare policy. Updated `DECISION_LOG.md`.  
**Reasoning:** The six public alpha routes are published and `output/` is generated. The deployment infrastructure must be established through a governed workflow that enforces the sovereign quality gate before and after build, deploys only `output/`, uses least-privilege permissions, and prohibits unsafe scripts, analytics, payment links, affiliate links, forms, JavaScript, external fonts, dependencies, or heavy 3D from entering the deployment pipeline.  
**Impact:** Deployment is now automated via GitHub Actions on every push to main and via manual dispatch. The sovereign quality gate runs before and after build — deployment is blocked if either run fails. Only `output/` is deployed as a Pages artifact. Deferred routes (`/seo-vs-sxo/`, `/ai-search-experience/`, `/acquisition/`) remain unpublished and are not included in the build or deployment. No JavaScript was introduced. No external scripts, analytics, tracking, forms, payment links, affiliate links, or monetization scripts were added. No external fonts or dependencies were introduced. No WebGL, Three.js, or heavy 3D was added. No Cloudflare API token is used in the publishing workflow. No deployment from root or docs/. Least-privilege workflow permissions are enforced.  
**Logged by:** agent

---

## [2026-05-20] — Core Authority Public Alpha Published

**Type:** route  
**Status:** decided  
**Decision:** Executed Sprint-8 controlled public alpha publication: set six routes to `status: published` in `data/routes.json` (`/`, `/what-is-sxo/`, `/sxo-framework/`, `/sxo-score/`, `/sxo-audit/`, `/methodology/`). Updated all six content files to `source_status: approved_for_build` with full doctrine-grade copy across 35 total sections. Resolved two internal link blockers documented in `data/public-alpha-plan.json`: removed `/seo-vs-sxo/` from `/what-is-sxo/` required_internal_links and replaced `/acquisition/` with `/` in `/methodology/` required_internal_links. Updated `data/public-alpha-plan.json` to mark all candidate routes `approved_for_build` and `requires_internal_link_resolution: false`. Set `/acquisition/` to `indexable: false`. Extended `/`'s `required_internal_links` to include all five published alpha routes. Ran sovereign quality gate before and after build — both passed across all 12 validators. Generated six static HTML files in `output/` via `scripts/build.py`.  
**Reasoning:** The public alpha readiness infrastructure was complete and all six internal link dependencies were resolvable within the alpha route set. No route linked to an unpublished route. All content was written to doctrine-grade, claim-classified standards without prohibited language. The quality gate enforced all governance conditions before and after build. The authority layer is now live at the file system level and ready for deployment.  
**Impact:** Six pages generated: `output/index.html`, `output/what-is-sxo/index.html`, `output/sxo-framework/index.html`, `output/sxo-score/index.html`, `output/sxo-audit/index.html`, `output/methodology/index.html`. Three routes remain `planned` and unpublished: `/seo-vs-sxo/`, `/ai-search-experience/`, `/acquisition/`. `/acquisition/` is now `indexable: false`. No JavaScript was introduced. No external scripts, analytics, tracking, forms, payment links, affiliate links, or monetization scripts were added. No external fonts or dependencies were introduced. No WebGL, Three.js, or heavy 3D was added. No guaranteed rankings, conversion, traffic, revenue, or AI visibility claims were made. Sovereign quality gate passed before and after build. The core authority layer is published.  
**Logged by:** agent

---

## [2026-05-20] — Public Alpha Readiness Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-7 public alpha readiness layer: `data/public-alpha-plan.json` listing six controlled alpha candidate routes, `scripts/validate_publication_readiness.py` enforcing approved_for_build content, published internal links, no prohibited claims, and acquisition route governance. Updated `scripts/build.py` to generate clean static HTML only for published routes with approved_for_build content and verified internal links. Updated `scripts/validate_repository_hygiene.py` to allow `output/` and root `index.html` only when the approved build pipeline has generated them for published routes. Updated `scripts/quality_gate.py` to include `validate_publication_readiness` after `validate_repository_hygiene` and before `validate_build_boundaries`.  
**Reasoning:** Internal governance is complete. The repository must now support controlled public generation of a limited authority layer without broken links, thin pages, random SEO, unsafe scripts, or premature monetization. Routes remain unpublished until content is approved_for_build and all quality gates pass. The build infrastructure is complete and ready for content authoring to begin on the six alpha candidate routes.  
**Impact:** Publication is only possible when route status is `published`, content source_status is `approved_for_build`, all required_internal_links resolve to published routes, and the full quality gate passes. No routes were published. No output was generated. No root `index.html` was created. No `output/` directory was created. No JavaScript, external scripts, dependencies, forms, analytics, payment, affiliate, or heavy 3D were introduced. The six alpha candidate routes (`/`, `/what-is-sxo/`, `/sxo-framework/`, `/sxo-score/`, `/sxo-audit/`, `/methodology/`) are listed in the public alpha plan. Two link resolution notes are documented: `/what-is-sxo/` links to `/seo-vs-sxo/` and `/methodology/` links to `/acquisition/` — both must be resolved before those routes are published.  
**Logged by:** agent  

---

## [2026-05-20] — Security and Technical Hardening Baseline Added

**Type:** security  
**Status:** decided  
**Decision:** Created Sprint-6 security and technical hardening baseline: `SECURITY_BASELINE.md`, `TECHNICAL_RISK_REGISTER.md`, `data/security-baseline.json`, `data/technical-risk-register.json`, `scripts/validate_security_baseline.py`, and `scripts/validate_repository_hygiene.py`. Updated `SECURITY_POLICY.md` with Security Baseline Enforcement section, `TECHNICAL_STANDARD.md` with Repository Hygiene Enforcement section, `.github/workflows/quality-gate.yml` with `permissions: contents: read`, and `scripts/quality_gate.py` to include both new validators after `validate_prototypes` and before `validate_build_boundaries`.  
**Reasoning:** Security and technical risk prevention must be first-class governance layers before any public page, JavaScript, form, monetization script, analytics, or deployment surface is introduced. Machine-readable controls and automated validators enforce the security posture on every push, converting documentation-only policies into programmatically enforced checks. GitHub Actions workflow permissions were hardened to `contents: read` to apply least-privilege principle.  
**Impact:** Security baseline controls were added for nine governance areas (repository secrets, public output, JavaScript policy, third-party policy, dependency policy, workflow policy, headers target, forms/payments/tracking, prototype safety). A technical risk register was added with fourteen risks, all high-severity risks marked `blocks_publication: true`. Repository hygiene validation was added to the sovereign quality gate. GitHub Actions workflow permissions were hardened to `contents: read`. No public pages were created. No route was published. No root `index.html` was created. No `output/` directory was created. No JavaScript, external scripts, dependencies, forms, analytics, payment, affiliate, or heavy 3D were introduced.  
**Logged by:** agent  

---

## [2026-05-20] — Non-Public Home Prototype Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-5 non-public home prototype: `templates/prototypes/home-control-plane.html`, four component skeletons (`templates/components/hero-control-plane.html`, `templates/components/journey-layer-panel.html`, `templates/components/diagnostic-preview.html`, `templates/components/authority-statement.html`), `data/prototype-registry.json`, and `scripts/validate_prototypes.py`. Updated `scripts/quality_gate.py` to include prototype validation after `validate_visual_system` and before `validate_build_boundaries`.  
**Reasoning:** The sovereign spatial visual system is governed but untested in a structural context. A non-public prototype allows the interface direction to be tested against the approved component registry, UX layer model, and spatial token system without generating any public output, publishing any route, or creating a root index.html. The prototype lives entirely inside `templates/prototypes/` and is enforced non-public by machine-readable governance in `data/prototype-registry.json`.  
**Impact:** A non-public home prototype was added inside `templates/prototypes/`. No public page was created. No route was published. No root `index.html` was created. No `output/` directory was created. No JavaScript or heavy 3D was introduced. No external libraries, fonts, analytics, tracking, forms, or monetization scripts were added. Prototype validation was added to the sovereign quality gate. The prototype is clearly marked `NON-PUBLIC PROTOTYPE — NOT GENERATED, NOT DEPLOYED, NOT INDEXABLE` and governed by `data/prototype-registry.json`.  
**Logged by:** agent  

---

## [2026-05-20] — Sovereign Spatial Visual System Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-4 sovereign spatial visual system: `VISUAL_SYSTEM.md`, `INTERFACE_GOVERNANCE.md`, `data/component-registry.json`, `data/interface-patterns.json`, `data/visual-tokens.json`, and `scripts/validate_visual_system.py`. Updated `static/css/tokens.css` (added `--surface-control-plane`, `--grid-line`, `--focus-ring-*` tokens), `static/css/main.css` (added `.spatial-panel`, `.diagnostic-grid`, `.signal-path`, `.trust-plane`, `.search-map`, `.control-plane-shell`), `UX_UI_STANDARD.md`, and `scripts/quality_gate.py`.  
**Reasoning:** The static architecture skeleton and content registry exist but have no governed visual system. The approved Sovereign Spatial Interface direction needed to be codified into machine-readable, validator-enforced governance before any public page can be styled. The visual system now governs all component definitions, approved and prohibited interface patterns, and design token usage.  
**Impact:** Ten interface components are registered with UX layer mappings, required data sources, and accessibility requirements. Eight approved patterns and nine prohibited patterns are machine-readable. Design tokens are dual-registered in CSS and JSON. The quality gate now runs `validate_visual_system` on every push. No public pages were created. No route was published. No JavaScript or heavy 3D was added. The Sovereign Spatial Interface is now governed before public implementation.  
**Logged by:** agent  

---

## [2026-05-20] — Core Content Registry Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-3 core content registry: `data/content-model.json`, `data/page-source-map.json`, nine content contract files in `content/pages/`, and `scripts/validate_content_sources.py`. Updated `scripts/quality_gate.py` to include content source validation.  
**Reasoning:** The static architecture skeleton exists but has no governed content contracts. Content contracts define the intended purpose, required sections, claim classification, internal link requirements, and publication blockers for each registered route before any copy is written. This prevents undocumented or ungoverned content from entering the build pipeline.  
**Impact:** All nine registered routes now have content contracts with `source_status: draft_contract`. No route status was changed to `published`. No public pages were created. No HTML was generated. The quality gate now validates content source governance on every push. Content remains governed before publication.  
**Logged by:** agent  

---

## [2026-05-20] — Static Architecture Skeleton Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-2 static architecture skeleton: `content/pages/`, `templates/` (base, page, and five components), `static/css/` (tokens.css and main.css), `static/js/README.md`, `static/images/README.md`, `scripts/build.py`, and `scripts/validate_build_boundaries.py`. Updated `scripts/quality_gate.py` to include the build boundary validator.  
**Reasoning:** The governance layer and validator skeleton are complete. The static architecture skeleton establishes the design token system, template structure, and build pipeline boundaries before any public page is authored. The build script refuses to generate output unless routes have status `published`. No routes are published, so no public pages were created.  
**Impact:** Future page authorship and build execution are governed by this skeleton. The quality gate enforces that no `index.html`, no `output/` directory, and no stray HTML files may appear outside the deliberate build pipeline.  
**Logged by:** agent  

---

## [2026-05-20] — Validator Skeleton Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-1 validator skeleton: five domain-specific validators, one orchestrator (`quality_gate.py`), and a GitHub Actions workflow (`.github/workflows/quality-gate.yml`).  
**Reasoning:** Machine-readable governance files in `data/` have no enforcement layer. Validators convert governance rules into automated checks that fail loudly on any structural violation before any public page is built. The GitHub Actions workflow ensures validation runs on every push and pull request.  
**Impact:** All future changes to `data/*.json` are automatically validated on every push. No public pages were created. No dependencies outside the Python standard library were introduced.  
**Logged by:** agent  

---

## [2026-05-20] — Machine-Readable Governance Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-0 machine-readable governance data layer: eight JSON files in `data/` that convert the Sprint-1 markdown documentation into structured, queryable governance data.  
**Reasoning:** Sprint-1 markdown documents are human-readable but not machine-enforceable. Converting governance rules into structured JSON enables future validators, build tools, and AI agents to check route compliance, claim classification, monetization boundaries, quality gates, and domain cluster rules programmatically without re-parsing prose.  
**Impact:** All future validation tooling, route generation, and content pipelines must reference the `data/` files as the authoritative governance source. The Sprint-1 markdown documents remain the human-readable canonical reference. No public pages were created. No routes outside `data/routes.json` were introduced. No HTML, CSS, JavaScript, or templates were added.  
**Logged by:** agent  

---

## [2026-05-20] — Sprint-1 Foundation Documentation Created

**Type:** architecture  
**Status:** decided  
**Decision:** Created ten Sprint-1 foundation documents to replace the monolithic README with a structured, governed documentation layer.  
**Reasoning:** The README contained all strategic, technical, security, and governance information in a single file. Separating concerns improves clarity, enforceability, and AI-agent operability across sessions.  
**Impact:** All future development must reference the relevant document rather than the README alone. The README remains as an orientation and onboarding layer.  
**Logged by:** agent  

---
