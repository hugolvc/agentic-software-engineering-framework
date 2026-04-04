#!/usr/bin/env python3
"""Validate example CR/IP JSON files against schemas/ (Phase P1).

Usage (from repository root):
  pip install -r scripts/requirements-validate.txt
  python3 scripts/validate_schemas.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    try:
        import jsonschema
        from jsonschema import Draft202012Validator
    except ImportError:
        print(
            "jsonschema is not installed. Run: pip install -r scripts/requirements-validate.txt",
            file=sys.stderr,
        )
        return 1

    examples = [
        (ROOT / "schemas/change_requirement.schema.json", ROOT / "examples/CR-001.example.json"),
        (ROOT / "schemas/implementation_plan.schema.json", ROOT / "examples/IP-001.example.json"),
    ]

    for schema_path, instance_path in examples:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        instance = json.loads(instance_path.read_text(encoding="utf-8"))
        Draft202012Validator(schema).validate(instance)
        print(f"OK  {instance_path.relative_to(ROOT)} validates against {schema_path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
