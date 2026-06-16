---
layout: printing-lesson
title: Choosing the Right Material
subtitle: PLA, PETG, ABS/ASA, TPU, and nylon — their properties and how to pick the right one for an FRC part.
permalink: /learning/printing/choosing-materials/
role: operator
order: 2
size: 2
time: "1–2 hrs"
---

## Overview

The single most important decision for a printed part is **what filament to print
it in**. The wrong material wastes hours and fails on the field. This lesson
covers the common FRC filaments, their strengths and weaknesses, and a simple way
to choose.

## Prerequisites

- [3D Printing Fundamentals & Safety](../fundamentals-safety/) completed.

## Unit 1 — The common filaments

- **PLA** — easy to print, stiff, dimensionally accurate, cheap. **Weak to heat**
  (softens in a hot car or near motors) and brittle under impact. Great for
  prototypes, jigs, fixtures, and non-structural parts.
- **PETG** — tougher and more heat-resistant than PLA, with good layer adhesion and
  some flex. The everyday workhorse for functional robot parts. Slightly stringy.
- **ABS / ASA** — heat-resistant and impact-tough; **needs an enclosure** and
  ventilation and is prone to warping. ASA also resists UV. Good for parts that see
  heat or sustained load.
- **TPU** — flexible/rubber-like. Used for bumpers pads, intake compliant parts,
  grips, and cable strain reliefs. Print slow.
- **Nylon (PA) & CF-filled** — strong, tough, heat- and wear-resistant engineering
  materials. Covered in the Lead lesson; they need drying and a hardened nozzle.

## Unit 2 — Properties that matter for FRC

- **Strength & toughness** — will it survive impacts and match loads?
- **Heat resistance** — parts near motors, brakes, or in a hot pit can soften
  (PLA is the main risk).
- **Stiffness vs. flexibility** — structural brackets want stiffness; compliant
  rollers and pads want TPU.
- **Printability** — ease of getting a good print (PLA easiest → engineering
  materials hardest).
- **Layer adhesion** — how well layers bond, which sets cross-layer strength.

## Unit 3 — A simple selection guide

- Prototype, jig, or display part → **PLA**.
- Functional robot part, general purpose → **PETG**.
- Sees heat or sustained structural load → **ASA/ABS** or an engineering material.
- Needs to flex, grip, or absorb impact → **TPU**.
- Structural, high-load, or wear surface → **CF nylon** (Lead lesson).

## Unit 4 — Bambu filament profiles & the AMS

- Bambu Studio includes tuned profiles for Bambu and generic filaments — start
  from the profile that matches your spool.
- Bambu spools have an **RFID tag** the AMS reads automatically; third-party
  spools must be set manually in the slicer/AMS.
- Each material has its own **nozzle and bed temperatures** and bed-surface
  preference — don't reuse a PLA profile for PETG.

## Steps & acceptance criteria

- [ ] Name the right material for three example parts and justify each choice.
- [ ] State which materials need an enclosure and which printers can run them.
- [ ] Find and select the correct filament profile in Bambu Studio.
- [ ] Explain why PLA is a poor choice for a part that gets hot.

## Resources

- [Bambu Lab filament guide](https://wiki.bambulab.com/en/filament-acc/filament) — temperatures and handling.
- [Prusa: Material table](https://help.prusa3d.com/article/material-table_2069)
- [Simplify3D Material Guide](https://www.simplify3d.com/resources/materials-guide/)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — record which filaments and brands your team stocks, which printer each material runs on, and any team standard (e.g., "PETG for all functional parts").</p>
</div>
