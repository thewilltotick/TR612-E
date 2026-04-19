# Power Flow Overview

This file is intentionally text-first so it stays easy to diff in Git.

## High-level power path

```mermaid
graph TD
    PV[PV Array 2S2P] --> INV[Inverter Charger AIO]
    SHORE[Shore AC In] --> INV
    BATA[Battery A 48V] --> BUS48[48V Main Bus]
    BATB[Battery B 48V] --> BUS48
    BUS48 --> INV
    BUS48 --> DCDC48[48V to 12V Converter]
    DCDC48 --> BUS12C[12V Clean Bus]
    DCDC48 --> BUS12D[12V Dirty Bus]
    BUS12C --> UPS12[12V Critical UPS]
    UPS12 --> DCDC5[12V to 5V Converter]
    DCDC5 --> UPS5[5V Pi UPS]
    UPS5 --> BUS5[5V Critical Bus]
    BUS5 --> RPI[Raspberry Pi 5]
    BUS5 --> RELAY[5V Relay Board]
    BUS12C --> POE[PoE Switch]
    POE --> STARLINK[Starlink Mini]
    POE --> CAMS[PoE Cameras]
    INV --> ACOUT[AC Distribution Panel]
```

## Intentional modeling choices
- `BUS_12V_CLEAN` and `BUS_12V_DIRTY` are modeled separately now so you can enforce cleaner power paths later.
- The Raspberry Pi is modeled behind both a 12V critical UPS stage and a 5V UPS stage because you have emphasized uptime and power stability.
- AC, PV, and telemetry are all present in the same project, but can be broken into separate diagrams once the layout stabilizes.

## Suggested next split
Create separate diagram files for:
- `01_overview.drawio`
- `02_48v_power.drawio`
- `03_12v_distribution.drawio`
- `04_5v_critical.drawio`
- `05_ac_distribution.drawio`
- `06_telemetry.drawio`
