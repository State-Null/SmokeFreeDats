# 💨 SmokeFreeDats: High-Performance FFXI DAT Overlay Pack

**SmokeFreeDats** is an open-source performance DAT replacement pack for Final Fantasy XI designed for use with **[XIPivot](https://github.com/Darkdoom/XIPivot)**. 

It eliminates continuous, unoptimized 3D particle emitter loops (**chimney smoke, dock/boiler steam, fountain spray, swamp miasma, volcanic ashfall, and ambient mist/fog**) across **31 major towns, hubs, battlefields, and endgame zones** in Final Fantasy XI.

---

## ⚡ The Problem: DirectX 8/9 Alpha Overdraw & Draw-Call Choke

1. **Transparent 2D Billboard Sprites**: FFXI renders environmental smoke, chimney plumes, harbor steam, waterfall mist, and ashfall as multi-layered 2D textured quads that continuously rotate to face the camera.
2. **Single-Threaded CPU Depth-Sorting**: In DirectX 8/9, every transparent pixel must be depth-sorted and alpha-blended against the background geometry on a **single CPU thread**.
3. **The Multiplier Effect**: When dozens of player models, trust companions, or alliance members stand inside or behind these smoke/steam plumes (such as in Ambuscade Mhaura, Whitegate, or Dynamis-Divergence), the CPU is forced to redraw every character model *through* 5 to 10 transparent particle planes simultaneously (**Alpha Overdraw**), causing heavy micro-stuttering and 10–15 FPS slideshows.

---

## 🛡️ The Solution: Clean Chunk Stripping

By deleting or zeroing out the self-contained particle emitter sub-chunks (`smok`, `mist`, `clod`, `fire`, `dust`) directly inside each zone DAT:
* **Zero Base-Game Modifications**: Overlaid entirely on-the-fly in memory using XIPivot without permanently altering your vanilla game installation.
* **100% Geometry & Texture Integrity**: Collision meshes, ground paths, buildings, doors, vendors, textures, lighting, and NPCs remain 100% intact.
* **Rock-Solid 60 FPS**: Eliminates the draw-call bottleneck, locking framerates at a smooth 60 FPS even during multiboxing and heavy player congestion.

---

## 📋 Comprehensive Zone Changelog (31 Zones)

### 🌊 1. High-Traffic Hubs & Port Towns
| Zone | Target DAT Path | Vanilla Bottleneck | Smokefree Modification | In-Game Impact |
|---|---|---|---|---|
| **Mhaura** (Zone 249) | `ROM/1/44.DAT` | Boiler exhaust, 24 chimney smoke plumes, harbor water mist | Stripped `smok` (9.7 KB) & `mist` (97 KB) | **Locked 60 FPS in Ambuscade.** Crystal clear harbor; zero chimney smoke. |
| **Nashmau** (Zone 53) | `ROM3/0/3.DAT` | Ferry dock boiler steam, Qiqirn cooking fire/kiln plumes, canal mist | Stripped `mist` (98.6 KB) canal haze | Eliminates town-wide stutter across the central canal basin. |
| **Aht Urhgan Whitegate** (Zone 50) | `ROM3/0/0.DAT` | Central plaza fountain water spray billboards, tea house steam | Stripped `mist` (97.7 KB) fountain haze | Smooth central plaza navigation; fountain mesh intact without spray lag. |
| **Al Zahbi** (Zone 48) | `ROM3/0/1.DAT` | Ambient desert dust haze planes, bazaar brazier smoke | Stripped 3 `mist` dust layers (100.8 KB) | Clean visibility; removes brownish dust haze across the central street. |
| **Selbina** (Zone 248) | `ROM/1/45.DAT` | Harbor dock steam, sheep farm dust particles | Stripped `mist` (816 B) emitter chunk | Eliminates harbor micro-stutters during high-traffic campaign periods. |

### 🏰 2. Adoulin Metro
| Zone | Target DAT Path | Vanilla Bottleneck | Smokefree Modification | In-Game Impact |
|---|---|---|---|---|
| **Western Adoulin** (Zone 256) | `ROM9/0/3.DAT` | Hearth smoke around Mog House, residential chimneys, bridge smog | Stripped hearth smoke & 2 `mist` chunks (71.3 KB) | **No more Adoulin stutter.** Mog House exits and Big Bridge crossings are completely fluid. |
| **Eastern Adoulin** (Zone 257) | `ROM9/0/4.DAT` | Big Bridge water spray mist, Castle Adoulin gate braziers, shop steam | Stripped 2 `mist` bridge/gate chunks (98.9 KB) | Fixes the massive draw-distance bottleneck when looking from Big Bridge towards Castle Adoulin. |

### 🏙️ 3. Jeuno Metro
| Zone | Target DAT Path | Vanilla Bottleneck | Smokefree Modification | In-Game Impact |
|---|---|---|---|---|
| **Upper Jeuno** (Zone 240) | `ROM/1/40.DAT` | Residential chimney smoke plumes, 3 layers of ambient alleyway fog | Stripped `smok` (35.8 KB) & 3 `mist` chunks (98.8 KB) | Clean rooftop views without chimney smoke; eliminates fog lag near Batallia gate. |
| **Lower Jeuno** (Zone 245) | `ROM/1/41.DAT` | Heavy alleyway mist layers, merchant lantern ambient fog | Stripped 3 `mist` fog layers (98.8 KB) | Crystal clear alleyway between Neptune's Spire and Auction House. |
| **Port Jeuno** (Zone 246) | `ROM/1/42.DAT` | Airship boiler exhaust steam, cloud backdrop particles, dock mist | Stripped 3 `mist` exhaust/dock chunks (98.8 KB) | Eliminates stutter when panning camera towards airship docks. |
| **Ru'Lude Gardens** (Zone 243) | `ROM/1/39.DAT` | Palace courtyard mist, fountain water spray billboards | Stripped 3 `mist` courtyard chunks (97.9 KB) | Eliminates frame drops around the central fountain and palace steps. |

### ⛏️ 4. Bastok Metro
| Zone | Target DAT Path | Vanilla Bottleneck | Smokefree Modification | In-Game Impact |
|---|---|---|---|---|
| **Bastok Mines** (Zone 234) | `ROM/1/30.DAT` | Ore blast furnace industrial smoke (21.2 KB), smelter smog | Stripped `smok` furnace (21.2 KB) & 3 `mist` chunks (98 KB) | Blast furnace chimneys no longer emit thick smoke; eliminates market lag. |
| **Bastok Markets** (Zone 235) | `ROM/1/31.DAT` | District-wide residential chimneys (44.3 KB), canal water spray | Stripped `smok` chimneys (44.3 KB) & 3 `mist` chunks (97 KB) | Eliminates heaviest residential chimney lag in original game; clean skyline. |
| **Port Bastok** (Zone 236) | `ROM/1/32.DAT` | Harbor boiler exhaust plumes (39.8 KB), ship dock spray | Stripped `smok` boiler (39.8 KB) & 4 `mist` chunks (98 KB) | Completely removes dock boiler exhaust and airship platform haze. |

### 🌳 5. Windurst Metro
| Zone | Target DAT Path | Vanilla Bottleneck | Smokefree Modification | In-Game Impact |
|---|---|---|---|---|
| **Windurst Woods** (Zone 241) | `ROM/1/34.DAT` | Massive treehouse chimney smoke (43.4 KB), ambient forest mist | Stripped `smok` treehouse (43.4 KB) & 5 `mist` chunks (99 KB) | Removes continuous chimney plumes across Mithra dwellings and AH district. |
| **Windurst Waters** (Zone 238) | `ROM/1/35.DAT` | Tarutaru residential chimney smoke (44.7 KB), canal water haze | Stripped `smok` chimneys (44.7 KB) & 2 `mist` chunks (97 KB) | Crystal clear canals; eliminates frame drops near cooking guild and bridges. |
| **Windurst Walls** (Zone 239) | `ROM/1/36.DAT` | Deep valley ambient fog layers, waterway mist | Stripped 3 `mist` valley fog chunks (98.3 KB) | Clears canyon fog looking toward Heavens Tower. |
| **Port Windurst** (Zone 240) | `ROM/1/37.DAT` | Harbor dock boiler smoke (37.5 KB), sea water spray | Stripped `smok` dock (37.5 KB) & 3 `mist` chunks (97 KB) | Eliminates dock chimney smoke near fishing guild and boat slips. |

### 🌴 6. Outpost & Island Towns
| Zone | Target DAT Path | Vanilla Bottleneck | Smokefree Modification | In-Game Impact |
|---|---|---|---|---|
| **Kazham** (Zone 250) | `ROM/1/47.DAT` | Dense jungle humidity haze, airship platform steam | Stripped `mist` humidity chunk (816 B) | Clears thick jungle haze over pathways. |
| **Norg** (Zone 252) | `ROM/1/48.DAT` | Subterranean waterfall spray, cavern moisture mist | Stripped `mist` waterfall chunk (432 B) | Waterfall mesh is intact; multi-layered spray quad is removed. |
| **Rabao** (Zone 247) | `ROM/1/46.DAT` | Oasis water haze, desert sandstorm billboard loops | Stripped `mist` haze chunk (832 B) | Eliminates continuous sandy haze over oasis water. |

### ⚔️ 7. Endgame & Battlefields
| Zone | Target DAT Path | Vanilla Bottleneck | Smokefree Modification | In-Game Impact |
|---|---|---|---|---|
| **Mount Zhayolm** (Zone 62) | `ROM3/0/12.DAT` | **Fullscreen Volcanic Ashfall**, lava bubbling steam, heat shimmer | Stripped `dust` ashfall, `fire`, `clod`, `mist` steam (11.2 KB) | **Zero ashfall lag.** Fullscreen depth-sorting passes eliminated; lava intact. |
| **Halvung** (Zone 63) | `ROM3/0/13.DAT` | Underground forge smoke & heavy fire effects | Stripped heavy `effe` sub-containers (230.2 KB) | Massive reduction in draw calls in narrow corridors. |
| **Caedarva Mire** (Zone 61) | `ROM3/0/11.DAT` | Toxic swamp miasma clouds, fly swarms, water haze | Stripped `dust`, `clod`, `mist`, `fire` (22.6 KB) | Eliminates murky green miasma fog that chokes framerates during Salvage. |
| **Al'Taieu (Sea)** (Zone 33) | `ROM2/0/33.DAT` | Translucent sea floor haze, fire/mist atmospheric shaders | Stripped `fire`, `clod`, `mist` shaders (27.9 KB) | Clearer ocean view with reduced alpha fill-rate load. |
| **Dynamis Cities** (6 Zones)<br>`ROM/1/85.DAT`–`90.DAT` | `ROM/1/85.DAT`–`90.DAT`<br>*(Sandy, Bastok, Windy, Jeuno, Beauc, Xarc)* | Continuous nightmare cloud motes, ambient ground mist layers | Stripped `mist`, `clod`, `effe` ambient markers (~900 B per zone) | Removes ambient nightmare particle clutter, freeing draw calls for alliance combat spells. |

---

## 🚀 Installation Guide (XIPivot)

### 1. Download & Extract
Clone or download this repository and place the folder into your Windower XIPivot DATs directory:
```text
Windower4/addons/XIPivot/data/DATs/SmokeFreeDats/
```

### 2. Enable in Windower
In-game, open your Windower console and run:
```text
//pivot add SmokeFreeDats
```
*(Or verify active overlays with `//pivot status`)*

### 3. Make Permanent Across Sessions
Open `Windower4/addons/XIPivot/data/settings.xml` in any text editor and add `SmokeFreeDats` to the front of your overlays list:
```xml
<?xml version="1.1" ?>
<settings>
    <global>
        <cache_enabled>false</cache_enabled>
        <cache_max_age>600</cache_max_age>
        <cache_size>2147483648</cache_size>
        <debug_log>false</debug_log>
        <overlays>SmokeFreeDats,XI-View,nohpglow</overlays>
    </global>
</settings>
```

---

## 🤝 Contributing & Community
Pull requests, bug reports, and additional zone contributions are welcome! If you identify another zone with heavy particle emitters, feel free to open an issue or PR with the target DAT path.
