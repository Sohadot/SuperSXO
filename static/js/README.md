# static/js/

## Governance Rule

No JavaScript is added to this directory yet.

## Future Requirements

When JavaScript is introduced, every script must:

- Be a **progressive enhancement only** — the page must be fully functional without it
- Not be required for core content delivery
- Not introduce tracking, analytics, or third-party embeds without explicit approval
- Not use `eval()` or unsafe execution patterns
- Not be added inline without a Content-Security-Policy update
- Not use WebGL, Three.js, canvas-only interfaces, or heavy animation libraries
- Be logged in `DECISION_LOG.md` before deployment

## Spatial Effects

Future spatial interface effects must:

- Be CSS-first where possible
- Be JavaScript-enhanced only where CSS cannot achieve the effect
- Not break the interface when disabled or absent
- Respect `prefers-reduced-motion` at the CSS level
