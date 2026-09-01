# 💨 SmokeFreeDats

A pure, zero-lag smoke particle removal pack for **[XIPivot](https://github.com/Darkdoom/XIPivot)**.

It eliminates laggy 3D **chimney smoke, blast furnace plumes, dock boiler exhaust, and residential smog** across all major cities and ports in Final Fantasy XI without altering terrain, weather skyboxes, or collision.

---

## 🚀 Quick Install (XIPivot)

1. Drop the `SmokeFreeDats` folder into your XIPivot directory:
   ```text
   Windower4/addons/XIPivot/data/DATs/SmokeFreeDats/
   ```
2. In-game, open your Windower console and run:
   ```text
   //pivot add SmokeFreeDats
   ```

To make it permanent, add `SmokeFreeDats` to `Windower4/addons/XIPivot/data/settings.xml`:
```xml
<overlays>SmokeFreeDats,XI-View</overlays>
```

---

## 📋 Included Cities & Stripped Smoke Emitters (9 Zones)

| City / Zone | DAT Path | Removed Smoke Emitters |
|---|---|---|
| **Mhaura** | `ROM/1/44.DAT` | Harbor boiler exhaust steam, dock haze, all chimney smoke plumes |
| **Western Adoulin** | `ROM9/0/3.DAT` | Hearth smog, residential chimneys, Big Bridge smog |
| **Bastok Mines** | `ROM/1/30.DAT` | Industrial blast furnace smoke (21.2 KB) |
| **Bastok Markets** | `ROM/1/31.DAT` | District-wide residential chimney smoke (44.3 KB) |
| **Port Bastok** | `ROM/1/32.DAT` | Harbor boiler exhaust plumes & dock smoke (39.8 KB) |
| **Windurst Woods** | `ROM/1/34.DAT` | Residential treehouse chimney smoke (43.4 KB) |
| **Windurst Waters** | `ROM/1/35.DAT` | Tarutaru residential chimney smoke (44.7 KB) |
| **Port Windurst** | `ROM/1/37.DAT` | Harbor dock boiler smoke (37.5 KB) |
| **Upper Jeuno** | `ROM/1/40.DAT` | Residential rooftop chimney smoke (35.8 KB) |

---

## ⚡ Technical Safety
* **Pure Smoke Targeting**: Only dedicated `smok` containers are modified. Zero weather or skybox domes are touched.
* **In-Place Nullification**: All file sizes and chunk byte offsets are 100% identical to vanilla to prevent pointer misalignment.
* **100% Skybox & Lighting Preserved**: Weather skybox domes (`mist`, `suny`, `rain`, `clod`, `thdr`), day/night palettes, and Mog House lighting are untouched.
* **100% Collision Intact**: Walkmeshes (`mode`), doors, vendors, and NPCs remain completely vanilla.
