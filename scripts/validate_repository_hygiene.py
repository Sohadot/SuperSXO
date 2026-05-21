#!/usr/bin/env python3
"""
SuperSXO Repository Hygiene Validator.

Scans the repository for prohibited patterns, dangerous files, and
governance violations that must be caught before any public deployment.
claude/add-home-prototype-jPdNY
"""



Allows root index.html and output/ only when the approved build pipeline
has generated them for published routes. All other violations are hard failures.
"""

import json
 main
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

VIOLATIONS = []


def fail(msg: str) -> None:
    VIOLATIONS.append(msg)
    print(f"  FAIL: {msg}")


 claude/add-home-prototype-jPdNY
# Directories that must not exist at the repository root
FORBIDDEN_ROOT_DIRS = ["output", "public", "dist"]

def load_routes() -> list:
    routes_path = ROOT_DIR / "data" / "routes.json"
    if not routes_path.exists():
        return []
    with open(routes_path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("routes", []) if isinstance(data, dict) else data


# Directories always forbidden at the repository root
ALWAYS_FORBIDDEN_DIRS = ["public", "dist"]

# output/ is forbidden unless routes are published (build pipeline creates it)
BUILD_OUTPUT_DIR = "output"
 main

# Secret markers scanned in .yml and .yaml files
YML_SECRET_MARKERS = [
    "API_KEY=",
    "SECRET_KEY=",
    "PRIVATE_KEY",
    "CLOUDFLARE_API_TOKEN",
    "GITHUB_TOKEN=",
]

# Patterns forbidden in HTML template files
HTML_FORBIDDEN_PATTERNS = [
    # Inline event handlers
    "onclick=",
    "onload=",
    "onerror=",
    "onmouseover=",
    # Dangerous JavaScript strings
    "eval(",
    "innerHTML",
    "document.write",
    # External script tags
    '<script src="http',
    # Prohibited libraries and frameworks
    "three.js",
    "webgl",
    "<canvas",
    # Analytics and tracking
    "google-analytics",
    "googletagmanager",
    "adsbygoogle",
    # Payment and monetization
    "stripe",
    "paypal",
    "affiliate",
]

# Directories to skip when walking the repository
SKIP_DIRS = {".git"}


 claude/add-home-prototype-jPdNY
def check_forbidden_dirs() -> None:
    for dirname in FORBIDDEN_ROOT_DIRS:
        target = ROOT_DIR / dirname
        if target.is_dir():
            fail(f"Forbidden directory exists at repository root: {dirname}/")


def check_root_index_html() -> None:
    if (ROOT_DIR / "index.html").exists():
        fail("Root index.html exists — public page must not be created without route publication approval")

def any_route_published(routes: list) -> bool:
    return any(r.get("status") == "published" for r in routes)


def home_route_published(routes: list) -> bool:
    return any(
        r.get("path") == "/" and r.get("status") == "published"
        for r in routes
    )


def check_always_forbidden_dirs() -> None:
    for dirname in ALWAYS_FORBIDDEN_DIRS:
        if (ROOT_DIR / dirname).is_dir():
            fail(f"Forbidden directory exists at repository root: {dirname}/")


def check_output_dir(routes: list) -> None:
    if not (ROOT_DIR / BUILD_OUTPUT_DIR).is_dir():
        return
    if not any_route_published(routes):
        fail(
            "output/ directory exists but no routes are published — "
            "only scripts/build.py may create output/ and only after routes are published"
        )


def check_root_index_html(routes: list) -> None:
    if not (ROOT_DIR / "index.html").exists():
        return
    if not home_route_published(routes):
        fail(
            "Root index.html exists but route '/' is not published — "
            "only scripts/build.py may create index.html after route '/' is published"
        )
 main


def check_env_files() -> None:
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in files:
            if filename == ".env" or filename.startswith(".env."):
                rel = Path(root).relative_to(ROOT_DIR) / filename
                fail(f".env file found (secrets must not be committed): {rel}")


def check_yml_secret_markers() -> None:
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in files:
            if not (filename.endswith(".yml") or filename.endswith(".yaml")):
                continue
            filepath = Path(root) / filename
            try:
                content = filepath.read_text(encoding="utf-8", errors="ignore")
                for marker in YML_SECRET_MARKERS:
 claude/add-home-prototype-jPdNY
                    if marker in content:
                        # Allow legitimate secrets references in workflow context
                        # Flag only if it looks like a hardcoded value assignment
                        rel = filepath.relative_to(ROOT_DIR)
                        # Skip if marker appears only as a secrets expression reference
                        import re
                        lines = content.splitlines()
                        for line in lines:
                            if marker in line:
                                stripped = line.strip()
                                # Allow ${{ secrets.X }} and secrets.X patterns
                                if "secrets." in stripped or "${{" in stripped:
                                    continue
                                fail(f"Potential hardcoded secret '{marker}' in {rel}: {stripped[:80]}")

                    if marker not in content:
                        continue
                    rel = filepath.relative_to(ROOT_DIR)
                    for line in content.splitlines():
                        if marker not in line:
                            continue
                        stripped = line.strip()
                        # Allow legitimate secrets references (${{ secrets.X }})
                        if "secrets." in stripped or "${{" in stripped:
                            continue
                        fail(
                            f"Potential hardcoded secret '{marker}' "
                            f"in {rel}: {stripped[:80]}"
                        )
 main
            except (OSError, PermissionError):
                pass


def check_js_files() -> None:
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in files:
            if filename.endswith(".js"):
 claude/add-home-prototype-jPdNY
                filepath = Path(root) / filename
                rel = filepath.relative_to(ROOT_DIR)

                rel = (Path(root) / filename).relative_to(ROOT_DIR)
 main
                fail(f"JavaScript file found (not approved): {rel}")


def check_html_templates() -> None:
    templates_dir = ROOT_DIR / "templates"
    if not templates_dir.is_dir():
        return
    for root, dirs, files in os.walk(templates_dir):
        for filename in files:
            if not filename.endswith(".html"):
                continue
            filepath = Path(root) / filename
            try:
                content = filepath.read_text(encoding="utf-8", errors="ignore")
                rel = filepath.relative_to(ROOT_DIR)
                for pattern in HTML_FORBIDDEN_PATTERNS:
                    if pattern in content:
 claude/add-home-prototype-jPdNY
                        fail(f"Forbidden pattern '{pattern}' in template: {rel}")

                        fail(
                            f"Forbidden pattern '{pattern}' "
                            f"in template: {rel}"
                        )
 main
            except (OSError, PermissionError):
                pass


def main() -> None:
    print("validate_repository_hygiene — SuperSXO Repository Security Scan")

 claude/add-home-prototype-jPdNY
    check_forbidden_dirs()
    check_root_index_html()

    routes = load_routes()

    check_always_forbidden_dirs()
    check_output_dir(routes)
    check_root_index_html(routes)
 main
    check_env_files()
    check_yml_secret_markers()
    check_js_files()
    check_html_templates()

    if VIOLATIONS:
 claude/add-home-prototype-jPdNY
        print(f"\n  {len(VIOLATIONS)} violation(s) found. Repository hygiene check FAILED.")
        print(
            f"\n  {len(VIOLATIONS)} violation(s) found. "
            f"Repository hygiene check FAILED."
        )
 main
        sys.exit(1)

    print("  validate_repository_hygiene PASSED — repository hygiene is clean")


if __name__ == "__main__":
    main()
