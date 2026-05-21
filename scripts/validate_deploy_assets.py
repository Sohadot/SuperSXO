#!/usr/bin/env python3
"""
Validate deployed assets in output/ after build.

Usage:
  python scripts/validate_deploy_assets.py          # pre-build mode (non-strict)
  python scripts/validate_deploy_assets.py --strict # post-build mode (strict)

Pre-build mode (default):
  - Skips safely if output/ does not exist.
  - If output/ exists but deploy assets are missing, prints a warning and exits 0.
  - Never blocks the pre-build quality gate.

Strict mode (--strict):
  - Requires output/static/css/tokens.css and output/static/css/main.css.
  - Requires output/static/js/interface-state.js (approved first-party script).
  - Requires output/CNAME (custom domain preservation).
  - Verifies generated HTML references both CSS files.
  - Verifies no unapproved .js files are deployed in output/.
  - Verifies no external stylesheet or script references in generated HTML.
  - Verifies no deferred route output exists.
  - Fails and exits non-zero on any violation.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = REPO_ROOT / "output"

REQUIRED_CSS = [
    "static/css/tokens.css",
    "static/css/main.css",
]

APPROVED_JS = "static/js/interface-state.js"

DEFERRED_ROUTES = [
    "seo-vs-sxo",
    "ai-search-experience",
    "acquisition",
]

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


def run_strict_checks() -> bool:
    errors: list = []

    check(
        (OUTPUT_DIR / "CNAME").is_file(),
        "output/CNAME exists (custom domain preserved)",
        errors,
    )

    for rel_path in REQUIRED_CSS:
        check(
            (OUTPUT_DIR / rel_path).is_file(),
            f"output/{rel_path} exists",
            errors,
        )

    approved_js_path = OUTPUT_DIR / APPROVED_JS
    check(
        approved_js_path.is_file(),
        f"output/{APPROVED_JS} exists (approved interface script deployed)",
        errors,
    )

    js_files = list(OUTPUT_DIR.rglob("*.js"))
    unapproved_js = [jf for jf in js_files if jf != approved_js_path]
    check(
        len(unapproved_js) == 0,
        "No unapproved .js files in output/",
        errors,
    )
    for jf in unapproved_js:
        print(f"    → {jf.relative_to(REPO_ROOT)}")

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

    for route_slug in DEFERRED_ROUTES:
        check(
            not (OUTPUT_DIR / route_slug).exists(),
            f"Deferred route output/{route_slug}/ not deployed",
            errors,
        )

    return len(errors) == 0


def main() -> None:
    strict = "--strict" in sys.argv
    mode = "strict" if strict else "pre-build"
    print(f"=== validate_deploy_assets: checking deployed output assets ({mode} mode) ===")

    if not OUTPUT_DIR.exists():
        print("  SKIP  output/ not found — deploy asset checks skipped")
        print("validate_deploy_assets: PASSED (no output/ present)")
        return

    if not strict:
        missing = [
            rel for rel in ["CNAME"] + REQUIRED_CSS + [APPROVED_JS]
            if not (OUTPUT_DIR / rel).is_file()
        ]
        if missing:
            print("  WARN  output/ exists but deploy assets are not yet present:")
            for rel in missing:
                print(f"    ! output/{rel} missing")
            print("  WARN  Deploy asset validation skipped in pre-build mode.")
            print("  WARN  Run: python scripts/build.py")
            print("  WARN  Then: python scripts/validate_deploy_assets.py --strict")
        else:
            print("  OK    output/CNAME, output/static/css/, and output/static/js/ deploy assets present")
        print("validate_deploy_assets: PASSED (pre-build, non-strict)")
        return

    if run_strict_checks():
        print("validate_deploy_assets: PASSED")
    else:
        print("validate_deploy_assets: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
