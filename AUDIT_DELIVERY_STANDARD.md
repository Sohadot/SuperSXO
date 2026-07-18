# SuperSXO — Audit Delivery Standard

## Purpose

This document governs how an SXO Audit is conducted, written, and delivered. It exists so that the first paid audit — and every audit after it — is produced to a defensible, reproducible standard that strengthens the asset's authority rather than merely consuming operator time.

The audit is the asset's first revenue rung (Rung 2 of `CATEGORY_REFERENCE_ENGINE.md`). Its delivery quality is therefore an asset-value event, not just a service transaction: every delivered report is evidence of the methodology working on a real property.

---

## Governing Sources

| Source | Role |
|---|---|
| `data/governing-conditions.json` | The fourteen conditions assessed — single source of record |
| `/sxo-framework/` (published) | The seven-layer model and each layer's failure modes |
| `/methodology/` (published) | The governance system the audit operates under |
| `/sxo-audit/` (published) | The public offer: scope, exclusions, intake |
| `docs/audit/audit-report-template.md` | The report skeleton every deliverable follows |
| `CLAIM_POLICY.md` | Claim discipline inside findings |

The published `/sxo-audit/` page is the contract of scope: the audit covers exactly what that page says it covers, and excludes exactly what it says it excludes. If delivery practice needs to diverge, the page changes first (through governance), then the practice.

---

## Process Stages

1. **Intake.** A request arrives at `pro@supersxo.com` with the asset URL and strategic purpose. Before acceptance, verify: the asset is reachable, the requester operates it or is authorized, and the strategic purpose is stated clearly enough to assess Layer 7 against it. Decline respectfully when these cannot be established.
2. **Scope confirmation.** Confirm in writing: the asset under review, the fourteen conditions to be assessed, the deliverable format, the delivery window, and the price. No work begins before written confirmation.
3. **Assessment.** Work layer by layer in framework order. For each condition in `data/governing-conditions.json`, follow its `audit_evidence_guidance`, record the observed state (present / partially present / absent), and capture the evidence that supports the determination.
4. **Findings drafting.** Write findings into the report template. Every finding carries its evidence. Prioritization follows journey continuity: a breakdown at an early layer outranks one at a later layer, because it blocks everything downstream.
5. **Claim review.** Before delivery, review the full report against `CLAIM_POLICY.md`: no outcome promises, no unsupported causal claims, no competitor disparagement, interpretations labeled as interpretations.
6. **Delivery.** The report is delivered as a document to the requester. Delivery includes a short cover note restating what the report is (findings) and is not (a performance contract).
7. **Record.** Each delivered audit is logged in `DECISION_LOG.md`: date, asset category (not the client's identity unless they consent), and any methodology friction discovered during delivery. Methodology friction feeds back into the registry through governance.

---

## Findings Discipline

- A finding states: the condition, the observed state, the evidence, the risk to journey continuity, and the recommended direction of correction. It does not state predicted outcomes of correcting it.
- Absent evidence means an absent finding. "Likely," "probably," and "in our experience" are not evidence; where judgment is unavoidable it is labeled as interpretation.
- The report never scores the operator. It scores the observable state of conditions on the asset.
- The non-guarantee boundary from the public offer is restated inside every report, verbatim in spirit: no ranking, traffic, conversion, or revenue outcome is promised.

## Pricing Governance

Prices are not published in this repository or on the public site at this stage. Each engagement's price is stated in the scope confirmation. Any decision to publish pricing is a monetization-boundary decision requiring a `DECISION_LOG.md` entry first.

## Delivery Boundary

The audit delivers findings. Implementation, retained consulting, monitoring subscriptions (Rung 3), and re-assessment engagements are separate offers governed by `MONETIZATION_BOUNDARY.md` — they may be mentioned in the cover note as available pathways, never inserted as pressure inside the findings.
