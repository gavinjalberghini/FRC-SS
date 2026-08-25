---
layout: printing-lesson
title: Running Your First Print
subtitle: Load filament and the AMS, prep the plate, calibrate, start a print, and monitor it to completion.
permalink: /learning/printing/first-print/
role: operator
order: 4
size: 2
time: "1–2 hrs"
---

## Description

Slicing is not a part. This ticket is the first time you turn the 3MF
from [Slicing in Bambu Studio](../slicing-bambu-studio/) into plastic
on a Bambu printer. **A mentor stays with you through load, first
layer, and the decision to keep going.** You do not start a printer
alone on this ticket.

The motion is always the same: load filament that matches the slice,
mount a **clean** plate that matches the slice, let Bambu run
calibration when it should, watch layer 1 like it is the whole print,
then let the bed cool before you pick anything up.

### Loading filament

- **Direct spool:** mount the spool, feed into the extruder, run
  **Load filament** on the screen, and wait until clean plastic of the
  right color purges.
- **AMS:** seat the spool in a slot. Bambu RFID fills material and
  color; third-party spools you set by hand. The AMS slot in the slice
  must match the slot in the box.

If the slice says PETG and the AMS is holding PLA, stop. That mismatch
is how you print a heat-soft part with the wrong temps.

### Build plate

Choose the plate the slice expects (textured PEI for everyday PLA /
PETG). Oils from fingerprints ruin adhesion. Wash with dish soap and
water or wipe with IPA, and handle by the edges. Seat the plate fully
on the locating features. A clean plate fixes most "it won't stick"
failures. When in doubt, wash it.

### Calibration

Bambu printers run automatic calibration at the start: bed leveling,
and on capable models flow and resonance. For a new filament or a
first print on a machine you do not know, let it run. Repeats of a
known-good job can skip some of it to save time — a mentor will say
which. Official steps live in
[Printer calibration](https://wiki.bambulab.com/en/general/printer-calibration)
and
[First print](https://wiki.bambulab.com/en/general/print-first).

### Start and monitor

Confirm filament, plate, and printer in the send dialog match reality.
Start the print. **Watch the first layer.** It should lay down evenly
and stick. If it is not adhering, or the nozzle is digging a trench,
stop and fix it — do not "hope layer 4 saves it."

You may monitor later layers on the camera / **Bambu Handy** app. That
does not replace staying for layer 1. **Never reach into a running
printer.** Pause or stop, wait for the toolhead to park, then act.

### Finish

Wait for the **bed to cool**. Most parts pop off a flexible plate on
their own. Removing supports and finishing the part is the next ticket,
[Post-Processing & Part Removal](../post-processing/). Today you get
the part off safely or leave it on the cooled plate for that lesson.
Return the plate. Clean the area.

If the print looks failed, do not mash restart. Diagnose first —
[Troubleshooting Failed Prints](../troubleshooting/) is the Veteran
ticket for that. On this ticket, stop and get a mentor.

This site does not track whether you finished. The finished practice
part (or the cooled plate with the part still on it) is what a mentor
sees.

## Prerequisites

- [Slicing in Bambu Studio](../slicing-bambu-studio/) completed, with
  a mentor-visible `.3mf`.
- Safety sign-off from
  [3D Printing Fundamentals & Safety](../fundamentals-safety/).
- A mentor present for load, start, and first layer.
- Shop filament and a plate that match the 3MF.

## What you'll learn

- How to load filament on a direct spool and through the AMS.
- How to pick, clean, and seat the plate the slice expects.
- How to start a Bambu job and judge a first layer.
- How to monitor without putting a hand in a moving, hot machine.

## Tasks

1. **Read the official first-print path.** Read
   [Bambu Wiki: First print](https://wiki.bambulab.com/en/general/print-first)
   and skim
   [Build plates](https://wiki.bambulab.com/en/x1/manual/bambu-cool-plate)
   (or the plate page for the model you are using). Note the plate
   type your 3MF selected.

2. **Load filament two ways if the shop can.** Load one spool **direct**
   (or watch a mentor do the path you cannot reach) and load or assign
   one spool **in the AMS**. Wait for a clean purge of the right
   color. If the shop has only AMS or only direct, do the one you
   have and write which one you still need to see.

3. **Prep the plate.** Choose the plate that matches the slice. Wash
   or IPA-wipe it. Handle edges only. Seat it fully. Tell the mentor
   why a fingerprint is enough to lift a corner.

4. **Start the sliced job with a mentor.** Open your 3MF, confirm
   printer, filament, and plate, and send or start from the printer.
   Let calibration run unless a mentor skips a known-good repeat.
   **Stay at the machine through the first layer.**

5. **Call the first layer.** Say out loud: sticking evenly, not
   sticking, or nozzle too low. If it is bad, stop. Do not reach in.
   If it is good, you may step back and use
   [Bambu Handy](https://bambulab.com/en/download) or the printer
   camera for later layers. Check in; do not vanish for a four-hour
   print.

6. **Finish the job.** When the printer is done, wait for the bed to
   cool. Flex the plate or leave the part for the next ticket. Do not
   yank a hot part. Return the plate and clean up. If the print
   failed, photograph it and stop — diagnosis is a later ticket, not
   a silent reprint.

7. **Show the part to a mentor.** A finished practice part they can
   hold (or a clearly failed first layer they watched you stop) is
   the evidence. If tickets are exported, note whose printer and
   which 3MF, and move the card to In Review.

## Acceptance Criteria

- [ ] Filament was loaded (direct, AMS, or both) and purged clean in
      the color / material the 3MF named.
- [ ] The correct plate was cleaned and seated; you can explain why
      fingerprints kill adhesion.
- [ ] A mentor was present when the print started.
- [ ] You watched the first layer and either kept a good one or
      stopped a bad one without reaching into the running printer.
- [ ] The print ran to completion or was stopped on purpose with a
      reason a mentor heard.
- [ ] A practice part exists off (or on a cooled) plate — the same
      job you sliced — and a mentor has seen it.

## Resources

- [Bambu Wiki: First print](https://wiki.bambulab.com/en/general/print-first)
- [Bambu Wiki: Build plates](https://wiki.bambulab.com/en/x1/manual/bambu-cool-plate)
- [Bambu Wiki: Printer calibration](https://wiki.bambulab.com/en/general/printer-calibration)
- [Bambu Wiki: First-layer test print](https://wiki.bambulab.com/en/knowledge-sharing/identify-and-fix-first-layer-issues-with-a-test-print)
- [Bambu Handy app](https://bambulab.com/en/download)

## Notes

- A clean plate fixes most first-layer adhesion problems. Wash before
  you change z-offset folklore.
- Never restart a "failed-looking" print by force. Stop, photograph,
  get a mentor. Troubleshooting is its own ticket.
- The camera is a check-in tool, not a first-layer substitute.
- Next: [Post-Processing & Part Removal](../post-processing/) — pull
  supports, deburr, and decide if the part is usable.
