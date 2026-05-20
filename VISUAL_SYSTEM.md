# SuperSXO — Visual System

## Visual Thesis

SuperSXO.com does not present search experience optimization as a service listing.
It makes the Search-to-Action Journey visible as a spatial control system.

The visual language must communicate institutional authority, diagnostic precision, and strategic depth — not marketing energy, not gaming aesthetics, not decorative futurism.

Every visual decision is governed. Every component maps to a strategic function. Every motion has a justification.

---

## Approved Interface Identity

**Name:** Sovereign Spatial Interface  
**Category:** Institutional Diagnostic Control Plane  
**Tone:** Authoritative, spatial, precise, future-facing  
**Reference Points:** Observatory control interfaces, institutional dashboards, spatial data visualization systems

The interface should feel like entering a **Search Experience Observatory** — a governed diagnostic environment where the full search-to-action journey is visible, measurable, and navigable.

### Approved Visual Concepts

| Concept | Function |
|---|---|
| Search Experience Control Plane | Primary shell layer surrounding navigable content |
| Search-to-Action Map | Spatial representation of the 7-layer journey model |
| Signal Path | Directional visual connector linking journey layers |
| Trust Plane | Surface area communicating established authority and evidence |
| Diagnostic Grid | Structured assessment layout for SXO measurement surfaces |
| Route Context Panel | In-page governance panel showing route role, layer, and claim type |
| Sovereign Spatial Interface | The governing interface identity and UX direction |
| Search Experience Observatory | Mental model for the overall site experience |

---

## Forbidden Interface Patterns

The following patterns are explicitly prohibited. Their presence in any design or implementation constitutes a governance violation.

| Pattern | Reason |
|---|---|
| Gaming HUD | Reduces institutional credibility; associated with entertainment contexts |
| Neon cyberpunk excess | Decorative without strategic function; reduces trust signal |
| Metaverse avatar scenes | Gimmick-tier; misrepresents the asset thesis |
| Canvas-only content | Breaks accessibility, indexability, and static-first architecture |
| Animation-required navigation | Inaccessible; breaks core content delivery |
| Intrusive popups | Violates trust plane; damages acquisition positioning |
| Cheap sales banners | Low-trust language; prohibited under MONETIZATION_BOUNDARY |
| Hidden text for SEO | Black-hat pattern; security violation under SECURITY_POLICY |
| Decorative 3D without function | Performance drag without strategic return |
| Heavy animation first | Motion must be progressive enhancement, not primary content delivery |

---

## Color Philosophy

The color system is token-governed. No color may appear in the interface without a corresponding design token in `static/css/tokens.css` and a registered group in `data/visual-tokens.json`.

**Surface layer:** Near-black surfaces at five depth levels (base, raised, panel, overlay, highlight). Depth communicates hierarchy without decoration.

**Ink layer:** Three ink levels (primary, secondary, muted) for text hierarchy. Typography must be readable without color dependency.

**Signal (Blue `#4a7cdc`):** Used exclusively for navigation, primary actions, and spatial connectors. Not decorative.

**Trust (Cyan-Green `#38a882`):** Used exclusively for established authority signals, evidence indicators, and verified claim markers.

**Action (Amber `#dfa030`):** Used exclusively for commercial CTAs and monetization surfaces. Governed by route monetization rules.

No colors outside the token system. Color improvisation is a governance violation.

---

## Spatial Depth Philosophy

Depth is a strategic tool, not a decoration.

- **Base surface (`--surface-base`):** Content background. The floor.
- **Raised surface (`--surface-raised`):** Header, footer, navigation. Elevated but neutral.
- **Panel surface (`--surface-panel`):** Content panels and components. Mid-depth.
- **Overlay surface (`--surface-overlay`):** Hover states, contextual overlays.
- **Highlight surface (`--surface-highlight`):** Focused or selected states.

Depth must communicate information architecture, not create visual drama.

Shadows and borders define spatial layers. Glow effects are permitted only on signal-carrying elements and only as progressive enhancement.

---

## Typography Philosophy

Typography communicates authority. It must not compete with content.

- **Font stack:** System UI only. No external font loading. No Google Fonts.
- **Weight system:** 400 for body text, 500 for navigation, 600 for headings, 700 for identity and labels.
- **Scale:** Token-governed from `--text-xs` to `--text-4xl`. No ad-hoc sizes.
- **Line height:** Token-governed. `--leading-tight` for headings, `--leading-normal` for body.
- **Letter spacing:** Minimal. Reserved for labels and navigation items only (`0.05em`–`0.08em`).
- **Color:** Ink tokens only. Never raw color values in typography rules.

---

## Motion Philosophy

Motion must justify itself. Every transition must answer: *what strategic function does this serve?*

**Permitted motion:**
- State transitions (hover, focus, active) — `--duration-fast` (150ms)
- Panel open/close transitions — `--duration-base` (250ms)
- Controlled reveal on scroll — `--duration-slow` (400ms), progressive enhancement only
- Navigation state changes — `--duration-fast` (150ms)

**Prohibited motion:**
- Looping animations without user trigger
- Motion that carries essential meaning not available statically
- Heavy entrance animations that delay content reading
- Any motion that cannot be disabled via `prefers-reduced-motion`

All motion is defined using duration tokens only. No ad-hoc durations. All motion must be suppressed under `@media (prefers-reduced-motion: reduce)`.

---

## Accessibility Requirements

The interface must be fully operable without JavaScript, without CSS, and without motion.

Minimum requirements:
- WCAG 2.1 AA color contrast on all text elements
- Visible focus indicator on all interactive elements (`:focus-visible`)
- Skip navigation link present on all pages
- All interactive elements keyboard-reachable in logical tab order
- No content conveyed by color alone
- All images have meaningful `alt` attributes or `alt=""` if decorative
- Spatial effects are progressive enhancements — content is readable without them
- Focus ring governed by `--focus-ring-color`, `--focus-ring-width`, `--focus-ring-offset` tokens

---

## Performance Constraints

- No external CSS files loaded
- No external fonts loaded
- No JavaScript required for core content delivery
- No WebGL, Three.js, or canvas-only rendering
- No image-heavy decorative backgrounds
- Target: Largest Contentful Paint under 1.5s on mobile 4G
- Motion enhancements must not increase Time-to-Interactive

---

## Relationship to the Search-to-Action Journey

Every interface layer maps to a journey layer defined in `data/ux-layers.json`:

| Journey Layer | UX Layer Name | Visual Expression |
|---|---|---|
| 1 | Search Intent | Signal Path origin point |
| 2 | Visibility | Route Context Panel surface |
| 3 | Experience | Spatial Panel depth system |
| 4 | Trust | Trust Plane component |
| 5 | Navigation | Primary navigation cluster |
| 6 | Action | Action CTA blocks (amber tokens) |
| 7 | Strategic Outcome | Acquisition and outcome surfaces |

The interface does not merely style pages — it makes the journey architecture visible.

---

## Machine Governance

This visual system is enforced by:
- `data/component-registry.json` — registered components with UX layer mappings
- `data/interface-patterns.json` — approved and prohibited patterns
- `data/visual-tokens.json` — token registry aligned with tokens.css
- `scripts/validate_visual_system.py` — automated governance validation
- `INTERFACE_GOVERNANCE.md` — component creation protocol

Any visual decision not registered in these files is ungoverned and prohibited.
