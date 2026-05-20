#!/usr/bin/env python3
"""
SuperSXO Repository Hygiene Validator.

Scans the repository for prohibited patterns, dangerous files, and
governance violations that must be caught before any public deployment.
"""

import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

VIOLATIONS = []


def fail(msg: str) -> None:
    VIOLATIONS.append(msg)
    print(f"  FAIL: {msg}")


# Directories that must not exist at the repository root
FORBIDDEN_ROOT_DIRS = ["output", "public", "dist"]

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


def check_forbidden_dirs() -> None:
    for dirname in FORBIDDEN_ROOT_DIRS:
        target = ROOT_DIR / dirname
        if target.is_dir():
            fail(f"Forbidden directory exists at repository root: {dirname}/")


def check_root_index_html() -> None:
    if (ROOT_DIR / "index.html").exists():
        fail("Root index.html exists — public page must not be created without route publication approval")


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
            except (OSError, PermissionError):
                pass


def check_js_files() -> None:
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in files:
            if filename.endswith(".js"):
                filepath = Path(root) / filename
                rel = filepath.relative_to(ROOT_DIR)
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
                        fail(f"Forbidden pattern '{pattern}' in template: {rel}")
            except (OSError, PermissionError):
                pass


def main() -> None:
    print("validate_repository_hygiene — SuperSXO Repository Security Scan")

    check_forbidden_dirs()
    check_root_index_html()
    check_env_files()
    check_yml_secret_markers()
    check_js_files()
    check_html_templates()

    if VIOLATIONS:
        print(f"\n  {len(VIOLATIONS)} violation(s) found. Repository hygiene check FAILED.")
        sys.exit(1)

    print("  validate_repository_hygiene PASSED — repository hygiene is clean")


if __name__ == "__main__":
    main()
