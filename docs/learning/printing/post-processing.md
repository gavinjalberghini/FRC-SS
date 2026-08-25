---
layout: printing-lesson
title: Post-Processing & Part Removal
subtitle: Remove parts from the plate, take off supports cleanly, and finish a part without damaging it.
permalink: /learning/printing/post-processing/
role: operator
order: 5
size: 1
time: "45–60 min"
---

## Description

The printer stopping is not the end of the job. A part that still has
supports on it is not a robot part, and a gouged PEI plate is a week of
failed first layers. This ticket is how you get the practice part from
[Running Your First Print](../first-print/) off the plate, pull
supports, and decide whether it is good enough to use.

### Removal

Let the **bed cool**. On a flexible plate, most parts release as the
plate contracts — flex the plate over an edge and they pop off. If a
part is stuck, keep flexing. A scraper is last resort, pushed **away
from your hand**. Never gouge the plate with a metal scraper; you will
spend the next month washing a wounded surface that will not stick.

### Supports and brims

Supports are meant to snap off. Start at an edge with flush cutters or
needle-nose pliers and work them free. A **brim** peels; clean the
scar with a deburring tool or knife. Fine or internal supports take
time — forcing them cracks the part, usually along a layer line (you
already know that is the weak direction).

If supports welded themselves to the part, that is a slicer gap
problem, not a "pull harder" problem. Note it for
[Dialing In Print Settings](../dialing-in-settings/).

### Finishing

Deburr edges and snip stringing or zits. Sand visible faces if the
part will be seen (wet sand, increasing grits; PLA and PETG sand
fine). ABS can be vapor-smoothed in industry videos — **do not**
invent an acetone setup in a school shop. Holes that will take bolts
or heat-set inserts often print slightly small — a careful pass with
a drill bit or tap by hand restores size. Do not power-drill a thin
wall like it is aluminum.

A part that will take a **heat-set insert** later should have a
clean, round boss. If you already ovalized the hole with a drill,
say so; the Veteran design ticket will not fix a wrecked boss.

Then **inspect**: layer separation, under-extrusion gaps, crushed
overhangs, holes that are not round. Check the first layer face —
if it is shiny-smooshed or full of gaps, the next print needs a
plate wash, not more sandpaper. A pretty fail is still a fail. Say
keep, reprint, or reprint with a change.

### Tool safety

Flush cutters launch plastic chips — eye protection. Cut and scrape
away from your body. The nozzle and bed may still be warm if someone
queued another job; do not assume cool. Return the plate, recycle
scrap supports, leave the station clean. The farm only works if the
next operator inherits a clean plate.

This site does not track whether you finished. The cleaned part in a
mentor's hand is the evidence.

## Prerequisites

- [Running Your First Print](../first-print/) completed, with a part
  on a plate (or already popped off and waiting).
- Eye protection and the shop's flush cutters / pliers / scraper.

## What you'll learn

- How to get a part off a Bambu plate without killing the plate.
- How to pull supports and a brim without cracking the part.
- How to deburr, clean fastener holes, and reject a bad print.

## Tasks

1. **Read how finishing is supposed to go.** Read
   [All3DP: Post-processing FDM prints](https://all3dp.com/2/fdm-3d-printing-post-processing-the-ultimate-guide/)
   through the sections on support removal and sanding. Skim Bambu's
   [support](https://wiki.bambulab.com/en/software/bambu-studio/support)
   page so you know what the slicer thought it was doing.

2. **Cool, then remove.** Confirm the bed is cool enough to touch.
   Flex the plate and pop the part. Use a scraper only if a mentor
   agrees it is stuck, and only away from your body. Show the mentor
   the plate afterward — no gouges.

3. **Pull the supports.** Remove every support and the brim, if any.
   Work from an edge. If a support will not release, stop before you
   snap the part and ask whether the z-gap was too small. Save a
   small piece of support in the scrap bin, not on the floor.

4. **Finish fastener features.** Deburr sharp edges. If the part has
   holes, clean them so a real bolt starts by hand. Do not chase a
   heat-set insert yet — that is
   [Designing for 3D Printing](../design-for-printing/).

5. **Inspect and call it.** Write three lines a mentor can read:

   - keep / reprint / reprint-with-change
   - one defect you see (or "none")
   - one thing you would change in the slice next time (orientation,
     supports, walls, or nothing)

   If you keep it, say where it is allowed to go (practice bot,
   jig, bag-of-spares) and where it is **not** allowed (competition
   load path without a rules check — that is the Lead farm ticket).

6. **Reset the station.** Return the clean plate, recycle scrap, put
   tools back. A mentor should be able to start the next job without
   washing your fingerprints off the PEI. If the next operator
   inherits a dirty plate, your first-layer luck will look like
   their incompetence.

## Acceptance Criteria

- [ ] The practice part is off the plate without damage to the part
      that a careful flex would have avoided, and without gouges in
      the plate.
- [ ] Supports and brim are removed cleanly enough that a mentor
      would mount the part (or agrees a remaining scar is cosmetic).
- [ ] Fastener holes, if present, take a bolt by hand or you noted
      they need a reprint / ream.
- [ ] You wrote the keep-or-reprint call and one slice change.
- [ ] Eye protection was on while cutting; the station is reset.
- [ ] A mentor has held the finished practice part.

## Resources

- [All3DP: Post-processing FDM prints](https://all3dp.com/2/fdm-3d-printing-post-processing-the-ultimate-guide/)
- [Bambu Wiki: Support settings](https://wiki.bambulab.com/en/software/bambu-studio/support)
- [Bambu Wiki: First print](https://wiki.bambulab.com/en/general/print-first) —
  cooling and removal reminders

## Notes

- Design later so supports land on non-critical faces. Pulling
  supports off a bearing bore is how you learn that lesson the hard
  way.
- This ticket closes the Operator path: FDM and safety, a material
  pick, a 3MF, a mentored first print, and a finished part. Veteran
  work starts at
  [Dialing In Print Settings](../dialing-in-settings/).
- Do not "improve" a bad print with filler and hope it is structural.
  Reprint.
