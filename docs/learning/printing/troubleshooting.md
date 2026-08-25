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

## Description

Prints fail. The skill is diagnosing **why** from the plastic in front
of you instead of reprinting the same 3MF and hoping. This ticket
closes the Veteran path: you already slice, print with a mentor, pull
supports, tune settings, and design for FDM. Now you treat a failure
like a pit repair — look, match, change one thing, record.

Most "mystery" failures on a Bambu farm are a **dirty plate** or
**wet filament**. Rule those out before you invent a new profile.

### First layer and adhesion

- Will not stick / corner lifts → dirty or wrong plate, nozzle too
  high, bed too cold, no brim, draft. Wash the plate, recalibrate,
  add a brim, check temps and plate type in the slice.
- Nozzle dragging or no extrusion on layer 1 → nozzle too low or
  clogged. Re-run bed / first-layer calibration; check the path.

Bambu's
[first-layer test print](https://wiki.bambulab.com/en/knowledge-sharing/identify-and-fix-first-layer-issues-with-a-test-print)
is the right coupon. Do not reach in to "nudge" a lifting corner.

### Warping and cracking

- Corners curl (warp) → shrinkage, common in ABS / ASA. Enclosure
  (X1C / P1S), correct bed temp, brim, no draft. An A1 is the wrong
  printer for that material — you learned that in
  [Choosing the Right Material](../choosing-materials/).
- Layers split → poor layer adhesion: hotter, slower, enclosed, or
  **dry the filament**.

### Surface defects

- Stringing → wet filament or too little retraction. Dry first;
  then tune retraction. PETG strings more than PLA.
- Zits / blobs → seam and retraction; move the seam.
- Under-extrusion (gaps) → clog, wet or empty spool, flow too low,
  AMS feed. Check the path before you raise flow 20%.
- Over-extrusion (fat, rough) → flow too high; calibrate flow.

### Mechanical failures

- Layer shift → toolhead hit something (a detached part, a tab),
  belt or lube issue, or too fast. Check collisions; run resonance
  calibration.
- Spaghetti → the part detached mid-print. Bambu AI / camera can
  pause. Fix adhesion before reprinting.
- Clog → debris, wet filament, or abrasive dust. Clear the nozzle.
  Hardened nozzle for CF / GF — a chewed brass nozzle is a clog
  factory.

### A method, not a vibe

1. **Look** at *where* it failed (layer 1 vs mid-print vs last
   layers).
2. **Match** the symptom to a category above.
3. **Change one thing** (wash, dry, recalibrate, one setting) and
   reprint a small test.
4. **Record** what fixed it so the next operator does not repeat
   your evening.

Teaching Tech's
[troubleshooting site](https://teachingtechyt.github.io/troubleshooting.html)
is written for hobby printers (endstops, BLTouch, terminals). Use the
**First layer** and **Filament jams** thinking; do not open a Marlin
console on a shop X1C. Official Bambu steps are in
[Wiki: Troubleshooting](https://wiki.bambulab.com/en/general/troubleshooting).

This site does not track failed prints. The write-up and the
successful reprint are what a mentor signs.

## Prerequisites

- [Designing for 3D Printing](../design-for-printing/) completed.
- Access to a failed print (shop scrap, a photo archive, or one you
  cause on a coupon — do not sabotage a competition part).
- Permission to wash plates, dry a spool, and run a short test.

## What you'll learn

- How to map a symptom to a first-layer, warp, surface, or
  mechanical cause.
- How to fix adhesion and stringing with one change each.
- What a layer shift actually is, and how you prevent the next one.

## Tasks

1. **Read three troubleshooting sources.** Skim
   [Bambu Wiki: Troubleshooting](https://wiki.bambulab.com/en/general/troubleshooting),
   [All3DP: common problems](https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/),
   and the First layer / Filament jams tabs on
   [Teaching Tech troubleshooting](https://teachingtechyt.github.io/troubleshooting.html).
   Keep Bambu's official steps as the ones you will *do* on shop
   machines.

2. **Diagnose three failures from symptoms.** Use three real
   failures (scrap bin, photos, or mentor examples). For each,
   write:

   - where in the print it died
   - the symptom name (adhesion, warp, stringing, under-extrusion,
     shift, spaghetti, clog)
   - the first thing you would change
   - what you would *not* change yet

   A mentor should disagree with at least one guess if you are
   guessing.

3. **Fix a first-layer adhesion failure.** Print a small first-layer
   coupon or restart a part that lifted. Wash the plate (soap or
   IPA), confirm plate type matches the slice, and re-run
   calibration if a mentor wants it. Get a first layer that sticks.
   Photograph before and after if you can.

4. **Kill stringing or name why you cannot.** If a shop print is
   hairy: dry the spool per
   [Bambu drying](https://wiki.bambulab.com/en/filament-acc/filament/dry-filament)
   (or the shop dryer) and / or change one retraction-related
   setting. If every spool is already dry and PLA-clean, write why
   PETG still strings and what you would try next. Do not boil a
   PLA profile to 280 °C.

5. **Explain a layer shift.** Point at a shifted scrap or a photo.
   Tell a mentor: what the toolhead hit or what ran loose, why
   reprinting the same file can shift again, and one prevention
   (clear the plate of debris, check belts, slow down, resonance
   calibration). Do not take a printer apart without a lead.

6. **Log the fix.** Add a short entry to the shop log or a note on
   the exported ticket: date, printer, symptom, one change, result.
   The farm ticket will ask for a real maintenance log — start the
   habit.

## Acceptance Criteria

- [ ] Three written diagnoses exist, each with a symptom, a first
      change, and a "do not touch yet."
- [ ] A first-layer adhesion failure was fixed and a coupon or part
      reprinted successfully (mentor-visible).
- [ ] Stringing was reduced by drying and / or one retraction
      change, *or* you wrote a PETG-specific reason a mentor
      accepts.
- [ ] You can explain a layer shift and one prevention without
      blaming "the slicer" in the abstract.
- [ ] A log line exists. This website is not the log.

## Resources

- [Bambu Wiki: Troubleshooting](https://wiki.bambulab.com/en/general/troubleshooting)
- [Bambu: First-layer test print](https://wiki.bambulab.com/en/knowledge-sharing/identify-and-fix-first-layer-issues-with-a-test-print)
- [Bambu: Filament drying](https://wiki.bambulab.com/en/filament-acc/filament/dry-filament)
- [All3DP: Common 3D printing problems](https://all3dp.com/1/common-3d-printing-problems-troubleshooting-3d-printer-issues/)
- [Simplify3D print quality guide](https://www.simplify3d.com/resources/print-quality-troubleshooting/)
- [Teaching Tech troubleshooting](https://teachingtechyt.github.io/troubleshooting.html)
- [Teaching Tech calibration site](https://teachingtechyt.github.io/calibration.html)

## Notes

- Dirty plate, then wet filament, then one setting. That order
  saves profiles.
- Never reach into a running printer to save a lifting corner.
  Pause or stop.
- Veteran path ends here. Lead work starts at
  [Engineering Materials & Advanced Printing](../engineering-materials/)
  — nylon, CF, hardened nozzles, and load-tested parts.
