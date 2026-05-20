#!/usr/bin/env python3
"""
SuperSXO Security Baseline Validator.

Validates data/security-baseline.json and data/technical-risk-register.json
against sovereign security governance rules.
"""

import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

SECURITY_BASELINE = ROOT_DIR / "data" / "security-baseline.json"
RISK_REGISTER = ROOT_DIR / "data" / "technical-risk-register.json"

REQUIRED_CONTROL_GROUPS = [
    "repository_secrets",
    "public_output",
    "javascript_policy",
    "third_party_policy",
    "dependency_policy",
    "workflow_policy",
    "headers_target",
    "forms_payments_tracking",
    "prototype_safety",
]

REQUIRED_CONTROL_FIELDS = [
    "control_id",
    "purpose",
    "prohibited_patterns",
    "required_checks",
    "escalation",
]

REQUIRED_RISK_FIELDS = [
    "risk_id",
    "category",
    "description",
    "severity",
    "prevention",
    "detection",
    "response",
    "blocks_publication",
]

ERRORS = []


def fail(msg: str) -> None:
    ERRORS.append(msg)
    print(f"  FAIL: {msg}")


def load_json(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_security_baseline(data: dict) -> None:
    controls = data.get("controls", [])
    if not controls:
        fail("No controls found in data/security-baseline.json")
        return

    found_ids = {c.get("control_id") for c in controls}

    for required_id in REQUIRED_CONTROL_GROUPS:
        if required_id not in found_ids:
            fail(f"Required control group missing: '{required_id}'")

    for control in controls:
        cid = control.get("control_id", "<unknown>")
        for field in REQUIRED_CONTROL_FIELDS:
            if field not in control:
                fail(f"Control '{cid}' missing required field: '{field}'")
            elif not control[field]:
                fail(f"Control '{cid}' field '{field}' must be non-empty")


def validate_risk_register(data: dict) -> None:
    risks = data.get("risks", [])
    if not risks:
        fail("No risks found in data/technical-risk-register.json")
        return

    for risk in risks:
        rid = risk.get("risk_id", "<unknown>")
        for field in REQUIRED_RISK_FIELDS:
            if field not in risk:
                fail(f"Risk '{rid}' missing required field: '{field}'")
            elif risk[field] == "" or risk[field] is None:
                fail(f"Risk '{rid}' field '{field}' must be non-empty")

        if risk.get("severity") == "high" and risk.get("blocks_publication") is not True:
            fail(
                f"Risk '{rid}' has severity 'high' but blocks_publication is not true"
            )


def main() -> None:
    print("validate_security_baseline — SuperSXO Security Governance")

    for path in (SECURITY_BASELINE, RISK_REGISTER):
        if not path.exists():
            fail(f"Required file missing: {path.relative_to(ROOT_DIR)}")

    if ERRORS:
        print(f"\n  {len(ERRORS)} error(s). Security baseline check FAILED.")
        sys.exit(1)

    baseline_data = load_json(SECURITY_BASELINE)
    risk_data = load_json(RISK_REGISTER)

    validate_security_baseline(baseline_data)
    validate_risk_register(risk_data)

    if ERRORS:
        print(f"\n  {len(ERRORS)} error(s) found. Security baseline check FAILED.")
        sys.exit(1)

    print("  validate_security_baseline PASSED — security governance controls are intact")


if __name__ == "__main__":
    main()
