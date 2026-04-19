#!/usr/bin/env python3
"""Simple validation helper for component IDs across project YAML files."""
from __future__ import annotations

from pathlib import Path
import re
import sys
import yaml

ID_PATTERN = re.compile(r"^[A-Z0-9_]+$")


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    components = load_yaml(root / "data_model" / "components.yaml")["components"]
    connections = load_yaml(root / "data_model" / "connections.yaml")["connections"]
    mappings = load_yaml(root / "telemetry" / "mappings.yaml")["mappings"]

    component_ids = {c["id"] for c in components}
    errors: list[str] = []

    for cid in sorted(component_ids):
        if not ID_PATTERN.match(cid):
            errors.append(f"Invalid component ID format: {cid}")

    for conn in connections:
        for key in ("from", "to"):
            cid = conn[key]
            if cid not in component_ids:
                errors.append(f"Connection references unknown component '{cid}'")
        for via in conn.get("via", []):
            if via not in component_ids:
                errors.append(f"Connection via references unknown component '{via}'")

    for mapping in mappings:
        cid = mapping["component_id"]
        if cid not in component_ids:
            errors.append(f"Telemetry mapping references unknown component '{cid}'")

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Validation passed: {len(component_ids)} components checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
