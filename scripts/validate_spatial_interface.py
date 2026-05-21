#!/usr/bin/env python3
"""
Validates that the sovereign search experience control interface is correctly implemented.

Checks:
- main.css contains required control-interface CSS classes and patterns
- main.css has no @import url() (no external font or stylesheet imports)
- main.css has no references to external resource URLs
- main.css has responsive @media queries
- main.css has overflow-x control
- base.html uses control-plane-shell
- header.html uses command-header (the realigned class from Sprint 10B)
- Only approved first-party JS files exist in static/ (per data/approved-scripts.json)
- Approved JS files contain no forbidden API patterns
- No external script tags in published templates
- No deferred route paths hardcoded in published templates
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
MAIN_CSS = ROOT / "static" / "css" / "main.css"
BASE_HTML = ROOT / "templates" / "base.html"
HEADER_HTML = ROOT / "templates" / "components" / "header.html"
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"
APPROVED_SCRIPTS_FILE = ROOT / "data" / "approved-scripts.json"

DEFERRED_ROUTES = ["/seo-vs-sxo/", "/ai-search-experience/", "/acquisition/"]

PUBLISHED_TEMPLATES = [
    ROOT / "templates" / "base.html",
    ROOT / "templates" / "page.html",
    ROOT / "templates" / "components" / "header.html",
    ROOT / "templates" / "components" / "footer.html",
    ROOT / "templates" / "components" / "route-context.html",
    ROOT / "templates" / "components" / "spatial-map.html",
]

REQUIRED_CSS_MARKERS = [
    "control-plane-shell",
    "command-header",       # Sprint 10B: replaced spatial-header
    "journey-control-map",  # Sprint 10B: replaced journey-orbit
    "route-telemetry",
    "@media",
    "overflow-x",
]

FORBIDDEN_CSS_PATTERNS = [
    "@import url(",
]

EXTERNAL_URL_FRAGMENTS = [
    "fonts.googleapis.com",
    "fonts.gstatic.com",
    "cdn.",
    "unpkg.com",
    "jsdelivr.net",
    "cdnjs.com",
]

JS_FORBIDDEN_PATTERNS = [
    "eval(",
    "innerHTML",
    "document.write(",
    "fetch(",
    "XMLHttpRequest",
    "localStorage",
    "sessionStorage",
    "document.cookie",
    "import(",
]


def load_approved_js_paths() -> set:
    """Return resolved paths of all approved JS files from data/approved-scripts.json."""
    if not APPROVED_SCRIPTS_FILE.exists():
        return set()
    try:
        data = json.loads(APPROVED_SCRIPTS_FILE.read_text(encoding="utf-8"))
        return {
            (ROOT / entry["file"]).resolve()
            for entry in data.get("approved_scripts", [])
            if "file" in entry
        }
    except (json.JSONDecodeError, KeyError):
        return set()


def check_main_css(failures: list) -> None:
    if not MAIN_CSS.exists():
        failures.append("FAIL  static/css/main.css not found")
        return

    content = MAIN_CSS.read_text(encoding="utf-8")

    for marker in REQUIRED_CSS_MARKERS:
        if marker not in content:
            failures.append(f"FAIL  main.css missing required pattern: {marker!r}")

    for pattern in FORBIDDEN_CSS_PATTERNS:
        if pattern in content:
            failures.append(f"FAIL  main.css contains forbidden pattern: {pattern!r}")

    for fragment in EXTERNAL_URL_FRAGMENTS:
        if fragment in content:
            failures.append(f"FAIL  main.css references external resource: {fragment!r}")


def check_templates(failures: list) -> None:
    if not BASE_HTML.exists():
        failures.append("FAIL  templates/base.html not found")
    else:
        content = BASE_HTML.read_text(encoding="utf-8")
        if "control-plane-shell" not in content:
            failures.append("FAIL  base.html missing class: control-plane-shell")

    if not HEADER_HTML.exists():
        failures.append("FAIL  templates/components/header.html not found")
    else:
        content = HEADER_HTML.read_text(encoding="utf-8")
        if "command-header" not in content:
            failures.append("FAIL  header.html missing class: command-header")


def check_js_files(failures: list) -> None:
    """Allow only approved first-party JS files. Block all unapproved JS."""
    if not STATIC_DIR.exists():
        return

    approved_resolved = load_approved_js_paths()

    for js_file in STATIC_DIR.rglob("*.js"):
        if not js_file.is_file():
            continue

        if js_file.resolve() not in approved_resolved:
            rel = js_file.relative_to(ROOT)
            failures.append(f"FAIL  Unapproved JS file in static/: {rel}")
            continue

        content = js_file.read_text(encoding="utf-8")
        rel = js_file.relative_to(ROOT)
        for pattern in JS_FORBIDDEN_PATTERNS:
            if pattern in content:
                failures.append(
                    f"FAIL  forbidden API {pattern!r} in approved script: {rel}"
                )
        if "http://" in content or "https://" in content:
            failures.append(
                f"FAIL  external URL reference in approved script: {rel}"
            )


def check_no_external_scripts(failures: list) -> None:
    for template_path in TEMPLATES_DIR.rglob("*.html"):
        if "prototypes" in template_path.parts:
            continue
        content = template_path.read_text(encoding="utf-8")
        rel = template_path.relative_to(ROOT)
        if '<script src="http' in content or "<script src='http" in content:
            failures.append(f"FAIL  external script tag in: {rel}")
        for fragment in ["fonts.googleapis.com", "fonts.gstatic.com"]:
            if fragment in content:
                failures.append(f"FAIL  external font reference in: {rel}")


def check_no_deferred_routes(failures: list) -> None:
    for template_path in PUBLISHED_TEMPLATES:
        if not template_path.exists():
            continue
        content = template_path.read_text(encoding="utf-8")
        rel = template_path.relative_to(ROOT)
        for route in DEFERRED_ROUTES:
            if route in content:
                failures.append(f"FAIL  deferred route {route!r} hardcoded in: {rel}")


def main() -> None:
    failures: list = []

    check_main_css(failures)
    check_templates(failures)
    check_js_files(failures)
    check_no_external_scripts(failures)
    check_no_deferred_routes(failures)

    if failures:
        for msg in failures:
            print(f"  {msg}")
        print("validate_spatial_interface: FAILED")
        sys.exit(1)

    print("validate_spatial_interface: PASSED")


if __name__ == "__main__":
    main()
