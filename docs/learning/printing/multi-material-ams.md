---
layout: printing-lesson
title: Multi-Color & Multi-Material with the AMS
subtitle: Run the AMS for multi-color and multi-material prints, and manage purging, flushing, and combos.
permalink: /learning/printing/multi-material-ams/
role: veteran
order: 7
size: 2
time: "1–2 hrs"
---

## Overview

The **Automatic Material System (AMS)** lets a Bambu printer use multiple spools in
one print — for team colors, labels, or combining materials. This lesson covers
how to set it up and the trade-offs to manage.

## Prerequisites

- [Dialing In Print Settings](../dialing-in-settings/) completed.

## Unit 1 — How the AMS works

- The AMS holds up to four spools and feeds the selected one to the extruder,
  switching automatically mid-print.
- A printer can chain **multiple AMS units** for more colors/materials.
- Bambu spools are identified by **RFID**; third-party spools must be set manually
  (material, color, temps).

## Unit 2 — Multi-color slicing

- In Bambu Studio, add filaments to the project and **paint** colors onto the model
  (by face, by height, or with the color tools), or assign colors to separate
  objects.
- Assign each project filament to an **AMS slot**.
- Preview to confirm the color changes happen where you expect.

## Unit 3 — Purging & flushing

- On every color change the printer **purges** old filament so colors don't mix —
  this creates waste (the "poop") and adds time.
- Tune **flushing volumes**: light→dark needs less purge than dark→light. Higher
  volumes = cleaner colors but more waste.
- A **prime tower** can absorb purges and keep the toolhead primed.

## Unit 4 — Multi-material combinations

- You can combine materials (e.g., a **PLA/PETG** body with **PVA/dissolvable** or
  breakaway supports), but only **compatible** materials bond or interface well.
- Mismatched temperatures and poor interlayer bonding cause failures — check that
  the materials are meant to be combined.
- Wet or stringy materials make AMS feeding unreliable; keep spools dry.

## Steps & acceptance criteria

- [ ] Load and assign multiple spools in the AMS and the slice.
- [ ] Paint a two-color model and verify the changes in preview.
- [ ] Explain purging waste and tune flushing volumes.
- [ ] Identify a valid vs. invalid multi-material combination.

## Resources

- [Bambu Wiki: AMS](https://wiki.bambulab.com/en/ams/manual)
- [Bambu Wiki: Multi-color printing](https://wiki.bambulab.com/en/software/bambu-studio/multi-color-printing)

## Notes

- Multi-color prints waste filament and time on purges — only use the AMS for color
  when it's worth it; for pure function, a single spool is faster.
