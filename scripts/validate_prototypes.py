#!/usr/bin/env python3
"""
SuperSXO Prototype Validator.

Validates all registered prototypes against sovereign governance rules.
Ensures no prototype generates public output, publishes routes, or creates root index.html.
"""

import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

PROTOTYPE_REGISTRY = ROOT_DIR / "data" / "prototype-registry.json"
ROUTES_FILE = ROOT_DIR / "data" / "routes.json"
COMPONENT_REGISTRY = ROOT_DIR / "data" / "component-registry.json"

ERRORS = []


def fail(msg: str) -> None:
    ERRORS.append(msg)
    print(f"  FAIL: {msg}")


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    print("validate_prototypes — SuperSXO Prototype Governance")

    for required in (PROTOTYPE_REGISTRY, ROUTES_FILE, COMPONENT_REGISTRY):
        if not required.exists():
            fail(f"Required file missing: {required.relative_to(ROOT_DIR)}")

    if ERRORS:
        print(f"\n  {len(ERRORS)} error(s). Prototype governance check FAILED.")
        sys.exit(1)

    registry = load_json(PROTOTYPE_REGISTRY)
    routes_data = load_json(ROUTES_FILE)
    components_data = load_json(COMPONENT_REGISTRY)

    route_paths = {r["path"] for r in routes_data.get("routes", [])}
    component_ids = {c["component_id"] for c in components_data.get("components", [])}

    prototypes = registry.get("prototypes", [])

    if not prototypes:
        fail("No prototypes found in data/prototype-registry.json")

    for proto in prototypes:
        proto_id = proto.get("prototype_id", "<unknown>")
        print(f"  Checking prototype: {proto_id}")

        # Verify route exists in routes.json
        route = proto.get("route")
        if route not in route_paths:
            fail(f"[{proto_id}] Route '{route}' not found in data/routes.json")

        # Verify public_output_allowed is false
        if proto.get("public_output_allowed") is not False:
            fail(f"[{proto_id}] public_output_allowed must be false")

        # Verify status is non_public_prototype
        if proto.get("status") != "non_public_prototype":
            fail(f"[{proto_id}] status must be 'non_public_prototype', got '{proto.get('status')}'")

        # Verify source_file exists
        source_file = proto.get("source_file", "")
        source_path = ROOT_DIR / source_file
        if not source_path.exists():
            fail(f"[{proto_id}] source_file '{source_file}' does not exist")

        # Verify source_file is inside templates/prototypes/
        prototypes_dir = (ROOT_DIR / "templates" / "prototypes").resolve()
        try:
            source_path.resolve().relative_to(prototypes_dir)
        except ValueError:
            fail(f"[{proto_id}] source_file '{source_file}' is not inside templates/prototypes/")

        # Verify no prototype source_file is root index.html
        if source_path.resolve() == (ROOT_DIR / "index.html").resolve():
            fail(f"[{proto_id}] source_file must not be root index.html")
        if source_path.name == "index.html":
            fail(f"[{proto_id}] source_file name must not be 'index.html'")

        # Verify allowed_components exist in component-registry.json
        allowed_components = proto.get("allowed_components", [])
        for comp in allowed_components:
            if comp not in component_ids:
                fail(f"[{proto_id}] allowed_component '{comp}' not found in data/component-registry.json")

        # Verify prohibited_behavior is present and non-empty
        prohibited = proto.get("prohibited_behavior", [])
        if not prohibited:
            fail(f"[{proto_id}] prohibited_behavior must be present and non-empty")

    # Verify home-control-plane.html contains the NON-PUBLIC PROTOTYPE marker
    home_proto = ROOT_DIR / "templates" / "prototypes" / "home-control-plane.html"
    if home_proto.exists():
        content = home_proto.read_text(encoding="utf-8")
        if "NON-PUBLIC PROTOTYPE" not in content:
            fail("templates/prototypes/home-control-plane.html is missing the 'NON-PUBLIC PROTOTYPE' marker")
    else:
        fail("templates/prototypes/home-control-plane.html does not exist")

    if ERRORS:
        print(f"\n  {len(ERRORS)} error(s) found. Prototype governance check FAILED.")
        sys.exit(1)

    print("  validate_prototypes PASSED — all prototype governance rules satisfied")


if __name__ == "__main__":
    main()
