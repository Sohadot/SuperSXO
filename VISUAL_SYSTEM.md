# SuperSXO — Visual System

## Visual Thesis

SuperSXO.com does not present search experience optimization as a service listing.
It makes the Search-to-Action Journey visible as a diagnostic adjudication system.

The interface is a light institutional adjudication environment. The visitor enters a governed examination record, not a dark control panel. The default visual mode is light — precise, authoritative, and institutional in character.

Every visual decision is governed. Every component maps to a strategic function. Every motion has a justification.

**The interface is not space-themed. It is not dark by default.** Structure communicates hierarchy. Records represent diagnostic layers. Case sheets represent governed findings. The adjudication trail tracks position in the examination journey. CTAs represent governed intake actions.

Dark mode is available as an opt-in session toggle governed by `static/js/theme-toggle.js` under Option A. It does not alter the asset's default presentation.

---

## Approved Interface Identity

**Name:** Light Institutional Adjudication System  
**Category:** Sovereign Search Experience Optimization Authority Layer  
**Tone:** Authoritative, precise, diagnostic, institutional  
**Reference Points:** Institutional record systems, governed authority interfaces, structured evidence documents, systematic diagnostic tools

The interface should feel like entering a **Search Experience Adjudication System** — a light, governed examination environment where the full search-to-action journey is visible, measurable, and documented as a case under examination.

### Sprint 13 Direction (Current)

| Component | Adjudication Term | Route | Function |
|---|---|---|---|
| `opening-chamber.html` | Opening Chamber | `/` | Case intake — thesis, CTAs, journey trail |
| `examination-record.html` | Examination Record | `/` | Seven layers under examination — case sheets |
| `assessment-entry.html` | Assessment Entry | `/` | Diagnostic entry — Score and Audit CTAs |
| `doctrine-statement.html` | Doctrine Statement | `/` | Canonical authority declaration |

### Approved Visual Concepts

| Concept | Function |
|---|---|
| Opening Chamber | Case intake hero section — establishes jurisdiction and doctrine |
| Examination Record | Seven-layer diagnostic case sheets with status badges |
| Assessment Entry | Diagnostic instrument entry — Score and Audit CTAs with sidebar records |
| Doctrine Statement | Canonical authority declaration — governed asset thesis |
| Chamber Header | Institutional header with navigation and theme toggle |
| Chamber Footer | Outcome register footer |
| Case Sheet | Individual layer examination record with status badge |
| SXO Diagnostic Environment | Inner pages: seven-station diagnostic panel (progressive enhancement) |
| Station Rail | Left-side positional indicator (inner pages — IntersectionObserver enhanced) |
| Route Telemetry Panel | In-page governance panel showing route role, layer, and claim type |

---

## Forbidden Interface Patterns

The following patterns are explicitly prohibited. Their presence in any design or implementation constitutes a governance violation.

| Pattern | Reason |
|---|---|
| Gaming HUD | Reduces institutional credibility |
| Neon cyberpunk excess | Decorative without strategic function |
| Metaverse avatar scenes | Misrepresents the asset thesis |
| Canvas-only content | Breaks accessibility, indexability, and static-first architecture |
| Animation-required navigation | Inaccessible; breaks core content delivery |
| Intrusive popups | Violates trust layer |
| Hidden text for SEO | Black-hat pattern; security violation |
| Decorative 3D without function | Performance drag without strategic return |
| Cosmic interface | Space, orbit, or astronomical imagery |
| Outer space metaphor | Dark background with star-field, nebula, or orbital visual language |
| Decorative sci-fi grid | Grid lines used as decoration |
| Conventional dark website | Standard dark content cards without diagnostic function |
| Black-first default | Near-black body background as the default mode (light is the sovereign default) |

---

## Color Philosophy

The color system is token-governed. No color may appear without a corresponding design token.

### Light Institutional Default (`:root`)

The default visual mode is light institutional. These are the sovereign defaults applied on every page load.

