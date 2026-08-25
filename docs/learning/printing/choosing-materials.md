---
layout: printing-lesson
title: Choosing the Right Material
subtitle: PLA, PETG, ABS/ASA, TPU, and nylon — their properties and how to pick the right one for an FRC part.
permalink: /learning/printing/choosing-materials/
role: operator
order: 2
size: 2
time: "1–2 hrs"
---

## Description

The single most important decision for a printed FRC part is **what
filament to print it in**. A beautiful PLA bracket that sits next to a
motor will sag in a hot pit. A brittle cover will shatter the first time
the robot takes a hit. Wrong material wastes hours and fails on the
field.

You already know from
[3D Printing Fundamentals & Safety](../fundamentals-safety/) that FDM
melts filament through a nozzle onto a bed, in layers, with walls and
infill. This ticket is about *which* plastic, and why that choice is an
engineering decision — not a color decision.

The everyday filaments in this shop:

- **PLA** — easy, stiff, dimensionally accurate, cheap. Softens in a
  hot car, near motors, or under a brake. Brittle under impact. Use it
  for prototypes, jigs, fixtures, and non-structural covers that stay
  cool.
- **PETG** — tougher and more heat-resistant than PLA, with good layer
  adhesion and a little flex. The everyday workhorse for functional
  robot parts. Slightly stringy; dry it if prints look hairy.
- **ABS / ASA** — heat-resistant and impact-tough. **Needs an
  enclosure** (X1C or P1S, not an open A1) and ventilation; prone to
  warping. ASA also resists UV. Use when the part sees heat or
  sustained load and PETG is not enough.
- **TPU** — flexible / rubber-like. Bumper pads, compliant intake
  pieces, grips, cable strain reliefs. Print slow. Not a structural
  bracket.
- **Nylon (PA) and CF-filled nylons** — strong, tough, heat- and
  wear-resistant. They need drying and a **hardened nozzle**. That
  workflow is the Lead ticket
  [Engineering Materials](../engineering-materials/). Know they exist
  so you do not grab a CF spool on an A1 with a brass nozzle.

Properties that actually matter on a robot:

- **Impact / toughness** — will a defensive hit crack it?
- **Heat** — pits, Texas sun, motors, and brakes cook PLA.
- **Stiffness vs. flex** — brackets want stiff; rollers and pads want
  TPU.
- **Printability** — PLA is easiest; engineering filaments are hardest.
- **Layer adhesion** — poor bonding is a crack waiting to happen,
  independent of the datasheet tensile number.

A simple selection guide you should be able to recite:

- Prototype, jig, or display → **PLA**
- Functional general-purpose robot part → **PETG**
- Heat or sustained structural load → **ASA / ABS** or an engineering
  filament
- Needs to flex, grip, or absorb a hit → **TPU**
- High-load or wear surface → **CF nylon** (after the Lead ticket)

Bambu Studio ships tuned **filament profiles**. Bambu spools have an
**RFID tag** the AMS reads; third-party spools you set by hand. Each
material has its own nozzle temperature, bed temperature, and plate
preference. Do not run PETG on a PLA profile.

FRC cares about printed parts as **FABRICATED ITEMS**, bumper-contact
rules (hard plastics can damage other bumpers), pit rules, and any
season-specific R-rules. You will do a full manual check in
[Maintenance & Print Farm Management](../maintenance-print-farm/).
Today you only need to know: material choice is also a *rules* choice,
and the current game manual wins.

This site does not track whether you finished. If your team exported
these tickets, close the issue once a mentor accepts the written
material picks below.

## Prerequisites

- [3D Printing Fundamentals & Safety](../fundamentals-safety/)
  completed (FDM vocabulary and safety sign-off).
- Bambu Studio installed, or a mentor computer that already has it, so
  you can open filament profiles. Full slicing is the next ticket.

## What you'll learn

- The common FRC filaments and which printers can run them.
- How to pick a material for impact, heat, flex, and printability.
- How Bambu profiles and the AMS identify a spool.
- Why PLA is the wrong default for a part that gets hot or hit.

## Tasks

