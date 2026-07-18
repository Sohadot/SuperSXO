#!/usr/bin/env python3
"""
Validate the machine-discovery files: sitemap.xml, robots.txt, llms.txt.

Invariant: every URL in every discovery surface corresponds to a route
that is both status published and indexable true in data/routes.json —
and every such route is present. No unpublished, deferred, or noindex
route may ever leak into a discovery file.

Runs in non-strict mode when output/ discovery files are absent
(pre-build state) and strict when they exist.
"""

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).parent.parent
ROUTES_FILE = ROOT / "data" / "routes.json"
OUTPUT_DIR = ROOT / "output"
SITEMAP = OUTPUT_DIR / "sitemap.xml"
ROBOTS = OUTPUT_DIR / "robots.txt"
LLMS = OUTPUT_DIR / "llms.txt"

CANONICAL_DOMAIN = "https://supersxo.com"
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def main() -> None:
    failures: list = []

    routes = json.loads(ROUTES_FILE.read_text(encoding="utf-8")).get("routes", [])
    expected = {
        r["canonical"]
        for r in routes
        if r.get("status") == "published" and r.get("indexable", False)
    }
    forbidden = {
        r["canonical"]
        for r in routes
        if not (r.get("status") == "published" and r.get("indexable", False))
    }

    if not (SITEMAP.exists() or ROBOTS.exists() or LLMS.exists()):
        print("  WARN  discovery files not yet built — run scripts/build.py")
        print("validate_discovery_files: PASSED (pre-build, non-strict)")
        return

    for path in (SITEMAP, ROBOTS, LLMS):
        if not path.exists():
            failures.append(f"FAIL  missing discovery file: {path.name}")

    # --- sitemap.xml ---
    if SITEMAP.exists():
        try:
            root = ET.fromstring(SITEMAP.read_text(encoding="utf-8"))
            locs = {
                el.text.strip()
                for el in root.iter(f"{SITEMAP_NS}loc")
                if el.text
            }
            if locs != expected:
                for missing in sorted(expected - locs):
                    failures.append(f"FAIL  sitemap missing published URL: {missing}")
                for extra in sorted(locs - expected):
                    failures.append(f"FAIL  sitemap contains ungoverned URL: {extra}")
            for loc in locs:
                if not loc.startswith(CANONICAL_DOMAIN):
                    failures.append(f"FAIL  sitemap URL off canonical domain: {loc}")
        except ET.ParseError as exc:
            failures.append(f"FAIL  sitemap.xml is not valid XML: {exc}")

    # --- robots.txt ---
    if ROBOTS.exists():
        robots = ROBOTS.read_text(encoding="utf-8")
        if f"Sitemap: {CANONICAL_DOMAIN}/sitemap.xml" not in robots:
            failures.append("FAIL  robots.txt missing canonical Sitemap pointer")
        if "User-agent:" not in robots:
            failures.append("FAIL  robots.txt missing User-agent directive")
        for line in robots.splitlines():
            if line.strip() == "Disallow: /":
                failures.append("FAIL  robots.txt blocks the entire site")

    # --- llms.txt ---
    if LLMS.exists():
        llms = LLMS.read_text(encoding="utf-8")
        listed = set(re.findall(r"\((https?://[^)]+)\)", llms))
        if listed != expected:
            for missing in sorted(expected - listed):
                failures.append(f"FAIL  llms.txt missing published surface: {missing}")
            for extra in sorted(listed - expected):
                failures.append(f"FAIL  llms.txt lists ungoverned URL: {extra}")
        for url in forbidden:
            if url in llms:
                failures.append(
                    f"FAIL  llms.txt references unpublished/noindex route: {url}"
                )
        if "SuperSXO.com" not in llms:
            failures.append("FAIL  llms.txt missing attribution statement")

    if failures:
        for msg in failures:
            print(f"  {msg}")
        print("validate_discovery_files: FAILED")
        sys.exit(1)

    print(
        f"  OK    discovery surfaces verified: {len(expected)} governed URLs "
        f"in sitemap and llms.txt, robots.txt sane"
    )
    print("validate_discovery_files: PASSED")


if __name__ == "__main__":
    main()
