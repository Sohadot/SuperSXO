#!/usr/bin/env python3
"""
SuperSXO Sovereign Quality Gate.

Runs all validators in sequence.
Fails immediately if any validator fails.
Prints SOVEREIGN QUALITY GATE PASSED only when all checks succeed.
"""

import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent

VALIDATORS = [
    ("validate_json",            SCRIPTS_DIR / "validate_json.py"),
    ("validate_routes",          SCRIPTS_DIR / "validate_routes.py"),
    ("validate_navigation",      SCRIPTS_DIR / "validate_navigation.py"),
    ("validate_domain_cluster",  SCRIPTS_DIR / "validate_domain_cluster.py"),
    ("validate_quality_gates",   SCRIPTS_DIR / "validate_quality_gates.py"),
    ("validate_content_sources", SCRIPTS_DIR / "validate_content_sources.py"),
    ("validate_visual_system",   SCRIPTS_DIR / "validate_visual_system.py"),
    ("validate_prototypes",         SCRIPTS_DIR / "validate_prototypes.py"),
    ("validate_security_baseline",    SCRIPTS_DIR / "validate_security_baseline.py"),
    ("validate_repository_hygiene",   SCRIPTS_DIR / "validate_repository_hygiene.py"),
    ("validate_publication_readiness",SCRIPTS_DIR / "validate_publication_readiness.py"),
    ("validate_build_boundaries",     SCRIPTS_DIR / "validate_build_boundaries.py"),
    ("validate_spatial_interface",    SCRIPTS_DIR / "validate_spatial_interface.py"),
    ("validate_control_interface",    SCRIPTS_DIR / "validate_control_interface.py"),
    ("validate_deploy_assets",        SCRIPTS_DIR / "validate_deploy_assets.py"),
]

SEP = "=" * 60


def run_validator(name: str, script: Path) -> bool:
    print(f"\n{SEP}")
    result = subprocess.run([sys.executable, str(script)])
    if result.returncode != 0:
        print(f"\nSOVEREIGN QUALITY GATE FAILED at: {name}")
        return False
    return True


def main() -> None:
    print(SEP)
    print("SOVEREIGN QUALITY GATE — SuperSXO.com")
    print(SEP)

    for name, script in VALIDATORS:
        if not run_validator(name, script):
            sys.exit(1)

    print(f"\n{SEP}")
    print("SOVEREIGN QUALITY GATE PASSED")
    print(SEP)


if __name__ == "__main__":
    main()
