# Trailer Electrical Digital Twin Starter

This starter project is organized so your wiring diagrams can be version controlled now and connected to live telemetry later.

## Goals
- Keep electrical diagrams diff-friendly and organized
- Assign stable `component_id` values to every major component
- Map sensors and telemetry to those same IDs
- Make it easy to build a future live system map from Raspberry Pi data

## Folder layout
- `diagrams/`: draw.io diagrams with `component_id` tags on shapes
- `data_model/`: canonical component and connection definitions
- `telemetry/`: sensor definitions and telemetry/component mappings
- `docs/`: design notes and naming rules
- `scripts/`: helper scripts for validation and future rendering

## Recommended workflow
1. Edit YAML files first when adding or renaming hardware
2. Update the draw.io diagrams to match the YAML IDs
3. Commit diagram and YAML changes together
4. Keep one commit per wiring/layout change where possible

## Current scope
This first pass includes:
- A starter 48V/12V/5V/AC architecture
- Core trailer power components
- Placeholder telemetry mappings for battery, inverter, temperature, network, and PoE power
- A starter draw.io system diagram

## Next review items
You should check these carefully:
- Component names and boundaries
- Which loads belong on clean vs dirty 12V
- Whether the Pi should be modeled on 5V UPS only or as part of a wider critical-power subtree
- Exact breaker/fuse placement
- Whether you want separate diagrams for solar, alternator charging, AC shore/generator input, and networking
