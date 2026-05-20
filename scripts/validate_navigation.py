#!/usr/bin/env python3
"""Validate that all navigation links resolve to registered routes."""

import json
import sys
from pathlib import Path


def load_registered_paths(routes_path: Path) -> set:
    with open(routes_path) as f:
        data = json.load(f)
    if isinstance(data, list):
        routes = data
    elif isinstance(data, dict) and "routes" in data:
        routes = data["routes"]
    else:
        raise ValueError("routes.json must be a list or a dict with a 'routes' key")
    return {r["path"] for r in routes if "path" in r}


def extract_nav_links(nav_data: dict) -> list:
    """Return [(section_name, path), ...] for all internal links in navigation.json."""
    links = []
    nav = nav_data.get("navigation", nav_data)
    for section_name, section in nav.items():
        if not isinstance(section, list):
            continue
        for item in section:
            if isinstance(item, dict) and "path" in item:
                links.append((section_name, item["path"]))
    return links


def validate_navigation(nav_path: Path, routes_path: Path) -> bool:
    errors = []

    try:
        with open(nav_path) as f:
            nav_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  FAIL  Cannot parse navigation.json: {e}")
        return False

    try:
        registered_paths = load_registered_paths(routes_path)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"  FAIL  Cannot load routes.json: {e}")
        return False

    links = extract_nav_links(nav_data)
    if not links:
        print("  WARN  No navigation links found in navigation.json")

    for section, path in links:
        if path.startswith("/"):
            if path not in registered_paths:
                errors.append(
                    f"  FAIL  navigation[{section}] links to "
                    f"unregistered route: '{path}'"
                )
            else:
                print(f"  OK    navigation[{section}] -> '{path}'")

    if errors:
        for e in errors:
            print(e)
        return False

    return True


def main() -> None:
    base = Path(__file__).parent.parent / "data"
    print("=== validate_navigation: checking data/navigation.json ===")
    passed = validate_navigation(base / "navigation.json", base / "routes.json")
    if passed:
        print("validate_navigation: PASSED")
    else:
        print("validate_navigation: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
