#!/usr/bin/env python3
"""
Validate static architecture boundaries.

Ensures the site skeleton is correctly structured and no unauthorized
public pages or generated output exist outside the governed build pipeline.
When routes are published, output/ is expected to exist after a build run.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def load_published_count() -> int:
    routes_path = REPO_ROOT / "data" / "routes.json"
    if not routes_path.exists():
        return 0
    with open(routes_path, encoding="utf-8") as f:
        data = json.load(f)
    routes = data.get("routes", []) if isinstance(data, dict) else data
    return sum(1 for r in routes if r.get("status") == "published")


def check(condition: bool, label: str, errors: list) -> None:
    if condition:
        print(f"  OK    {label}")
    else:
        print(f"  FAIL  {label}")
        errors.append(label)


def validate_build_boundaries() -> bool:
    errors: list = []
    published_count = load_published_count()

    # Required skeleton directories
    check(
        (REPO_ROOT / "templates").is_dir(),
        "templates/ directory exists",
        errors,
    )
    check(
        (REPO_ROOT / "content" / "pages").is_dir(),
        "content/pages/ directory exists",
        errors,
    )

    # Required CSS files
    check(
        (REPO_ROOT / "static" / "css" / "tokens.css").is_file(),
        "static/css/tokens.css exists",
        errors,
    )
    check(
        (REPO_ROOT / "static" / "css" / "main.css").is_file(),
        "static/css/main.css exists",
        errors,
    )

    # Build script exists
    check(
        (REPO_ROOT / "scripts" / "build.py").is_file(),
        "scripts/build.py exists",
        errors,
    )

    # Root index.html must never exist at the repository root
    # (build.py writes output/index.html, never REPO_ROOT/index.html)
    check(
        not (REPO_ROOT / "index.html").exists(),
        "No root index.html at repository root (build output goes to output/)",
        errors,
    )

    # output/ is only permitted when routes are published
    output_dir = REPO_ROOT / "output"
    if published_count == 0:
        check(
            not output_dir.exists(),
            "No output/ directory (build pipeline not yet triggered)",
            errors,
        )
    else:
        # output/ may or may not exist; if it exists that is expected after build
        if output_dir.exists():
            print(f"  OK    output/ directory exists ({published_count} route(s) published)")
        else:
            print(f"  OK    output/ not yet generated ({published_count} route(s) published — run build.py)")

    # No stray HTML files at repository root
    root_html = list(REPO_ROOT.glob("*.html"))
    check(
        len(root_html) == 0,
        f"No public HTML files at repository root ({len(root_html)} found)",
        errors,
    )

    return len(errors) == 0


def main() -> None:
    print("=== validate_build_boundaries: checking site skeleton ===")
    passed = validate_build_boundaries()
    if passed:
        print("validate_build_boundaries: PASSED")
    else:
        print("validate_build_boundaries: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
