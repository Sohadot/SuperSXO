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

## [2026-05-21] — True Search Experience Control Interface Added

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 11 true search experience control interface rebuild. Identified that the interface after Sprints 10 and 10B still presented as a dark card-based content website with a CSS grid background and box-shadow float cards, not as a search experience control or diagnostic system. Checked `templates/base.html` for viewport meta — `width=device-width, initial-scale=1.0` was already present; no change required. Completely rewrote `static/css/main.css`: removed CSS grid background from `.control-plane-shell`, removed box-shadow float card styling from content sections, removed radial glow decorations; added solid dark surface, `route-status-strip` (thin contextual bar below command header), `search-to-action-control-map` as the primary class for the seven-layer journey map, CSS-only signal line through journey checkpoints via `::before` pseudo-element on `.journey-plane`, numbered circular checkpoint nodes in `.layer-index`, `content-control-deck` using `gap: 1px` on dark background for diagnostic panel appearance, `governed-action-routes` replacing CTA buttons with functional diagnostic link list, `diagnostic-layer-rail` styling, full mobile breakpoints for 768px and 480px. Restructured `templates/page.html`: added `route-status-strip` at the top of every page, added `system-label` div inside `page-signal-header`, moved the seven-layer journey map to the top of the content area (above page body sections), renamed `content-deck` to `content-control-deck`, renamed `related-routes-panel` to `governed-action-routes`. Updated `templates/components/spatial-map.html` to use `search-to-action-control-map` as primary class with `journey-control-map` as backward-compatible alias. Created `scripts/validate_control_interface.py` checking: viewport meta present in base.html, main.css contains command-header, control-map, diagnostic-layer, route-telemetry, @media, overflow-x; main.css has no @import url; no external resource references; no JS files; no external script tags in templates; no deferred route paths hardcoded in published templates. Added `validate_control_interface` to `scripts/quality_gate.py` after `validate_spatial_interface` (15 validators total).  
**Reasoning:** After Sprints 10 and 10B the CSS class naming was corrected but the visual design still produced a dark blog with floating card sections and a cosmic grid background. The interface must not look like a content site — it must itself demonstrate the search-to-action journey it describes. The seven SXO layers are the central intellectual property of the asset and must be the first structural element after the heading, not buried at the bottom. The CSS grid background pattern was associated with a space aesthetic by the previous sprints and was removed entirely. Card floats were replaced with diagnostic panel rows (border-left, no shadow, gap-separated). The route-status-strip provides persistent route context without requiring JavaScript. The signal line through the journey checkpoints expresses the governed, sequential nature of the SXO system through structure rather than decoration.  
**Impact:** All six published alpha routes will render with a rebuilt search experience control interface after the next build and deployment. The seven-layer journey map is now structurally central — visible near the top of every page above content sections. Route-status-strip added to every page. CSS grid background removed. Card float styling removed. Diagnostic panel row styling added. Mobile layout comprehensively updated: command header stacks cleanly, journey becomes vertical checkpoints, no horizontal overflow, adequate padding. `validate_control_interface.py` added as validator 15 in the quality gate. No JavaScript was introduced. No external scripts, analytics, tracking, forms, payment links, affiliate links, or heavy 3D were added. No external fonts or dependencies were introduced. No WebGL, Three.js, or canvas-only content was added. No new routes were created. Deferred routes (`/seo-vs-sxo/`, `/ai-search-experience/`, `/acquisition/`) remain unpublished. No validators were weakened. Sovereign quality gate passes before and after build.  
**Logged by:** agent

---

