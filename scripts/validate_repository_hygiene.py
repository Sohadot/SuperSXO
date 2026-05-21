#!/usr/bin/env python3
"""
SuperSXO Repository Hygiene Validator.

Scans the repository for prohibited patterns, dangerous files, and
governance violations that must be caught before any public deployment.

Allows root index.html and output/ only when the approved build pipeline
has generated them for published routes. All other violations are hard failures.

First-party JS: only static/js/interface-state.js is approved.
All other .js files are violations.
"""

import json
import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

VIOLATIONS = []

APPROVED_JS_PATHS = {
    "static/js/interface-state.js",
}


def fail(msg: str) -> None:
    VIOLATIONS.append(msg)
    print(f"  FAIL: {msg}")


def load_routes() -> list:
    routes_path = ROOT_DIR / "data" / "routes.json"
    if not routes_path.exists():
        return []
    with open(routes_path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("routes", []) if isinstance(data, dict) else data


ALWAYS_FORBIDDEN_DIRS = ["public", "dist"]
BUILD_OUTPUT_DIR = "output"

YML_SECRET_MARKERS = [
    "API_KEY=",
    "SECRET_KEY=",
    "PRIVATE_KEY",
    "CLOUDFLARE_API_TOKEN",
    "GITHUB_TOKEN=",
]

HTML_FORBIDDEN_PATTERNS = [
    "onclick=",
    "onload=",
    "onerror=",
    "onmouseover=",
    "eval(",
    "innerHTML",
    "document.write",
    '<script src="http',
    "three.js",
    "webgl",
    "<canvas",
    "google-analytics",
    "googletagmanager",
    "adsbygoogle",
    "stripe",
    "paypal",
    "affiliate",
]

SKIP_DIRS = {".git"}


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
                    if marker not in content:
                        continue
                    rel = filepath.relative_to(ROOT_DIR)
                    for line in content.splitlines():
                        if marker not in line:
                            continue
                        stripped = line.strip()
                        if "secrets." in stripped or "${{" in stripped:
                            continue
                        fail(
                            f"Potential hardcoded secret '{marker}' "
                            f"in {rel}: {stripped[:80]}"
                        )
            except (OSError, PermissionError):
                pass


def check_js_files() -> None:
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for filename in files:
            if not filename.endswith(".js"):
                continue
            rel = str((Path(root) / filename).relative_to(ROOT_DIR))
            if rel not in APPROVED_JS_PATHS:
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
                        fail(
                            f"Forbidden pattern '{pattern}' "
                            f"in template: {rel}"
                        )
            except (OSError, PermissionError):
                pass


def main() -> None:
    print("validate_repository_hygiene — SuperSXO Repository Security Scan")

    routes = load_routes()

    check_always_forbidden_dirs()
    check_output_dir(routes)
    check_root_index_html(routes)
    check_env_files()
    check_yml_secret_markers()
    check_js_files()
    check_html_templates()

    if VIOLATIONS:
        print(
            f"\n  {len(VIOLATIONS)} violation(s) found. "
            f"Repository hygiene check FAILED."
        )
        sys.exit(1)

    print("  validate_repository_hygiene PASSED — repository hygiene is clean")


if __name__ == "__main__":
    main()
