# SuperSXO — Interface Governance

## Governing Statement

No component, pattern, or visual rule may enter the interface without satisfying these governance rules. Interface components are governed assets, not design preferences.

---

## Component Governance Rules

### 1. No Decorative Component Without Strategic Function

Every component in the interface must:
- Map to a defined UX layer from `data/ux-layers.json`
- Serve a specific content delivery, navigation, or diagnostic function
- Be registered in `data/component-registry.json`

A component that exists purely for visual decoration is a governance violation.

### 2. Every Component Must Map to a UX Layer or Route Function

Components must declare their `ux_layer` alignment in the component registry. Permitted values are drawn from `data/ux-layers.json`. Components that cannot be assigned a UX layer are prohibited from production.

### 3. Every CTA Must Come From Route Governance

Calls-to-action must only appear if:
- The route's `allowed_cta` array in `data/routes.json` explicitly permits them
- The route's `monetization_allowed` field is `true` if the CTA is commercial
- The CTA text matches an approved definition in `data/navigation.json`

No CTA may be created ad hoc. No commercial CTA may appear on a non-monetization-approved route.

### 4. Navigation Must Come From `data/navigation.json`

All navigation links — primary, secondary, footer, and CTA — must be generated from `data/navigation.json`. No hardcoded navigation links are permitted in templates or components.

### 5. Page Context Must Come From Route and Content Governance

Every public page must read its:
- Route role, UX layer, and claim level from `data/routes.json`
- Content sections from the corresponding `content/pages/*.json` contract
- Allowed CTAs from the route definition

No page may invent context not registered in the governance files.

### 6. Motion Must Not Carry Essential Meaning

No information, navigation state, or user instruction may be conveyed exclusively through motion. If an animation is removed, the content must remain fully comprehensible.

Motion is a progressive enhancement layer, not an information layer.

### 7. No Component May Require JavaScript to Make Core Content Readable

The HTML document must be fully readable, navigable, and comprehensible without JavaScript execution. JavaScript may enhance interaction but may not gate content access.

This applies to all route types including commercial and diagnostic routes.

### 8. No Visual Pattern May Reduce Accessibility, Performance, or SEO Clarity

Any visual pattern that:
- Reduces color contrast below WCAG 2.1 AA
- Hides content from search engines
- Slows Largest Contentful Paint beyond acceptable thresholds
- Removes keyboard focus visibility
- Breaks semantic HTML structure

...is a governance violation regardless of aesthetic intent.

---

## Component Creation Protocol

To create a new component:

1. **Register** it in `data/component-registry.json` with all eight required fields
2. **Assign** a UX layer from `data/ux-layers.json`
3. **Declare** allowed routes — specific paths or `"*"` for all routes
4. **Define** required data sources — no hardcoded content
5. **Document** accessibility requirements
6. **Define** prohibited behavior
7. **Assess** publication risk (low / medium / high)
8. **Validate** via `scripts/validate_visual_system.py`

No component may be published without completing all steps.

---

## Pattern Governance

All interface patterns must be registered in `data/interface-patterns.json`.

- Patterns with `"status": "approved"` may be used in registered components
- Patterns with `"status": "prohibited"` may not be used in any component or template
- Patterns not registered are prohibited by default

Any proposal to add a new approved pattern must be logged in `DECISION_LOG.md` before implementation.

---

## Visual Token Governance

All visual decisions must reference tokens from `data/visual-tokens.json` and their CSS implementations in `static/css/tokens.css`.

No inline color, spacing, or motion value may appear in production HTML or CSS without a corresponding token. Exceptions require a `DECISION_LOG.md` entry.

---

## Prohibited Interface Elements (Zero Tolerance)

The following may never appear regardless of context:

- Monetization scripts (AdSense, affiliate networks, display advertising)
- Analytics tracking pixels without explicit operator authorization
- Third-party fonts loaded from external URLs
- WebGL or Three.js scenes as the primary content medium
- Canvas-only rendering that replaces HTML content
- Hidden text intended to manipulate search engine indexing
- Pop-up overlays that block content access
- Auto-playing media with sound
- Fake urgency signals (countdown timers, false scarcity claims)

---

## Governance Validation

Run `scripts/validate_visual_system.py` to verify:

- All required components are registered with required fields
- All allowed_routes reference registered paths or `"*"`
- No prohibited pattern is marked approved
- All required token groups are defined
- CSS token files exist at expected paths

This validator runs automatically via the quality gate on every push.