## [2026-05-20] — Conceptual Interface Realignment Added

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 10B conceptual interface realignment. Corrected the visual direction established in Sprint 10 away from space/cosmic/orbit metaphors toward a search experience control and diagnostic system identity. Updated `VISUAL_SYSTEM.md` to reframe the interface as a "Sovereign Search Experience Control Interface" and the mental model as "Search-to-Action Control Plane"; added cosmic/orbital patterns to the Forbidden Patterns table. Updated `UX_UI_STANDARD.md` with a new section "Interface Metaphor: Diagnostic Control, Not Space"; added space-themed and orbital metaphors to the prohibited list; added step 4 to UX Decision Protocol. Updated `data/interface-patterns.json`: renamed `search_to_action_orbit` → `search_to_action_control_map`, `spatial_command_header` → `command_header_interface`, `sovereign_signal_grid` → `governed_signal_grid`; added five new prohibited patterns (cosmic_interface, outer_space_metaphor, orbit_metaphor_without_function, decorative_sci_fi_grid, visual_depth_without_diagnostic_meaning). Updated `data/component-registry.json`: renamed `spatial_header` → `command_header`, `journey_orbit` → `journey_control_map` with updated role descriptions. Updated `data/visual-tokens.json`: added control-system tokens; kept old space-themed tokens as legacy aliases. Updated `scripts/validate_spatial_interface.py` to check for `command-header` and `journey-control-map` instead of old names. Updated `static/css/tokens.css` with all new control-system tokens; old tokens converted to variable aliases. Updated `static/css/main.css`, `templates/components/header.html`, `templates/components/spatial-map.html`, and `templates/page.html`. Updated `summary` fields in four content JSON files to replace internal-planning language with sovereign asset copy.  
**Reasoning:** Sprint 10 introduced orbit, deep-space, and cosmic visual language throughout CSS class names, token names, and template classes. This framing was wrong for the asset story. The `summary` fields in four content JSON files contained internal planning notes rendered publicly via `build.py`.  
**Impact:** All six published alpha routes render with control-system class names and tokens. Old space-themed class names preserved as combined CSS selectors. No layout changes. No content changes. No route changes. No validators weakened. Quality gate passes before and after build.  
**Logged by:** agent

---

## [2026-05-20] — Sovereign VR-Spatial Interface Upgrade Added

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 10 sovereign spatial interface upgrade: transformed public alpha from a conventional styled text site into a sovereign spatial search-experience control plane. Updated base template, page template, header component, route-context component, spatial-map component. Updated `static/css/tokens.css` and `static/css/main.css`. Created `scripts/validate_spatial_interface.py`. Added `validate_spatial_interface` to `scripts/quality_gate.py`.  
**Reasoning:** The public alpha was rendering as a readable but visually conventional styled text site — insufficient for a sovereign-grade strategic digital asset.  
**Impact:** Six published alpha routes rendered with sovereign spatial interface. 14 validators total. No JavaScript, external scripts, analytics, tracking, forms, payment links, affiliate links, or heavy 3D introduced. No new routes. Deferred routes remain unpublished. Sovereign quality gate passes before and after build.  
**Logged by:** agent

---

## [2026-05-20] — CNAME Copied to output/ for Custom Domain Stability

**Type:** architecture  
**Status:** decided  
**Decision:** Updated `scripts/build.py` to copy the repository root `CNAME` file into `output/CNAME` during every build. Updated `scripts/validate_deploy_assets.py` to verify `output/CNAME` exists in strict mode.  
**Reasoning:** When GitHub Pages deploys from a GitHub Actions artifact, `CNAME` must be in the artifact or the custom domain binding is dropped.  
**Impact:** `output/CNAME` generated on every build. Strict deploy asset validator enforces its presence. Operator action required: Settings → Pages → Source → GitHub Actions.  
**Logged by:** agent

---

## [2026-05-20] — Deploy Asset Validation Context Fixed

**Type:** architecture  
**Status:** decided  
**Decision:** Added `--strict` flag support to `scripts/validate_deploy_assets.py`. Without `--strict`: skips safely pre-build. With `--strict`: full enforcement of CSS assets, HTML references, no JS files, no external resources, no deferred route output. Updated `deploy-pages.yml` to use `--strict` after build.  
**Reasoning:** Pre-build quality gate was failing because `output/` existed without CSS from a previous sprint. Strict validation is a deployment-time concern, not a source governance concern.  
**Impact:** Push/PR quality gate passes in both pre-build and post-build states. Deployment workflow enforces strict validation after build.  
**Logged by:** agent

---

## [2026-05-20] — Static Asset Deployment Fixed

**Type:** architecture  
**Status:** decided  
**Decision:** Fixed `scripts/build.py` to copy `static/css/tokens.css` and `static/css/main.css` into `output/static/css/`. Created `scripts/validate_deploy_assets.py`.  
**Reasoning:** CSS files were not being copied to the output artifact. GitHub Pages served unstyled HTML.  
**Impact:** `output/static/css/` generated on every build. Quality gate validates deployed assets.  
**Logged by:** agent

---

## [2026-05-20] — GitHub Pages Deployment Workflow Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created `.github/workflows/deploy-pages.yml`. Created `DEPLOYMENT_POLICY.md`. Least-privilege permissions enforced.  
**Reasoning:** Deployment infrastructure needed for the six published alpha routes.  
**Impact:** Automated deployment via GitHub Actions on push to main and manual dispatch.  
**Logged by:** agent

