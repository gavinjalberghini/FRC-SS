---
layout: printing-lesson
title: 3D Printing Fundamentals & Safety
subtitle: How FDM printing works, the Bambu printer lineup and anatomy, and the safety rules before you print.
permalink: /learning/printing/fundamentals-safety/
role: operator
order: 1
size: 1
time: "45–60 min"
---

## Description

An FRC shop that owns printers still fails prints when nobody can name the
parts of the machine or say why a part cracked. This ticket is the gate.
**You do not run a printer unsupervised until a mentor signs off the
criteria below.**

**Fused-deposition modeling (FDM)** is how every Bambu Lab printer on this
team works. The printer melts a plastic **filament** and pushes it through a
**nozzle**. The nozzle draws the outline of one thin **layer**, then fills
the inside, then steps up and draws the next layer. Those layers fuse while
they are still hot. The stack of fused layers *is* the part.

A few words you will use for the rest of this track:

- **Filament** — the spool of plastic the printer melts. Diameter on Bambu
  machines is 1.75 mm. The material (PLA, PETG, ABS, and the rest) is a
  later ticket; the idea that *material choice matters* starts here.
- **Nozzle / hotend** — the heated tip that extrudes plastic. Typical
  temperatures are 200–300 °C. That is a burn, instantly.
- **Bed / build plate** — the removable plate the first layer sticks to.
  It is often heated. Textured PEI is the everyday plate for PLA and PETG.
- **Layer** — one horizontal slice of the part. Smaller layers look finer
  and take longer. Parts are **weakest between layers** — the bond between
  two layers is weaker than the plastic along a layer. That fact drives
  orientation, which you will practice when you slice.
- **Walls (shells)** — the solid loops around the outside of each layer.
  Most of a functional part's strength lives in the walls, not the infill.
- **Infill** — the internal pattern that fills the hollow. Density and
  pattern are slicer settings, not something the printer invents.

The printer cannot read a CAD model. A **slicer** — we use **Bambu
Studio** — turns an STL or 3MF into layer-by-layer toolpaths. You will
install and use Studio in ticket 3. You only need to know it exists now.

This shop standardizes on **Bambu Lab** machines:

- **X1 / X1-Carbon (X1C)** — enclosed, fastest, lidar and a camera.
  Rated for high-temp and abrasive filaments when the right hotend and
  nozzle are installed.
- **P1S** — enclosed workhorse with the same core motion as the X1C and
  fewer sensors.
- **A1 / A1 mini** — open-frame bed-slingers. Excellent for PLA and PETG.
  Not the printer for ABS, ASA, or nylon that need a closed, warm chamber.
- **AMS / AMS lite** — the Automatic Material System. Holds multiple
  spools and switches them mid-print.

On a real printer you should be able to point to the **nozzle**, **bed**,
**extruder / toolhead**, **AMS** (if fitted), and the **touchscreen**.
Remote monitoring uses the **Bambu Handy** app. Watching a camera is not
the same as standing there for the first layer.

Safety is not a poster. The nozzle and bed burn skin. **Never reach into
a running printer** — pause or stop it and wait. PLA and PETG are
low-odor; **ABS, ASA, and nylon emit fumes** and belong on an enclosed
printer in a ventilated area. Hair, hoodie strings, and fingers stay
clear of the toolhead. Scrapers and flush cutters cut *away* from your
body. Do not leave the first layer of a new setup unattended. Know the
printer's power switch and the shop fire extinguisher.

This site does not track whether you finished. If your team exported these
tickets into its own GitHub, close this issue there once a mentor accepts
the criteria below.

## Prerequisites

- None. This is the first lesson for every 3D-printing team member.
- A mentor who can walk the shop printers with you.

## What you'll learn

- How FDM builds a part from filament, nozzle, bed, layers, walls, and
  infill — and why parts are weakest between layers.
- Which Bambu printers the shop has, which are enclosed, and what each
  is for.
- The safety rules that keep you from burns, cuts, and breathing ABS
  fumes.

## Tasks

1. **Watch how FDM works.** Read
   [All3DP: How FDM / FFF 3D printing works](https://all3dp.com/2/fused-deposition-modeling-fdm-3d-printing-simply-explained/)
   and skim the overview on the
   [Bambu Lab Wiki](https://wiki.bambulab.com/).
   Write four sentences in a scratch note (keep it — later tickets reuse
   it): *Filament is …*; *A layer is …*; *Walls are …*; *Infill is …*.
   Add one more sentence: *Parts are weakest between layers because …*.

2. **Walk the shop lineup.** With a mentor, stand in front of every Bambu
   printer the team owns. For each machine, say out loud whether it is an
   X1C, P1S, A1, or A1 mini, whether it is **enclosed**, and which
   materials a mentor will allow on it. Open-frame A1-class printers are
   not the place to learn ABS. Confirm which machines have an AMS.

3. **Point to the anatomy.** On one printer, point to the nozzle, the
   build plate, the extruder / toolhead, the AMS (if present), and the
   screen. State a typical nozzle temperature range and that the bed can
   also be hot enough to burn. If the shop uses Bambu Handy, have a
   mentor show you the camera view — and say why the camera does not
   replace watching the first layer in person.

4. **Learn the safety rules, then say them back.** Read Bambu's
   [First print](https://wiki.bambulab.com/en/general/print-first)
   page far enough to see the warnings about heat and the first layer.
   Then tell a mentor, without reading:

   - never reach into a running printer
   - wait for the nozzle and bed to cool before you touch them
   - ABS / ASA / nylon need an enclosure and ventilation
   - cut and scrape away from your body
   - where the power switch and the fire extinguisher are

5. **Hand the note to a mentor.** Show the five sentences from Task 1
   and complete the shop walk. If your team exported these tickets, paste
   a photo of the signed safety line (or the mentor's name and date) on
   this issue and move it to In Review.

## Acceptance Criteria

- [ ] You can explain, in your own words, how FDM builds a part and why
      it is weakest between layers.
- [ ] Your scratch note defines filament, layer, walls, and infill.
- [ ] You identified each Bambu printer in the shop, said whether it is
      enclosed, and named at least one material that does *not* belong
      on an open-frame machine.
- [ ] On a real printer you pointed to the nozzle, bed, extruder, and
      AMS (or said the shop has none).
- [ ] You stated the hot-surface, fume, moving-part, and first-layer
      rules, including **never reach into a running printer**.
- [ ] A mentor has given 3D-printing safety sign-off. This website is
      not that sign-off.

## Resources

- [Bambu Lab Wiki](https://wiki.bambulab.com/) — official printer
  documentation
- [Bambu Wiki: First print](https://wiki.bambulab.com/en/general/print-first)
- [Bambu Lab printers and specs](https://bambulab.com/)
- [All3DP: How FDM / FFF 3D printing works](https://all3dp.com/2/fused-deposition-modeling-fdm-3d-printing-simply-explained/)
- [Teaching Tech companion site](https://teachingtechyt.github.io/) —
  later tickets use the calibration and troubleshooting pages; the
  homepage is enough today
- [Bambu Handy / Studio downloads](https://bambulab.com/en/download)

## Notes

- Safety sign-off is a shop conversation, not a checkbox on this
  website. This site does not store progress.
- You are not loading filament or starting a print in this ticket. That
  is [Running Your First Print](../first-print/), after materials and
  slicing.
- The next ticket ([Choosing the Right Material](../choosing-materials/))
  is where filament choice meets FRC: impact, heat, and the game manual.
  Bring the sentences from Task 1 with you.
