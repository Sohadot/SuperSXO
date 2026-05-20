#!/usr/bin/env python3
"""
Validate static architecture boundaries.

Ensures the site skeleton is correctly structured and no unauthorized
public pages or generated output exist outside the governed build pipeline.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def check(condition: bool, label: str, errors: list) -> None:
    if condition:
        print(f"  OK    {label}")
    else:
        print(f"  FAIL  {label}")
        errors.append(label)


def validate_build_boundaries() -> bool:
    errors: list = []

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

    # No root index.html — public pages not published yet
    check(
        not (REPO_ROOT / "index.html").exists(),
        "No root index.html (public pages not yet published)",
        errors,
    )

    # No output/ directory — only created by a deliberate build run
    check(
        not (REPO_ROOT / "output").exists(),
        "No output/ directory (build pipeline not yet triggered)",
        errors,
    )

    # No stray HTML files at repository root
    root_html = [f for f in REPO_ROOT.glob("*.html")]
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
