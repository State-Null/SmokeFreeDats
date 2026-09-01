# 💨 SmokeFreeDats

A high-performance DAT overlay pack for **[XIPivot](https://github.com/Darkdoom/XIPivot)** that strips lag-inducing 3D particle emitters (**chimney smoke, dock steam, fountain spray, swamp miasma, and volcanic ashfall**) across 31 zones in Final Fantasy XI to lock framerates at a smooth 60 FPS.

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

## 📋 Included Zones (31 Zones)

### 🏙️ Major Hubs & Towns (21 Zones)
| Zone | DAT Path | Stripped Emitters |
|---|---|---|
| **Mhaura** | `ROM/1/44.DAT` | Harbor boiler steam, dock haze, all chimney smoke |
| **Western Adoulin** | `ROM9/0/3.DAT` | Hearth smog, residential chimneys, bridge mist |
| **Eastern Adoulin** | `ROM9/0/4.DAT` | Big Bridge water spray, Castle gate braziers, shop steam |
| **Nashmau** | `ROM3/0/3.DAT` | Dock boiler steam, Qiqirn cooking kilns, canal mist |
| **Aht Urhgan Whitegate** | `ROM3/0/0.DAT` | Central plaza fountain spray, tea house steam vents |
| **Al Zahbi** | `ROM3/0/1.DAT` | Desert dust storm haze, bazaar firepit smoke |
| **Lower Jeuno** | `ROM/1/41.DAT` | Alleyway fog layers, door lantern glow emitters |
| **Port Jeuno** | `ROM/1/42.DAT` | Airship boiler exhaust, dock cloud particles |
| **Upper Jeuno** | `ROM/1/40.DAT` | Residential chimney smoke, ambient alley fog |
| **Ru'Lude Gardens** | `ROM/1/39.DAT` | Palace courtyard mist, fountain water spray |
| **Bastok Mines** | `ROM/1/30.DAT` | Blast furnace smoke, industrial smelter smog |
| **Bastok Markets** | `ROM/1/31.DAT` | District chimneys, canal bridge water spray |
| **Port Bastok** | `ROM/1/32.DAT` | Harbor boiler exhaust, dock mist |
| **Windurst Woods** | `ROM/1/34.DAT` | Residential smoke plumes, tree mist |
| **Windurst Waters** | `ROM/1/35.DAT` | Tarutaru chimney smoke, canal water haze |
| **Windurst Walls** | `ROM/1/36.DAT` | Deep valley ambient fog, bridge mist |
| **Port Windurst** | `ROM/1/37.DAT` | Harbor dock boiler smoke, sea water spray |
| **Kazham** | `ROM/1/47.DAT` | Airship landing steam, waterfall spray |
| **Norg** | `ROM/1/48.DAT` | Subterranean cave mist, waterfall spray |
| **Selbina** | `ROM/1/45.DAT` | Harbor dock steam, sheep farm dust |
| **Rabao** | `ROM/1/46.DAT` | Oasis water haze, desert sandstorm loops |

### ⚔️ Battlefields & Endgame Zones (10 Zones)
| Zone | DAT Path | Stripped Emitters |
|---|---|---|
| **Mount Zhayolm** | `ROM3/0/12.DAT` | **Fullscreen volcanic ashfall**, lava steam, heat shimmer |
| **Halvung** | `ROM3/0/13.DAT` | Underground forge smoke, heavy fire effects |
| **Caedarva Mire** | `ROM3/0/11.DAT` | Toxic swamp miasma clouds, water haze |
| **Al'Taieu (Sea)** | `ROM2/0/33.DAT` | Sea floor haze, fire/mist shaders |
| **Dynamis - San d'Oria** | `ROM/1/85.DAT` | Nightmare cloud motes, ground mist |
| **Dynamis - Bastok** | `ROM/1/86.DAT` | Nightmare cloud motes, ground mist |
| **Dynamis - Windurst** | `ROM/1/87.DAT` | Nightmare cloud motes, ground mist |
| **Dynamis - Jeuno** | `ROM/1/88.DAT` | Nightmare cloud motes, ground mist |
| **Dynamis - Beaucedine** | `ROM/1/89.DAT` | Blizzard cloud motes, nightmare mist |
| **Dynamis - Xarcabard** | `ROM/1/90.DAT` | Blizzard cloud motes, nightmare mist |

---

## ⚡ Notes
* **Zero Base-Game Edits**: Loaded in memory on-the-fly with XIPivot.
* **100% Geometry Intact**: All map collision, buildings, doors, vendors, textures, and lighting remain completely vanilla.