1. **Read the material comparisons.** Read
   [All3DP: PLA vs ABS vs PETG](https://all3dp.com/2/pla-vs-abs-vs-petg-differences-compared/)
   and skim
   [All3DP: filament types](https://all3dp.com/1/3d-printer-filament-types-3d-printing-3d-filament/)
   for TPU and nylon. Then open Bambu's
   [filament guide](https://wiki.bambulab.com/en/filament-acc/filament)
   and note nozzle / bed temperature bands for PLA, PETG, and ABS or
   ASA. You are not memorizing every number. You are learning that
   the numbers are *different*.

2. **Walk the filament shelf.** With a mentor, find one spool each of
   PLA, PETG, and (if the shop has them) ABS/ASA, TPU, and a CF-filled
   nylon. For each spool say: enclosed printer required or not, fumes
   or not, brass nozzle OK or hardened required. Do not load CF
   filament onto a brass nozzle.

3. **Open the matching Studio profile.** In Bambu Studio, select the
   printer you will actually use and switch the filament dropdown
   between Generic or Bambu PLA, PETG, and one other material the shop
   stocks. Write down the nozzle and bed temperatures the profile
   proposes. Confirm they change when the material changes.

4. **Write material picks for named robot parts.** In a note a mentor
   can read (paper, a doc, or a file in your learning repo), pick a
   filament for **each** of these and justify it in two sentences
   (impact, heat, rules, or printability — not "because it's what we
   have"):

   - a **practice-bot intake paddle** that slaps game pieces
   - an **electronics cover** over the roboRIO that sees no motor heat
   - a **motor-adjacent spacer** next to a hot Falcon / Kraken
   - a **soft pad** that sits on the bumper and may touch another
     robot's bumper
   - a **drill jig** used once in the shop

   If your robot uses different names, substitute real parts — the
   point is a *named* part, not "a bracket."

5. **State the enclosure rule.** Write one paragraph: which of the
   materials above need an enclosed, ventilated printer, and which
   shop machines (X1C, P1S, A1, A1 mini) are legal for them. A mentor
   should be able to catch a wrong printer from that paragraph.

6. **Preview the rulebook, do not finish it.** Open the current
   [FRC Game Manual and Q&A](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
   (or this season's
   [Season Materials](https://www.firstinspires.org/resources/library/frc/season-materials)
   page). Find the definition of a **FABRICATED ITEM** and skim the
   bumper rules for hard plastics. You are not inspecting a robot
   today. You are proving you know where the rules live. Full
   printed-part legality is
   [Maintenance & Print Farm Management](../maintenance-print-farm/).

## Acceptance Criteria

- [ ] You named a material and a two-sentence justification for each
      of the five named parts in Task 4. A mentor can read the note
      without you narrating it.
- [ ] The motor-adjacent pick is **not** PLA, and you can say why
      heat matters.
- [ ] The bumper-pad pick is a flexible material (TPU or equivalent),
      and you noted that hard plastics on bumpers can violate bumper
      interaction rules.
- [ ] You stated which materials need an enclosure and which shop
      printers can run them.
- [ ] You opened the matching PLA and PETG profiles in Bambu Studio
      and recorded that their temperatures differ.
- [ ] You found FABRICATED ITEM (or the current equivalent) in this
      season's manual.

## Resources

- [Bambu Lab filament guide](https://wiki.bambulab.com/en/filament-acc/filament)
- [All3DP: PLA vs ABS vs PETG](https://all3dp.com/2/pla-vs-abs-vs-petg-differences-compared/)
- [All3DP: filament types](https://all3dp.com/1/3d-printer-filament-types-3d-printing-3d-filament/)
- [Prusa: Material table](https://help.prusa3d.com/article/material-table_2069)
- [FIRST: Game Manual and Q&A](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [FIRST: Season Materials](https://www.firstinspires.org/resources/library/frc/season-materials)
- [Bambu Studio download](https://bambulab.com/en/download/studio)

## Notes

- "It's what was already loaded" is not a material pick. Unload and
  change the spool if the part needs it.
- Do not reuse a PLA profile for PETG. Temps, cooling, and the plate
  are different.
- CF-filled filament on a brass nozzle will destroy the nozzle. Leave
  those spools for the Lead ticket.
- The next ticket ([Slicing in Bambu Studio](../slicing-bambu-studio/))
  is where you turn a real STL into a 3MF using the material you
  just chose.
