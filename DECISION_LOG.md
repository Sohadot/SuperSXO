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
claude/add-sprint-documentation-vNg8S
**Reasoning:** Sprint-1 markdown documents are human-readable but not machine-enforceable. Converting governance rules into structured JSON enables future validators, build tools, and AI agents to check route compliance, claim classification, monetization boundaries, quality gates, and domain cluster rules programmatically without re-parsing prose.  
**Impact:** All future validation tooling, route generation, and content pipelines must reference the `data/` files as the authoritative governance source. The Sprint-1 markdown documents remain the human-readable canonical reference. No public pages were created. No routes outside `data/routes.json` were introduced. No HTML, CSS, JavaScript, or templates were added.  
**Reasoning:** Sprint-1 markdown documents are human-readable but not machine-enforceable. Converting governance rules into structured JSON enables future validators, build tools, and AI agents to check route compliance, claim classification, monetization boundaries, quality gates, and domain cluster rules programmatically.  
**Impact:** All future validation tooling, route generation, and content pipelines must reference the `data/` files as the authoritative governance source. No public pages were created.  
main
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
