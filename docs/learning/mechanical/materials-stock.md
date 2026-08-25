---
layout: mechanical-lesson
title: Materials & Stock
subtitle: Aluminum box tube, sheet, polycarbonate, and COTS parts — what the robot is built from and why.
permalink: /learning/mechanical/materials-stock/
role: fabricator
order: 4
size: 1
time: "45–60 min"
---

## Description

You can read a tape and name a #10-32. That is useless if you pull 2×1
tube when the bill of materials says 1×1 × 1/16 in wall. This ticket is
a stock walk: what the robot is actually made of, why a designer picked
it, and how to pull the right stick without asking three people.

[Shop Safety & PPE](../shop-safety/) is still the gate. You may handle
stock (gloves are fine for carrying cut ends). You may not cut, drill,
or grind until later tickets and a mentor says so.

**Aluminum** is the structural default: light, stiff enough, and
machinable with the tools an FRC shop owns. You will see it as:

- **Box tube** — hollow rectangular extrusion. **1×1 in** and **2×1 in**
  are the everyday sizes. Wall is usually **1/16 in (0.0625)** or
  **1/8 in (0.125)**. Thicker wall is heavier and harder to crush; it is
  not "better" on a wrist joint that has to stay under the weight limit.
- **Punched / patterned tube** — the same shapes with a 1/2 in grid of
  #10 clearance holes. REV
  [MAXTube 1×1](https://www.revrobotics.com/MAXTube-1x1/) and
  [MAXTube 2×1](https://www.revrobotics.com/maxtube-2x1/), AndyMark
  [pre-drilled box tube](https://andymark.com/products/pre-drilled-box-tube-extrusion),
  and WCP punched tube all exist so you can assemble on a pitch instead
  of laying out every hole. The holes are **clearance for #10**, not
  magic — a 1/4-20 still needs a bigger hole.
- **Plate and sheet** — gussets, gearbox plates, bellypans. Common
  thicknesses: 1/16, 1/8, 1/4 in. Measure with calipers; "the thin
  stuff" is not a thickness.
- **Angle, channel, and bar** — brackets and spacers when tube is the
  wrong shape.

Alloys: **6061-T6** is general structure. **7075** is stronger and
crankier to machine; it shows up where a plate takes a beating. If the
drawing says 6061, do not substitute mystery scrap from the steel rack.

**Plastics** are not all "the clear one."

- **Polycarbonate (Lexan)** — tough, impact-resistant, used for guards,
  bellypans, and intake hoods. It drills and saws if you support it and
  do not climb a dull bit. Score an edge carelessly and it can crack
  later.
- **HDPE / UHMW** — slippery wear surfaces and sliders. A game piece
  that has to slide wants UHMW, not raw aluminum.
- **Delrin (acetal)** — rigid, machinable, good for rollers, bushings,
  and spacers. It is not a structural beam.

**Raw stock** is what you cut: a 47 in stick of tube, a sheet of
polycarb. **COTS** (commercial off-the-shelf) is what you buy finished:
a WCP gearbox, a REV swerve module, an AndyMark wheel, a bearing, a
hex shaft. COTS exists so you spend build season on the mechanism that
is unique, not on reinventing a 3:1 reduction. Read the vendor page
before you "just trim" a COTS part — some are not meant to be cut.

Weight is a design choice. A 47 in stick of 2×1 × 1/8 in wall is a lot
of robot. Pull the wall thickness the BOM calls, not the leftover that
is closest.

The next ticket, [Hand Tools](../hand-tools/), is how you hold and shape
this stuff before anyone hands you a power tool.

## Prerequisites

- [Shop Safety & PPE](../shop-safety/) signed off.
- [Measurement & Layout](../measurement-layout/) completed — you will
  measure wall thickness and tube size with calipers.

## What you'll learn

- How to identify 1×1 and 2×1 tube, plate, and polycarbonate on the rack.
- Why wall thickness and alloy change the part you are about to make.
- The difference between raw stock and a COTS part, with examples from
  this shop's shelves.

## Tasks

1. **Read how vendors talk about tube.** Skim REV
   [Introduction to Structure](https://docs.revrobotics.com/ion-build/structure/introduction-to-structure)
   and the
   [FRC Robot Basics Guide (PDF)](https://www.revrobotics.com/content/docs/FRC-Robot-Basics-Guide.pdf)
   structure section. Then open AndyMark
   [pre-drilled box tube](https://andymark.com/products/pre-drilled-box-tube-extrusion)
   and note profile, wall, and hole pitch. Write: hole pitch, default
   hardware size, and one reason a team buys patterned tube instead of
   drilling every hole.

2. **Walk the stock rack.** With a mentor, put a finger on:

   - 1×1 aluminum box tube
   - 2×1 aluminum box tube
   - a piece of aluminum plate or sheet (say the thickness)
   - polycarbonate
   - one other plastic the shop stocks (UHMW, HDPE, or Delrin)
   - one COTS part (gearbox, wheel, bearing, or hex shaft)

   Measure the tube **outside** and the **wall** with calipers from
   [Measurement & Layout](../measurement-layout/). 1×1 is not always
   a true 1.000 in after powder coat or a cheap extrusion. Write the
   numbers on a card.

3. **Pull to a mini BOM.** A mentor writes a four-line bill of
   materials, for example:

   - 1× 2×1 × 1/16 wall tube, 12 in
   - 1× 1/8 in 6061 plate, about 4×3 in
   - 1× polycarb scrap, any small piece
   - 1× COTS bearing or hex shaft from the labeled bin

   You walk to the rack and pull those four things (or point if the
   mentor does not want stock moved). If the shop is out of 1/16 wall,
   you say so — you do not silently substitute 1/8.

4. **Name a use.** For aluminum tube, aluminum plate, polycarb, and
   UHMW/Delrin, tell a mentor one typical FRC use and one thing that
   material is *bad* at (for example: polycarb is a poor choice for a
   high-load gearbox plate; 7075 plate is a poor choice if you only
   have a dull hand drill and no cutting fluid).

5. **Look at WCP and VEX-style catalogs so the names stick.** Skim
   [WCP FRC Build System](https://docs.wcproducts.com/welcome/frc-build-system)
   (framing / shaft stock) and know that hex shaft, bearings, and
   punched tube are COTS even when they look like "just metal." You
   will assemble them for real in
   [Power Transmission & Drivetrains](../power-transmission-drivetrains/).

## Acceptance Criteria

- [ ] A card lists measured outside size and wall thickness for a 1×1
      and a 2×1 tube from this shop, plus the thickness of one plate.
- [ ] You pointed to polycarb, one other plastic, and one COTS part on
      the shelf and named each.
- [ ] You pulled (or pointed to) the four items on a mentor-written mini
      BOM without substituting a different wall or material.
- [ ] You stated a typical use *and* a bad use for tube, plate,
      polycarb, and one plastic wear material.
- [ ] You wrote hole pitch and default hardware size for patterned tube
      after reading a vendor page.

## Resources

- [REV ION: Introduction to Structure](https://docs.revrobotics.com/ion-build/structure/introduction-to-structure)
- [REV: FRC Robot Basics Guide (PDF)](https://www.revrobotics.com/content/docs/FRC-Robot-Basics-Guide.pdf)
- [REV MAXTube 1×1](https://www.revrobotics.com/MAXTube-1x1/)
- [REV MAXTube 2×1](https://www.revrobotics.com/maxtube-2x1/)
- [AndyMark: Pre-drilled box tube](https://andymark.com/products/pre-drilled-box-tube-extrusion)
- [WCP FRC Build System](https://docs.wcproducts.com/welcome/frc-build-system)
- [McMaster-Carr](https://www.mcmaster.com/) — search 6061 tube or
  polycarbonate sheet when the shop is buying, not guessing
- [WPILib: Hardware Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/index.html)

## Notes

- Steel lives on some robots (sprockets, shafts, bellypan weights). It
  is heavier and harder on blades. Do not cut it on a blade the shop
  reserved for aluminum unless a mentor says the blade is for steel.
- Polycarb scratches and creeps. Do not park it under a battery or a
  vise jaw without a pad.
- Level 1 ends here. [Hand Tools](../hand-tools/) starts the veteran
  path: hex keys, hacksaw, files, and a vise — still no power tools
  until that ticket and shop-safety are both done.
