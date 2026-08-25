---
layout: printing-lesson
title: Maintenance & Print Farm Management
subtitle: Calibration and maintenance routines, firmware, managing multiple printers, and FRC rules on printed parts.
permalink: /learning/printing/maintenance-print-farm/
role: lead
order: 11
size: 2
time: "Ongoing"
---

## Description

A single tuned X1C is a tool. Three printers with no log, mixed
nozzles, and wet nylon is a liability. As printing lead you keep every
Bambu machine healthy and you keep the parts that leave the farm
**legal**. This last ticket is maintenance, calibration, queue
discipline, and the **current FIRST game manual** — not a vibe about
what was legal two seasons ago.

You have already printed, diagnosed, and (if the shop runs them)
printed engineering filaments. The new work is *systems*: a checklist
someone else can follow on a Saturday, and a rules check before a
printed part is the robot's only intake.

### Routine maintenance

Follow Bambu's periodic guides for the model you own (X1-class
starting point:
[X1 maintenance](https://wiki.bambulab.com/en/x1/maintenance)). In
practice:

- **Plates** — wash often; replace when the texture is dead.
- **Nozzles** — inspect wear after abrasive filament; keep brass and
  hardened nozzles on the *right* printers. Label the toolhead.
- **Lube** — lead screws and rails on Bambu's schedule; dirty carbon
  rods make quality look like a slicer bug.
- **Belts** — tension. Loose belts are layer shifts and ringing.
- **Hotend / extruder** — debris, clogs, clean path.
- **A log per printer** — date, who, what. Memory is not a log.

### Calibration

Run Bambu
[auto calibration](https://wiki.bambulab.com/en/general/printer-calibration)
(bed, flow, resonance) after maintenance, nozzle changes, or when
quality drifts. Calibrate flow / pressure advance per new filament
when cosmetics or dimensions matter. Verify with a **test coupon**
when you introduce a material. Teaching Tech's
[calibration site](https://teachingtechyt.github.io/calibration.html)
explains the *ideas*; Bambu's on-printer routines are what you run.

### Firmware and software

Keep printer **firmware** and **Bambu Studio** current, but do not
update the night before an event without a test print. Keep a shared
library of **validated profiles** so an Operator does not invent
`final-final-v3`. Release notes:
[firmware history](https://wiki.bambulab.com/en/general/firmware-release-history).

### Running a small farm

Queue and prioritize in build season: long structural jobs get a
named printer and a named owner. Track filament (and keep engineering
spools dry). Dedicate a machine to abrasive CF if you can, so you are
not swapping nozzles twice a day. Label finished parts. Monitor with
cameras / Handy — still never reach into a running printer, including
at 11 p.m.

### FRC rules (read this season's text)

Printed parts are typically **FABRICATED ITEMS**: they are not COTS
just because the STL came from the internet. They have a material
cost. Inspectors will ask.

Every season's **Robot rules (R-section)** can restrict materials,
bumpers, and mechanisms. Hard plastics on bumper faces can damage
another robot's bumper fabric — a printed "bumper pad" that is actually
PETG is a rules problem, which is why the Operator material ticket
wanted TPU there.

Event rules that have shown up in recent manuals (confirm the
**current** numbers; they move):

- **Load-in exceptions** — 3D printed parts have been listed among
  items that may enter after the main robot load-in (see the Load-In
  section of the event rules, e.g. E401 in the 2026 REBUILT manual).
- **No automated tools overnight** — teams may not run a 3D printer
  (or similar) overnight in the pit (e.g. E510 in that same manual).
  Plan reprints *before* pits close.

Start from
[Game Manual and Q&A](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
and
[Season Materials](https://www.firstinspires.org/resources/library/frc/season-materials).
Search the PDF for `3D print`, `FABRICATED`, `BUMPER`, and `pit`.
When this curriculum and the manual disagree, the manual wins.
Q&A answers are part of the rules.

This site does not track your farm. The checklist and the rules
write-up live on the team's drive or exported GitHub.

## Prerequisites

- [Engineering Materials & Advanced Printing](../engineering-materials/)
  completed (or a mentor waiver if the shop has no CF filament —
  you still do maintenance and rules).
- Authority to maintain printers and to say no to an illegal part.

## What you'll learn

- A maintenance and calibration rhythm for Bambu X1C / P1S / A1
  machines.
- How to run more than one printer without losing filament or
  nozzles.
- How to prove a printed part is legal under *this* season's
  manual, including pit printer rules.

## Tasks

1. **Read Bambu maintenance for your models.** Open
   [X1 maintenance](https://wiki.bambulab.com/en/x1/maintenance)
   and the matching pages for P1S / A1 if the shop has them. List
   the periodic items (plates, nozzles, rods, lead screws, belts)
   you will put on the checklist.

2. **Perform and log maintenance on one printer.** With a mentor,
   do a real service: clean plate, inspect nozzle, clean rails or
   rods as specified, check belt feel. Write the log line (date,
   printer, actions, next due). If something is worn, tag it — do
   not quietly put a bald plate back.

3. **Calibrate and coupon.** Run the appropriate
   [calibration](https://wiki.bambulab.com/en/general/printer-calibration)
   after that service (or after a nozzle change). Print a small
   dimensional coupon. Measure one feature with calipers and record
   nominal vs actual.

4. **Publish one validated profile.** Save a named Studio process
   or filament profile the next Operator is allowed to use (example:
   `team-PETG-functional-0.20-4wall`). Put it where the team
   actually looks (shared drive, exported 3MF, Studio team library).
   One sentence on what it is *for*.

5. **Run a short farm sprint.** For one meeting or weekend: a
   written queue (part, material, printer, owner, priority), a
   filament count for those jobs, and a note on which printer is
   allowed to run abrasive filament. You do not need five machines.
   Two jobs and a leftover spool count is enough to prove the
   habit.

6. **Check printed-part rules in the current manual.** Open this
   season's manual from
   [Season Materials](https://www.firstinspires.org/resources/library/frc/season-materials)
   or
   [Game Manual and Q&A](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system).
   Write a one-page (or equivalent) brief a mentor can file:

   - definition of FABRICATED ITEM (quote or paraphrase with
     section number)
   - any R-rule that affects plastics, printed mechanisms, or
     bumpers
   - current pit / load-in rules that mention 3D printers or
     printed parts (search `3D print`)
   - a **named robot part** (the engineering-material part or
     another) marked **legal / illegal / needs Q&A**, with the
     citation
   - a sentence that Q&A and Team Updates override last year's
     memory

   If the manual has changed names or numbers since this ticket was
   written, use the current ones.

7. **Hand over the maintenance checklist.** Turn Task 1–2 into a
   one-page checklist the next lead can photocopy: daily (plates,
   first layer), weekly (nozzle look, rails), per-spool (dry,
   profile), per-event (no overnight pit prints, spare plates,
   legal-parts list). A mentor initials that they have seen it.

## Acceptance Criteria

- [ ] Routine maintenance was performed on a real printer and
      logged.
- [ ] Calibration ran after that work; a coupon was measured.
- [ ] A named, shared, validated print profile exists.
- [ ] A multi-job queue and filament note existed for one build
      sprint (even a small one).
- [ ] A written rules brief cites **this season's** manual for
      fabricated / printed parts, bumpers if relevant, and pit
      printer rules, plus a legal/illegal call on a named part.
- [ ] A mentor-visible **maintenance checklist** exists on paper
      or the team's drive. This website is not that checklist.

## Resources

- [Bambu Wiki: X1 maintenance](https://wiki.bambulab.com/en/x1/maintenance)
- [Bambu Wiki: Printer calibration](https://wiki.bambulab.com/en/general/printer-calibration)
- [Bambu firmware release notes](https://wiki.bambulab.com/en/general/firmware-release-history)
- [Bambu Lab Wiki home](https://wiki.bambulab.com/)
- [Teaching Tech calibration site](https://teachingtechyt.github.io/calibration.html)
- [FIRST: Game Manual and Q&A](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [FIRST: Season Materials](https://www.firstinspires.org/resources/library/frc/season-materials)
- [2026 Game Manual PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf) —
  use only if it is still the current season file; prefer Season
  Materials when a newer manual exists

## Notes

- Updating firmware in the venue parking lot is how you print
  nothing on Friday. Test at home.
- The Operator path started at safety and FDM words. The Lead path
  ends when the farm is logged, the checklist is real, and a named
  part has a manual citation. If a student only wanted to "learn
  3D printing," they still owe the rules page before a part goes
  in a bag for inspection.
- This site does not close the ticket for you. A mentor does, on
  the team's board.