- `--surface-console` (#f8f7f5): Primary surface. Institutional warm off-white. The governing background layer.
- `--surface-instrument` (#f2f1ef): Instrument area, diagnostic panels.
- `--surface-readout` (#ededeb): Readout surfaces, examination records.
- `--surface-control-base` (#f5f4f2): Base control surface.
- `--surface-control-panel` (#ffffff): Elevated panel surfaces, card surfaces.

**Ink system:**
- `--ink-primary` (#1a1f2e): Primary text. Deep institutional navy.
- `--ink-secondary` (#3d4456): Secondary text, labels.
- `--ink-muted` (#6b7280): Muted text, metadata.

**Signal accent (Blue `#2955b8` / `--signal-primary`):** Navigation, primary actions, active states, primary CTAs.

**Trust accent (`--trust-confirmed`):** Established authority signals, confirmed status badges.

**Action accent (`--action-ready`):** Action-ready status badges, commercial CTAs.

**Outcome accent (`--outcome-registered`):** Outcome register station, strategic consequence signals.

### Opt-In Dark Mode (`[data-theme="dark"]`)

Dark mode is available as a session-only opt-in. The visitor toggles it via the theme toggle button (`[data-theme-toggle]`). No preference is stored. On next visit, the interface returns to light institutional.

In dark mode, all tokens revert to the immersive diagnostic environment palette:
- `--surface-console` (#020304): Deepest layer. Command header, station rail background.
- `--surface-instrument` (#080b0f): Content instrument area, diagnostic panels.
- `--surface-readout` (#0b0e14): Station panels, readout surfaces.

Governed by `static/js/theme-toggle.js` under Option A (no localStorage, no sessionStorage, no cookies, no network calls).

### System Preference Fallback

`@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { ... } }` — if the visitor has not explicitly chosen a mode and their OS is set to dark, the dark palette applies. The explicit `data-theme="light"` attribute on `<html>` (set in `templates/base.html`) takes precedence over system preference on first load.

---

## Spatial Depth Philosophy

Depth is a structural tool. It maps the information hierarchy of the examination record.

- `--surface-console`: Governing background layer.
- `--surface-instrument`: Content instrument area.
- `--surface-readout`: Active readout surfaces, case sheet panels.
- `--surface-control-panel`: Elevated panel surfaces.

---

## Typography Philosophy

- **Display headings:** Georgia serif (`--font-display: Georgia, 'Times New Roman', serif`). Institutional authority register.
- **Body/UI font stack:** System UI only. No external font loading.
- **Monospace:** `SF Mono`, `Fira Code` for diagnostic labels, case indices, status codes, and docket identifiers.
- **Weight system:** 400 body, 500 nav, 600 headings, 700 identity/labels.
- **Scale:** Token-governed from `--text-xs` to `--text-4xl`.

---

## Motion Philosophy

Motion must justify itself.

**Permitted motion:**
- Station active state transitions (IntersectionObserver) — `--duration-slow` (400ms), progressive enhancement only
- State transitions (hover, focus, active) — `--duration-fast` (150ms)
- Panel transitions — `--duration-base` (250ms)

**Prohibited motion:**
- Looping animations without user trigger
- Motion that carries essential meaning not available statically
- Heavy entrance animations that delay content reading
- Any motion not suppressible via `prefers-reduced-motion`

**Governed JS motion:** `static/js/interface-state.js` uses IntersectionObserver to add/remove `is-active` class on station rail items and station panels as the visitor scrolls. This is the only approved JavaScript motion enhancement on inner pages.

---

## Accessibility Requirements

- WCAG 2.1 AA color contrast on all text
- Visible focus indicator on all interactive elements
- Skip navigation link present on all pages
- Keyboard-reachable in logical tab order
- Station rail is `aria-hidden="true"` (decorative; content is in station panels)
- All station panel content fully readable without JavaScript
- Spatial effects are progressive enhancements only
- All motion suppressed under `@media (prefers-reduced-motion: reduce)`
- Theme toggle button labeled with `aria-label`

---

## Relationship to the Search-to-Action Journey

| Layer | Journey Step | UX Expression |
|---|---|---|
| 01 | Search Intent | Case intake — intent alignment |
| 02 | Visibility | Entry condition examination |
| 03 | Experience | Post-arrival quality |
| 04 | Trust | Authority and credibility |
| 05 | Navigation | Path confidence |
| 06 | Action | Governed action surface |
| 07 | Strategic Outcome | Outcome register |

---

## Machine Governance

- `data/component-registry.json` — registered components with UX layer mappings
- `data/interface-patterns.json` — approved and prohibited patterns
- `data/visual-tokens.json` — token registry aligned with tokens.css
- `data/approved-scripts.json` — approved first-party JavaScript registry
- `scripts/validate_visual_system.py` — automated visual governance
- `scripts/validate_approved_scripts.py` — JS governance
- `scripts/validate_immersive_experience.py` — diagnostic environment enforcement (inner pages)
- `scripts/validate_adjudication_interface.py` — adjudication interface enforcement (source components, tokens, light-first default)
- `INTERFACE_GOVERNANCE.md` — component creation protocol
