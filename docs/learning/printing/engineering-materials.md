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

## Description

When a printed part has to survive match loads — not just look like
one — you leave PLA and everyday PETG behind. **Engineering
filaments** (nylons, CF-filled nylons, polycarbonate, PET-CF) are
stronger, hotter, more abrasive, and more expensive. They demand an
**enclosed** printer, a **hardened nozzle**, and **dry filament**.
This is Lead work. Operators should not grab a PA-CF spool because
the color was right.

You already chose everyday materials in
[Choosing the Right Material](../choosing-materials/), designed for
FDM in
[Designing for 3D Printing](../design-for-printing/), and diagnosed
wet-filament symptoms in
[Troubleshooting](../troubleshooting/). This ticket is the workflow
that makes a structural print *repeatable*.

### The engineering filaments

- **PA (nylon)** — tough, wear- and heat-resistant, a bit flexible.
  Good for gears, bushings, and high-wear guides. Extremely
  **hygroscopic** (drinks water from the air).
- **PAHT-CF / PA-CF (carbon-fiber nylon)** — stiff, strong,
  dimensionally stable, high-temp. The usual structural printed FRC
  part when you have decided print beats aluminum for this geometry.
- **PC (polycarbonate)** — very strong and heat-resistant; hard to
  print; high nozzle temps.
- **PET-CF / PETG-CF** — stiffer, more heat-resistant cousins of
  PETG.

Filled materials are **abrasive**. Carbon and glass chew **brass
nozzles** in a single spool. A ruined brass nozzle then under-extrudes
on PLA for the next operator. That is a farm failure, not a badge.

### Hardware

- **Hardened steel** (or ruby / tungsten) nozzle — required for any
  CF / GF filament.
- **Enclosed printer** with a high-temp hotend: **X1C or P1S**, not
  an open A1 / A1 mini. Check max nozzle temp against the spool (PC
  and some nylons want 280–300 °C).
- The correct Bambu high-flow / high-temp hotend and the plate the
  profile names.

### Drying and storage

Nylon and CF-nylon take up moisture **in hours**. Wet nylon prints
stringy, weak, and full of voids — it can look fine and fail on the
field. Dry before (and ideally during) the print with a filament
dryer, AMS 2 Pro / AMS HT if the shop has them, or the process Bambu
documents. Store in **sealed containers with desiccant**. Official
numbers live in
[Filament drying recommendations](https://wiki.bambulab.com/en/filament-acc/filament/dry-filament).

### Getting a strong part

Material is not enough. Keep DfAM: correct orientation, high wall
count, enough infill. Some nylons can be **annealed** (controlled
heat after printing) to raise strength and heat resistance; they can
also shrink. Test a coupon first. **Load-test** the real geometry
before it is the only intake pivot on a Friday.

### Cost and rules

Engineering filament is slow and expensive. Prototype the geometry in
PLA or PETG. Reserve CF-nylon for parts that earned it. FRC still
treats the result as a **FABRICATED ITEM**; legality and bumper /
structure rules are confirmed in the next ticket against the **current
manual**. When in doubt, do not put an untested printed structural
part on the competition robot.

Fumes: nylons and PC are not "print in the classroom with the door
shut." Enclosed printer, ventilation, no hovering over the chamber.

This site does not track load tests. The written material pick, the
dry-log, and the tested part are mentor-visible.

## Prerequisites

- All Veteran tickets completed.
- Access to an enclosed printer (X1C / P1S) rated for the filament,
  and a hardened nozzle already installed or ready to install with a
  mentor.
- A named structural candidate (real robot part or a load coupon
  that represents one).

## What you'll learn

- Which engineering filaments the shop will actually run, and on
  which machine.
- Why brass nozzles and open-frame printers are out of scope.
- How to dry and store hygroscopic filament.
- How to justify CF-nylon (or not) for a named part, then print and
  load-test it.

## Tasks

1. **Read the vendor constraints.** Read
   [Bambu engineering filaments](https://bambulab.com/en/filament)
   (or the shop's specific PA-CF / PAHT-CF wiki page) and
   [Filament drying](https://wiki.bambulab.com/en/filament-acc/filament/dry-filament).
   Optional: Prusa's
   [annealing note](https://help.prusa3d.com/article/annealing_2191)
   so you know annealing is a test, not a default. Write the nozzle
   temp, bed temp, enclosure need, and dry time for the **one**
   filament you will use.

2. **Select the material for a named part.** Reuse or update the
   written pick style from
   [Choosing the Right Material](../choosing-materials/). Name the
   robot part (example: elevator bearing block, intake pivot, gearbox
   spacer that sees heat). Justify **why PETG is not enough**
   (impact, heat, wear, or stiffness). If PETG *is* enough, say so
   and pick a different part — do not burn CF-nylon on a cable clip.

3. **Confirm hardware with a mentor.** Verify the printer is
   enclosed, the hotend is high-temp, and a **hardened nozzle** is
   installed. Do not "just try" CF on brass. Note the printer name
   on the write-up.

4. **Dry and store.** Dry the spool per the Bambu table (shop dryer
   or AMS drying if equipped). Record start time, temperature, and
   duration. Afterward, bag it with desiccant or leave it in a dry
   AMS. If the spool already sat out overnight, dry it again — do
   not guess.

5. **Prototype, then print the real material.** If the geometry is
   new, print a PLA / PETG fit check first (cheap). Then slice the
   engineering profile: walls and orientation from the design
   ticket, not a 2-wall vase. Print on the enclosed machine. Stay
   for the first layer. Ventilation on. No reaching in.

6. **Load-test before the robot depends on it.** Apply a realistic
   load (hang weight, lever, or the actual mechanism in the shop —
   a mentor sets the safe test). Write pass / fail and the failure
   mode if it fails (layer peel, hole ovalizing, insert pull-out).
   A pretty part that you never loaded is not done.

## Acceptance Criteria

- [ ] A written material pick for a **named** structural part
      explains why an everyday filament is not enough.
- [ ] Hardened nozzle and enclosed printer were confirmed before
      the abrasive or high-temp job started.
- [ ] The spool was dried (logged) and stored with desiccant or in
      a dry AMS.
- [ ] A part (or representative coupon of that part) was printed
      in the engineering filament.
- [ ] A mentor-visible load test has a written pass / fail.
- [ ] You can state the fume and heat rules for nylon / PC without
      being prompted.

## Resources

- [Bambu: Filament drying](https://wiki.bambulab.com/en/filament-acc/filament/dry-filament)
- [Bambu: Filament index](https://wiki.bambulab.com/en/filament-acc/filament)
- [Bambu engineering filaments](https://bambulab.com/en/filament)
- [Prusa: Annealing](https://help.prusa3d.com/article/annealing_2191)
- [Bambu Wiki: Troubleshooting](https://wiki.bambulab.com/en/general/troubleshooting) —
  wet-filament symptoms
- [FIRST Game Manual and Q&A](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system) —
  full legality is the next ticket; do not skip it

## Notes

- Prototype geometry in PLA / PETG. Engineering filament is not a
  first-article material.
- Annealing can warp the part you just printed. Coupon first.
- Next — and last:
  [Maintenance & Print Farm Management](../maintenance-print-farm/).
  You will write a maintenance checklist and check printed parts
  against this season's manual, including pit rules about printers.
