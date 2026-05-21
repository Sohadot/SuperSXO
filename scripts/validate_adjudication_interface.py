#!/usr/bin/env python3
"""
validate_adjudication_interface.py

Enforces that the light institutional adjudication interface is correctly
integrated at source level: templates, CSS tokens, and base.html.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

REQUIRED_COMPONENTS = [
    ROOT / "templates" / "components" / "opening-chamber.html",
    ROOT / "templates" / "components" / "examination-record.html",
    ROOT / "templates" / "components" / "assessment-entry.html",
    ROOT / "templates" / "components" / "doctrine-statement.html",
    ROOT / "templates" / "components" / "chamber-footer.html",
]

HOME_TEMPLATE = ROOT / "templates" / "home.html"
PAGE_TEMPLATE = ROOT / "templates" / "page.html"
BASE_TEMPLATE = ROOT / "templates" / "base.html"
MAIN_CSS = ROOT / "static" / "css" / "main.css"
TOKENS_CSS = ROOT / "static" / "css" / "tokens.css"

DEFERRED_ROUTES = ["/seo-vs-sxo/", "/ai-search-experience/", "/acquisition/"]

REQUIRED_CSS_CLASSES = [
    "opening-chamber",
    "examination-record",
    "case-sheet",
    "doctrine-statement",
    "chamber-footer",
]


def main() -> None:
    errors = []

    def fail(msg: str) -> None:
        errors.append(msg)
        print(f"  FAIL: {msg}")

    for component in REQUIRED_COMPONENTS:
        if not component.is_file():
            fail(f"Required component missing: {component.relative_to(ROOT)}")

    if not HOME_TEMPLATE.is_file():
        fail(f"Home template missing: {HOME_TEMPLATE.relative_to(ROOT)}")

    if PAGE_TEMPLATE.is_file():
        page_content = PAGE_TEMPLATE.read_text(encoding="utf-8")
        if "sxo_diagnostic_environment" not in page_content:
            fail("templates/page.html must reference {{ sxo_diagnostic_environment }}")
    else:
        fail(f"Page template missing: {PAGE_TEMPLATE.relative_to(ROOT)}")

    if BASE_TEMPLATE.is_file():
        base_content = BASE_TEMPLATE.read_text(encoding="utf-8")
        if 'data-theme="light"' not in base_content:
            fail('templates/base.html must have data-theme="light" on the <html> element')
    else:
        fail(f"Base template missing: {BASE_TEMPLATE.relative_to(ROOT)}")

    if MAIN_CSS.is_file():
        main_content = MAIN_CSS.read_text(encoding="utf-8")
        for cls in REQUIRED_CSS_CLASSES:
            if cls not in main_content:
                fail(f"static/css/main.css must contain CSS class: {cls}")
    else:
        fail(f"main.css missing: {MAIN_CSS.relative_to(ROOT)}")

    if TOKENS_CSS.is_file():
        tokens_content = TOKENS_CSS.read_text(encoding="utf-8")
        if not re.search(r"--surface-console:\s+#f8f7f5", tokens_content):
            fail(
                "static/css/tokens.css :root must define --surface-console: #f8f7f5 "
                "(light institutional default)"
            )
        if '[data-theme="dark"]' not in tokens_content:
            fail(
                'static/css/tokens.css must contain a [data-theme="dark"] block '
                "(dark mode must be opt-in, not the default)"
            )
        light_section = tokens_content.split('[data-theme="dark"]')[0]
        black_backgrounds = [
            "background: #020304",
            "background: #000",
            "background: #000000",
            "background-color: #020304",
            "background-color: #000",
            "background-color: #000000",
        ]
        for pattern in black_backgrounds:
            if pattern in light_section:
                fail(
                    f"tokens.css light default section must not hardcode a black "
                    f"background ({pattern!r})"
                )
    else:
        fail(f"tokens.css missing: {TOKENS_CSS.relative_to(ROOT)}")

    for component in REQUIRED_COMPONENTS:
        if not component.is_file():
            continue
        comp_content = component.read_text(encoding="utf-8")
        for deferred in DEFERRED_ROUTES:
            if f'href="{deferred}"' in comp_content:
                fail(
                    f"{component.name}: must not link to deferred route {deferred!r}"
                )

    if errors:
        print(f"\nadjudication interface: {len(errors)} violation(s) found.")
        sys.exit(1)

    print("adjudication interface: all checks passed.")


if __name__ == "__main__":
    main()
