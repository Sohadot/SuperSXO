#!/usr/bin/env python3
"""
Validate content source contracts against governance rules.

Checks:
- Every route in page-source-map.json exists in routes.json
- Every mapped source file exists on disk
- Every source file includes all required fields from content-model.json
- No source file introduces a route not registered in routes.json
- required_internal_links in each source point only to registered routes
- source_status is an allowed value from content-model.json
- No source has source_status 'approved_for_build' while its route status is not 'published'
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def load_json(path: Path):
    with open(path) as f:
        return json.load(f)


def load_routes_map(routes_path: Path) -> dict:
    data = load_json(routes_path)
    if isinstance(data, list):
        routes = data
    elif isinstance(data, dict) and "routes" in data:
        routes = data["routes"]
    else:
        raise ValueError("routes.json must be a list or dict with 'routes' key")
    return {r["path"]: r for r in routes if "path" in r}


def validate_content_sources() -> bool:
    errors = []

    routes_path    = REPO_ROOT / "data" / "routes.json"
    model_path     = REPO_ROOT / "data" / "content-model.json"
    src_map_path   = REPO_ROOT / "data" / "page-source-map.json"

    # Load governance files
    try:
        routes_map = load_routes_map(routes_path)
    except (json.JSONDecodeError, ValueError, FileNotFoundError) as e:
        print(f"  FAIL  Cannot load routes.json: {e}")
        return False

    try:
        content_model = load_json(model_path)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"  FAIL  Cannot load content-model.json: {e}")
        return False

    try:
        src_map_data = load_json(src_map_path)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"  FAIL  Cannot load page-source-map.json: {e}")
        return False

    required_fields  = content_model.get("required_fields", [])
    allowed_statuses = set(content_model.get("allowed_source_status", []))
    mappings         = src_map_data.get("mappings", {})

    if not mappings:
        print("  FAIL  page-source-map.json: 'mappings' is empty or missing")
        return False

    registered_paths = set(routes_map.keys())

    for route_path, source_file in mappings.items():

        # Mapped route must exist in routes.json
        if route_path not in registered_paths:
            errors.append(
                f"  FAIL  page-source-map.json maps '{route_path}' "
                f"which is not registered in routes.json"
            )
            continue

        source_path = REPO_ROOT / source_file

        # Source file must exist
        if not source_path.exists():
            errors.append(f"  FAIL  Source file missing: {source_file}")
            continue

        # Load the source file
        try:
            source = load_json(source_path)
        except json.JSONDecodeError as e:
            errors.append(f"  FAIL  Cannot parse {source_file}: {e}")
            continue

        print(f"  OK    {source_file}")

        # Required fields check
        for field in required_fields:
            if field not in source:
                errors.append(
                    f"  FAIL  {source_file}: missing required field '{field}'"
                )

        # route field must match the map key
        if source.get("route") != route_path:
            errors.append(
                f"  FAIL  {source_file}: route field '{source.get('route')}' "
                f"does not match map key '{route_path}'"
            )

        # source_status must be an allowed value
        status = source.get("source_status", "")
        if status not in allowed_statuses:
            errors.append(
                f"  FAIL  {source_file}: source_status '{status}' is not "
                f"in allowed values: {sorted(allowed_statuses)}"
            )

        # approved_for_build requires route status 'published'
        if status == "approved_for_build":
            route_status = routes_map.get(route_path, {}).get("status", "")
            if route_status != "published":
                errors.append(
                    f"  FAIL  {source_file}: source_status is 'approved_for_build' "
                    f"but route status is '{route_status}' "
                    f"(must be 'published')"
                )

        # required_internal_links must point only to registered routes
        for link in source.get("required_internal_links", []):
            if link not in registered_paths:
                errors.append(
                    f"  FAIL  {source_file}: required_internal_links entry "
                    f"'{link}' is not a registered route"
                )

    if errors:
        for e in errors:
            print(e)
        return False

    return True


def main() -> None:
    print("=== validate_content_sources: checking content/pages/*.json ===")
    passed = validate_content_sources()
    if passed:
        print("validate_content_sources: PASSED")
    else:
        print("validate_content_sources: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
