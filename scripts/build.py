#!/usr/bin/env python3
"""
SuperSXO static site builder.

Loads data/routes.json and identifies routes with status exactly 'published'.
If no routes are published, exits cleanly with no output generated.

Only routes registered in data/routes.json with status 'published'
may ever be built. All other routes are refused.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def load_routes(routes_path: Path) -> list:
    with open(routes_path) as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "routes" in data:
        return data["routes"]
    raise ValueError("routes.json must be a list or a dict with a 'routes' key")


def main() -> None:
    routes_path = REPO_ROOT / "data" / "routes.json"

    if not routes_path.exists():
        print("ERROR: data/routes.json not found. Cannot build.")
        sys.exit(1)

    try:
        routes = load_routes(routes_path)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"ERROR: Cannot load data/routes.json: {e}")
        sys.exit(1)

    registered_paths = {r.get("path") for r in routes if r.get("path")}
    published = [r for r in routes if r.get("status") == "published"]

    if not published:
        print("No published routes found. Build skipped safely.")
        return

    print(f"{len(published)} published route(s) found. Starting build.")

    output_dir = REPO_ROOT / "output"
    output_dir.mkdir(exist_ok=True)

    built = 0
    for route in published:
        path = route.get("path", "")
        if path not in registered_paths:
            print(f"  BLOCKED: '{path}' is not in the approved route registry.")
            sys.exit(1)
        # Route is registered and published: build it.
        # Full HTML generation will be implemented when the first route is approved.
        print(f"  PLANNED BUILD: {path} (renderer not yet implemented)")
        built += 1

    print(f"Build complete. {built} route(s) processed.")


if __name__ == "__main__":
    main()
