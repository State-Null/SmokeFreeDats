# 💨 SmokeFreeDats Performance Pack

A plug-and-play, zero-lag performance DAT collection for Final Fantasy XI via **[XIPivot](https://github.com/Darkdoom/XIPivot)**.

It eliminates lag-heavy transparent particle effects across:
1. 🌆 **City & Port Smoke**: 9 major town hubs (chimneys, blast furnaces, boilers, smog).
2. 🔮 **Battle Summons & Fetters**: All **8 Elemental Crystal Fetters & Wave 3 Halos** (Sortie, Odyssey, Dynamis-D, Lilith, Provenance).
3. 💠 **Home Point Crystals**: Silences rotating crystal particle auras.

---

## 🚀 Quick Install (XIPivot)

1. Download or clone this repository directly into your XIPivot `DATs` folder:
   ```text
   Windower4/addons/XIPivot/data/DATs/SmokeFreeDats/
   ```
2. In-game, run:
   ```text
   //pivot add SmokeFreeDats
   ```

To make it permanent across sessions, add `SmokeFreeDats` to `Windower4/addons/XIPivot/data/settings.xml`:
```xml
<overlays>SmokeFreeDats,XI-View</overlays>
```

---

## 📋 Included Optimizations

### 🌆 1. Town & Port Chimney Smoke Removal (9 Hubs)
*Cleanly excises chimney and boiler smoke containers without altering terrain, weather skyboxes, or collision.*

| City / Zone | DAT Path | What Was Removed |
|---|---|---|
| **Mhaura** | `ROM/1/44.DAT` | Harbor boiler steam, dock haze, all chimney smoke |
| **Western Adoulin** | `ROM9/0/3.DAT` | Hearth smog, residential chimneys, bridge smog |
| **Upper Jeuno** | `ROM/1/40.DAT` | Rooftop residential chimney smoke (35.8 KB) |
| **Bastok Mines** | `ROM/1/30.DAT` | Industrial blast furnace smoke (21.2 KB) |
| **Bastok Markets** | `ROM/1/31.DAT` | District-wide residential chimney smoke (44.3 KB) |
| **Port Bastok** | `ROM/1/32.DAT` | Harbor boiler exhaust plumes & dock smoke (39.8 KB) |
| **Windurst Woods** | `ROM/1/34.DAT` | Residential treehouse chimney smoke (43.4 KB) |
| **Windurst Waters** | `ROM/1/35.DAT` | Tarutaru residential chimney smoke (44.7 KB) |
| **Port Windurst** | `ROM/1/37.DAT` | Harbor dock boiler smoke (37.5 KB) |

---

### 🔮 2. Elemental Crystal Fetters & Halos (All 8 Elements)
*Silences spinning particle halos on Crystal Fetters & Halos across **Sortie**, **Odyssey** (Agon Halos), **Dynamis-Divergence Wave 3**, **Lady Lilith**, and **Provenance Watcher**.*

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

---

### 💠 3. Home Point Crystals
*Silences the rotating crystal particle glow around all Home Points.*

| Object | DAT Path | What Was Silenced |
|---|---|---|
| **Home Point Crystal** | `ROM/3/25.DAT` | Rotating crystal particle aura |
