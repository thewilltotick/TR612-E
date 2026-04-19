# Naming and generation rules

## Single source of truth
Use `data_model/system_graph.yaml` as the canonical system definition.

## Why this structure
You asked for the diagram and YAML to define each other instead of drifting apart.
This repo now treats the graph model as canonical and generates both:
- visual diagram
- component and connection tables

## Editing workflow
- Add or remove components in `system_graph.yaml`
- Add or remove links in `system_graph.yaml`
- Adjust `diagram_layout.positions` when you want the visual layout to change
- Regenerate the outputs

## Design intent
Each component has:
- `id`
- `label`
- `type`
- `domain`
- `location`

Each link has:
- `id`
- `from`
- `to`
- `kind`

For DC systems, positive and negative paths are intentionally modeled separately.
