---
layout: cad-lesson
title: Slapdown Intake
subtitle: Design a robust slapdown intake using the intake golden rules, pivots, rollers, and zombie axles.
permalink: /learning/cad/slapdown-intake/
role: lead
order: 9
size: 2
time: "2–3 hrs"
---

## Description

A **slapdown intake** flips down to grab game pieces off the floor and
folds back up inside the frame. It is an over-the-bumper (OTB) intake with
one set of arms and rollers — as opposed to a four-bar that stows more
flat. You already have the pivot language from Stage 2B; this ticket adds
rollers, a game-piece path, and the rules that separate a reliable intake
from a highlight-reel toy.

This is **Stage 2C** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage2/2c/introduction/).
The reference is inspired by 4414's 2023 slapdown (on a 2022-style piece).
Read the concept pages, copy the provided document, then build layout,
part studio, and assembly. Stage 2C expects you to apply the dead-axle
pivot instead of learning mates from scratch.

Engineering you must be able to show on the model:

- **Intake golden rules** (Andrew Torrance / 254, as quoted on FRCDesign):
  roller surface speed at least about 2× robot max speed; maximize grip;
  rigid rollers on a squishy piece, compliant rollers on a hard piece;
  maximize intake width; build it to be hit; use sensors when you can.
  Reliability beats cleverness. An intake that works 95% of the time loses
  matches.
- **Robustness.** Intakes live outside the frame. They hit the floor,
  walls, and other robots. Design them to survive and to deflect. Thin
  unsupported plates and cantilevered roller shafts fail first.
- **Pivot.** Reuse the dead-axle pattern. The reference uses a Kraken into
  a two-stage MAXPlanetary plus chain to a long cross-axle so **both**
  arms rise together. Around 30:1–42:1 is a typical intake-pivot band;
  justify yours. Tension the chains. Clock sprockets so the arms do not
  twist.
- **Rollers.** Spacing and compression against the piece (and against a
  hard floor or bumper) decide whether you grab an off-center piece or
  knock it away. Dead-axle rollers (Stage 1C Exercise 2) are common here
  because the roller can carry an integrated pulley.
- **Zombie axle.** On FRCDesign this is a *feature*, not a defect. The
  pivot tube is a **dead** axle for the arm and a **live** axle for a
  pulley that drives the rollers. The roller motor can sit on the robot
  base, which unloads the arm and protects the motor. That only works if
  the pivot shaft is actually captured and the pulley is supported.
  Unsupported, single-ended roller shafts are a different problem — do not
  build those.

Layout-wise you will draw **two** poses (deployed and retracted) plus the
ball path. If it does not fold inside the frame perimeter in CAD, it will
not pass inspection on the field.

This site does not track whether you finished. The intake document lives
in your Onshape account. Mentors review a share link.

## Prerequisites

- [Dead Axle Pivot](../dead-axle-pivot/) completed.
- Stage 1C Exercise 1 (flat intake) and Exercise 2 (dead axle rollers) so
  roller assemblies are not new.

## What you'll learn

- The intake golden rules, and how to point to each one on a CAD model.
- How a slapdown differs from a four-bar, and what the layout must prove
  about stow and deploy.
- How to reuse a dead-axle pivot and dead-axle rollers on one mechanism.
- What a zombie axle is (pivot dead, roller drive live on the same shaft)
  and why both ends of every roller still need support.

## Tasks

1. **Read the concept pages, then copy the document.** Start at
   [Slapdown Intake Introduction](https://frcdesign.org/learning-course/stage2/2c/introduction/)
   and read:

   - [Intake Golden Rules](https://frcdesign.org/learning-course/stage2/2c/intake-golden-rules/)
   - [Pivot](https://frcdesign.org/learning-course/stage2/2c/pivot/)
   - [Zombie Axles](https://frcdesign.org/learning-course/stage2/2c/zombie-axles/)

   Follow the next-page arrows through robustness, rollers, and any other
   concept pages. Copy the Stage 2C reference / exercise document into your
   account as `Stage 2C Intake — YourName`. Write, in your scratch note,
   which golden rules the reference follows and which it skips (the golden
   rules page already admits the sensor skip).

2. **Unit 1 — Layout sketch.** On the Stage 2C layout-sketch page, define
   deployed and retracted positions, roller diameters and spacing, the
   pivot, and the path a game piece takes over the bumper into the robot.
   Confirm the retracted pose is inside the frame. Origin Cube first.
   Fully constrain the sketch. If the path only works for a perfectly
   centered piece, widen it — that is the golden rule you are practicing.

3. **Unit 2 — Part studio.** Follow the Stage 2C part-studio page. Model
   rollers, pivoting frame, structure, and the drives for **both** the
   pivot and the rollers. Support every roller axle on both ends. If you
   use a zombie axle, model the pulley on the pivot shaft and the path to
   the first roller explicitly. Name parts. No overlapping solids.

4. **Unit 3 — Assembly.** Follow the Stage 2C assembly page. Mate the
   pivot (revolve) and the rollers (revolve). Add motors and transmissions.
   Drag deploy, ingest, and retract. Watch for belts that slap the bumper,
   arms that hit the frame at stow, and rollers that collide when
   compressed against a piece. Use isolate / hide (`Y`) instead of
   deleting hardware you cannot see.

5. **Write one design note.** In a few sentences pick one: *why slapdown
   instead of a four-bar for this piece*, *how the zombie axle earns its
   keep*, or *which golden rule your model still violates and what you
   would change*. "It matches the reference" is not a design choice.

6. **Hand it to a mentor.** Share `Stage 2C Intake — YourName` or export
   screenshots of the layout (both poses), the named studio, and the
   assembly deployed and retracted. If your team exported these tickets,
   paste the link and move the issue to In Review.

## Acceptance Criteria

- [ ] A shareable Onshape document contains your Stage 2C slapdown intake.
- [ ] Layout, part studio, and assembly work from the FRCDesign Stage 2C
      pages is complete in that document.
- [ ] The layout sketch is fully constrained and shows deployed, retracted,
      and a game-piece path that fits the frame when stowed.
- [ ] Custom parts are named; no overlapping solids; every roller shaft is
      supported on both ends.
- [ ] The assembly deploys, the rollers spin, and the intake retracts
      without collisions.
- [ ] A short written note defends one intake choice (golden rule, zombie
      axle, or slapdown vs four-bar).

## Resources

- [Stage 2C introduction](https://frcdesign.org/learning-course/stage2/2c/introduction/)
- [Intake Golden Rules](https://frcdesign.org/learning-course/stage2/2c/intake-golden-rules/)
- [Pivot](https://frcdesign.org/learning-course/stage2/2c/pivot/)
- [Zombie Axles](https://frcdesign.org/learning-course/stage2/2c/zombie-axles/)
- [Stage 2C summary](https://frcdesign.org/learning-course/stage2/2c/summary/)
- [Dead Axle Pivot](../dead-axle-pivot/)
- [Practice Mechanisms](../practice-mechanisms/)
- [Onshape Learning Center](https://learn.onshape.com/)

## Notes

- Design for the worst-case approach angle, not the perfect centered piece
  in the render.
- A zombie axle is a dual-use pivot shaft, not a shaft held on one end.
  Cantilevered rollers still fail — support them.
- Dual-sided chain (or a stiff cross-axle) keeps the two arms from
  winding up. One-sided drive on a wide intake is how frames crack.
- The next ticket ([Cascade Elevator](../cascade-elevator/)) is Stage 2D
  and the capstone: linear stages, rigging, and a gearbox that must hold
  against gravity.
