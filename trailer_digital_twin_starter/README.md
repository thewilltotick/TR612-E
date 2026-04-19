# Trailer digital twin starter v2

This version fixes the core issue from v1:

- `data_model/system_graph.yaml` is the **single source of truth**
- `components.yaml` and `connections.yaml` are derived views
- `diagrams/01_overview.drawio` is generated from `system_graph.yaml`

Do not hand-edit the generated draw.io file if you want reproducibility.
Instead:
1. edit `system_graph.yaml`
2. run `python scripts/generate_drawio.py`
3. optionally run `python scripts/validate_graph.py`

## Model rules
- Every component must appear in `system_graph.yaml.components`
- Every link must appear in `system_graph.yaml.links`
- Every positive and negative power path should be explicit as separate links
- Layout is stored in `system_graph.yaml.diagram_layout.positions`
- Generated files:
  - `data_model/components.yaml`
  - `data_model/connections.yaml`
  - `diagrams/01_overview.drawio`

## Link kinds
- `power_pos`
- `power_neg`
- `ac_line`
- `data_power`
- `telemetry`

## Current approximations still to review
- exact protection ratings
- exact PoE / Starlink path
- exact negative-return strategy for all subloads
- whether some branches need separate fuses instead of shared breakers
