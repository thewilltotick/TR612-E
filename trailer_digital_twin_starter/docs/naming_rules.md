# Component ID Rules

## Purpose
Stable IDs make it possible to connect diagrams, YAML config, logs, dashboards, and future live overlays.

## Rules
- Keep IDs stable once created
- Use upper snake case
- Prefix by category
- Do not encode temporary wiring details in the ID
- Do not rename IDs just because a component moves physically
- If hardware changes but the system role stays the same, prefer updating metadata instead of changing the ID

## Suggested prefixes
- `BAT_` battery
- `BUS_` busbar or distribution rail
- `BRK_` breaker
- `FUSE_` fuse
- `SW_` disconnect or switch
- `INV_` inverter or inverter charger
- `DCDC_` DC-DC converter
- `UPS_` UPS or ride-through module
- `PANEL_` AC/DC panel
- `SPD_` surge protection device
- `CAM_` camera
- `TEMP_` temperature sensor
- `RS232_` serial interface
- `RS485_` serial interface
- `SENS_` telemetry sensor definition

## Good examples
- `BAT_48V_A`
- `BUS_12V_CLEAN`
- `DCDC_48V_TO_12V_MAIN`
- `UPS_5V_PI`

## Bad examples
- `new_battery`
- `left-side-bus`
- `pi power v2 maybe`
