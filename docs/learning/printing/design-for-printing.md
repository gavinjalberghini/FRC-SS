---
layout: printing-lesson
title: Designing for 3D Printing
subtitle: Orient for strength, set tolerances and clearances, handle overhangs, and add bosses and heat-set inserts.
permalink: /learning/printing/design-for-printing/
role: veteran
order: 8
size: 3
time: "Multi-session"
---

## Overview

The best print settings can't save a part that was designed badly for printing.
This lesson is the bridge between CAD and the printer: how to design parts that
print reliably, come out strong, and fit the robot. Pairs naturally with the
[CAD & Design curriculum](../../cad/).

## Prerequisites

- [Multi-Color & Multi-Material with the AMS](../multi-material-ams/) completed.
- Comfort with a CAD tool (see the [CAD track](../../cad/)).

## Unit 1 — Orientation & layer strength

- Parts are **weakest between layers**. Orient so the main load runs **along**
  layers, not peeling them apart.
- A bracket loaded in bending should have its layers running with the bending
  stress, not stacked across it.
- Sometimes the strongest orientation needs more supports — balance strength,
  supports, and surface finish.

## Unit 2 — Tolerances & clearances

- Printers are accurate but not perfect; **holes print slightly undersize** and
  outer dimensions slightly oversize.
- Leave **clearance** for mating parts — a typical press/slip fit needs ~0.2 mm of
  gap; tune by test-printing.
- For shafts, bearings, and bolts, design the nominal size and plan to **ream or
  drill** holes to final size after printing.

## Unit 3 — Printability rules

- **Overhangs** beyond ~45° need support — chamfer or redesign to avoid them.
- **Bridges** (gaps spanned in air) print only over short distances — keep them
  short or add support.
- **Wall thickness** should be a multiple of your nozzle/line width (≥1.2 mm /
  multiple walls) so walls are solid.
- Add **fillets/chamfers** at stress concentrations and to help bed adhesion.
- Avoid large flat bottoms prone to warping; avoid tiny unsupported pillars.

## Unit 4 — Fasteners in printed parts

- **Heat-set inserts** give strong, reusable threads — design a boss with the
  insert manufacturer's recommended hole diameter and install with a soldering
  iron.
- **Captured nuts** (a hex pocket) and **clearance holes for bolts** are simple and
  strong alternatives.
- Don't tap threads directly into plastic for high-load joints — they strip.
- Add **bosses and ribs** to reinforce mounting points rather than thickening the
  whole part.

## Unit 5 — Print vs. machine

- Print when the part is **complex, low-load, or quick to iterate**; choose
  aluminum/COTS when the part is **highly loaded or wear-critical**.
- Printed parts are great for brackets, spacers, guides, mounts, gauges, and
  prototypes — and, in engineering materials, some structural parts.

## Steps & acceptance criteria

- [ ] Orient a sample part for maximum strength and explain why.
- [ ] Add correct clearances for a mating part and a bolt hole.
- [ ] Redesign an overhang/bridge so it prints without support.
- [ ] Design a boss for a heat-set insert and install one.

## Resources

- [Bambu Wiki: Design for FDM](https://wiki.bambulab.com/en/knowledge-sharing)
- [Markforged: Design for FDM guide](https://markforged.com/resources/learn/design-for-additive-manufacturing-plastics-composites)
- [Heat-set insert installation (CNC Kitchen)](https://www.cnckitchen.com/blog/the-amazing-and-easy-way-to-put-threads-in-your-3d-prints)

## Notes

- Test-print small fit checks before committing to a long print — a 10-minute
  coupon saves a 10-hour failure.
