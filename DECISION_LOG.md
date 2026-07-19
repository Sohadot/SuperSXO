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

## [2026-07-19] — Phase D Distribution Started: First Public Announcement on LinkedIn; Social Preview Metadata Brought Under Control

**Type:** other  
**Status:** decided  
**Decision:** (A) Recorded the operator's publication of the first external announcement: the operating-phase conceptual post on the operator's personal LinkedIn profile (Substack planned), claim-reviewed by the manager before publication — zero performance promises, all listed components live and verifiable. This is the first distribution action of Phase D, addressed to the learner/press layer of the audience matrix. (B) Finding from the live post's link preview: LinkedIn rendered a preview title not authored by the asset ("Search Brings the Visitor. SXO Governs What Happens Next.") because the site emitted no Open Graph or Twitter card metadata — social preview metadata was present-but-not-controlled, the exact defect class the Visibility playbook's own metadata-control practice names. Fixed in the same commit: `templates/base.html` now emits `og:type`, `og:site_name`, `og:title`, `og:description`, `og:url`, and `twitter:card`/`title`/`description` on every page, populated from the same governed title, meta description, and canonical the page already declares — one metadata source, all consumers.  
**Reasoning:** The first share exposed the gap under favorable conditions (the extractor happened to quote doctrine); governance does not rely on extractors' good luck. Every future share of any route now renders exactly what the asset governs. An `og:image` brand card is deliberately deferred: it is a visual-direction decision governed by `VISUAL_DIRECTION_LOCK.md` and needs a designed asset, not an improvised one.  
**Impact:** All 17 routes emit controlled social preview metadata. Follow-ups registered: watch Search Console for first referral signals from the announcement (next metrics entry), capture any professional feedback for the evidence dossier. Full CI sequence passed.  
**Logged by:** both

---

## [2026-07-19] — Build Phase Closed: Full-Asset Production Verification Green; Operational Posture Adopted

**Type:** other  
**Status:** decided  
**Decision:** Closed the internal build phase with a full-asset production verification and adopted the operational posture. Verification: all 20 production URLs return 200 (17 routes plus the three discovery files), the live sitemap serves 16 governed URLs, and the playbook cycle closes on production — the final playbook links to the first. Evidence dossier and metrics log updated to current state.  
**Reasoning:** Every layer of the Category Reference Engine that can be built from inside the repository is now built and live. From this point, asset value accrues primarily from external signals — indexation maturing, first citations, first client — and from the operating disciplines the asset defined for itself. The repository's own Layer 7 doctrine applies to the repository: the review loop is now the work.  
**Impact:** Operational rhythm adopted: (1) metrics entries appended on every meaningful external signal (Search Console data, citations, inquiries); (2) the evidence dossier refreshed with each entry; (3) first-client readiness standing (delivery standard, report template, and channel all live); (4) Tier 3 (benchmark evidence) begins when real usage data exists, per the engine's guardrails; (5) periodic full-asset verification against the live site. Known gaps register unchanged and honest: no traffic history yet, no citations yet, no revenue yet, no owned audience yet, edge security headers still pending operator action.  
**Logged by:** agent

---

## [2026-07-19] — PLAYBOOK LIBRARY COMPLETE: Strategic Outcome Alignment Published (Tier 4 #7 of 7)

**Type:** content  
**Status:** decided  
**Decision:** Published `/playbooks/strategic-outcome-alignment/`, completing the Tier 4 practitioner library: seven playbooks, one per journey layer, each operationalizing its layer's two governing conditions from `data/governing-conditions.json`, chained through the journey sequence, and closed as a cycle — the final playbook links back to the first, because a strategy that moves redefines the intents worth serving. Seventeen published routes (sixteen indexable). Library-completion milestone appended to `data/metrics-log.json`.  
**Reasoning:** Layer 7 closes the framework because it is the only layer whose failure hides inside apparent success: "an ordinary website succeeds when actions complete; a governed asset succeeds when completed actions compound into what the asset was built to produce."  
**Impact:** Six sections: sovereign-asset scope; the needed-actions practice (the action-to-need mapping as "an audit of honesty about the asset's own machinery" — unconnected actions are "decoration wearing the costume of conversion," unmeasured actions are "a rumor about the asset's performance"); the review-loop practice (deliberately mundane requirements — scheduled cadence, written findings, and the distinguishing rule that findings must change the asset: "a review that produces findings which change nothing is a ritual"); hollow-conversion diagnosis (two-ledger divergence, traced past where the analytics stop, with three findings: alignment, broken chain, wrong action); maintenance against strategy drift (the loop itself is the maintenance; "drift, by definition, does not announce itself"); and the closing measurement pathway that loops the library to Layer 1. With this entry, the Category Reference Engine's four content tiers are all live: Tier 1 glossary, Tier 2 framework, Tier 4 playbooks — Tier 3 (benchmark evidence) awaits usage data by design. Route registered (alpha plan candidate 17); sitemap and llms.txt at 16 governed URLs. Full CI sequence passed.  
**Logged by:** agent

---

## [2026-07-19] — Action Pathway Integrity Playbook Published (Tier 4 #6)

**Type:** content  
**Status:** decided  
**Decision:** Published `/playbooks/action-pathway-integrity/` as the sixth Tier 4 surface, operationalizing Layer 6's conditions Q11–Q12. Sixteen published routes (fifteen indexable). Chain: intent ↔ visibility ↔ experience ↔ trust ↔ navigation ↔ action.  
**Reasoning:** Completion mechanics only, with the boundary stated in scope: nothing in this playbook manufactures intention, and no practice substitutes for the upstream layers that do. The layer's history on this asset (RISK-015) informed the discipline without being referenced on the public page.  
**Impact:** Six sections: scope with the completion-mechanics boundary; the terminal-action practice ("one is the operative number — a page assigned two terminal actions has been assigned a conflict, and the visitor inherits it"; the execution test on real devices and conditions, every unnecessary form field named as unnecessary friction); the uninterrupted-path practice (the interruption inventory with its single test — does removing it cost the journey anything? — and competing calls resolved by hierarchy, not elimination); failure diagnosis of dissipation (boundary with navigation failure drawn: never saw the path versus worn out on it; repair from the end backward because "the deepest friction is destroying the most committed visitors"); maintenance ("interruption removal has no natural constituency, which is why it must have a governed one"); measurement pathway handing the strategic question to Layer 7. Route registered (alpha plan candidate 16); sitemap and llms.txt at 15 governed URLs. Full CI sequence passed.  
**Logged by:** agent

