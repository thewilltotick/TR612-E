
import yaml, sys, pathlib

root = pathlib.Path(__file__).resolve().parents[1]
graph = yaml.safe_load((root / "data_model" / "system_graph.yaml").read_text())
components = {c["id"] for c in graph["components"]}
errors = []

for link in graph["links"]:
    if link["from"] not in components:
        errors.append(f'{link["id"]}: missing source component {link["from"]}')
    if link["to"] not in components:
        errors.append(f'{link["id"]}: missing target component {link["to"]}')

link_ids = [l["id"] for l in graph["links"]]
if len(link_ids) != len(set(link_ids)):
    errors.append("Duplicate link IDs found")

comp_ids = [c["id"] for c in graph["components"]]
if len(comp_ids) != len(set(comp_ids)):
    errors.append("Duplicate component IDs found")

positions = graph.get("diagram_layout", {}).get("positions", {})
for cid in components:
    if cid not in positions:
        errors.append(f'Missing diagram position for {cid}')

if errors:
    print("Validation failed:")
    for e in errors:
        print("-", e)
    sys.exit(1)

print(f"Validation passed: {len(components)} components, {len(graph['links'])} links.")
