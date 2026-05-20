#!/usr/bin/env python3
"""Validate the route registry in data/routes.json."""

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "path",
    "title",
    "role",
    "purpose",
    "status",
    "indexable",
    "canonical",
    "ux_layer",
    "required_internal_links",
    "allowed_cta",
    "claim_level",
    "monetization_allowed",
    "publication_rule",
]

CANONICAL_DOMAIN = "supersxo.com"


def load_routes(routes_path: Path) -> list:
    with open(routes_path) as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "routes" in data:
        return data["routes"]
    raise ValueError("routes.json must be a list or a dict with a 'routes' key")


def validate_routes(routes_path: Path) -> bool:
    errors = []

    try:
        routes = load_routes(routes_path)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"  FAIL  Cannot load routes.json: {e}")
        return False

    if not routes:
        print("  FAIL  routes.json: route list is empty")
        return False

    # Collect all registered paths first
    registered_paths = {r.get("path") for r in routes if r.get("path")}

    # Check for duplicate paths
    seen: set = set()
    for route in routes:
        path = route.get("path")
        if path:
            if path in seen:
                errors.append(f"  FAIL  Duplicate path: '{path}'")
            seen.add(path)

    # Validate each route
    for route in routes:
        label = route.get("path", "[no path]")

        for field in REQUIRED_FIELDS:
            if field not in route:
                errors.append(f"  FAIL  Route '{label}': missing required field '{field}'")

        path = route.get("path", "")
        if not path.startswith("/"):
            errors.append(f"  FAIL  Route '{label}': path must start with '/'")

        canonical = route.get("canonical", "")
        if canonical and CANONICAL_DOMAIN not in canonical:
            errors.append(
                f"  FAIL  Route '{label}': canonical '{canonical}' "
                f"must contain '{CANONICAL_DOMAIN}'"
            )

        for link in route.get("required_internal_links", []):
            if link not in registered_paths:
                errors.append(
                    f"  FAIL  Route '{label}': required_internal_links entry "
                    f"'{link}' is not a registered route"
                )

    if errors:
        for e in errors:
            print(e)
        return False

    print(f"  OK    {len(routes)} routes validated")
    return True


def main() -> None:
    routes_path = Path(__file__).parent.parent / "data" / "routes.json"
    print("=== validate_routes: checking data/routes.json ===")
    passed = validate_routes(routes_path)
    if passed:
        print("validate_routes: PASSED")
    else:
        print("validate_routes: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
