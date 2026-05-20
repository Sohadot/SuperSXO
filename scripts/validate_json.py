#!/usr/bin/env python3
"""Validate that every file in data/*.json can be parsed as valid JSON."""

import json
import sys
from pathlib import Path


def validate_json_files(data_dir: Path) -> bool:
    json_files = sorted(data_dir.glob("*.json"))
    if not json_files:
        print(f"  FAIL  No JSON files found in {data_dir}")
        return False

    all_passed = True
    for path in json_files:
        try:
            with open(path) as f:
                json.load(f)
            print(f"  OK    {path.name}")
        except json.JSONDecodeError as e:
            print(f"  FAIL  {path.name}: {e}")
            all_passed = False

    return all_passed


def main() -> None:
    data_dir = Path(__file__).parent.parent / "data"
    print("=== validate_json: checking data/*.json ===")
    if not data_dir.exists():
        print(f"  FAIL  data/ directory not found at {data_dir}")
        sys.exit(1)
    passed = validate_json_files(data_dir)
    if passed:
        print("validate_json: PASSED")
    else:
        print("validate_json: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