---

## [2026-07-19] — Navigation Clarity Playbook Published (Tier 4 #5)

**Type:** content  
**Status:** decided  
**Decision:** Published `/playbooks/navigation-clarity/` as the fifth Tier 4 surface, operationalizing Layer 5's conditions Q9–Q10. Fifteen published routes (fourteen indexable). Chain: intent ↔ visibility ↔ experience ↔ trust ↔ navigation.  
**Reasoning:** Path-confidence framing held throughout, per the framework's definition — never menu design or generic usability language: "a menu offers everywhere and path confidence requires somewhere."  
**Impact:** Six sections: scope (the layer that converts a trusting visitor into an acting one); the next-step practice (a decision before a design — each entry page's intended next step recorded beside its intent definition, with evident as a higher bar than present); the no-dead-ends practice (onward-link audit judging destinations as purposeful, catching both pages with nowhere to go and links that "serve the operator's sitemap rather than the visitor's journey"); failure diagnosis by walking journeys, not pages (three stall-point kinds: the fork with no signpost, the finished page, the ambiguous label); maintenance with the structural rule that new pages enter with their journey position defined at publication; measurement pathway pairing navigation readings with trust readings ("a visitor stalls either because they do not believe the source or because they cannot see the path — the treatments are entirely different"). Route registered (alpha plan candidate 15); sitemap and llms.txt at 14 governed URLs. Full CI sequence passed.  
**Logged by:** agent

---

## [2026-07-19] — Trust Signal Coherence Playbook Published (Tier 4 #4)

**Type:** content  
**Status:** decided  
**Decision:** Published `/playbooks/trust-signal-coherence/` as the fourth Tier 4 surface, operationalizing Layer 4's conditions Q7–Q8. Fourteen published routes (thirteen indexable). The chain now runs intent ↔ visibility ↔ experience ↔ trust.  
**Reasoning:** The doctrinally central playbook: trust is the layer the editorial standard names as what separates SXO from shallow search practice, and its failure mode is the most expensive — "an experience failure loses a visit; a trust failure loses the visitor." The page was written to survive its own adversarial reading: every claim doctrine-classified, no promises anywhere.  
**Impact:** Six sections: threshold-condition scope; the claim-support practice (claim inventory with three resolutions — supported, reframable, removable — and the cardinal violation defined: unsubstantiatable promises as "trust debt, borrowed from the visitor at the moment of persuasion and repaid with interest at the moment of disappointment"); the consistency practice (identity, terminology, presentation held to canonical reference forms — "consistency is not a matter of taste but of conformance"); failure diagnosis by adversarial reading (the silent failure that renders no error); maintenance with the double-weight record (the verification log is itself a trust signal); measurement pathway noting this layer gates the two that follow. Route registered (alpha plan candidate 14); sitemap and llms.txt at 13 governed URLs. Full CI sequence passed.  
**Logged by:** agent

---

## [2026-07-19] — Ruling: Playbook Chain Confirmed Live by Three Methods; /acquisition/ Published-Noindex Reaffirmed

**Type:** quality  
**Status:** decided  
**Decision:** (A) Closed the operator's repeated finding that playbook cross-links are absent from live pages: three independent verification methods confirm the chain is present and visible on production. (1) Raw HTML via curl with cache busters: the live Continue Examination panels contain intent→visibility, visibility→intent+experience, and experience→visibility as plain `<li><a href>` markup. (2) Rendered-visibility check in headless Chromium against the built pages: the panel has a real bounding box, `display: block`, `visibility: visible`, and its links pass an offsetParent visibility filter. (3) Registry-to-output verification in the quality gate. Root cause of the discrepancy: the operator's checking tool does not report links inside the `<nav aria-label="Continue examination">` landmark — a tool-extraction artifact, not an asset defect. Verification guidance for manual confirmation: open the live page, scroll to the "Continue Examination" panel above the CTA zone, or view page source and search for `related-routes-panel`. (B) Reaffirmed the `/acquisition/` ruling in answer to the operator's direct question: the route is **deliberately published with `indexable: false`** — live at 200 for direct-link access by qualified acquirers and via the footer, excluded from sitemap.xml, llms.txt, and the index via meta robots. This is the design ordered by `ASSET_VALUE_MAXIMIZATION_PLAN.md` Phase F ("kept non-indexable") and logged at publication on 2026-07-18. The alternative (fully unpublished) would leave the acquisition inquiry channel with no destination page; the operator may override this ruling, and an override reverts the route to `planned` in one commit.  
**Reasoning:** A finding repeated twice deserved escalation from single-method to triple-method verification before any code was touched — and the evidence shows the build, the governance data, and the live product are consistent. No fix is applied because there is nothing to fix; recording the verification protects the next operator from re-investigating the same artifact.  
**Impact:** No code changes. Verification evidence recorded. `/acquisition/` status unchanged pending any operator override.  
**Logged by:** both

---

## [2026-07-19] — Playbook Chain Verified Live; Experience Quality Playbook Published (Tier 4 #3)

**Type:** content  
**Status:** decided  
**Decision:** (A) Resolved the operator's finding that the two published playbooks did not cross-link on production: verification against the live site shows both directions present (`/playbooks/visibility-conditions/` → intent, intent → visibility) in the Continue Examination panels; the links shipped in the visibility commit and the operator's check predated deploy propagation (live `last-modified` 2026-07-19 06:32 GMT). No structural defect; no fix required. (B) Published `/playbooks/experience-quality/` as the third Tier 4 surface, operationalizing Layer 3's conditions Q5–Q6. Thirteen published routes (twelve indexable).  
**Reasoning:** The operator's ruling — playbooks must work as an operational chain, not isolated pages — was verified satisfied before proceeding, per their instruction. Layer 3 continues the journey order; the playbook's discipline is one the asset itself practices (all core routes readable without JavaScript), stated as engineering rationale rather than self-praise.  
**Impact:** Six sections in the Tier 4 register: scope (functional quality from the visitor's perspective — "this playbook governs what actually renders"); the performance-and-mobile practice (a budget, not an aspiration — performance decays by accumulation); the resilience practice (the core/enhancement line, the disabled-script review, and the machine-reader extraction rationale); failure diagnosis (honest reproduction on the visitor's constraints — "a visitor who left before the page settled never met the content at all; only that is this layer's failure"); maintenance as change discipline (regressions caught at introduction, not archaeology); measurement pathway. No tool names anywhere — tools change, conditions do not. Chain extended: visibility ↔ experience. Route registered (alpha plan candidate 13); sitemap and llms.txt at 12 governed URLs. Full CI sequence passed.  
**Logged by:** both

---

## [2026-07-18] — Email Obfuscation Resolved; Visibility Conditions Playbook Published (Tier 4 #2)

**Type:** content  
**Status:** decided  
**Decision:** (A) Confirmed resolved: the operator disabled Cloudflare Email Address Obfuscation (Security → Settings) and purged the edge cache; live verification shows both governed addresses rendering as plain text on `/sxo-audit/` and `/acquisition/` with no email-protection remnants — the readable-without-JavaScript doctrine holds on production again. (B) Published `/playbooks/visibility-conditions/` as the second Tier 4 practitioner surface, operationalizing Layer 2's conditions Q3–Q4. Twelve published routes (eleven indexable).  
**Reasoning:** Playbook library proceeds in journey order. Visibility carries the highest claim risk of any layer — the discipline's own doctrine is the defense: conditions, never outcomes; the playbook governs the conditions of being found and explicitly promises nothing about position, traffic, or what any search system decides.  
**Impact:** (1) Six sections mirroring the Tier 4 register: scope (necessary-but-insufficient framing); the metadata-control practice (control as the operative word — templated titles are "present but not controlled"; a metadata registry making duplication visible before publication); the indexation practice (sitemap discipline — "a page in the sitemap but absent from the index is a finding to investigate, not a statistic to accept"; designed-query verification connecting back to Layer 1); twofold failure diagnosis (invisibility via coverage data, misdirected visibility via query data — "a Layer 1 remedy reached through a Layer 2 diagnosis"); condition maintenance (pages become indexable through governance, never by being published and left for discovery); and the measurement pathway. (2) Playbooks now chain through the journey sequence: intent ↔ visibility linked both directions. (3) Route registered (alpha plan candidate 12), sitemap and llms.txt at 11 governed URLs. Full CI sequence passed.  
**Logged by:** both

---

## [2026-07-18] — First Tier 4 Practitioner Surface Published: Intent Alignment Playbook

**Type:** content  
**Status:** decided  
**Decision:** Published `/playbooks/intent-alignment/` as the first Tier 4 operational playbook of the Category Reference Engine, opening the `/playbooks/` route family. Eleven published routes (ten indexable).  
**Reasoning:** The audience matrix's practitioner layer needs operational depth: the framework defines what must be true; playbooks define the working practices that make it true. Layer 1 goes first because it is the journey's entry condition and the first pair of statements in every Score reading and audit. The playbook operationalizes conditions Q1–Q2 without tutorial tone or performance promises, consistent with the content standard.  
**Impact:** (1) Six sections: scope anchored to the governing-conditions registry; the intent-definition practice (a dated artifact answering four questions, written before the page — retroactive documentation explicitly fails the condition); the first-screen discipline (ordering rule plus mechanical viewport review); misalignment diagnosis working backward from query data (alignment / drift / absence findings, per the layer's published failure mode); condition maintenance (decay detection as the difference between evidence and assumption); and the measurement pathway bridging to Score and audit. (2) Route registered (role `operational_playbook`, ux_layer `search_intent`, nested path — first non-flat route, build and validators handle it), alpha plan candidate 11, source mapped. (3) Framework page links to the playbook via required internal links (inbound path). (4) Sitemap and llms.txt automatically include the new surface (10 governed URLs). (5) Full CI sequence passed post-build; the pre-build gate correctly flagged the stale committed sitemap against the updated registry before rebuild — the discovery validator working as designed.  
**Logged by:** agent

---

## [2026-07-18] — Asset Evidence Dossier Started; Metrics Log Established; Full Production Verification Green

**Type:** other  
**Status:** decided  
**Decision:** (A) Created `docs/evidence/ASSET_EVIDENCE_DOSSIER.md` as the living buyer-facing evidence file (Phase F preparation started early, per the one-week-presentation exit criterion) and `data/metrics-log.json` as its append-only machine-readable source of record, seeded with the official baseline. (B) Ran the first full production verification of the live site: all 13 URLs (10 routes + three discovery files) return 200; acquisition noindex confirmed live; Score form, DefinedTermSet, and both contact channels confirmed live; sitemap serves 9 URLs. (C) Finding recorded: Cloudflare Email Obfuscation is active at the edge — published email addresses are rewritten into JS-decoded protected links. Functional for JS users, but it conflicts with the asset's readable-without-JavaScript doctrine (no-JS visitors see "[email protected]"). Recommendation to operator: disable Scrape Shield → Email Address Obfuscation; the aliases are deliberate governed routing addresses, and inbox filtering is the appropriate spam control.  
**Reasoning:** Evidence must accrue in a governed place from the day the baseline exists, not be assembled retroactively at sale time; the dossier's rules (every claim verifiable from a named source; append-only metrics; an honest known-gaps register) are what make it worth more than a pitch deck. The production check also confirmed deploys #26–27 landed correctly.  
**Impact:** Dossier sections: asset identity, product/content state, governance evidence (including the publicly logged deploy incident as evidence the gate works), measurement trail, and the honest gaps register (no traffic history, no citations, no revenue, no audience, headers pending) — kept deliberately because a dossier that hides gaps fails due diligence. Metrics log entry 1: the 2026-07-18 baseline with GSC, production, and repository-state facts. Full CI sequence passed: 20 validators.  
**Logged by:** agent

---

## [2026-07-18] — Audit Delivery Package: Governing-Conditions Registry, Delivery Standard, Report Template

**Type:** monetization  
**Status:** decided  
**Decision:** Built the audit delivery package so the first paid audit can be delivered to standard within days of a request: (1) `data/governing-conditions.json` created as the single source of record for the fourteen governing conditions, with per-condition audit evidence guidance; (2) `validate_score_instrument` extended to enforce verbatim synchronization between the Score component's statements and the registry; (3) `AUDIT_DELIVERY_STANDARD.md` adopted as the governance document for conducting, writing, claim-reviewing, and delivering audits; (4) `docs/audit/audit-report-template.md` created as the deliverable skeleton.  
**Reasoning:** With the intake channel live, a paid request can arrive any day; delivering it ad hoc would waste the asset's central claim — that the methodology is governed and reproducible. The fourteen conditions previously existed only as component HTML and framework prose with no machine-readable source; the registry extends the single-source doctrine to the instrument itself, and the sync validator makes divergence impossible (negative-tested: a one-word statement change fails the gate). Each delivered report becomes evidence of the methodology working on a real property — a delivery-quality event is an asset-value event.  
**Impact:** (1) Registry: 14 conditions with ids Q1–Q14, layer mapping, verbatim statements extracted from the published component, score weights, and evidence guidance per condition. (2) Delivery standard: seven process stages (intake through decision-log record), findings discipline (evidence-or-no-finding, interpretation labeling, no operator-scoring, non-guarantee restated in every report), pricing governance (no published prices without a logged decision), and the delivery boundary (findings only; Rung 3+ pathways in the cover note, never as pressure inside findings). (3) Template: engagement scope with non-guarantee block, method, layer readings summary, per-condition findings blocks (state / evidence / continuity risk / direction of correction), continuity-ordered priority register, limitations, and framework/glossary references as governing texts. (4) Full CI sequence passed: 20 validators, build, strict deploy validation.  
**Logged by:** agent

---

## [2026-07-18] — OFFICIAL BASELINE RECORDED: Search Console Verified, Sitemap Accepted; Contact Channels Live; /acquisition/ Published; RISK-015 Resolved

**Type:** other  
**Status:** decided  
**Decision:** Recorded the Phase A official measurement baseline and completed the search-to-action loop: both operator-side actions from the value plan are done, the contact channels are wired into the published pages, the acquisition brief is live (noindex), and RISK-015 is resolved — all in one commit, as committed to in the risk's resolution path.  
**Reasoning:** The baseline is the dated starting point that all future growth evidence is measured against; it must be logged the day it exists. The contact channels resolve the asset's only high-severity open risk and complete, for the first time, a functioning end-to-end journey on the asset itself: search → content → Score → audit request that can actually be sent.  
**Impact:** **(A) Official baseline, 2026-07-18:** Google Search Console verified for supersxo.com; `sitemap.xml` submitted and accepted same day (status: success); **9 pages discovered, 0 videos**; organic impressions at measurement start: effectively zero (property newly verified). All future traffic, indexing, and citation growth is measured against this entry. **(B) Contact infrastructure live:** Cloudflare Email Routing active with two governed aliases — `pro@supersxo.com` (professional inquiries) and `acquisition@supersxo.com` (acquisition inquiries), both forwarding to the operator's private inbox without exposing it. **(C) Wiring:** `/sxo-audit/` intake now names `pro@supersxo.com` as the submission channel — the primary commercial terminal action is completable; homepage `Organization` JSON-LD gained `email` and `contactPoint`. **(D) `/acquisition/` published** (route published, `indexable: false`, meta robots noindex): reachable by direct link and footer navigation, structurally excluded from sitemap.xml, llms.txt, and the index; inquiry section names `acquisition@supersxo.com`; alpha plan candidate 10; deferred-route lists in the five validators are now empty — all ten registered routes are published. **(E) RISK-015 downgraded** to low/resolved with the alias-governance rule (any routing change is a logged event) and residual-risk note. Full CI sequence passed: 20 validators, 10 routes built, strict deploy validation green.  
**Logged by:** both

---

## [2026-07-18] — Acquisition Brief Authored; Missing Contact Channel Registered as Blocking Risk; WebPage Structured Data Generalized

**Type:** content  
**Status:** decided  
**Decision:** (A) Authored the full `/acquisition/` buyer-facing brief against its draft contract; source moved to `draft_content`, route intentionally kept unpublished. (B) Registered RISK-015 in the technical risk register: the asset has no functioning contact or inquiry channel anywhere — the audit request terminal action and the future acquisition inquiry have no completion mechanism, meaning the asset currently fails its own Layer 6 (Action Pathway Integrity) governing condition. Severity high, blocks_publication true: no new surface that names a submission mechanism may publish until the operator defines the channel. (C) Extended the build so every route without explicit structured data receives an auto-generated `WebPage` JSON-LD node derived from the route registry.  
**Reasoning:** The acquisition contract's own blocker list anticipated this: "Acquisition contact mechanism must be defined and in place." Authoring the brief now means the page publishes the same day the channel exists. The risk had to be formally registered rather than silently tolerated — an asset whose doctrine defines Action Pathway Integrity cannot leave its own terminal actions uncompletable without recording that as a governance finding. The recommended resolution is a dedicated alias via Cloudflare Email Routing (available since NS delegation), an operator-side action.  
**Impact:** (1) All five acquisition sections written at executive-brief register: positioning, the six-component asset package, cluster summary, a strategic value statement grounded in verifiability ("no claim in this brief requires taking the operator's word"), and an inquiry section defining qualification and the hold-indefinitely posture — its final sentence is the designated insertion point for the channel. Publication blockers updated to the exact remaining steps. (2) RISK-015 recorded with prevention, detection, and a resolution path that downgrades the risk in the same commit that ships the channel. (3) `render_structured_data` auto-generates a `WebPage` node (canonical `@id`, title, description, `isPartOf` the site's `#website`) for the seven routes without explicit structured data; homepage and glossary keep their richer graphs. Verified in built output. (4) Full CI sequence passed — including one governance catch during the sprint itself: the security baseline validator rejected RISK-015 as originally filed (severity high without blocks_publication), forcing the honest classification. The gate corrected its operator.  
**Logged by:** agent

---

## [2026-07-18] — Phase B Closed: Methodology Drift Corrected, Commercial Pages Deepened

**Type:** content  
**Status:** decided  
**Decision:** Completed the reference-deepening pass across `/methodology/`, `/sxo-audit/`, and `/sxo-score/`, correcting two factual drift defects in the published methodology page. Phase B (category definition completion) of `ASSET_VALUE_MAXIMIZATION_PLAN.md` is closed: ten routes at reference depth. The homepage is intentionally excluded from this pass — it renders from the governed component set, is a deliberate design surface, and carries no reference-content burden.  
**Reasoning:** The methodology page — which claims the asset's governance is strict — itself contradicted the governance files: it enumerated eighteen quality gates by name (twenty exist) and described three claim classes (`data/claim-types.json` defines six). A governance page that drifts from its own registries undermines the exact trust it exists to build. The rewrite also removed the brittle pattern: gates are now described by their seven enforcement domains with the machine-readable registry named as authoritative, so the page no longer decays with every validator added.  
**Impact:** (1) `/methodology/` `claim_discipline` rewritten to define all six governed claim classes; `quality_governance` rewritten around seven enforcement domains (data, route, content, interface, script, security, deployment) with the growth rule — every new surface ships with its validator; new `definition_governance` section documents the glossary source-of-record rule, stable anchors, and why citability depends on it; `/glossary/` added to required internal links. (2) `/sxo-audit/` gained `relation_to_the_score`: the same framework at two depths — self-reported directional signal versus independent professional diagnosis, with the honest sequence stated (Score first). (3) `/sxo-score/` gained `reading_the_assessment`: the three governance bands (Governed, Partially governed, Ungoverned) defined as published doctrine with the re-assessment cadence — bands describe condition states, not operator grades, not metric predictions. (4) Full CI sequence passed locally: 20 validators, build, strict deploy validation.  
**Logged by:** agent

---

## [2026-07-18] — Cloudflare NS Delegation Active; Reference Deepening of Framework and Definition Pages

**Type:** architecture  
**Status:** decided  
**Decision:** (A) Recorded the operator's report that supersxo.com DNS is now delegated to Cloudflare nameservers — Cloudflare is active as the DNS/edge layer, GitHub Pages remains the deployment target, exactly as `DEPLOYMENT_POLICY.md` and `DOMAIN_CLUSTER_STRATEGY.md` prescribe. This unlocks the edge-configured security headers named as a target in `SECURITY_BASELINE.md`; header configuration is an operator-side Cloudflare action, recommended next. (B) Executed the first reference-deepening pass of Phase B: `/sxo-framework/` and `/what-is-sxo/`.  
**Reasoning:** The framework page defined the seven layers but not their governing conditions — leaving the Score instrument's 14 statements without a published doctrinal source, a defensibility gap for the asset's core IP. The definition page lacked boundary-setting (what SXO is not), audience mapping, and a bridge to the glossary citation core. Deepening means adding governing substance, not word count.  
**Impact:** (1) Each of the seven framework layer sections now defines its two governing conditions — verbatim-aligned with the Score instrument statements — and its characteristic failure mode; the assessment-pathway section states the traceability rule: the instrument measures exactly what the framework governs. (2) `/what-is-sxo/` gained three sections: `what_sxo_is_not` (boundary-setting against CRO, UX, and reporting-layer readings, respectful of each discipline), `who_practices_sxo` (the four practitioner altitudes, public-facing reflection of the audience layer matrix), and `canonical_definitions` (glossary bridge with the attribution rule). (3) `/glossary/` added to `/what-is-sxo/` required internal links in routes.json and the content source. (4) Full CI sequence passed locally: pre-build gate, build, strict deploy validation, post-build gate — 20 validators.  
**Logged by:** both

---

## [2026-07-18] — Machine-Discovery Surfaces Shipped: sitemap.xml, robots.txt, llms.txt

**Type:** architecture  
**Status:** decided  
**Decision:** Added the three machine-discovery files to the governed build: `sitemap.xml`, `robots.txt`, and `llms.txt`, all generated by `scripts/build.py` exclusively from `data/routes.json` — published and indexable routes only — with `validate_discovery_files` as the 20th quality gate validator enforcing the invariant.  
**Reasoning:** Phase A (measurement foundation) and Phase D (authority and AI-search readiness) both require the asset to be discoverable by machines: a sitemap for search engine indexing, robots directives with the canonical sitemap pointer, and an `llms.txt` declaring the canonical citable surfaces with an attribution statement for AI answer engines — the machine-audience requirement of the Category Reference Engine. None existed. Generation from the route registry (never a hand-maintained list) extends the single-source-of-truth doctrine reaffirmed by the deploy incident earlier today.  
**Impact:** (1) `build.py` `write_discovery_files()` emits all three files into `output/` on every build: sitemap with the 9 published indexable canonical URLs; robots.txt allowing all crawling with the canonical Sitemap pointer; llms.txt with the doctrine summary, attribution statement, and one line per canonical surface using each route's governed meta description. (2) `/acquisition/` (unpublished, noindex) is structurally excluded from all three surfaces. (3) `scripts/validate_discovery_files.py` added: verifies exact set equality between discovery URLs and governed routes (no missing, no leaked), sitemap XML validity and canonical-domain purity, robots sanity (no site-wide Disallow, canonical Sitemap pointer), and llms.txt attribution presence; pre-build non-strict mode mirrors the deploy-assets validator. Negative-tested: an injected unpublished URL in the sitemap is caught. (4) Full CI sequence replicated locally per the incident process correction: pre-build gate, build, strict deploy validation, post-build gate — all pass with 20 validators.  
**Logged by:** agent

---

## [2026-07-18] — Incident: Production Deploy Blocked by Stale Script List in Deploy Validator

**Type:** quality  
**Status:** decided  
**Decision:** Completed the script-source unification that the hardening pass began: `scripts/validate_deploy_assets.py` now derives its approved-JS list from `data/approved-scripts.json` instead of carrying its own hardcoded copy. No validator or build script carries a script list anymore.  
**Reasoning:** Deploy run #19 (workflow "Deploy SuperSXO Public Alpha", main commit cd84f0a) failed at the strict post-build asset validation: `output/static/js/sxo-score.js` was flagged as unapproved because `validate_deploy_assets.py` still held a hardcoded two-script list predating the Score instrument. This was precisely the drift class the script-source-unification review identified — the hardening pass unified `build.py` but missed this validator's private list. It escaped local verification because the local quality gate runs this validator in non-strict pre-build mode; the strict mode executes only post-build, and the strict step was not run locally before the Score sprint was pushed. No security impact and no public breakage: the failed gate correctly blocked the deploy, and the previously deployed site remained live.  
**Impact:** (1) `validate_deploy_assets.py` loads its approved-JS list from `data/approved-scripts.json`; a comment records the incident at the load site. (2) Repository swept for remaining hardcoded script lists: none remain (`validate_repository_hygiene` already derives from the data file; other matches are documentation comments). (3) Process correction adopted: every sprint that touches scripts or output must replicate the full CI sequence locally before push — pre-build gate, build, `validate_deploy_assets.py --strict`, post-build gate. This fix was verified with that exact sequence: all four steps pass.  
**Logged by:** agent

---

## [2026-07-18] — Security Hardening: Escaping, Script Source Unification, Baseline Alignment

**Type:** security  
**Status:** decided  
**Decision:** Accepted four advisor findings and executed them as a hardening pass: (1) HTML escaping in the build pipeline, (2) `data/approved-scripts.json` unified as the single source of truth for scripts, (3) `validate_approved_scripts` strengthened, (4) `SECURITY_BASELINE.md` realigned with repository reality. Two additional contradictions found and fixed during the review: the baseline described a Cloudflare Pages deployment with uncommitted output (reality: GitHub Pages with governed committed `output/`), and `DEPLOYMENT_POLICY.md` prohibited all JavaScript and forms while three governed scripts and the client-side instrument form exist.  
**Reasoning:** Content sources are trusted governed files, but unescaped injection is a latent defect that grows with every content contributor and every new surface; the duplicated script list was three-way drift waiting to happen; the validator's global `defer` check would pass a template with one deferred tag and one undeferred; and a security baseline that contradicts observable reality trains operators to ignore it.  
**Impact:** (1) `build.py`: every leaf value originating in JSON data (titles, meta descriptions, headings, section bodies, summaries, nav labels, route context values, anchors) is HTML-escaped before template injection; component/template HTML is never escaped; JSON-LD serialization hardens `<` to `<` so no data value can close the script element. (2) `build.py` derives its script list from `data/approved-scripts.json` (rejecting anything outside `static/js/`) — the hardcoded list is gone. (3) `validate_approved_scripts`: per-entry governance fields enforced (`defer: true`, `external_dependencies: false`, purpose/allowed/forbidden APIs), per-tag defer verification via exact tag pattern, detection of unapproved script tags and executable inline scripts in `base.html` (ld+json exempt). Negative-tested: an undeferred tag and a rogue script tag are both caught. (4) `SECURITY_BASELINE.md`: JavaScript policy rewritten from "not approved" to approved-under-governance with the single-source rule and enforcement map; forms prohibition refined to data-transmitting forms with a registered-instrument carve-out; deployment assumptions rewritten for GitHub Pages with governed committed output; `DEPLOYMENT_POLICY.md` prohibited-actions aligned; `data/security-baseline.json` `javascript_policy` and `public_output` controls updated to match the enforced validators. Full 19-validator gate passes; browser re-verification confirms the instrument computes correctly (28/28 = 100% on all-Present), no raw entities render, glossary JSON-LD parses, zero page errors.  
**Logged by:** agent

---

## [2026-07-18] — Interactive SuperSXO Score Instrument Shipped (Rung 0)

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Phase C of `ASSET_VALUE_MAXIMIZATION_PLAN.md`: converted `/sxo-score/` from a descriptive page into a working interactive self-assessment instrument — Rung 0 of the recurring income ladder in `CATEGORY_REFERENCE_ENGINE.md`. Also emitted `Organization` and `WebSite` JSON-LD on the homepage via the governed structured-data mechanism.  
**Reasoning:** The instrument is the single highest-leverage value action in the adopted plans: it converts the asset from content about SXO into the instrument that measures SXO, and it is the acquisition surface feeding the paid audit pathway. Privacy-first design was mandatory: the free assessment must build trust, so all answers stay in browser memory with no transmission, storage, or gating — verified in a real browser (zero external requests).  
**Impact:** (1) `templates/components/score-instrument.html` created: 14 claim-governed condition statements across the seven journey layers, each answered Present/Partially present/Absent (2/1/0), in accessible fieldsets with `role=group` labeling, an `aria-live` result region, a noscript fallback, and a compute button that ships disabled until the script activates it — statements remain fully readable without JavaScript. (2) `static/js/sxo-score.js` approved as the third first-party script: builds the assessment reading with createElement/textContent only (per-layer bands Governed / Partially governed / Ungoverned, weakest-layer finding, mandatory non-guarantee disclaimer, clinical pointer to `/sxo-audit/`); no-op on every other page. (3) `scripts/build.py` extended with a governed `interactive_component` allowlist; `templates/page.html` gained the instrument slot. (4) `score_instrument` registered in `data/component-registry.json` with prohibited behaviors including answer transmission, email gating, fake urgency, and guarantee-implying result wording. (5) Instrument styles appended to `main.css` using existing visual tokens. (6) `scripts/validate_score_instrument.py` added as the 19th validator: verifies script approval and forbidden-pattern absence, component structure (7 fieldsets, q1–q14, 42 radios valued 0/1/2, aria-live, noscript, disabled-by-default button), no inline script/style or external URLs, and instrument exclusivity to `/sxo-score/` in sources and built output. (7) Functional verification in headless Chromium: computation exact (19/28 = 68% on a mixed answer set), incomplete-answer detection correct, zero external network requests, script inert on other routes, homepage JSON-LD parsing as Organization + WebSite. Full quality gate (19 validators) passed.  
**Logged by:** agent

---

## [2026-07-18] — Governed Glossary Published as Tier 1 Citation Core

**Type:** content  
**Status:** decided  
**Decision:** Published `/glossary/` as the Tier 1 citation core defined in `CATEGORY_REFERENCE_ENGINE.md`: eleven canonical, claim-classified category definitions at stable anchors, with `DefinedTermSet` JSON-LD structured data. Extended the governed build pipeline with stable section anchors and a data-driven structured-data mechanism.  
**Reasoning:** The Category Reference Engine identifies canonical definitions as the surface that humans and AI answer engines cite. `data/asset-glossary.json` already held governed definitions but exposed none publicly. A curated public glossary — category and asset terms only — turns that data into the citation surface. Editorial decision: the three internal interface-design terms (Sovereign Spatial Interface, Control Plane, Search Experience Observatory) are internal doctrine describing the site's own UI direction, not category vocabulary, and are intentionally excluded from the public glossary. JSON-LD was approved as descriptive metadata, not executable script: it contains no code, loads no external resources, and is emitted only from governed content sources by the build.  
**Impact:** (1) `content/pages/glossary.json` created with definitions verbatim-synchronized to `data/asset-glossary.json` (declared source of record; sync rule recorded in editorial notes and publication rule). (2) `/glossary/` registered and published in `data/routes.json` (role `reference_glossary`); mapped in `page-source-map.json`; added to secondary and footer navigation; candidate route 9 in the publication plan. (3) `scripts/build.py`: `render_page_body` now emits a stable `id` anchor per section on all pages and supports per-section display headings; new `render_structured_data` serializes an optional `structured_data` object from content sources into a JSON-LD block via a new `{{ structured_data }}` slot in `templates/base.html`. (4) Site rebuilt: 9 routes; full quality gate and strict deploy-asset validation passed; JSON-LD verified parseable with 11 anchored DefinedTerm entries.  
**Logged by:** agent

---

## [2026-07-18] — Category Definition Expansion: /seo-vs-sxo/ and /ai-search-experience/ Published

**Type:** content  
**Status:** decided  
**Decision:** Executed Phase B (category definition completion) of `ASSET_VALUE_MAXIMIZATION_PLAN.md`: authored, claim-reviewed, and published the two deferred reference routes `/seo-vs-sxo/` and `/ai-search-experience/`, raising the published route count from six to eight.  
**Reasoning:** The asset claims to be the canonical SXO reference; the category definition was incomplete without the SEO–SXO comparison (the highest-intent informational query in the category) and the AI search positioning (the emerging entry surface named in the Category Reference Engine's audience matrix). Both content sources existed as draft contracts. The interpretive-claim review required by the original `/ai-search-experience/` deferral was performed: every claim about AI search dynamics is explicitly framed as interpretation, no performance promises appear, and ranking-outcome language is avoided in favor of govern/structure framing per the editorial contract. The `/seo-vs-sxo/` comparison was reviewed against its blocked-claim list: SEO is treated as a complete, respected discipline; no replacement or disparagement framing appears.  
**Impact:** (1) Both content sources authored to reference-grade depth and set to `approved_for_build`. (2) Both routes set to `published` in `data/routes.json`. (3) `/seo-vs-sxo/` restored to `/what-is-sxo/` required internal links (routes.json + content source), resolving the previously dangling pointer section. (4) `data/public-alpha-plan.json` updated: both routes promoted from `deferred_routes` to `candidate_routes` (publication orders 7–8) with review notes; plan renamed "Public Alpha — Category Definition Expansion"; `/acquisition/` remains the only deferred route. (5) `DEFERRED_ROUTES` lists updated in five validators (control, spatial, immersive, adjudication, deploy-assets) to reflect the new publication state. (6) Site rebuilt: 8 routes generated; full quality gate and strict deploy-asset validation passed. Secondary and footer navigation now automatically include both routes via the published-route filter.  
**Logged by:** agent

---

## [2026-07-18] — Category Reference Engine Adopted

**Type:** other  
**Status:** decided  
**Decision:** Adopted `CATEGORY_REFERENCE_ENGINE.md` as the governing mechanism for combining recurring income with category-reference authority, extending `ASSET_VALUE_MAXIMIZATION_PLAN.md`.  
**Reasoning:** The owner requires the asset to generate continuous income while simultaneously becoming the citable reference for multiple audience layers — executives, practitioners, designers, agencies, learners/press, and AI answer engines — so that SuperSXO.com becomes the address of the SXO category. A single engine (instrument → data → citations → authority → recurring income → reinvestment) achieves both goals without violating the monetization boundary, whereas separate income and authority plans would compete for the same surfaces.  
**Impact:** Introduces the governing Audience Layer Matrix (routes must serve declared audience layers), a four-tier citable content architecture (canonical definitions, named framework, original benchmark evidence, playbooks) with machine-audience requirements, a seven-rung recurring income ladder ordered inside `MONETIZATION_BOUNDARY.md`, data-ethics and claim-discipline guardrails for any benchmark data collection, and sequencing that threads the engine through master plan phases A–F. No routes, scripts, content, or monetization surfaces change with this entry; each rung, tier, and data-collection mechanism requires its own governed implementation and log entry.  
**Logged by:** agent

---

## [2026-07-18] — Asset Value Maximization Plan Adopted

**Type:** other  
**Status:** decided  
**Decision:** Adopted `ASSET_VALUE_MAXIMIZATION_PLAN.md` as the governing execution plan for maximizing the strategic and financial value of the SuperSXO asset system.  
**Reasoning:** The asset has a complete governance foundation, a live six-route alpha, and a governed build pipeline, but none of the value drivers a strategic buyer verifies: measured traffic, external citations, an interactive product surface, an owned audience, or revenue. A phased plan was required to build those drivers in order (measurement → category completion → product → authority → monetization → acquisition readiness) without violating the asset thesis, claim policy, or monetization boundary.  
**Impact:** Introduces six execution phases (A–F) over a twelve-month horizon, a five-layer value model, a KPI table with baseline logging requirements, and standing rules binding all phases to the existing governance corpus. No routes, scripts, content, or monetization surfaces change with this entry; each future phase action requires its own governed implementation and log entry.  
**Logged by:** agent

---

## [2026-05-21] — Light Institutional Adjudication Interface Integrated

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 13: Judicial Interface Source Integration. Converted the light institutional adjudication redesign from a prototype/output-level implementation into a governed source-level implementation.  
**Reasoning:** The previous interface direction (immersive dark SXO diagnostic environment) was technically correct but conflicted with the institutional authority positioning of the asset. A light institutional adjudication system better reflects the governed, precise, authoritative character of a canonical authority layer. The dark mode is preserved as an opt-in session toggle, not removed.  
**Impact:** (1) `templates/home.html` created as homepage layout template. (2) Four homepage source components created: opening-chamber.html, examination-record.html, assessment-entry.html, doctrine-statement.html. (3) `scripts/build.py` updated with `render_homepage()` — `output/index.html` is now generated from source, not manually authored. (4) `static/css/tokens.css` updated with light institutional default in `:root`, dark mode in `[data-theme="dark"]`, system preference fallback via `@media (prefers-color-scheme: dark)`. (5) `static/css/main.css` rebuilt as light institutional stylesheet with full adjudication class set. (6) `static/js/theme-toggle.js` created as first-party approved script under Option A (session-only, no localStorage, no cookies, no network calls). (7) `data/approved-scripts.json` updated to include theme-toggle.js. (8) `templates/base.html` updated: `data-theme="light"` on `<html>`, both JS files loaded with `defer`. (9) `scripts/validate_adjudication_interface.py` created as 18th validator. (10) Quality gate extended to 18 validators. (11) Six content source files updated with adjudication-aligned section names. No new routes. No external dependencies. No tracking. Deferred routes remain unpublished. Core content readable without JavaScript.  
**Logged by:** agent

---

## [2026-05-21] — Immersive SXO Diagnostic Environment Added

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 12 immersive SXO diagnostic environment rebuild.  
**Reasoning:** After Sprint 11, the interface was technically clean but visually ordinary — still functioning as a dark website with content panels rather than a VR-inspired sovereign UX/UI reference interface. The owner requirement is that the visitor must feel as if they are inside a governed Search Experience Control System, not reading about one.  
**Impact:** All six published alpha routes now render within an immersive SXO Diagnostic Environment featuring a seven-station diagnostic panel, a station rail with IntersectionObserver-driven active state, and a rebuilt immersive CSS layout. First-party JavaScript (interface-state.js) is now approved as a governed progressive enhancement. Governed by data/approved-scripts.json. Two new validators added: validate_approved_scripts and validate_immersive_experience. Quality gate extended to 17 validators. CSS tokens extended with 15 Sprint 12 tokens. No new routes. No external dependencies. No tracking. Core content readable without JavaScript.  
**Logged by:** agent

---

## [2026-05-21] - True Search Experience Control Interface Added

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 11 true search experience control interface rebuild.  
**Reasoning:** After Sprint 10 and 10B, the CSS class naming and conceptual language were corrected, but the visual delivery still behaved too much like a dark content site rather than a governed search-to-action control interface. The interface needed to make the seven SXO layers structurally central and correct mobile rendering behavior.  
**Impact:** All six published alpha routes now render within a rebuilt search experience control interface with a route status strip, system label, top-level journey control map, diagnostic panel rows, mobile-safe layout, and validator coverage for viewport and control-interface requirements.  
**Logged by:** agent

---

## [2026-05-20] - Conceptual Interface Realignment Added

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 10B conceptual interface realignment.  
**Reasoning:** Sprint 10 introduced orbit, deep-space, and cosmic visual language that did not serve the SuperSXO conceptual story. The asset is not about outer space; it is about governing the journey from search visibility to trust, clarity, navigation confidence, and action.  
**Impact:** All six published alpha routes render with control-system class names and tokens rather than space-themed metaphors. The visual system now frames the interface as a search-experience control system, not a cosmic or orbital interface.  
**Logged by:** agent

---

## [2026-05-20] - Sovereign VR-Spatial Interface Upgrade Added

**Type:** architecture  
**Status:** decided  
**Decision:** Executed Sprint 10 sovereign spatial interface upgrade.  
**Reasoning:** The public alpha rendered as a readable but visually conventional styled content site. The interface needed to move toward the agreed non-traditional, future-facing, immersive direction while preserving static-first architecture and accessibility.  
**Impact:** Six published alpha routes rendered with sovereign spatial interface structure and an upgraded visual system. Fourteen validators were active in the quality gate.  
**Logged by:** agent

---

## [2026-05-20] - CNAME Copied to output/ for Custom Domain Stability

**Type:** architecture  
**Status:** decided  
**Decision:** Updated `scripts/build.py` to copy the repository root `CNAME` file into `output/` during every build.  
**Reasoning:** When GitHub Pages deploys from a GitHub Actions artifact, `CNAME` must be included in the deployed artifact to preserve the custom domain configuration.  
**Impact:** `output/CNAME` is generated on every build. Strict deployment validation enforces that the custom domain remains stable during future deployments.  
**Logged by:** agent

---

## [2026-05-20] — Deploy Asset Validation Context Fixed

**Type:** architecture  
**Status:** decided  
**Decision:** Added `--strict` flag support to `scripts/validate_deploy_assets.py`. Without `--strict`: skips safely pre-build. With `--strict`: full enforcement of CSS assets, HTML references, no unapproved JS files, no external resources, no deferred route output.  
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
