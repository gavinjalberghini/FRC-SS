---
layout: printing-lesson
title: Troubleshooting Failed Prints
subtitle: Read the symptoms of adhesion, warping, stringing, layer shifts, and clogs — and fix the root cause.
permalink: /learning/printing/troubleshooting/
role: veteran
order: 9
size: 2
time: "1–2 hrs"
---

## Overview

Prints fail — the skill is diagnosing **why** from the symptoms instead of guessing.
This lesson maps the common failures to their root causes and fixes.

## Prerequisites

- [Designing for 3D Printing](../design-for-printing/) completed.

## Unit 1 — First-layer & adhesion problems

- **Part won't stick / lifts** → dirty or wrong plate, nozzle too high, bed too
  cold, or no brim. Clean the plate, re-level/recalibrate, add a brim, verify temps.
- **Nozzle dragging / no extrusion on layer 1** → nozzle too low or clogged; re-run
  bed calibration and check the z-offset.

## Unit 2 — Warping & cracking

- **Corners curl up (warping)** → material shrinkage, common in ABS/ASA; use an
  **enclosure**, a heated bed at the right temp, a brim, and avoid drafts.
- **Layers split/crack** → poor layer adhesion: print hotter, slower, or in an
  enclosure; dry the filament.

## Unit 3 — Surface defects

- **Stringing / wisps** → wet filament or too little retraction; **dry the
  filament** and tune retraction. PETG strings more than PLA.
- **Zits/blobs** → seam and retraction settings; reposition the seam.
- **Under-extrusion (gaps, thin layers)** → clog, wet/low filament, flow too low,
  or feeding issue (AMS). Check flow and the path.
- **Over-extrusion (rough, oversized)** → flow too high; calibrate flow rate.

## Unit 4 — Mechanical failures

- **Layer shift** → toolhead hit something, belt/lubrication issue, or printing too
  fast; check for collisions and run resonance calibration.
- **Spaghetti** → the part detached mid-print; Bambu's AI/camera can detect and
  pause. Fix the adhesion cause before reprinting.
- **Clog** → debris or wet/abrasive filament; clear the nozzle, and use a hardened
  nozzle for abrasive materials.

## Unit 5 — A diagnostic method

1. **Look** at where in the print it failed (layer 1 vs. mid-print tells you a lot).
2. **Match** the symptom to the categories above.
3. **Change one thing** (clean plate, dry filament, recalibrate, adjust one
   setting) and reprint a small test.
4. **Record** what fixed it so the team learns.

## Steps & acceptance criteria

- [ ] Diagnose three failed prints from their symptoms.
- [ ] Fix a first-layer adhesion failure and reprint successfully.
- [ ] Resolve stringing by drying filament and/or tuning retraction.
- [ ] Explain what causes a layer shift and how to prevent it.

## Resources

- [Bambu Wiki: Troubleshooting](https://wiki.bambulab.com/en/general/troubleshooting)
- [Simplify3D Print Quality Guide](https://www.simplify3d.com/resources/print-quality-troubleshooting/)
- [All3DP: Common problems](https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/)

## Notes

- Most "mystery" failures are a **dirty plate** or **wet filament**. Rule those out
  first before changing settings.
