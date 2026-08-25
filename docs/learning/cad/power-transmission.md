---
layout: cad-lesson
title: Power Transmission & Gearboxes
subtitle: Motors, shafts, bearings, torque and speed — and modeling gear, belt, and chain gearboxes.
permalink: /learning/cad/power-transmission/
role: designer
order: 3
size: 3
time: "Multi-session"
---

## Description

Structure holds a robot still. **Power transmission** makes it move. A motor
turns; shafts, bearings, gears, belts, and chain turn that rotation into the
speed and torque a mechanism needs. Almost every later ticket — intakes,
shooters, pivots, elevators — is a gearbox wearing a different costume.

This ticket is **Stage 1B** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage1/1b/introduction/).
Stage 1B teaches you to *model* transmissions. Picking motors and calculating
an optimal ratio for a real mechanism comes in Stage 2. Read the concept
pages first, then build the three gearbox exercises in the document you copy
from those pages.

The physics you need before you touch a sketch:

- **Torque** is rotational force (newton-meters). **Speed** is how fast the
  shaft spins (RPM). For a given motor power they trade: a 4:1 reduction
  gives about 4× the torque at 1/4 the speed. Write
  `ratio = driven teeth / driving teeth` and do the arithmetic *before* you
  pick parts.
- **CIM-class motors** (Kraken, NEO, Falcon, Vortex, and the older CIM)
  share a 2.5" outline and a 2" bolt circle. That is why Stage 1A's motor
  plate still works here.
- **Shafts** carry rotation. 1/2" hex is the FRC default because the shape
  transmits torque without a keyway. **Bearings** let that shaft spin in a
  plate. Every rotating shaft needs support, usually at two points; a gear
  that meshes perfectly but cannot be bearing-supported is scrap.
- **Gears** mesh and reverse direction. They must share a **diametral pitch**
  (20 DP and 32 DP are common). Center distance is set by tooth count and
  pitch — your layout sketch is those pitch circles, tangent.
- **Belts and pulleys** (typically 5 mm HTD) transmit power across a gap
  without reversing direction. Belt tooth count must be an integer; center
  distance is a function of that length. **Belt & Chain Gen** and Origin
  Cube's `#BeltCTC_5mm(...)` exist so you do not guess.
