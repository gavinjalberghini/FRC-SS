---
layout: cad-lesson
title: Dead Axle Pivot
subtitle: Build a pivoting arm on a dead axle — strength, friction, power transmission, tensioning, and backlash.
permalink: /learning/cad/dead-axle-pivot/
role: veteran
order: 8
size: 2
time: "2–3 hrs"
---

## Description

Many mechanisms pivot: arms, wrists, hoods, intakes. This ticket teaches
the **dead axle** pivot — the axle is fixed to the robot, and the arm
rotates on bearings or bushings *around* it. A **live** axle would spin
with the arm and carry the bending load through hex shaft and bearings in
the plates. Dead axles win on stiffness: a large fixed tube does not
transmit torque, so it can be fat, short, and bolted into structure.

This is **Stage 2B** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage2/2b/introduction/).
The project is a simple arm (MAXPlanetary gearbox, #25 chain, 7/8" tube
axle) that is not tied to one game. Read the engineering pages, copy the
reference document, then build layout, part studio, and assembly.

Ideas you must be able to point to on your model:

- **Strength.** A pivot sees large bending and torsion at the joint.
  Support the axle on both sides. 3/4" and 7/8" round tube beat 1/2" hex
  for stiffness at similar weight; 7/8" also matches 1.125" OD bushings
  that fit most COTS sprocket bores. The reference uses 7/8" for that
  reason, not aesthetics.
- **Friction.** The arm should rotate on bushings or bearings, not
  aluminum-on-aluminum. Bushings like high load and low RPM (pivots).
  Bearings like higher speed. Metal-on-metal rub wastes motor and wears
  holes oval.
- **Power transmission.** Chain and a large sprocket bolted to the *arm*
  keep the axle dead: torque goes into the rotating structure, not into
  twisting a shaft. Large output sprockets also add reduction and put more
  teeth in mesh.
- **Tensioning.** Chain stretches. Design a way to take up slack (slots,
  a turnbuckle, an idler). A pivot with no tensioner is a pivot that will
  slap after three events.
- **Backlash.** Slop in hex fits, loose bolts, extra gearbox stages, and
  floppy chain shows up as the arm nodding when it should hold. Fewer
  stages, shimmed hex, aligned sprockets, and real tension are the usual
  fixes. You cannot fully model backlash in CAD; you *can* refuse designs
  that guarantee it.

You already modeled a dead-axle *roller* in Stage 1C. This is the same
idea at arm scale: bearings ride on a fixed tube, power is applied to the
rotating body.

This site does not track whether you finished. The pivot document lives in
your Onshape account. Mentors review a share link.

## Prerequisites

- All Designer tickets completed.
- [Basic Shooter](../basic-shooter/) recommended first so the Stage 2
  layout → studio → assembly loop is already familiar.
- Stage 1C Exercise 2 (dead axle rollers) is the conceptual preview.

## What you'll learn

- Why dead axles are stiffer than live axles for loaded pivots, and when
  a live axle is still fine.
- How bushings, chain reduction, and a large output sprocket work together.
- How to put tensioning and backlash reduction into the layout, not as an
  afterthought.
- How to mate an arm through a full sweep and find collisions at the
  ends of travel.

## Tasks

1. **Read the engineering pages, then copy the document.** Start at
   [Dead Axle Pivot Introduction](https://frcdesign.org/learning-course/stage2/2b/introduction/)
   and
   [Project Overview](https://frcdesign.org/learning-course/stage2/2b/project-overview/).
   Copy the **Dead Axle Reference Document** into your account as
   `Stage 2B Pivot — YourName`. Read:

   - [Strength](https://frcdesign.org/learning-course/stage2/2b/strength/)
   - [Friction](https://frcdesign.org/learning-course/stage2/2b/friction/)
   - [Power Transmission](https://frcdesign.org/learning-course/stage2/2b/power-transmission/)
   - [Backlash](https://frcdesign.org/learning-course/stage2/2b/backlash/)

   Follow the next-page arrows through any remaining concept pages
   (tensioning). Note the project constraints: MAXPlanetary, #25 chain,
   7/8" dead axle, both sides supported.

2. **Unit 1 — Layout sketch.** On the FRCDesign layout-sketch page for
   Stage 2B (next arrows from the concept pages, typically
   `.../stage2/2b/layout-sketch/`), define the pivot center, arm length,
   range of motion, gearbox location, and chain run. The pivot point is
   the anchor for everything. Origin Cube first. Fully constrain the
   sketch. If you set travel limits with construction lines, keep them;
   you will need them when you drag the assembly.

3. **Unit 2 — Part studio.** Follow the Stage 2B part-studio page. Model
   the dead axle, the rotating arm with bushing/bearing seats, structure,
   and the drive. Capture the axle so it cannot slide out. Name parts.
   No overlapping solids. Use Tube Converter and Robot Shaft where they
   apply; do not invent a 7/8" tube from a random extrude if the course
   gives you a better feature.

4. **Unit 3 — Assembly.** Follow the Stage 2B assembly page. Mate the arm
   to **revolve** about the dead axle. Add the gearbox and chain (Belt &
   Chain Gen). Drag the arm through the **full** sweep. Collisions hide at
   the extremes. Check that chain stay-clear and that you did not
   accidentally fasten the arm so it cannot move.

5. **Write one design note.** In a few sentences: *Why is this axle dead
   instead of live, and what on your model limits backlash or takes up
   chain stretch?* If the answer is "the reference did it," say what *you*
   would change for a heavier end effector.

6. **Hand it to a mentor.** Share `Stage 2B Pivot — YourName` or export
   screenshots of the black layout, the named studio, and the arm at both
   ends of travel. If your team exported these tickets, paste the link and
   move the issue to In Review.

## Acceptance Criteria

- [ ] A shareable Onshape document contains your Stage 2B pivot.
- [ ] Layout, part studio, and assembly work from the FRCDesign Stage 2B
      pages is complete in that document.
- [ ] The layout sketch is fully constrained; pivot center, travel, and
      chain/gearbox locations are visible.
- [ ] The axle is captured and supported on both sides; custom parts are
      named; no overlapping solids.
- [ ] The arm revolves through its designed range with no binding in the
      assembly.
- [ ] A short written note defends dead-vs-live and one backlash or
      tensioning choice.

## Resources

- [Stage 2B introduction](https://frcdesign.org/learning-course/stage2/2b/introduction/)
- [Project Overview](https://frcdesign.org/learning-course/stage2/2b/project-overview/)
- [Strength](https://frcdesign.org/learning-course/stage2/2b/strength/)
- [Friction](https://frcdesign.org/learning-course/stage2/2b/friction/)
- [Power Transmission](https://frcdesign.org/learning-course/stage2/2b/power-transmission/)
- [Backlash](https://frcdesign.org/learning-course/stage2/2b/backlash/)
- [Stage 1C dead-axle rollers](https://frcdesign.org/learning-course/stage1/1c/exercise2/)
- [Onshape Learning Center](https://learn.onshape.com/)
- [Basic Shooter](../basic-shooter/)
- [Power Transmission](../power-transmission/)

## Notes

- Dead axles are common because they are strong and put the bearings in
  the rotating part instead of spanning a long spinning hex shaft.
- Always drag the *full* sweep in the assembly. The collision you miss is
  the one at 110 degrees, not at the stowed screenshot.
- Backlash is mostly a real-world tolerance problem. CAD that uses three
  sloppy hex stages and no tensioner is still a bad design even if the
  mates look tight on screen.
- The next ticket ([Slapdown Intake](../slapdown-intake/)) is Stage 2C:
  this pivot plus rollers, including a zombie axle for roller power.
