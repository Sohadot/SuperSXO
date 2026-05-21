#!/usr/bin/env python3
"""
SuperSXO Publication Readiness Validator.

Verifies that the repository is in a valid state for controlled public
generation. Fails if published routes have missing content, unresolved
internal links to unpublished routes, prohibited claims, or no content source.
"""

import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

ROUTES_FILE = ROOT_DIR / "data" / "routes.json"
CONTENT_DIR = ROOT_DIR / "content" / "pages"
ALPHA_PLAN_FILE = ROOT_DIR / "data" / "public-alpha-plan.json"

ERRORS = []


def fail(msg: str) -> None:
    ERRORS.append(msg)
    print(f"  FAIL: {msg}")


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_content_sources() -> dict:
    sources = {}
    if not CONTENT_DIR.is_dir():
        return sources
    for content_file in CONTENT_DIR.glob("*.json"):
        try:
            data = load_json(content_file)
            route_key = data.get("route")
            if route_key:
                sources[route_key] = data
        except (json.JSONDecodeError, KeyError):
            pass
    return sources


def main() -> None:
    print("validate_publication_readiness — SuperSXO Publication Governance")

    for required in (ROUTES_FILE, ALPHA_PLAN_FILE):
        if not required.exists():
            fail(f"Required file missing: {required.relative_to(ROOT_DIR)}")

    if ERRORS:
        print(f"\n  {len(ERRORS)} error(s). Publication readiness check FAILED.")
        sys.exit(1)

    routes_data = load_json(ROUTES_FILE)
    all_routes = routes_data.get("routes", [])
    alpha_plan = load_json(ALPHA_PLAN_FILE)
    content_sources = load_content_sources()

    all_route_paths = {r["path"] for r in all_routes}
    published_routes = [r for r in all_routes if r.get("status") == "published"]
    published_paths = {r["path"] for r in published_routes}
    all_routes_map = {r["path"]: r for r in all_routes}

    # --- Check 1: all alpha plan candidate routes exist in routes.json ---
    for candidate in alpha_plan.get("candidate_routes", []):
        if candidate["path"] not in all_route_paths:
            fail(
                f"Alpha plan candidate '{candidate['path']}' "
                f"not found in data/routes.json"
            )

    # --- Check 2: every published route has approved_for_build content ---
    for route in published_routes:
        path = route["path"]
        content = content_sources.get(path)
        if not content:
            fail(
                f"Published route '{path}' has no content source file "
                f"in content/pages/"
            )
        elif content.get("source_status") != "approved_for_build":
            fail(
                f"Published route '{path}' content source_status is "
                f"'{content.get('source_status')}' — must be 'approved_for_build'"
            )

    # --- Check 3: every internal link on a published route is also published ---
    for route in published_routes:
        path = route["path"]
        for link in route.get("required_internal_links", []):
            if link not in published_paths:
                fail(
                    f"Published route '{path}' requires internal link to "
                    f"'{link}' which is not published"
                )

    # --- Check 4: no published route is missing content entirely ---
    for path in published_paths:
        if path not in content_sources:
            fail(f"Published route '{path}' has no content source")

    # --- Check 5: no published page contains prohibited claims ---
    for route in published_routes:
        path = route["path"]
        content = content_sources.get(path)
        if not content:
            continue
        blocked_claims = content.get("blocked_claims", [])
        for section in content.get("required_sections", []):
            section_body = section.get("content", "")
            if not section_body:
                continue
            for claim in blocked_claims:
                if claim.lower() in section_body.lower():
                    fail(
                        f"Route '{path}' section '{section.get('name')}' "
                        f"contains prohibited claim: {claim}"
                    )

    # --- Check 6: /acquisition/ is not published outside the alpha plan ---
    acq_route = all_routes_map.get("/acquisition/")
    alpha_candidate_paths = {
        c["path"] for c in alpha_plan.get("candidate_routes", [])
    }
    if acq_route and acq_route.get("status") == "published":
        if "/acquisition/" not in alpha_candidate_paths:
            fail(
                "Route '/acquisition/' is published but not listed in "
                "public-alpha-plan.json candidate_routes — "
                "acquisition requires explicit approval before indexing"
            )

    # --- Check 7: no unpublished route has been generated ---
    output_dir = ROOT_DIR / "output"
    if output_dir.is_dir():
        for html_file in output_dir.rglob("index.html"):
            rel = html_file.relative_to(output_dir)
            if rel == Path("index.html"):
                generated_path = "/"
            else:
                generated_path = "/" + str(rel.parent) + "/"
            if generated_path not in published_paths:
                fail(
                    f"Generated output found for unpublished route "
                    f"'{generated_path}': {html_file.relative_to(ROOT_DIR)}"
                )

    if ERRORS:
        print(f"\n  {len(ERRORS)} error(s) found. Publication readiness check FAILED.")
        sys.exit(1)

    route_summary = (
        f"{len(published_routes)} published route(s)" if published_routes
        else "0 published routes (pre-publication state)"
    )
    print(
        f"  validate_publication_readiness PASSED — "
        f"{route_summary}, publication governance is intact"
    )


if __name__ == "__main__":
    main()
