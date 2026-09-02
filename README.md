# 💨 SmokeFreeDats & Performance Pack

A modular, zero-lag performance DAT collection for Final Fantasy XI via **[XIPivot](https://github.com/Darkdoom/XIPivot)**.

---

## 📦 Packs

1. 🌆 **zones/**: Town & port smoke and mist removal across **12 major cities, hubs and Mog Garden**.
2. 🔮 **objects/**: Particle glow removal for **Elemental Crystal Fetters & Gyres** and **Home Points**.
3. 🧪 **experimental/**: Large-scale outdoor battlefield emitter optimizations.

---

## 🚀 Quick Install (XIPivot)

Drop the desired pack folders directly into your XIPivot DATs directory:

`	ext
Windower4/addons/XIPivot/data/DATs/
├── zones/
├── objects/
└── experimental/
    └── batallia_s/
        └── ROM5/0/7.DAT
`

Enable in XIPivot:
`	ext
//pivot add zones
//pivot add objects
//pivot add batallia_s
`

---

## 🌆 1. Zones Pack (zones/)

| City / Zone | Target DAT | Optimizations |
|---|---|---|
| **Mhaura** | ROM/1/44.DAT | Harbor boiler steam & chimney smoke |
| **Selbina** | ROM/1/43.DAT | 19 Residential & smokehouse chimneys |
| **Western Adoulin** | ROM9/0/3.DAT | 27 Hearth smog & chimney plumes |
| **Upper Jeuno** | ROM/1/40.DAT | 15 Rooftop chimney smoke plumes |
| **Bastok Mines** | ROM/1/30.DAT | Industrial blast furnace smoke plumes |
| **Bastok Markets** | ROM/1/31.DAT | 32 District-wide residential chimneys |
| **Port Bastok** | ROM/1/32.DAT | 30 Harbor boiler exhaust plumes |
| **Windurst Woods** | ROM/1/34.DAT | 35 Treehouse residential chimneys |
| **Windurst Waters** | ROM/1/35.DAT | 34 Tarutaru residential chimneys |
| **Port Windurst** | ROM/1/37.DAT | 24 Dock boiler smoke plumes |
| **Nashmau** | ROM3/0/3.DAT | Canal water haze, steam & cooking smoke |
| **Mog Garden** | ROM/309/10.DAT | 125 Continuous particle, lantern glow & insect emitters |

---

## 🔮 2. Objects Pack (objects/)

| Element / Object | Target DAT | What Was Silenced |
|---|---|---|
| **All 8 Crystal Fetters & Gyres** | ROM/259/73..80.DAT | 3D Rotating elemental glow flare (Sortie, Odyssey, D-Divergence) |
| **Home Point Crystal** | ROM/3/25.DAT | Rotating crystal particle aura |

---

## 🧪 3. Experimental Pack (experimental/)

| Zone | Target DAT | Optimizations |
|---|---|---|
| **Batallia Downs [S]** | ROM5/0/7.DAT | 32 Battlefield campfire, smoke plume & beacon emitters |
