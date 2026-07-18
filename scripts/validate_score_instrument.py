#!/usr/bin/env python3
"""
Validate the SuperSXO Score interactive instrument.

Checks:
- static/js/sxo-score.js is approved in data/approved-scripts.json,
  exists, contains no forbidden patterns, and is loaded from base.html
  with defer
- templates/components/score-instrument.html exists with the governed
  structure: the instrument form, 7 layer fieldsets with legends,
  14 statement groups (q1..q14), 42 radios restricted to values 0/1/2,
  an aria-live result region, a noscript fallback note, and a compute
  button that ships disabled until the script activates it
- the component contains no inline script/style and no external URLs
- only /sxo-score/ declares the instrument via interactive_component,
  and built output contains the form only under output/sxo-score/
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
COMPONENT = ROOT / "templates" / "components" / "score-instrument.html"
SCRIPT = ROOT / "static" / "js" / "sxo-score.js"
BASE_HTML = ROOT / "templates" / "base.html"
APPROVED = ROOT / "data" / "approved-scripts.json"
CONTENT_DIR = ROOT / "content" / "pages"
OUTPUT_DIR = ROOT / "output"

FORBIDDEN_JS_PATTERNS = [
    "eval(", "innerHTML", "document.write(", "fetch(",
    "XMLHttpRequest", "localStorage", "sessionStorage",
    "document.cookie", "import(", "http://", "https://",
]

STATEMENT_COUNT = 14
LAYER_COUNT = 7
ALLOWED_VALUES = {"0", "1", "2"}


def main() -> None:
    failures: list = []

    # --- approved script governance ---
    approved_files = set()
    if APPROVED.exists():
        data = json.loads(APPROVED.read_text(encoding="utf-8"))
        approved_files = {s.get("file") for s in data.get("approved_scripts", [])}
    if "static/js/sxo-score.js" not in approved_files:
        failures.append("FAIL  sxo-score.js not listed in data/approved-scripts.json")

    if not SCRIPT.is_file():
        failures.append("FAIL  static/js/sxo-score.js missing")
    else:
        js = SCRIPT.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_JS_PATTERNS:
            if pattern in js:
                failures.append(f"FAIL  forbidden pattern {pattern!r} in sxo-score.js")

    if BASE_HTML.exists():
        base = BASE_HTML.read_text(encoding="utf-8")
        if 'src="/static/js/sxo-score.js" defer' not in base:
            failures.append("FAIL  base.html does not load sxo-score.js with defer")

    # --- component structure ---
    if not COMPONENT.is_file():
        failures.append("FAIL  templates/components/score-instrument.html missing")
        report(failures)
        return

    comp = COMPONENT.read_text(encoding="utf-8")

    if 'id="sxo-score-form"' not in comp:
        failures.append("FAIL  component missing instrument form id")

    fieldsets = comp.count("<fieldset")
    if fieldsets != LAYER_COUNT:
        failures.append(
            f"FAIL  expected {LAYER_COUNT} layer fieldsets, found {fieldsets}"
        )
    if comp.count("<legend") != LAYER_COUNT:
        failures.append("FAIL  every layer fieldset requires a legend")

    groups = set(re.findall(r'name="(q\d+)"', comp))
    expected_groups = {f"q{i}" for i in range(1, STATEMENT_COUNT + 1)}
    if groups != expected_groups:
        failures.append(
            f"FAIL  statement groups mismatch: expected q1..q{STATEMENT_COUNT}, "
            f"found {sorted(groups)}"
        )

    radios = re.findall(r'<input type="radio" name="q\d+" value="(\d+)"', comp)
    if len(radios) != STATEMENT_COUNT * len(ALLOWED_VALUES):
        failures.append(
            f"FAIL  expected {STATEMENT_COUNT * len(ALLOWED_VALUES)} radios, "
            f"found {len(radios)}"
        )
    if set(radios) - ALLOWED_VALUES:
        failures.append(
            f"FAIL  radio values outside governed range 0/1/2: "
            f"{sorted(set(radios) - ALLOWED_VALUES)}"
        )

    if 'aria-live="polite"' not in comp or 'id="score-result"' not in comp:
        failures.append("FAIL  result region must exist with aria-live=polite")
    if "<noscript>" not in comp:
        failures.append("FAIL  component missing noscript fallback note")
    if 'id="score-compute"' not in comp or "disabled" not in comp:
        failures.append("FAIL  compute button must ship disabled until JS activates it")

    if "<script" in comp or "<style" in comp:
        failures.append("FAIL  component must not contain inline script or style")
    if "http://" in comp or "https://" in comp:
        failures.append("FAIL  component must not reference external URLs")

    # --- instrument is exclusive to /sxo-score/ ---
    for source_file in CONTENT_DIR.glob("*.json"):
        source = json.loads(source_file.read_text(encoding="utf-8"))
        declared = source.get("interactive_component", "")
        route = source.get("route", "")
        if route == "/sxo-score/":
            if declared != "score-instrument.html":
                failures.append(
                    "FAIL  /sxo-score/ content source must declare "
                    "interactive_component score-instrument.html"
                )
        elif declared:
            failures.append(
                f"FAIL  {source_file.name}: interactive_component is not "
                f"permitted outside /sxo-score/"
            )

    if OUTPUT_DIR.is_dir():
        for html_file in OUTPUT_DIR.rglob("index.html"):
            has_form = 'id="sxo-score-form"' in html_file.read_text(encoding="utf-8")
            is_score_page = html_file.parent.name == "sxo-score"
            if is_score_page and not has_form:
                failures.append("FAIL  output/sxo-score/ missing instrument form")
            if has_form and not is_score_page:
                failures.append(
                    f"FAIL  instrument form leaked into "
                    f"{html_file.relative_to(ROOT)}"
                )

    report(failures)


def report(failures: list) -> None:
    if failures:
        for msg in failures:
            print(f"  {msg}")
        print("validate_score_instrument: FAILED")
        sys.exit(1)
    print(f"  OK    instrument governance verified: {LAYER_COUNT} layers, "
          f"{STATEMENT_COUNT} statements, in-browser only")
    print("validate_score_instrument: PASSED")


if __name__ == "__main__":
    main()
