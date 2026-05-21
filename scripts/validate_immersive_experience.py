#!/usr/bin/env python3
"""
validate_immersive_experience.py

Validates the governed experience interface across both page types:

  Inner pages (all routes except "/"):
    The SXO diagnostic environment (Sprint 12, preserved) with station rail,
    active station readout, and sxo-diagnostic-environment.html component.

  Homepage ("/"):
    The light institutional adjudication system (Sprint 13, current standard)
    with opening chamber, examination record, assessment entry, and doctrine
    statement source components.

This validator accepts the adjudication model as the current immersive
experience standard. Sprint 12-only markers that no longer exist in the
Sprint 13 interface have been removed.

Obsolete markers removed:
  signal-path -- renamed/removed in Sprint 13 rebuild; the adjudication
                 interface does not use this class and it is no longer
                 present in static/css/main.css.

Current markers enforced:
  Inner page:   diagnostic-environment, station-rail, active-station-readout
  Adjudication: opening-chamber, examination-record, case-sheet
  Shared:       @media
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = ROOT / "templates"

DIAGNOSTIC_COMPONENT = (
    ROOT / "templates" / "components" / "sxo-diagnostic-environment.html"
)
PAGE_HTML = ROOT / "templates" / "page.html"
BASE_HTML = ROOT / "templates" / "base.html"
MAIN_CSS = ROOT / "static" / "css" / "main.css"
TOKENS_CSS = ROOT / "static" / "css" / "tokens.css"

ADJUDICATION_TEMPLATES = [
    ROOT / "templates" / "home.html",
    ROOT / "templates" / "components" / "opening-chamber.html",
    ROOT / "templates" / "components" / "examination-record.html",
    ROOT / "templates" / "components" / "assessment-entry.html",
    ROOT / "templates" / "components" / "doctrine-statement.html",
    ROOT / "templates" / "components" / "chamber-footer.html",
]

# Inner-page immersive markers (Sprint 12, preserved) +
# Adjudication markers (Sprint 13, homepage) +
# Shared infrastructure
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

# External resources and tracking patterns forbidden in all templates
FORBIDDEN_FRAGMENTS = [
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    "analytics.google.com",
    "google-analytics.com",
    "googletagmanager.com",
    "facebook.com/tr",
    "hotjar.com",
    "segment.com",
    'script src="http',
    "script src='http",
    "@import url(\"http",
    "@import url('http",
]


def main() -> None:
    failures: list = []

    def fail(msg: str) -> None:
        failures.append(msg)
        print(f"  FAIL: {msg}")

    def ok(msg: str) -> None:
        print(f"  OK    {msg}")

    # ── Inner page diagnostic environment ─────────────────────────────

    if not DIAGNOSTIC_COMPONENT.exists():
        fail("templates/components/sxo-diagnostic-environment.html not found")
    else:
        ok("sxo-diagnostic-environment.html exists")

    if PAGE_HTML.exists():
        page_content = PAGE_HTML.read_text(encoding="utf-8")
        if "sxo_diagnostic_environment" not in page_content:
            fail("templates/page.html does not reference sxo_diagnostic_environment")
        else:
            ok("page.html references sxo_diagnostic_environment")
    else:
        fail("templates/page.html not found")

    # ── Adjudication source templates (Sprint 13) ─────────────────────

    for tmpl in ADJUDICATION_TEMPLATES:
        if not tmpl.is_file():
            fail(f"adjudication template missing: {tmpl.relative_to(ROOT)}")
        else:
            ok(f"{tmpl.name} exists")

    # ── main.css markers ──────────────────────────────────────────────

    if MAIN_CSS.exists():
        css_content = MAIN_CSS.read_text(encoding="utf-8")
        for marker in REQUIRED_CSS_MARKERS:
            if marker not in css_content:
                fail(f"main.css missing required pattern: {marker!r}")
            else:
                ok(f"main.css contains {marker!r}")
    else:
        fail("static/css/main.css not found")

    # ── tokens.css: light-first default, opt-in dark ──────────────────

    if TOKENS_CSS.exists():
        tokens_content = TOKENS_CSS.read_text(encoding="utf-8")
        if not re.search(r"--surface-console:\s+#f8f7f5", tokens_content):
            fail(
                "tokens.css :root must define --surface-console: #f8f7f5 "
                "(light institutional default)"
            )
        else:
            ok("tokens.css has light institutional default (--surface-console: #f8f7f5)")
        if '[data-theme="dark"]' not in tokens_content:
            fail(
                'tokens.css missing [data-theme="dark"] block -- '
                "dark mode must exist only as an opt-in override"
            )
        else:
            ok('tokens.css has opt-in [data-theme="dark"] block')
    else:
        fail("static/css/tokens.css not found")

    # ── base.html: viewport meta + light-first default ────────────────

    if BASE_HTML.exists():
        base_content = BASE_HTML.read_text(encoding="utf-8")
        if "width=device-width" not in base_content:
            fail("base.html missing viewport meta width=device-width")
        else:
            ok("base.html has viewport meta")
        if 'data-theme="light"' not in base_content:
            fail(
                'base.html must set data-theme="light" on <html> -- '
                "light institutional is the sovereign default"
            )
        else:
            ok('base.html sets data-theme="light" as default')
    else:
        fail("templates/base.html not found")

    # ── Template scan: deferred routes + forbidden external resources ──

    for tmpl in TEMPLATES_DIR.rglob("*.html"):
        if "prototypes" in tmpl.parts:
            continue
        try:
            content = tmpl.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = tmpl.relative_to(ROOT)
        for route in DEFERRED_ROUTES:
            if route in content:
                fail(f"deferred route {route!r} hardcoded in {rel}")
        for fragment in FORBIDDEN_FRAGMENTS:
            if fragment in content:
                fail(f"forbidden external reference {fragment!r} in {rel}")

    if failures:
        print(f"\nvalidate_immersive_experience: {len(failures)} violation(s) found.")
        sys.exit(1)

    print("validate_immersive_experience: PASSED")


if __name__ == "__main__":
    main()
