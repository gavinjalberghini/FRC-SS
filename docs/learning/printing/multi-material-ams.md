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

## Description

The **Automatic Material System (AMS)** is why a Bambu printer can
hold several spools and switch mid-print — team colors on a cover,
a label in a second plastic, or a breakaway support material. It is
also why a four-color mascot can burn a half-spool of purge ("poop")
overnight. This ticket is how to run the AMS on purpose, not because
the button existed.

You already load a single AMS slot in
[Running Your First Print](../first-print/) and you already tune
supports in
[Dialing In Print Settings](../dialing-in-settings/). Here the new
skills are **slot assignment**, **color painting**, **flushing**, and
**which materials may share a nozzle**.

### How the AMS works

One AMS holds up to four spools and feeds the selected one to the
extruder. Some shops chain **multiple AMS units**. Bambu spools
identify themselves with **RFID**. Third-party spools need material,
color, and temperatures set by hand — wrong temps are still wrong
when the box is fancy.

Wet or stringy filament makes AMS feeding unreliable. Keep everyday
spools dry enough to feed; engineering dryness is the Lead ticket.

### Multi-color in Studio

Add filaments to the project. **Paint** color onto the model (face,
height, or the color tools) or assign colors to separate objects.
Map each project filament to an **AMS slot**. Preview the toolpath
and confirm the color changes happen where you think. A painted
model that still slices as one color is almost always a slot or
filament-assignment miss.

### Purging and flushing

Every color change **purges** old filament so colors do not mix.
That waste is real time and real money. **Flushing volumes**:
light-into-dark needs less purge than dark-into-light. Higher
volumes look cleaner and waste more. A **prime tower** can absorb
purges and keep the nozzle primed. If the part is functional and
one color, **do not use the AMS for theater**.

### Multi-material combinations

You can combine materials — for example a PLA or PETG body with
PVA / dissolvable or breakaway supports — only when the pair is
**meant to interface**. Mismatched nozzle temperatures and poor
interlayer bonding delaminate. PLA + PETG can work for some
assemblies and fail as a single fused body. TPU next to a rigid
material is a grip, not a weld, unless you have a known process.
Never mix a CF-filled abrasive with a brass-nozzle PLA workflow
on the same toolhead without a mentor and a hardened nozzle.

This site does not track whether you finished. A mentor should see
a two-color (or two-material) 3MF and hear you explain the purge
cost.

## Prerequisites

- [Dialing In Print Settings](../dialing-in-settings/) completed.
- A printer with an AMS (or AMS lite) and at least two spools a
  mentor will let you load.
- Safety habits from
  [Fundamentals & Safety](../fundamentals-safety/) still apply:
  do not reach into a running printer during a toolchange.

## What you'll learn

- How RFID and manual AMS slots map onto Studio filaments.
- How to paint a two-color model and verify it in Preview.
- Why purge exists, and how flushing volume changes waste.
- Which material pairs are valid on one nozzle.

## Tasks

1. **Read the AMS docs.** Read
   [Bambu Wiki: AMS](https://wiki.bambulab.com/en/ams/manual)
   and
   [Multi-color printing](https://wiki.bambulab.com/en/software/bambu-studio/multi-color-printing).
   Write two sentences: what the AMS does mechanically, and what
   RFID does *not* do for a third-party spool.

2. **Load and assign two spools.** Load two compatible filaments
   (two PLA colors, or PLA + PETG only if a mentor wants that
   experiment). Set any third-party spool by hand. In Studio,
   assign each project filament to the actual AMS slot. Photograph
   or write the slot map (`slot 1 = PLA red`, …).

3. **Paint a two-color model.** Import a simple part (a cover, a
   team-number plaque, or a calibration cube). Paint a second color
   on a face or a letter. Slice and scrub Preview until you see the
   color change. If Preview is still one color, fix the assignment
   before you waste a plate.

4. **Account for purge.** In the slice estimates, find filament
   used for the part versus flushed / purged. Write whether this
   job is worth AMS color: a competition cover with a legal number,
   or a one-off that should have been a marker. Tune flushing
   volumes one step (dark-into-light vs light-into-dark) and note
   which way needed more.

5. **Name a valid and an invalid combo.** On paper:

   - one pair you would print (two PLA colors, or PLA body +
     official support filament)
   - one pair you would refuse (example: CF-nylon and TPU on a
     brass nozzle; ABS on an A1 with PLA still in the AMS path)

   A mentor should agree with both.

6. **Print only if the queue and waste budget allow.** A short
   two-color coupon is enough. A four-color mascot is not this
   ticket. Stay for the first layer and the first toolchange. Never
   reach in during a purge. If you do not print, the 3MF plus the
   purge math is still acceptable — say so to the mentor.

## Acceptance Criteria

- [ ] Two (or more) spools are loaded and mapped to Studio
      filaments / AMS slots. Third-party spools are set manually.
- [ ] A two-color model was painted and the color change is visible
      in Preview. A mentor can open the 3MF and see it.
- [ ] You stated how much extra filament purge would use on that
      job and whether the color was worth it.
- [ ] You named one valid and one invalid multi-material
      combination, with a reason (temps, enclosure, nozzle, or
      bonding).
- [ ] If a print ran, a mentor saw the first toolchange and you
      did not reach into the machine.

## Resources

- [Bambu Wiki: AMS](https://wiki.bambulab.com/en/ams/manual)
- [Bambu Wiki: Multi-color printing](https://wiki.bambulab.com/en/software/bambu-studio/multi-color-printing)
- [Bambu Wiki: Support filament](https://wiki.bambulab.com/en/filament/support)
- [Bambu Studio Wiki](https://wiki.bambulab.com/en/software/bambu-studio)

## Notes

- Multi-color wastes filament and time. Use it when a second color
  is function (labels, inspection marks) or a rare demo — not as
  the default for every bracket.
- Wet filament in the AMS is a feed failure looking for a place to
  happen. If a slot keeps chewing, dry or reseat before you redesign
  the model.
- Next:
  [Designing for 3D Printing](../design-for-printing/)
  — CAD decisions that make supports, holes, and orientation
  someone else's problem.
