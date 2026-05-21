# SuperSXO — UX/UI Standard

## Governing Principle

> **SuperSXO does not merely explain search experience.**
> **The visitor enters a governed adjudication system for the search-to-action journey.**

---

## Sprint 13: Light Institutional Adjudication System

The approved interface direction as of Sprint 13 is the **Light Institutional Adjudication System**.

This is the current governing direction. Dark mode is preserved as a governed opt-in session toggle — not removed.

**Default visual mode:** Light institutional. `data-theme="light"` on `<html>`. No storage. On every new session, the interface opens in light institutional mode.

**Opt-in dark mode:** The visitor may toggle dark mode for their session using the theme toggle button (`[data-theme-toggle]`). Governed by `static/js/theme-toggle.js` under Option A.

### Homepage Adjudication Components

The homepage is rendered from four source components:

| Component | Adjudication Term | Function |
|---|---|---|
| `opening-chamber.html` | Opening Chamber | Case intake hero — H1, thesis, CTAs, journey trail |
| `examination-record.html` | Examination Record | Seven layers under examination — case sheets with status badges |
| `assessment-entry.html` | Assessment Entry | Diagnostic entry — Score and Audit CTAs with sidebar records |
| `doctrine-statement.html` | Doctrine Statement | Canonical authority declaration |

`templates/home.html` is the layout template. `scripts/build.py` renders the homepage via `render_homepage()`. `output/index.html` is generated from source, not manually authored.

### Adjudication Status System

Case sheets in the examination record carry status badges:

| Status Class | Label | Meaning |
|---|---|---|
| `status--review` | Under Examination | Layer under active diagnostic review |
| `status--confirmed` | Confirmed | Layer condition confirmed |
| `status--verdict` | Ready | Layer condition assessed, action ready |
| `status--registered` | Registered | Layer outcome registered |

### Theme Toggle Governance (Option A)

`static/js/theme-toggle.js` is a first-party approved script under Option A:

- **Allowed APIs:** querySelector, getAttribute, setAttribute, addEventListener
- **Forbidden:** localStorage, sessionStorage, cookies, fetch, XMLHttpRequest, eval, innerHTML, document.write, import, external script loading
- **Default:** `data-theme="light"` (set in `templates/base.html`, not by JavaScript)
- **Toggle:** sets `data-theme="dark"` or `data-theme="light"` on `document.documentElement`
- **Persistence:** none — session-only

### Inner Page Direction (Sprint 12 — Preserved)

Inner pages (all routes except `/`) continue to render the SXO Diagnostic Environment — the seven-station diagnostic panel with IntersectionObserver station active state. Adjudication language applies to the header, footer, and route label elements on inner pages.

---

## Sprint 12: Immersive SXO Diagnostic Environment

The Sprint 12 direction (immersive dark SXO diagnostic environment) is preserved as the opt-in dark mode and as the governing standard for inner pages.

The visitor does not read about SXO. They navigate through it.

The diagnostic environment surfaces seven stations on every inner page:

| Station | Label | Status |
|---|---|---|
| 01 | Intent Channel | Receiving |
| 02 | Visibility Gate | Monitoring |
| 03 | Experience Layer | Active |
| 04 | Trust Layer | Confirmed |
| 05 | Navigation Path | Mapped |
| 06 | Action Route | Ready |
| 07 | Outcome Register | Registered |

Each station shows a diagnostic question, a system meaning, and a status label.

The station rail on the left tracks which station the visitor is currently reading. This state is managed by `static/js/interface-state.js` using IntersectionObserver as a governed progressive enhancement. Without JavaScript, all seven stations are fully readable.

---

## Approved Interface Direction

SuperSXO.com must not look like:

- a generic SEO blog
- a SaaS template
- a digital agency site
- an affiliate website
- an ordinary marketing landing page
- a space-themed or cosmic interface
- a gaming or metaverse environment
- a dark website with standard content panels

The approved direction is a **Light Institutional Adjudication System** with an immersive diagnostic environment on inner pages.

---

## Interface Metaphor: Adjudication, Not Space

The correct conceptual frame is:

- **Opening Chamber** — not landing page
- **Examination Record** — not feature list
- **Case Sheet** — not content card
- **Doctrine Statement** — not about section
- **Intake** — not sign up
- **Docket** — not project ID
- **Jurisdiction** — not category

Depth is used to express hierarchy — the layered architecture of the search-to-action journey. It is not used to suggest outer space, cosmic distance, or astronomical scale.

---

## Approved Interface Language

The interface may use:

- layered panels (diagnostic layers)
- signal paths (directional connectors)
- station rails (diagnostic position indicators)
- station panels (full diagnostic readouts per layer)
- controlled depth (information hierarchy)
- controlled motion via IntersectionObserver (progressive enhancement only)
- diagnostic grids (structured assessment)
- search-to-action control maps (journey visualization)
- trust and clarity layers (authority signals)
- institutional precision design language
- Georgia serif for display headings (institutional authority register)

---

## Prohibited Interface Direction

The interface must not become:

- gaming-like
- childish
- metaverse gimmick
- cyberpunk decoration
- heavy 3D spectacle
- animation-first
- canvas-only
- inaccessible
- slow
- confusing
- space-themed or cosmic
- orbital or astronomical in metaphor
- decorative dark without diagnostic function
- a conventional dark website with content cards
- black-first default (light is the sovereign default)

---

## Technical Constraints for UX/UI

Interface enhancements must be **progressive enhancements**, not the core content delivery mechanism.

The interface must remain:

- accessible
- readable without JavaScript
- navigable without JavaScript
- fast on mobile
- compliant with accessibility basics
- free of animation that cannot be disabled

**Approved JS:**
- `static/js/interface-state.js` — IntersectionObserver only. No network requests, no storage, no tracking.
- `static/js/theme-toggle.js` — Session-only `data-theme` toggle. Option A. No network requests, no storage, no tracking.

---

## Typography and Visual Hierarchy

- Display headings use Georgia serif (`--font-display`) — institutional authority register
- Body and UI use system UI font stack — no external font loading
- Typography must reinforce institutional authority, not playfulness
- Color palette must be disciplined — not decorative
- Motion must be purposeful — every animation must have a functional justification
- Monospace type is permitted for diagnostic labels, station indices, and status codes

---

## UX Decision Protocol

Any interface direction change must:

1. Be evaluated against the Light Institutional Adjudication System standard
2. Pass the prohibited list check (including the cosmic/space metaphor prohibition and black-first prohibition)
3. Confirm progressive enhancement compliance
4. Confirm the change serves the search-to-action journey narrative
5. Be logged in `DECISION_LOG.md` before implementation

---

## Visual System Governance (Sprint 4 → Sprint 13)

The approved visual direction is machine-governed. All interface decisions must reference:

- `VISUAL_SYSTEM.md` — visual thesis, color philosophy, spatial depth, typography, motion, and accessibility rules
- `INTERFACE_GOVERNANCE.md` — component creation protocol and prohibited interface elements
- `data/component-registry.json` — registry of all approved interface components with UX layer mappings
- `data/interface-patterns.json` — approved and prohibited interface patterns
- `data/visual-tokens.json` — token registry aligned with `static/css/tokens.css`
- `data/approved-scripts.json` — registry of approved first-party JavaScript files

The validators `scripts/validate_visual_system.py`, `scripts/validate_approved_scripts.py`, `scripts/validate_immersive_experience.py`, and `scripts/validate_adjudication_interface.py` enforce these rules on every push via the quality gate.
