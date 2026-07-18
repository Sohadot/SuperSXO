# SuperSXO — Asset Evidence Dossier

## Purpose

This is the living evidence file for the SuperSXO asset. It compiles, in one place, the verifiable facts a strategic acquirer's due diligence would ask for — so that when the decision to sell is made, the asset can be presented within one week (Phase F exit criterion of `ASSET_VALUE_MAXIMIZATION_PLAN.md`).

Rules: every claim in this dossier must be verifiable from a named source (repository, decision log, Search Console export, or the live site). Metrics come from `data/metrics-log.json`, which is append-only. Nothing in this dossier is aspirational — planned work lives in the plans, not here.

---

## 1. Asset Identity

| Item | Fact | Verify at |
|---|---|---|
| Primary domain | supersxo.com — live, custom domain on GitHub Pages, DNS/edge on Cloudflare | Live site; `CNAME` |
| Domain cluster | Six domains with defined, documented roles | `DOMAIN_CLUSTER_STRATEGY.md` |
| Category position | Canonical definitional layer for Search Experience Optimization: named framework, governed glossary, measurement instrument | Live site |

## 2. Product & Content State (as of 2026-07-18)

| Component | State | Verify at |
|---|---|---|
| Published routes | 10 (9 indexable + acquisition brief, noindex) | `data/routes.json`; live site |
| SuperSXO Framework | Seven layers, each with governing conditions and failure modes published | `/sxo-framework/` |
| Governing conditions registry | 14 machine-readable conditions; Score statements validator-synchronized | `data/governing-conditions.json` |
| SuperSXO Score | Live interactive diagnostic; in-browser only, zero data transmission (browser-verified) | `/sxo-score/` |
| Glossary | 11 canonical definitions, stable anchors, DefinedTermSet JSON-LD | `/glossary/` |
| Machine discovery | sitemap.xml, robots.txt, llms.txt — generated from route registry only | Live URLs |
| Structured data | 100% route coverage (Organization/WebSite, DefinedTermSet, WebPage nodes) | Page source |
| Commercial readiness | Audit offer live with working intake; delivery standard and report template ready | `/sxo-audit/`; `AUDIT_DELIVERY_STANDARD.md` |

## 3. Governance Evidence

| Item | Fact | Verify at |
|---|---|---|
| Quality gate | 20 automated validators; enforced on every push and deploy | `scripts/quality_gate.py`; CI history |
| Decision log | Every architectural, content, security, and monetization decision recorded with reasoning | `DECISION_LOG.md` |
| Claim discipline | Six claim classes; publication structurally blocked for unclassified claims | `CLAIM_POLICY.md`; `data/claim-types.json` |
| Security posture | Static-first, three governed first-party scripts, no tracking, no third-party code, secrets policy enforced | `SECURITY_BASELINE.md` |
| Incident history | One deploy blocked by quality gate (2026-07-18), root-caused, fixed, process-corrected — publicly logged | `DECISION_LOG.md` |

The governance trail is public and timestamped in git history: an acquirer can verify that the asset was built the way its documentation claims.

## 4. Measurement Trail

Source of record: `data/metrics-log.json` (append-only).

| Date | Entry | Headline facts |
|---|---|---|
| 2026-07-18 | Official baseline | GSC verified; sitemap accepted same day; 9 pages discovered; 13/13 production URLs verified live; revenue 0; audience 0; referring domains 0 |

Growth against this baseline is the asset's forward evidence. Each future entry is dated and sourced.

## 5. Known Gaps (honest register)

- No organic traffic history yet — measurement began 2026-07-18.
- No external citations or referring domains yet.
- No revenue yet; first paid audit delivery pending first request.
- No owned audience (email list) yet — Rung 1 not launched.
- Edge security headers not yet configured (operator action, Cloudflare).

This section shrinks as the value plan executes; it is kept because a dossier that hides gaps fails due diligence and costs trust exactly when trust is priced.
