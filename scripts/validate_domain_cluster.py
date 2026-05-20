#!/usr/bin/env python3
"""Validate the domain cluster definition in data/domain-cluster.json."""

import json
import sys
from pathlib import Path

REQUIRED_DOMAINS = {
    "supersxo.com",
    "sxosolution.com",
    "supersxo.info",
    "sxosolution.info",
    "supersxo.link",
    "sxosolution.link",
}

CANONICAL_ROLES = {"primary_authority", "canonical", "canonical_authority"}
INFO_ROLES = {"informational_routing", "solution_explanation_routing", "defensive"}
LINK_ROLES = {"campaign_routing", "action_routing", "routing_only"}


def validate_domain_cluster(cluster_path: Path) -> bool:
    errors = []

    try:
        with open(cluster_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"  FAIL  Cannot parse domain-cluster.json: {e}")
        return False

    domains = data.get("domains", [])
    if not domains:
        print("  FAIL  domain-cluster.json: 'domains' list is empty or missing")
        return False

    found: dict = {d.get("domain", "").lower(): d for d in domains}

    # Presence check
    for required in sorted(REQUIRED_DOMAINS):
        if required not in found:
            errors.append(f"  FAIL  Required domain missing: '{required}'")
        else:
            print(f"  OK    Domain present: '{required}'")

    # SuperSXO.com must have canonical authority
    supersxo = found.get("supersxo.com", {})
    if (
        supersxo.get("role") not in CANONICAL_ROLES
        and supersxo.get("authority_level") not in CANONICAL_ROLES
    ):
        errors.append(
            f"  FAIL  supersxo.com must have a canonical authority role. "
            f"Found role='{supersxo.get('role')}', "
            f"authority_level='{supersxo.get('authority_level')}'"
        )

    # .info domains must be informational/defensive
    for domain, entry in found.items():
        if domain.endswith(".info") and entry.get("role") not in INFO_ROLES:
            errors.append(
                f"  FAIL  {domain}: .info domain must have an informational or "
                f"defensive routing role. Found role='{entry.get('role')}'"
            )

    # .link domains must be campaign/action routing
    for domain, entry in found.items():
        if domain.endswith(".link") and entry.get("role") not in LINK_ROLES:
            errors.append(
                f"  FAIL  {domain}: .link domain must have a campaign or action "
                f"routing role. Found role='{entry.get('role')}'"
            )

    if errors:
        for e in errors:
            print(e)
        return False

    return True


def main() -> None:
    cluster_path = Path(__file__).parent.parent / "data" / "domain-cluster.json"
    print("=== validate_domain_cluster: checking data/domain-cluster.json ===")
    passed = validate_domain_cluster(cluster_path)
    if passed:
        print("validate_domain_cluster: PASSED")
    else:
        print("validate_domain_cluster: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
