#!/usr/bin/env python3
"""
Verifies that only governed, approved JavaScript files exist in static/js/.

Checks:
- data/approved-scripts.json exists and is valid
- Every approved script file exists on disk
- No forbidden API patterns appear in any approved script
- No unapproved .js files exist in static/js/
- base.html references each approved script with the defer attribute
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
APPROVED_SCRIPTS_FILE = ROOT / "data" / "approved-scripts.json"
STATIC_JS_DIR = ROOT / "static" / "js"
BASE_HTML = ROOT / "templates" / "base.html"

FORBIDDEN_PATTERNS = [
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


def main() -> None:
    failures: list = []

    if not APPROVED_SCRIPTS_FILE.exists():
        print("  FAIL  data/approved-scripts.json not found")
        print("validate_approved_scripts: FAILED")
        sys.exit(1)

    try:
        data = json.loads(APPROVED_SCRIPTS_FILE.read_text(encoding="utf-8"))
        approved_scripts = data.get("approved_scripts", [])
    except (json.JSONDecodeError, KeyError) as exc:
        print(f"  FAIL  data/approved-scripts.json parse error: {exc}")
        print("validate_approved_scripts: FAILED")
        sys.exit(1)

    approved_paths = set()
    for script in approved_scripts:
        rel = script.get("file", "")
        if not rel:
            failures.append("FAIL  approved script entry missing 'file' key")
            continue
        script_path = ROOT / rel
        approved_paths.add(script_path.resolve())

        if not script_path.is_file():
            failures.append(f"FAIL  approved script not found: {rel}")
            continue

        content = script_path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in content:
                failures.append(
                    f"FAIL  forbidden pattern {pattern!r} found in: {rel}"
                )

        if "http://" in content or "https://" in content:
            failures.append(
                f"FAIL  external URL reference found in approved script: {rel}"
            )

    if STATIC_JS_DIR.exists():
        for js_file in STATIC_JS_DIR.rglob("*.js"):
            if js_file.is_file() and js_file.resolve() not in approved_paths:
                failures.append(
                    f"FAIL  unapproved .js file in static/js/: {js_file.relative_to(ROOT)}"
                )

    if BASE_HTML.exists():
        base_content = BASE_HTML.read_text(encoding="utf-8")
        for script in approved_scripts:
            rel = script.get("file", "")
            script_name = Path(rel).name
            if script_name not in base_content:
                failures.append(
                    f"FAIL  base.html does not reference approved script: {script_name}"
                )
            elif "defer" not in base_content:
                failures.append(
                    f"FAIL  approved script {script_name!r} in base.html missing defer attribute"
                )
    else:
        failures.append("FAIL  templates/base.html not found")

    if failures:
        for msg in failures:
            print(f"  {msg}")
        print("validate_approved_scripts: FAILED")
        sys.exit(1)

    print(f"  OK    {len(approved_scripts)} approved script(s) verified")
    print("validate_approved_scripts: PASSED")


if __name__ == "__main__":
    main()
