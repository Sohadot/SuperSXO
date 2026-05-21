#!/usr/bin/env python3
"""
Validates that the governed experience interface is correctly implemented.

Covers both the inner-page immersive SXO diagnostic environment (Sprint 12,
preserved for all routes except '/') and the homepage light institutional
adjudication interface (Sprint 13, the current immersive experience standard).

Checks:
- templates/components/sxo-diagnostic-environment.html exists
- templates/page.html references sxo_diagnostic_environment
- main.css contains required CSS markers for both inner-page and
  adjudication-interface experience layers
- templates/base.html has viewport meta width=device-width
- No deferred routes hardcoded in published templates
- No external scripts or fonts in templates

Spring 12 markers removed from required CSS:
  signal-path — renamed/removed in Sprint 13 adjudication rebuild;
                inner pages no longer use this specific class name.

Sprint 13 markers added to required CSS:
  opening-chamber, examination-record, case-sheet
"""

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
COMPONENT = ROOT / "templates" / "components" / "sxo-diagnostic-environment.html"
PAGE_HTML = ROOT / "templates" / "page.html"
MAIN_CSS = ROOT / "static" / "css" / "main.css"
BASE_HTML = ROOT / "templates" / "base.html"
TEMPLATES_DIR = ROOT / "templates"

REQUIRED_CSS_MARKERS = [
    "diagnostic-environment",
    "station-rail",
    "active-station-readout",
    "opening-chamber",
    "examination-record",
    "case-sheet",
    "@media",
]

DEFERRED_ROUTES = ["/seo-vs-sxo/", "/ai-search-experience/", "/acquisition/"]

EXTERNAL_FRAGMENTS = [
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    'script src="http',
    "script src='http",
]


def main() -> None:
    failures: list = []

    if not COMPONENT.exists():
        failures.append(
            "FAIL  templates/components/sxo-diagnostic-environment.html not found"
        )
    else:
        print("  OK    sxo-diagnostic-environment.html component exists")

    if not PAGE_HTML.exists():
        failures.append("FAIL  templates/page.html not found")
    else:
        page_content = PAGE_HTML.read_text(encoding="utf-8")
        if "sxo_diagnostic_environment" not in page_content:
            failures.append(
                "FAIL  templates/page.html does not reference sxo_diagnostic_environment"
            )
        else:
            print("  OK    page.html references sxo_diagnostic_environment")

    if not MAIN_CSS.exists():
        failures.append("FAIL  static/css/main.css not found")
    else:
        css_content = MAIN_CSS.read_text(encoding="utf-8")
        for marker in REQUIRED_CSS_MARKERS:
            if marker not in css_content:
                failures.append(
                    f"FAIL  main.css missing required pattern: {marker!r}"
                )
            else:
                print(f"  OK    main.css contains {marker!r}")

    if not BASE_HTML.exists():
        failures.append("FAIL  templates/base.html not found")
    else:
        base_content = BASE_HTML.read_text(encoding="utf-8")
        if "width=device-width" not in base_content:
            failures.append(
                "FAIL  base.html missing viewport meta width=device-width"
            )
        else:
            print("  OK    base.html has viewport meta")

    for tmpl in TEMPLATES_DIR.rglob("*.html"):
        if "prototypes" in tmpl.parts:
            continue
        content = tmpl.read_text(encoding="utf-8", errors="ignore")
        rel = tmpl.relative_to(ROOT)
        for route in DEFERRED_ROUTES:
            if route in content:
                failures.append(
                    f"FAIL  deferred route {route!r} hardcoded in: {rel}"
                )
        for fragment in EXTERNAL_FRAGMENTS:
            if fragment in content:
                failures.append(
                    f"FAIL  external resource reference in: {rel}"
                )

    if failures:
        for msg in failures:
            print(f"  {msg}")
        print("validate_immersive_experience: FAILED")
        sys.exit(1)

    print("validate_immersive_experience: PASSED")


if __name__ == "__main__":
    main()
