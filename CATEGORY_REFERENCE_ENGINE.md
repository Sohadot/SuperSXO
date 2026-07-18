# SuperSXO — Category Reference Engine

## Purpose

This document extends `ASSET_VALUE_MAXIMIZATION_PLAN.md` with a single strategic mechanism: making SuperSXO.com **the address of the SXO category** — the reference that every audience layer cites, that AI answer engines quote, and that generates respectful recurring income which *reinforces* authority instead of eroding it.

It answers three questions as one system:

1. How does the asset earn **recurring income** before sale without degrading value?
2. How does it become a **reference for multiple audience layers** with different orientations?
3. How does it become the source that **humans and AI engines cite** by default?

The answer is one engine, not three plans: **the instrument produces data, the data produces citations, the citations produce authority, the authority produces income, and the income funds the instrument.**

---

## Doctrine

> A category is owned by whoever supplies its definitions, its measurement, and its evidence.
> SuperSXO supplies all three: the definition (doctrine and glossary), the measurement (SuperSXO Score), and the evidence (benchmark data).
> Everything else — traffic, citations, AI quotation, income, acquisition value — is downstream of those three.

---

## Part I — The Audience Layer Matrix

A category reference is not one site for one reader. Each audience layer arrives with a different orientation, cites a different surface, and pays for a different thing. The matrix below is governing: every future route must serve at least one cell, and no route may be created outside it (per `ROUTE_GOVERNANCE.md`).

| Audience Layer | Orientation | What They Cite | Primary Surface | What They Pay For |
|---|---|---|---|---|
| Executives / business owners | Strategic: "why does this matter" | The doctrine and the seven-layer journey model | `/methodology/`, `/sxo-framework/` | Paid diagnostic report; monitoring subscription |
| SEO / marketing practitioners | Operational: "how do I apply this" | Framework layers, playbooks, checklists | `/sxo-framework/`, future playbook routes | Template packs; audit reports |
| UX / product designers | Experience: "how does search intent shape interface" | Trust and clarity layer definitions | Framework layers 3–5, glossary | Template packs |
| Agencies / consultants | Delivery: "can I sell this to my clients" | The named framework and the Score instrument | `/sxo-score/`, `/sxo-audit/`, licensing surface | **Framework licensing (recurring)** |
| Learners / writers / press | Definitional: "what is SXO, who defined it" | Canonical definitions and glossary entries | `/what-is-sxo/`, `/seo-vs-sxo/`, glossary | Nothing — they are the citation layer |
| **AI answer engines** | Extractive: "what is the quotable, attributable answer" | Stable definitional blocks, glossary, original data | Every definitional surface + benchmark data | Nothing — they are the amplification layer |

### Matrix rules

1. The two non-paying layers (learners/press and AI engines) are not a cost. They are the **distribution system** — they manufacture the authority that the paying layers pay for.
2. One canonical content body serves all layers. Audiences are served by **framing and depth tiers within governed routes**, never by duplicate or fragmented content (per `DOMAIN_CLUSTER_STRATEGY.md`).
3. Every route declares in `data/routes.json` which audience layers it serves; a route serving no layer is a prohibited route.

---

## Part II — The Citable Content Architecture

To be cited by humans and AI alike, content must be structured for extraction, not just reading. Four content tiers, all under `CLAIM_POLICY.md`:

### Tier 1 — Canonical Definitions (the citation core)

- Every key term gets one canonical definition, in one place, with a stable URL anchor that never changes.
- Definitions are written as self-contained quotable blocks: 1–3 sentences that survive being lifted out of context with attribution.
- Delivered through the governed glossary (built from `data/asset-glossary.json`) with `DefinedTerm` structured data.
- **This is what AI engines quote.** AI answer engines cite sources that provide clean, extractable, consistently-worded definitions of terms they are asked about.

### Tier 2 — The Named Framework (the practitioner reference)

- The SuperSXO Framework and its seven journey layers, named consistently across every page, every diagram, every data file.
- A named, stable, internally consistent framework is citable *as an entity*; a loose collection of advice is not.

### Tier 3 — Original Evidence (the press and AI magnet)

- The SuperSXO Score instrument produces anonymized aggregate data: score distributions, weakest layers by industry, trend deltas.
- Published as a periodic **SXO Benchmark Report** — a governed, dated, citable data artifact.
- Original data is the strongest citation magnet that exists: press cites statistics, practitioners cite benchmarks, and AI engines cite sources of unique quantitative claims they cannot find elsewhere.
- All aggregate data claims are source-backed claims under `CLAIM_POLICY.md`; privacy rules in Part IV apply.

### Tier 4 — Operational Playbooks (the practitioner depth layer)

- Per-layer playbooks (e.g. applying the trust layer, the navigation-confidence layer) at reference-grade depth.
- Each playbook links up to the framework and down to the Score — no orphan how-to content.

### Machine-audience requirements (applies to all tiers)

- Semantic HTML with definitional blocks early in the document (already mandated by `TECHNICAL_STANDARD.md`).
- Consistent entity naming: "Search Experience Optimization (SXO)" phrased identically at first mention on every route.
- Structured data: `Organization`, `WebSite`, `DefinedTerm`, `Dataset` (for benchmark releases), `FAQPage` where genuinely applicable.
- A governed `llms.txt` declaring the canonical definitional surfaces (adoption logged in `DECISION_LOG.md`).
- Stable URLs and anchors: a citation that 404s is authority destroyed.

