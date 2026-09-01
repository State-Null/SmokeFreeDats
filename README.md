# 💨 SmokeFreeDats & Performance Pack

A modular, zero-lag performance DAT collection for Final Fantasy XI via **[XIPivot](https://github.com/Darkdoom/XIPivot)**.

This repository is split into two modular packs:
1. 🌆 **`zones`**: Town & port 3D chimney/boiler smoke removal across 9 major hubs.
2. 🔮 **`objects`**: Particle glow removal for all **8 Elemental Crystal Fetters** and **Home Point Crystals**.

---

## 🚀 Quick Install (XIPivot)

Download the repository and place the `zones` and/or `objects` folders directly into your XIPivot `DATs` directory:

```text
Windower4/addons/XIPivot/data/DATs/
├── zones/
│   ├── ROM/1/...
│   └── ROM9/0/...
└── objects/
    ├── ROM/3/...
    └── ROM/259/...
```

### Enable in XIPivot
In-game, run the console commands:
```text
//pivot add zones
//pivot add objects
```

To make them permanent across sessions, add them to `Windower4/addons/XIPivot/data/settings.xml`:
```xml
<overlays>zones,objects,XI-View</overlays>
```

---

## 🌆 1. Zones Pack (`zones/`)

Eliminates laggy 3D **chimney smoke, blast furnace plumes, dock boiler exhaust, and residential smog** while keeping ground collision, weather skyboxes, and door coordinates 100% vanilla.

| City / Zone | DAT Path | Removed Smoke Emitters | Status |
|---|---|---|---|
| **Mhaura** | `ROM/1/44.DAT` | Harbor boiler steam, dock haze, all chimney smoke | ✅ Verified |
| **Western Adoulin** | `ROM9/0/3.DAT` | Hearth smog, residential chimneys, bridge smog | ✅ Verified |
| **Upper Jeuno** | `ROM/1/40.DAT` | Rooftop residential chimney smoke (35.8 KB) | ✅ Verified |
| **Bastok Mines** | `ROM/1/30.DAT` | Industrial blast furnace smoke (21.2 KB) | ✅ Verified |
| **Bastok Markets** | `ROM/1/31.DAT` | District-wide residential chimney smoke (44.3 KB) | ✅ Verified |
| **Port Bastok** | `ROM/1/32.DAT` | Harbor boiler exhaust plumes & dock smoke (39.8 KB) | ✅ Verified |
| **Windurst Woods** | `ROM/1/34.DAT` | Residential treehouse chimney smoke (43.4 KB) | ✅ Verified |
| **Windurst Waters** | `ROM/1/35.DAT` | Tarutaru residential chimney smoke (44.7 KB) | ✅ Verified |
| **Port Windurst** | `ROM/1/37.DAT` | Harbor dock boiler smoke (37.5 KB) | ✅ Verified |

---

## 🔮 2. Objects Pack (`objects/`)

Silences heavy rotating alpha-transparent particle glows on interactive objects and battle summons.

### A. All 8 Elemental Crystal Fetters & Gyres
*Silences spinning particle halos on Crystal Fetters across Sortie, Odyssey (Agon Halos), Lady Lilith, Geas Fete, and Provenance Watcher.*

| Element | DAT Path | What Was Silenced |
|---|---|---|
| **Fire Fetter** | `ROM/259/73.DAT` | 3D Rotating elemental glow flare |
| **Ice Fetter** | `ROM/259/74.DAT` | 3D Rotating elemental glow flare |
| **Wind Fetter** | `ROM/259/75.DAT` | 3D Rotating elemental glow flare |
| **Earth Fetter** | `ROM/259/76.DAT` | 3D Rotating elemental glow flare |
| **Lightning Fetter** | `ROM/259/77.DAT` | 3D Rotating elemental glow flare |
| **Water Fetter** | `ROM/259/78.DAT` | 3D Rotating elemental glow flare |
| **Light Fetter** | `ROM/259/79.DAT` | 3D Rotating elemental glow flare |
| **Dark Fetter** | `ROM/259/80.DAT` | 3D Rotating elemental glow flare |

### B. Home Point Crystals
*Silences the rotating crystal particle glow around all Home Points.*

| Object | DAT Path | What Was Silenced |
|---|---|---|
| **Home Point Crystal** | `ROM/3/25.DAT` | Rotating crystal particle aura |
