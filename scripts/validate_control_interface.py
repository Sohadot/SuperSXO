#!/usr/bin/env python3
"""
Validates that the search experience control interface is correctly implemented.

Checks:
- viewport meta (width=device-width) present in base.html
- main.css contains command-header
- main.css contains control-map or search-to-action-control-map
- main.css contains diagnostic-layer styling
- main.css contains route-telemetry styling
- main.css has mobile @media rules
- main.css has overflow-x protection
- main.css has no @import url() (no external stylesheet imports)
- main.css has no external resource references
- only approved JS files exist in static/ (per data/approved-scripts.json)
- templates have no external script tags
- no deferred route paths hardcoded in published templates
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
MAIN_CSS = ROOT / "static" / "css" / "main.css"
BASE_HTML = ROOT / "templates" / "base.html"
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
    ROOT / "templates" / "components" / "sxo-diagnostic-environment.html",
]

REQUIRED_CSS_MARKERS = [
    "command-header",
    "control-map",
    "diagnostic-layer",
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


def load_approved_js_paths() -> set:
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


def check_viewport(failures: list) -> None:
    if not BASE_HTML.exists():
        failures.append("FAIL  base.html not found")
        return
    content = BASE_HTML.read_text(encoding="utf-8")
    if "width=device-width" not in content:
        failures.append(
            "FAIL  base.html missing viewport meta: width=device-width"
        )


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
            failures.append(
                f"FAIL  main.css contains forbidden pattern: {pattern!r}"
            )
    for fragment in EXTERNAL_URL_FRAGMENTS:
        if fragment in content:
            failures.append(
                f"FAIL  main.css references external resource: {fragment!r}"
            )


def check_no_unapproved_js(failures: list) -> None:
    if not STATIC_DIR.exists():
        return
    approved_paths = load_approved_js_paths()
    for js_file in STATIC_DIR.rglob("*.js"):
        if js_file.is_file() and js_file.resolve() not in approved_paths:
            failures.append(
                f"FAIL  Unapproved JS file in static/: {js_file.relative_to(ROOT)}"
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
                failures.append(
                    f"FAIL  deferred route {route!r} hardcoded in: {rel}"
                )


def main() -> None:
    failures: list = []

    check_viewport(failures)
    check_main_css(failures)
    check_no_unapproved_js(failures)
    check_no_external_scripts(failures)
    check_no_deferred_routes(failures)

    if failures:
        for msg in failures:
            print(f"  {msg}")
        print("validate_control_interface: FAILED")
        sys.exit(1)

    print("validate_control_interface: PASSED")


if __name__ == "__main__":
    main()