- **Chain and sprockets** (#25 most years, #35 for very high torque) do the
  same job when the load is high or the span is long. Chain needs
  **tensioning**. Loose chain skips; tight chain binds.

Layout sketches are not optional decoration. In each gearbox you will draw
pitch circles and motor outlines first, fully constrain them, then build
plates around that sketch. That is the same habit Stage 1D will demand of a
whole robot.

This site does not track whether you finished. The copied Stage 1B document
lives in your Onshape account. Mentors review a share link.

## Prerequisites

- [Onshape Fundamentals](../onshape-fundamentals/) completed (Stage 1A
  sketches, plates, assemblies, and FRCDesignLib rivets).
- Robot Shaft, Robot Spacer, Belt & Chain Gen, Origin Cube, and Part Lighten
  installed from [Getting Started](../getting-started/).

## What you'll learn

- How torque and speed trade through a gear, belt, or chain ratio, and how
  to compute a single-stage and two-stage reduction by hand.
- How FRC motors, hex shafts, and bearings are modeled and supported.
- How to build a layout sketch of pitch circles, then plates, shafts, and an
  assembly around it.
- When to use gears vs belts vs chain, and how Belt & Chain Gen and Robot
  Shaft remove the guesswork from center distance and shaft length.

## Tasks

1. **Read the concept pages, then find the parts.** Start at
   [Power Transmissions Introduction](https://frcdesign.org/learning-course/stage1/1b/introduction/)
   and read through:

   - [Motors](https://frcdesign.org/learning-course/stage1/1b/motors/)
   - [Shafts and Bearings](https://frcdesign.org/learning-course/stage1/1b/shafts-bearings/)
   - [Torque and Speed](https://frcdesign.org/learning-course/stage1/1b/torque-speed/)
   - [Gear Basics](https://frcdesign.org/learning-course/stage1/1b/gears/)
   - [Belt and Pulley Basics](https://frcdesign.org/learning-course/stage1/1b/belts/)
   - [Chain and Sprocket Basics](https://frcdesign.org/learning-course/stage1/1b/chain/)

   In FRCDesignLib (or a vendor catalog), locate one CIM-class motor, one
   1/2" hex bearing, one 20 DP gear, one 5 mm pulley, and one #25 sprocket.
   You are training your eye, not buying yet.

2. **Copy the Stage 1B document.** The introduction and Exercise 1 pages
   provide the document button. Copy it into your account and rename it
   `Stage 1B — YourName`. All three gearbox exercises happen in this copy.

3. **Exercise 1 — Simple gearbox.** Complete
   [Exercise 1: Simple Gearbox](https://frcdesign.org/learning-course/stage1/1b/exercise1/)
   in your copy. Model a single-stage gearbox: a pinion on the motor driving
   a larger gear on the output shaft. Use Robot Shaft and Robot Spacer.
   Verify the pitch-circle center distance in the layout sketch, then
   compute the reduction on paper (`driven / driving`) and write it on a
   text tab or in the share comment. Insert configurable gears from
   FRCDesignLib in the assembly; notice you can change tooth count without
   re-mating.

4. **Exercise 2 — Two-stage gearbox.** Complete
   [Exercise 2: Two Stage Gearbox](https://frcdesign.org/learning-course/stage1/1b/exercise2/).
   Stack a second reduction, support the intermediate shaft on bearings, and
   pocket the plate with **Part Lighten**. Overall ratio is the product of
   the stages. Compute it by hand and check it against the tooth counts in
   the model. Name the plates, shafts, and spacers.

5. **Exercise 3 — Gear and belt gearbox.** Complete
   [Exercise 3: Gear and Belt Gearbox](https://frcdesign.org/learning-course/stage1/1b/exercise3/).
   Combine a gear stage and a belt stage, and integrate frame tubes and
   gussets from Stage 1A. Use Belt & Chain Gen (keep teeth modeling off so
   the studio stays fast) and Origin Cube center-distance functions so the
   belt pitch length is a real integer-tooth belt. Confirm the belt does
   not collide with the plate.

6. **Write one design note.** In a few sentences: *Which stage of Exercise
   3 sets most of the reduction, and why did you (or the reference) put the
   belt where it is instead of using a third gear?* Mention center distance,
   packaging, or direction of rotation if that drove the choice.

7. **Hand it to a mentor.** Share `Stage 1B — YourName` or export
   screenshots of all three assembled gearboxes plus the written ratios.
   Sketches should be black; parts named; no overlapping solids. If your
   team exported these tickets, paste the link and move the issue to In
   Review.

## Acceptance Criteria

- [ ] A copy of the Stage 1B document exists in your Onshape account and a
      mentor has a shareable link (or equivalent screenshots).
- [ ] Exercises 1, 2, and 3 are complete in that copy, with layout sketches,
      part studios, and assemblies.
- [ ] You wrote the reduction for each gearbox on paper (or in the document)
      and it matches the tooth counts in the model.
- [ ] Sketches that drive plates and shaft locations are fully constrained.
- [ ] No overlapping solids; custom parts and important features are named.
- [ ] A short written note explains one transmission choice in Exercise 3.

## Resources

- [Stage 1B introduction](https://frcdesign.org/learning-course/stage1/1b/introduction/)
- [Motors](https://frcdesign.org/learning-course/stage1/1b/motors/)
- [Shafts and Bearings](https://frcdesign.org/learning-course/stage1/1b/shafts-bearings/)
- [Torque and Speed](https://frcdesign.org/learning-course/stage1/1b/torque-speed/)
- [Gear Basics](https://frcdesign.org/learning-course/stage1/1b/gears/)
- [Belt and Pulley Basics](https://frcdesign.org/learning-course/stage1/1b/belts/)
- [Chain and Sprocket Basics](https://frcdesign.org/learning-course/stage1/1b/chain/)
- [Exercise 1: Simple Gearbox](https://frcdesign.org/learning-course/stage1/1b/exercise1/)
- [Exercise 2: Two Stage Gearbox](https://frcdesign.org/learning-course/stage1/1b/exercise2/)
- [Exercise 3: Gear and Belt Gearbox](https://frcdesign.org/learning-course/stage1/1b/exercise3/)
- [Stage 1B summary](https://frcdesign.org/learning-course/stage1/1b/summary/)
- [FRCDesignLib](https://www.frcdesign.org/resources/frcdesignlib/)
- [WCP product catalog](https://www.wcproducts.com/)
- [Onshape Learning Center](https://learn.onshape.com/)

## Notes

- Always write the target reduction *before* picking gears. Design the math,
  then the pitch circles, then the plate.
- Leave room for bearings, retaining rings or bolts, and a wrench when you
  place shafts. A mesh that cannot be supported is not a gearbox.
- Configurable FRCDesignLib gears and pulleys are there so a tooth-count
  change does not force a remate. Use them.
- Stage 1B is a modeling intro. Do not treat these ratios as competition
  recommendations; Stage 2 mechanisms will make you justify a ratio against
  a load.
- The next ticket ([Practice Mechanisms](../practice-mechanisms/)) is Stage
  1C: eight small mechanisms with steadily less guidance.