---

## [2026-05-20] — Core Authority Public Alpha Published

**Type:** route  
**Status:** decided  
**Decision:** Set six routes to `status: published`. Updated all six content files to `source_status: approved_for_build`. Resolved internal link blockers. Generated six static HTML files via `scripts/build.py`.  
**Reasoning:** Public alpha readiness infrastructure was complete.  
**Impact:** Six pages generated. Three routes remain planned and unpublished. Sovereign quality gate passed before and after build.  
**Logged by:** agent

---

## [2026-05-20] — Public Alpha Readiness Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-7 public alpha readiness layer: `data/public-alpha-plan.json`, `scripts/validate_publication_readiness.py`. Updated `scripts/build.py` and `scripts/validate_repository_hygiene.py`.  
**Reasoning:** Repository needed controlled publication infrastructure before any public output.  
**Impact:** Publication gated behind route publication status, content approval, and quality gate passage.  
**Logged by:** agent

---

## [2026-05-20] — Security and Technical Hardening Baseline Added

**Type:** security  
**Status:** decided  
**Decision:** Created Sprint-6 security and technical hardening baseline: `SECURITY_BASELINE.md`, `TECHNICAL_RISK_REGISTER.md`, security data files, `scripts/validate_security_baseline.py`, `scripts/validate_repository_hygiene.py`. GitHub Actions workflow permissions hardened to `contents: read`.  
**Reasoning:** Security must be first-class governance before any public page is introduced.  
**Impact:** Nine security governance areas enforced. Fourteen risk register entries. Quality gate updated.  
**Logged by:** agent

---

## [2026-05-20] — Non-Public Home Prototype Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-5 non-public prototype in `templates/prototypes/`. Created `data/prototype-registry.json` and `scripts/validate_prototypes.py`.  
**Reasoning:** Visual system needed to be tested against governed standards without creating public output.  
**Impact:** Prototype validation added to quality gate. No public output created.  
**Logged by:** agent

---

## [2026-05-20] — Sovereign Spatial Visual System Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-4 sovereign spatial visual system: `VISUAL_SYSTEM.md`, `INTERFACE_GOVERNANCE.md`, `data/component-registry.json`, `data/interface-patterns.json`, `data/visual-tokens.json`, `scripts/validate_visual_system.py`. Updated CSS and `scripts/quality_gate.py`.  
**Reasoning:** No governed visual system existed before any public page was styled.  
**Impact:** Ten components, eight approved patterns, nine prohibited patterns registered. Visual system validated on every push.  
**Logged by:** agent

---

## [2026-05-20] — Core Content Registry Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-3 core content registry: content model, page source map, nine content contract files, `scripts/validate_content_sources.py`.  
**Reasoning:** Content contracts enforce governed authorship before copy is written.  
**Impact:** All nine routes have content contracts. Quality gate validates content source governance.  
**Logged by:** agent

---

## [2026-05-20] — Static Architecture Skeleton Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-2 static architecture skeleton: templates, CSS, build script, boundary validator.  
**Reasoning:** Design token system and build pipeline boundaries established before public page authorship.  
**Impact:** Future page authorship and execution governed by this skeleton.  
**Logged by:** agent

---

## [2026-05-20] — Validator Skeleton Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-1 validator skeleton: five validators, one orchestrator, one GitHub Actions workflow.  
**Reasoning:** Machine-readable governance needed an enforcement layer.  
**Impact:** All future changes to `data/*.json` validated on every push.  
**Logged by:** agent

---

## [2026-05-20] — Machine-Readable Governance Added

**Type:** architecture  
**Status:** decided  
**Decision:** Created Sprint-0 machine-readable governance data layer: eight JSON files in `data/`.  
**Reasoning:** Prose documents needed to become machine-enforceable structured data.  
**Impact:** All future tooling references `data/` as the authoritative governance source.  
**Logged by:** agent

---

## [2026-05-20] — Sprint-1 Foundation Documentation Created

**Type:** architecture  
**Status:** decided  
**Decision:** Created ten Sprint-1 foundation documents replacing the monolithic README.  
**Reasoning:** Single README contained all concerns. Separation improves enforceability and AI operability.  
**Impact:** All future development references the relevant document. README is orientation only.  
**Logged by:** agent

---
