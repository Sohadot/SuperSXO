#!/usr/bin/env python3
"""
validate_visual_system.py
SuperSXO — Visual System Governance Validator

Validates:
- data/component-registry.json structure and required components
- data/interface-patterns.json approved/prohibited pattern integrity
- data/visual-tokens.json required token groups
- static/css/tokens.css and main.css exist
- Every component's allowed_routes references registered routes or "*"
- No prohibited pattern is marked approved
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "data"
CSS_DIR = REPO_ROOT / "static" / "css"

COMPONENT_REGISTRY = DATA_DIR / "component-registry.json"
INTERFACE_PATTERNS = DATA_DIR / "interface-patterns.json"
VISUAL_TOKENS = DATA_DIR / "visual-tokens.json"
ROUTES_FILE = DATA_DIR / "routes.json"

REQUIRED_COMPONENTS = {
    "site_header", "site_footer", "route_context_panel",
    "search_to_action_map", "spatial_panel", "diagnostic_grid",
    "trust_plane", "signal_path", "allowed_cta_block",
    "related_routes_cluster",
}

COMPONENT_REQUIRED_FIELDS = {
    "component_id", "role", "ux_layer", "allowed_routes",
    "required_data_sources", "accessibility_requirements",
    "prohibited_behavior", "publication_risk",
}

REQUIRED_PROHIBITED_PATTERNS = {
    "gaming_hud", "neon_cyberpunk_excess", "metaverse_avatar_scene",
    "canvas_only_content", "animation_required_navigation",
    "hidden_text_for_seo", "decorative_3d_without_function",
    "intrusive_popup", "cheap_sales_banner",
}

REQUIRED_TOKEN_GROUPS = {
    "surfaces", "ink", "signal_colors", "trust_colors",
    "action_colors", "borders", "spacing", "radius", "depth",
    "motion", "focus",
}


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_registered_paths(routes_data: dict) -> set:
    return {r["path"] for r in routes_data.get("routes", [])}


def validate_component_registry(errors: list) -> dict:
    print(f"  Checking {COMPONENT_REGISTRY.name} ...")
    data = load_json(COMPONENT_REGISTRY)
    components = data.get("components", [])
    found_ids = set()

    for comp in components:
        cid = comp.get("component_id", "<missing>")
        found_ids.add(cid)
        missing_fields = COMPONENT_REQUIRED_FIELDS - set(comp.keys())
        if missing_fields:
            errors.append(
                f"Component '{cid}' missing required fields: {sorted(missing_fields)}"
            )

    missing_components = REQUIRED_COMPONENTS - found_ids
    if missing_components:
        errors.append(
            f"Missing required components: {sorted(missing_components)}"
        )

    print(f"    Found {len(components)} components, {len(found_ids)} unique IDs.")
    return data


def validate_allowed_routes(components: list, registered_paths: set, errors: list) -> None:
    print("  Checking allowed_routes against data/routes.json ...")
    for comp in components:
        cid = comp.get("component_id", "<unknown>")
        allowed = comp.get("allowed_routes", [])
        if allowed == "*":
            continue
        if isinstance(allowed, list):
            for route in allowed:
                if route not in registered_paths:
                    errors.append(
                        f"Component '{cid}' references unregistered route '{route}'"
                    )
        else:
            errors.append(
                f"Component '{cid}' has invalid allowed_routes type: {type(allowed).__name__}"
            )


def validate_interface_patterns(errors: list) -> None:
    print(f"  Checking {INTERFACE_PATTERNS.name} ...")
    data = load_json(INTERFACE_PATTERNS)
    prohibited = data.get("prohibited_patterns", [])
    found_prohibited_ids = set()

    for p in prohibited:
        pid = p.get("pattern_id", "<missing>")
        found_prohibited_ids.add(pid)
        if p.get("status", "") != "prohibited":
            errors.append(
                f"Prohibited pattern '{pid}' has status '{p.get('status')}' — must be 'prohibited'"
            )

    missing_prohibited = REQUIRED_PROHIBITED_PATTERNS - found_prohibited_ids
    if missing_prohibited:
        errors.append(
            f"Missing required prohibited patterns: {sorted(missing_prohibited)}"
        )

    approved = data.get("approved_patterns", [])
    approved_ids = {p.get("pattern_id") for p in approved}
    collision = approved_ids & found_prohibited_ids
    if collision:
        errors.append(
            f"Pattern IDs appear in both approved and prohibited lists: {sorted(collision)}"
        )

    print(
        f"    Found {len(approved)} approved patterns, "
        f"{len(prohibited)} prohibited patterns."
    )


def validate_visual_tokens(errors: list) -> None:
    print(f"  Checking {VISUAL_TOKENS.name} ...")
    data = load_json(VISUAL_TOKENS)
    groups = data.get("token_groups", {})
    missing_groups = REQUIRED_TOKEN_GROUPS - set(groups.keys())
    if missing_groups:
        errors.append(
            f"Missing required token groups: {sorted(missing_groups)}"
        )
    for group_name, group_data in groups.items():
        for field in ("purpose", "allowed_use", "prohibited_use"):
            if field not in group_data:
                errors.append(f"Token group '{group_name}' missing '{field}' field")
    print(f"    Found {len(groups)} token groups.")


def validate_css_files(errors: list) -> None:
    print("  Checking static/css files exist ...")
    for css_file in [CSS_DIR / "tokens.css", CSS_DIR / "main.css"]:
        if not css_file.exists():
            errors.append(f"Required CSS file missing: {css_file.relative_to(REPO_ROOT)}")
        else:
            print(f"    OK: {css_file.name}")


def main() -> None:
    print("validate_visual_system — SuperSXO Visual System Governance")
    errors: list = []

    for path in [COMPONENT_REGISTRY, INTERFACE_PATTERNS, VISUAL_TOKENS, ROUTES_FILE]:
        if not path.exists():
            print(f"FAIL: Required file not found: {path.relative_to(REPO_ROOT)}")
            sys.exit(1)

    routes_data = load_json(ROUTES_FILE)
    registered_paths = get_registered_paths(routes_data)

    registry_data = validate_component_registry(errors)
    components = registry_data.get("components", [])
    validate_allowed_routes(components, registered_paths, errors)
    validate_interface_patterns(errors)
    validate_visual_tokens(errors)
    validate_css_files(errors)

    if errors:
        print(f"\nFAIL: {len(errors)} visual system governance violation(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("\nOK: validate_visual_system passed — visual system governance is intact.")


if __name__ == "__main__":
    main()