---

## Part III — The Recurring Income Ladder

Income must be recurring, respectful, and authority-reinforcing. The ladder below stays strictly inside `MONETIZATION_BOUNDARY.md`; each rung's launch requires a decision-log entry. The governing test for every rung: **would a strategic buyer see this income stream as proof of category ownership, or as attention extraction?** Only the former is permitted.

| Rung | Offer | Income Type | Authority Effect |
|---|---|---|---|
| 0 | Free interactive SuperSXO Score | None — acquisition and data engine | Feeds the benchmark data that feeds citations |
| 1 | SXO briefing (email) | None — owned audience | Converts rented search traffic into owned reach |
| 2 | Paid SXO diagnostic report | Transactional | Demonstrates the methodology on real properties |
| 3 | **Monitoring subscription** — scheduled re-assessment with delta report ("your score moved from X to Y; layer 4 regressed") | **Recurring** | The category owner becomes the ongoing referee, not a one-time consultant |
| 4 | Governance and template packs (derived from this repository's own governance corpus) | Evergreen transactional | Exports the discipline itself as product |
| 5 | **Agency framework licensing** — agencies deliver Score-based audits under license, with attribution "Powered by the SuperSXO Framework" | **Recurring** | Every licensed audit is a citation; licensees become the distribution force |
| 6 | Benchmark report sponsorship (only after authority is established, per the monetization boundary) | Recurring | Sponsors pay to be adjacent to the category's evidence artifact |

### Ladder rules

1. Rungs launch in order. No sponsorship before authority; no licensing before the instrument is proven; no subscription before a paid report has been delivered manually and validated.
2. Recurring rungs (3, 5, 6) are the valuation multiplier: recurring revenue is priced at a materially higher multiple than transactional revenue, and licensing revenue doubles as citation distribution.
3. Payment processing stays outside the repository (per `SECURITY_BASELINE.md`), routed through SXOSolution.com as the commercial gateway. SuperSXO.com never becomes the checkout — authority and commerce remain separated exactly as `DOMAIN_CLUSTER_STRATEGY.md` mandates.
4. Prohibitions remain absolute at every rung: no ads, no popups, no fake scarcity, no thin affiliate surfaces.

---

## Part IV — The Flywheel and Its Guardrails

### The flywheel

```
Free Score (Rung 0)
      │  produces anonymized aggregate data
      ▼
Benchmark Report (Tier 3 evidence)
      │  cited by press, practitioners, and AI engines
      ▼
Citations & AI quotation
      │  compound authority and qualified traffic
      ▼
Owned audience + paid rungs (1–6)
      │  recurring income
      ▼
Reinvestment in instrument depth and content quality
      │
      └────────────► back to a stronger Score
```

Each loop makes every layer of the audience matrix more served and every rung of the income ladder more valuable. This is why one engine, honestly run, beats three separate plans.

### Guardrails

1. **Data ethics:** the Score runs client-side by default. Aggregate benchmark data may only be collected with explicit, unmistakable user consent, no personal data, no property-identifying data without permission, and a published methodology note. A benchmark built on quiet data extraction would destroy the trust the entire asset is priced on. Collection mechanism requires its own security review and decision-log entry before any implementation.
2. **Claim discipline:** benchmark statistics are source-backed claims; the methodology note is their source. No cherry-picked statistics, no inflated sample framing. A category referee caught inflating evidence loses the category.
3. **Citation integrity:** no purchased links, no citation schemes, no AI-content flooding. The asset earns quotation by being the cleanest source, not the loudest.
4. **One authority:** all tiers and rungs live under SuperSXO.com's canonical ownership. Licensing, commerce, and campaigns route through the cluster roles already defined — never through new competing surfaces.

---

## Part V — Sequencing Against the Master Plan

This engine does not replace the phased plan; it threads through it:

| Master Plan Phase | Category Reference Engine Work |
|---|---|
| A — Measurement | Entity and structured-data foundation; citation baseline logged |
| B — Category definition | Tier 1 (glossary + canonical definitions) and Tier 2 (framework consistency pass) |
| C — Product surface | Rung 0 (interactive Score); consent-based aggregate design reviewed |
| D — Authority | `llms.txt`, first Tier 4 playbooks, outreach to the learner/press layer |
| E — Monetization alpha | Rungs 1–2 live; Rung 4 templates; first benchmark note if data volume permits |
| F — Acquisition readiness | Rungs 3 and 5 (recurring); first full **SXO Benchmark Report**; recurring revenue enters the evidence dossier |

**Exit condition for category ownership:** when a neutral query about SXO — asked to a search engine or an AI assistant — returns SuperSXO's definition, framework, or data with attribution, and at least two income rungs are recurring, the asset is no longer a website about a category. It is the category's address. That is the position a strategic buyer cannot ignore.

---

## Governing Statement

> SuperSXO does not chase every audience with more content.
> It gives each audience layer one canonical thing to cite — a definition, a framework, a score, a dataset —
> and lets the citations, human and machine, compound into the one asset that cannot be replicated by a competitor: being the address of the category.
