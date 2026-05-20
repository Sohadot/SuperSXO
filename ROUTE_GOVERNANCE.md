# SuperSXO — Route Governance

## Governing Rule

> No public page may be created unless it is registered, purposeful, internally linked, and quality-gated.

---

## Route Registration Requirements

Every route must define:

| Field | Purpose |
|---|---|
| `path` | Defines the public URL |
| `purpose` | Explains why the page exists |
| `status` | `planned` / `drafted` / `approved` / `published` |
| `indexability` | Whether search engines may index it |
| `canonical_url` | Prevents duplicate authority |
| `page_role` | Strategic role of the page |
| `required_internal_links` | Prevents isolated or weak pages |
| `allowed_cta` | Keeps conversion paths controlled |
| `content_standard` | Expected depth and quality |
| `claim_requirements` | Controls factual and commercial claims |
| `monetization_permission` | Prevents improper monetization |

---

## Route Status Definitions

| Status | Meaning |
|---|---|
| `planned` | Approved for planning but not yet drafted |
| `drafted` | Content exists but has not passed quality gate |
| `approved` | Passed quality gate, ready for publication |
| `published` | Live on the site and indexed |
| `archived` | Removed from indexing, kept for reference |
| `blocked` | Route suspended pending review |

---

## Route Prohibitions

Routes must not be:

- published as placeholders
- linked to non-existent pages
- generated only for SEO volume
- created without a documented purpose
- published before passing quality gate
- assigned duplicate canonical URLs

---

## Approved Initial Route Structure

| Path | Purpose | Status |
|---|---|---|
| `/` | Primary homepage and asset introduction | `planned` |
| `/what-is-sxo/` | Reference definition of SXO | `planned` |
| `/sxo-framework/` | Core methodology and framework | `planned` |
| `/supersxo-score/` | Self-assessment diagnostic tool | `planned` |
| `/sxo-audit/` | Commercial diagnostic offer | `planned` |
| `/about/` | Asset context and institutional voice | `planned` |

---

## SEO Route Policy

No page may be created only because a keyword exists.

Every indexable page must have:

- a clear strategic purpose
- a defined user intent
- a unique canonical URL
- a controlled title
- a controlled meta description
- one clear H1
- logical heading structure
- sufficient content depth
- strong internal links
- no placeholder sections
- no broken links
- no duplicate content

---

## Defensive Domain Route Rules

Routes on `.info` and `.link` cluster domains must:

- route to canonical pages on `SuperSXO.com`
- not create independent content
- not fragment domain authority
- not operate as independent sites

See `DOMAIN_CLUSTER_STRATEGY.md` for full cluster rules.

---

## Route Governance Log

Changes to route status must be recorded in `DECISION_LOG.md`.

No route may move from `planned` to `published` without a quality gate passage entry.
