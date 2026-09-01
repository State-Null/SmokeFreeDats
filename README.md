# 💨 SmokeFreeDats & Performance Pack

A modular, zero-lag performance DAT collection for Final Fantasy XI via **[XIPivot](https://github.com/Darkdoom/XIPivot)**.

This repository is organized into two independent packs:
1. 🌆 **`zones`**: Town & port smoke and mist removal across **11 major cities and hubs** using native engine Auto-Run emitter toggles.
2. 🔮 **`objects`**: Particle glow removal for all **8 Elemental Crystal Fetters & Gyres** and **Home Point Crystals**.

---

## 🚀 Quick Install (XIPivot)

1. Download or clone this repository.
2. Place the `zones` and/or `objects` folders directly into your XIPivot `DATs` directory:

```text
Windower4/addons/XIPivot/data/DATs/
├── zones/
│   ├── ROM/1/...
│   ├── ROM3/0/...
│   └── ROM9/0/...
└── objects/
    ├── ROM/3/...
    └── ROM/259/...
```

### Enable in XIPivot
In your Windower console in-game, run:
```text
//pivot add zones
//pivot add objects
```

To make them load automatically on every startup, add them to `Windower4/addons/XIPivot/data/settings.xml`:
```xml
<overlays>zones,objects,XI-View</overlays>
```

---

## 🌆 1. Zones Pack (`zones/`)

*All town smoke and mist emitters are disabled natively at the engine level (using Aamace's 1-bit Auto-Run toggle). Every DAT is **100% byte-exact to retail with zero offset shifting**, making zone-in crashes impossible.*

| City / Zone | Target DAT | Optimizations | Status |
|---|---|---|---|
| **Mhaura** | `ROM/1/44.DAT` | Harbor boiler steam & chimney smoke | ✅ 100% Retail Exact |
| **Selbina** | `ROM/1/43.DAT` | 19 Residential & smokehouse chimneys | ✅ 100% Retail Exact |
| **Western Adoulin** | `ROM9/0/3.DAT` | 27 Hearth smog & chimney plumes | ✅ 100% Retail Exact |
| **Upper Jeuno** | `ROM/1/40.DAT` | 15 Rooftop chimney smoke plumes | ✅ 100% Retail Exact |
| **Bastok Mines** | `ROM/1/30.DAT` | Industrial blast furnace smoke plumes | ✅ 100% Retail Exact |
| **Bastok Markets** | `ROM/1/31.DAT` | 32 District-wide residential chimneys | ✅ 100% Retail Exact |
| **Port Bastok** | `ROM/1/32.DAT` | 30 Harbor boiler exhaust plumes | ✅ 100% Retail Exact |
| **Windurst Woods** | `ROM/1/34.DAT` | 35 Treehouse residential chimneys | ✅ 100% Retail Exact |
| **Windurst Waters** | `ROM/1/35.DAT` | 34 Tarutaru residential chimneys | ✅ 100% Retail Exact |
| **Port Windurst** | `ROM/1/37.DAT` | 24 Dock boiler smoke plumes | ✅ 100% Retail Exact |
| **Nashmau** | `ROM3/0/3.DAT` | Canal water haze, steam & cooking smoke | ✅ 100% Retail Exact |

---

## 🔮 2. Objects Pack (`objects/`)

*Silences heavy rotating alpha-transparent particle glows on interactive objects and battle summons.*

### A. All 8 Elemental Crystal Fetters & Gyres
*Silences spinning particle halos on Crystal Fetters & Gyres across **Sortie**, **Odyssey** (Agon Halos), **Dynamis-Divergence Wave 3**, **Lady Lilith**, and **Provenance Watcher**.*

| Element | Target DAT | What Was Silenced |
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

| Object | Target DAT | What Was Silenced |
|---|---|---|
| **Home Point Crystal** | `ROM/3/25.DAT` | Rotating crystal particle aura |
