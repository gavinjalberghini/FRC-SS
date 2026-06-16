---
layout: printing-lesson
title: Dialing In Print Settings
subtitle: Supports, brims and rafts, infill patterns, wall count, seams, and the speed-vs-quality trade-off.
permalink: /learning/printing/dialing-in-settings/
role: veteran
order: 6
size: 2
time: "2–3 hrs"
---

## Overview

As an Operator you used Bambu's defaults. As a Veteran you tune settings to get
stronger, cleaner, faster prints. This lesson goes deeper into the settings that
matter most for functional FRC parts.

## Prerequisites

- All Operator lessons completed.

## Unit 1 — Walls, infill & strength

- **Wall loops** carry most of a part's strength — adding walls is usually more
  effective than adding infill. 3–4 walls for load-bearing parts.
- **Infill density** — 15% is fine for general parts; 30–50%+ for higher load.
  Above ~50% you get diminishing returns versus just adding walls.
- **Infill pattern** — **gyroid** is strong in all directions; **grid/cubic** are
  fast; **rectilinear** is light. Match the pattern to how the part is loaded.
- **Top/bottom layers** — enough solid layers to fully close the part (more for
  watertight or high-load tops).

## Unit 2 — Bed adhesion: brims & rafts

- **Brim** — a flat skirt attached to the part that adds first-layer grip; use it
  for tall, small-footprint, or warp-prone parts. Peels off after.
- **Raft** — a full platform under the part; rarely needed on Bambu's textured
  plates but useful for tiny contact areas.
- More adhesion = harder removal, so use the minimum that holds.

## Unit 3 — Supports

- **Normal supports** are strong and removable; **tree supports** use less material
  and are gentler on surfaces with organic overhangs.
- Set the **overhang threshold** (~45° is typical) so supports only generate where
  needed.
- Tune the **support–part gap (z distance)** so supports release cleanly without
  leaving the part unsupported.
- Place supports to land on **non-critical faces**.

## Unit 4 — Quality details & speed

- **Seam** — where each layer starts/stops; hide it on a back edge or align it to a
  corner.
- **Ironing** smooths flat top surfaces at a time cost.
- **Speed vs. quality** — faster prints can lose accuracy and layer adhesion; slow
  down for strength and fine detail. Bambu's speed presets are a good starting
  point.

## Steps & acceptance criteria

- [ ] Choose walls + infill for a load-bearing part and justify the trade-off.
- [ ] Add and tune supports so they release cleanly on a real print.
- [ ] Use a brim appropriately and explain when a raft is needed instead.
- [ ] Reposition the seam and explain the speed-vs-quality trade-off.

## Resources

- [Bambu Studio parameters reference](https://wiki.bambulab.com/en/software/bambu-studio/parameter)
- [Bambu: Support settings](https://wiki.bambulab.com/en/software/bambu-studio/support)
- [CNC Kitchen: Infill & walls testing](https://www.cnckitchen.com/)

## Notes

- Change **one setting at a time** and label your saved profiles, or you'll never
  know which change helped.
