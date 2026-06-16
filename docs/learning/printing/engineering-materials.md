---
layout: printing-lesson
title: Engineering Materials & Advanced Printing
subtitle: Carbon-fiber nylon, PC, and other engineering filaments — hardened nozzles, drying, and strong parts.
permalink: /learning/printing/engineering-materials/
role: lead
order: 10
size: 3
time: "Multi-session"
---

## Overview

When a printed part needs to survive real match loads, you reach for **engineering
materials**. These are harder to print and demand the right printer, nozzle, and
prep. This lesson covers the materials and the workflow to print them reliably.

## Prerequisites

- All Veteran lessons completed.
- Access to an enclosed printer (X1C/P1S) rated for high-temp materials.

## Unit 1 — The engineering filaments

- **PA (Nylon)** — tough, wear- and heat-resistant, slightly flexible; excellent
  for gears, bushings, and high-wear parts. Very hygroscopic (absorbs water).
- **PAHT-CF / PA-CF (carbon-fiber nylon)** — stiff, strong, dimensionally stable,
  high-temp. The go-to for structural printed FRC parts.
- **PC (Polycarbonate)** — very strong and heat-resistant; demanding to print.
- **PET-CF / PETG-CF** — stiffer, more heat-resistant versions of PETG.
- **Filled materials are abrasive** — the carbon/glass fibers wear out brass
  nozzles fast.

## Unit 2 — Hardware requirements

- **Hardened steel or ruby/tungsten nozzle** is **required** for any CF/GF-filled
  filament — a brass nozzle will be destroyed.
- **Enclosed printer** with a high-temp hotend; check the printer's max nozzle temp
  against the filament (PC and some nylons need 280–300 °C).
- Bambu's high-flow / high-temp hotend and the right plate for the material.

## Unit 3 — Drying filament

- Nylon and CF-nylon **absorb moisture from the air within hours**; wet filament
  prints stringy, weak, and full of voids.
- **Dry** spools before (and ideally during) printing using a filament dryer or the
  AMS/heated chamber per the material's spec.
- Store engineering filament in **sealed containers with desiccant**.

## Unit 4 — Getting strong parts

- Combine engineering material with **design for strength**: correct orientation,
  high wall count, and solid-enough infill (see the design lesson).
- **Annealing** some materials (controlled heat after printing) increases strength
  and heat resistance but can shrink/distort the part — test first.
- Validate parts under realistic load before trusting them on the robot.

## Steps & acceptance criteria

- [ ] Select an engineering material for a structural part and justify it.
- [ ] Install/confirm a hardened nozzle and the correct enclosed printer.
- [ ] Dry a hygroscopic filament and store it correctly.
- [ ] Print and load-test a structural part in CF nylon.

## Resources

- [Bambu Wiki: Filament drying](https://wiki.bambulab.com/en/filament-acc/filament/drying-filament)
- [Bambu engineering filaments](https://bambulab.com/en/filament)
- [Prusa: Annealing & advanced materials](https://help.prusa3d.com/article/annealing_2191)

## Notes

- Engineering materials are expensive and slow — reserve them for parts that truly
  need them, and prototype the geometry in PLA/PETG first.

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — record which engineering materials and nozzles your team owns, which printer is dedicated to abrasive materials, and your drying/storage setup.</p>
</div>
