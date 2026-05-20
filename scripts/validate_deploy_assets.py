#!/usr/bin/env python3
"""
Validate deployed assets in output/ after build.

Skips safely if output/ does not exist (pre-build mode).
When output/ exists, verifies:
  - output/static/css/tokens.css present
  - output/static/css/main.css present
  - generated HTML references the CSS files
  - no .js files in output/
  - no external stylesheet or script references in generated HTML
  - no deferred route output exists
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "output"

REQUIRED_CSS = [
    "static/css/tokens.css",
    "static/css/main.css",
]

DEFERRED_ROUTES = [
    "seo-vs-sxo",
    "ai-search-experience",
    "acquisition",
]

# Patterns that indicate external stylesheet or script injection
EXTERNAL_ASSET_PATTERNS = [
    'rel="stylesheet" href="http',
    "rel='stylesheet' href='http",
    '<script src="http',
    "<script src='http",
]


def check(condition: bool, label: str, errors: list) -> None:
    if condition:
        print(f"  OK    {label}")
    else:
        print(f"  FAIL  {label}")
        errors.append(label)


def validate_deploy_assets() -> bool:
    if not OUTPUT_DIR.exists():
        print("  SKIP  output/ not found — pre-build mode, deploy asset checks skipped")
        return True

    errors: list = []

    # Required CSS files must exist in output/static/css/
    for rel_path in REQUIRED_CSS:
        check(
            (OUTPUT_DIR / rel_path).is_file(),
            f"output/{rel_path} exists",
            errors,
        )

    # No .js files in output/
    js_files = list(OUTPUT_DIR.rglob("*.js"))
    check(
        len(js_files) == 0,
        "No .js files in output/",
        errors,
    )
    for jf in js_files:
        print(f"    → {jf.relative_to(REPO_ROOT)}")

    # HTML file checks
    html_files = list(OUTPUT_DIR.rglob("*.html"))
    check(
        len(html_files) > 0,
        f"{len(html_files)} HTML file(s) found in output/",
        errors,
    )

    css_refs_found = {rel: False for rel in REQUIRED_CSS}
    external_refs: list = []

    for html_file in html_files:
        try:
            content = html_file.read_text(encoding="utf-8", errors="ignore")
        except (OSError, PermissionError):
            continue

        for rel_path in REQUIRED_CSS:
            if f"/{rel_path}" in content:
                css_refs_found[rel_path] = True

        for pattern in EXTERNAL_ASSET_PATTERNS:
            if pattern in content:
                external_refs.append(
                    f"{html_file.relative_to(REPO_ROOT)}: contains '{pattern}'"
                )

    for rel_path, found in css_refs_found.items():
        check(
            found,
            f"Generated HTML references /{rel_path}",
            errors,
        )

    check(
        len(external_refs) == 0,
        "No external stylesheet or script references in generated HTML",
        errors,
    )
    for ref in external_refs:
        print(f"    → {ref}")

    # No deferred route output
    for route_slug in DEFERRED_ROUTES:
        check(
            not (OUTPUT_DIR / route_slug).exists(),
            f"Deferred route output/{route_slug}/ not deployed",
            errors,
        )

    return len(errors) == 0


def main() -> None:
    print("=== validate_deploy_assets: checking deployed output assets ===")
    passed = validate_deploy_assets()
    if passed:
        print("validate_deploy_assets: PASSED")
    else:
        print("validate_deploy_assets: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
