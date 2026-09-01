# 💨 SmokeFreeDats

A pure, zero-lag smoke & particle removal pack for **[XIPivot](https://github.com/Darkdoom/XIPivot)**.

It eliminates laggy 3D **chimney smoke, blast furnace plumes, dock boiler exhaust, canal water mist, fountain spray, swamp miasma, and sea distortion** across 14 major hubs and zones in Final Fantasy XI without altering terrain, weather skyboxes, or collision.

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

To make it permanent across sessions, add `SmokeFreeDats` to `Windower4/addons/XIPivot/data/settings.xml`:
```xml
<overlays>SmokeFreeDats,XI-View</overlays>
```

---

## 📋 Included Zones & Stripped Emitters (14 Zones)

| Zone | DAT Path | Removed Particle Emitters |
|---|---|---|
| **Mhaura** | `ROM/1/44.DAT` | Harbor boiler exhaust steam, dock haze, all chimney smoke plumes |
| **Western Adoulin** | `ROM9/0/3.DAT` | Hearth smog, residential chimneys, Big Bridge smog |
| **Eastern Adoulin** | `ROM9/0/4.DAT` | Big Bridge water spray mist & Castle Adoulin gate haze (98.5 KB) |
| **Nashmau** | `ROM3/0/3.DAT` | Central canal water mist & dock boiler haze (98.1 KB) |
| **Aht Urhgan Whitegate** | `ROM3/0/0.DAT` | Central plaza fountain water spray & tea house steam (97.7 KB) |
| **Al'Taieu (Sea)** | `ROM2/0/33.DAT` | Atmospheric luminous particle haze & sea distortion (27.0 KB) |
| **Caedarva Mire** | `ROM3/0/11.DAT` | Swamp sulphur gas vents & 12 bog poison miasma nodes (541 KB) |
| **Bastok Mines** | `ROM/1/30.DAT` | Industrial blast furnace smoke (21.2 KB) |
| **Bastok Markets** | `ROM/1/31.DAT` | District-wide residential chimney smoke (44.3 KB) |
| **Port Bastok** | `ROM/1/32.DAT` | Harbor boiler exhaust plumes & dock smoke (39.8 KB) |
| **Windurst Woods** | `ROM/1/34.DAT` | Residential treehouse chimney smoke (43.4 KB) |
| **Windurst Waters** | `ROM/1/35.DAT` | Tarutaru residential chimney smoke (44.7 KB) |
| **Port Windurst** | `ROM/1/37.DAT` | Harbor dock boiler smoke (37.5 KB) |
| **Upper Jeuno** | `ROM/1/40.DAT` | Residential rooftop chimney smoke (35.8 KB) |

---

## ⚡ Technical Safety & Zero-Shift Guarantee
* **In-Place Emitter Nullification**: Every file size and byte alignment is **100% exact to vanilla FFXI**.
* **Weather Skyboxes 100% Preserved**: All weather cloud domes (`mist`, `suny`, `rain`, `clod`, `thdr`), day/night lighting palettes, and Mog House lighting are untouched.
* **100% Collision & Doors Intact**: Walkmeshes (`mode`), door spawn vectors (`_6c0`..`_6fd`), and NPC pointers remain completely vanilla.
