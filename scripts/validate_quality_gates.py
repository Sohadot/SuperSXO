#!/usr/bin/env python3
"""Validate the quality gates definition in data/quality-gates.json."""

import json
import sys
from pathlib import Path

REQUIRED_GATES = [
    "route_gate",
    "seo_gate",
    "content_gate",
    "link_gate",
    "technical_gate",
    "performance_gate",
    "accessibility_gate",
    "monetization_gate",
    "security_gate",
]

REQUIRED_GATE_FIELDS = [
    "purpose",
    "required_checks",
    "failure_condition",
    "blocks_publication",
]


def validate_quality_gates(gates_path: Path) -> bool:
    errors = []

    try:
        with open(gates_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  FAIL  Cannot parse quality-gates.json: {e}")
        return False

    gates = data.get("gates", {})
    if not gates:
        print("  FAIL  quality-gates.json: 'gates' object is empty or missing")
        return False

    for gate_name in REQUIRED_GATES:
        if gate_name not in gates:
            errors.append(f"  FAIL  Required gate missing: '{gate_name}'")
            continue

        gate = gates[gate_name]
        print(f"  OK    Gate present: '{gate_name}'")

        for field in REQUIRED_GATE_FIELDS:
            if field not in gate:
                errors.append(
                    f"  FAIL  Gate '{gate_name}': missing required field '{field}'"
                )

        if gate.get("blocks_publication") is not True:
            errors.append(
                f"  FAIL  Gate '{gate_name}': blocks_publication must be true. "
                f"Found: {gate.get('blocks_publication')!r}"
            )

        checks = gate.get("required_checks", [])
        if not isinstance(checks, list) or not checks:
            errors.append(
                f"  FAIL  Gate '{gate_name}': required_checks must be a non-empty list"
            )

    if errors:
        for e in errors:
            print(e)
        return False

    return True


def main() -> None:
    gates_path = Path(__file__).parent.parent / "data" / "quality-gates.json"
    print("=== validate_quality_gates: checking data/quality-gates.json ===")
    passed = validate_quality_gates(gates_path)
    if passed:
        print("validate_quality_gates: PASSED")
    else:
        print("validate_quality_gates: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
