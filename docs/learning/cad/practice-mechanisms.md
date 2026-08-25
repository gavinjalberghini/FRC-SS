---
layout: cad-lesson
title: Practice Mechanisms
subtitle: Eight progressively less-guided drills to make Onshape second nature.
permalink: /learning/cad/practice-mechanisms/
role: designer
order: 4
size: 2
time: "Multi-session"
---

## Description

By now you know the tools. This ticket is **reps**. You will model eight small
mechanisms that get progressively less guided, combining Stage 1A structure
and plates with Stage 1B power transmission until the workflow is automatic.

This is **Stage 1C** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage1/1c/introduction/).
FRCDesign is explicit: these mechanisms are *practice*, not competition
designs. They sit out of context of a full robot. Copy them into a real
robot later only after you understand why each choice was made.

Three Onshape ideas this stage is meant to burn in:

- **Layout sketch first.** Every mechanism starts with a sketch of the
  things that *drive* the design: roller diameters, belt center-to-center,
  game-piece path, motor outline. Details (bearing holes, plate outline)
  live in later sketches that reference that layout. Change the layout, and
  the plates should follow. You already did this on gearboxes; 1C makes it
  the default.
- **Origin Cube in every studio.** Put Origin Cube down as the first
  feature. Fasten it to the assembly origin after you insert and group
  parts. That is how FRCDesign keeps part studios, assemblies, and later
  the robot code origin aligned. Skipping it now makes Stage 1D and Stage 2
  flexible mates much harder.
- **Live axle vs dead axle.** A **live** axle spins: bearings sit in the
  plates, the shaft turns the roller. A **dead** axle is fixed: bearings
  sit in the roller, and you power the roller itself (often through an
  integrated pulley). You will model both. Stage 2B and 2C will make you
  *choose*.

Guidance drops after Exercise 2. From Exercise 3 on, the slides give
part-by-part intent and the solutions document is for checking — not for
blindly copying feature-for-feature. Getting stuck and reasoning it out is
the point.

This site does not track whether you finished. The copied Stage 1C document
lives in your Onshape account. Mentors review a share link.

## Prerequisites

- [Onshape Fundamentals](../onshape-fundamentals/) and
  [Power Transmission](../power-transmission/) completed.
- Origin Cube, Tube Converter, Robot Shaft, and Belt & Chain Gen on your
  toolbar.

## What you'll learn

- How to start every mechanism from a layout sketch and an Origin Cube.
- The difference between live-axle and dead-axle rollers, by modeling both.
- How to assemble COTS wheels, belts, motors, and tube plugs without
  overlapping solids or unnamed instances.
- How to keep working when the instructions stop spelling out every click.

## Tasks

1. **Read the intro and copy the document.** Open
   [Practice Mechanisms Introduction](https://frcdesign.org/learning-course/stage1/1c/introduction/)
   and
   [Exercise Overview](https://frcdesign.org/learning-course/stage1/1c/exercise-overview/).
   Copy the **Stage 1C Exercises Document** into your account and rename it
   `Stage 1C — YourName`. Each exercise folder has a reference tab (what
   "done" looks like) and empty tabs for your work. The solutions document
   is linked on the overview page — look at it *after* you try, not instead
   of trying. You do not need to copy the solutions document.

2. **Do the exercises in order.** Use the next-page arrows on FRCDesign.
   For each one: layout sketch (black), Origin Cube first, named parts, no
   overlapping solids, then assembly with FRCDesignLib hardware.

   - [Exercise 1 — Flat Intake](https://frcdesign.org/learning-course/stage1/1c/exercise1/).
     A roller intake on structure. Live-axle compliant wheels, a belt
     reduction, and tube plugs. Practice mounting rollers and a driving
     motor. Use Origin Cube belt center-to-center functions the way you did
     in Stage 1B Exercise 3.
   - [Exercise 2 — Dead Axle Rollers](https://frcdesign.org/learning-course/stage1/1c/exercise2/).
     Rollers that spin on a fixed axle, bearings inside the roller, power
     through the roller pulley. Compare the section view on that page to
     Exercise 1 until live vs dead is obvious.
   - [Exercise 3 — Shooter](https://frcdesign.org/learning-course/stage1/1c/exercise3/).
     A simple flywheel shooter — your first taste of
     [Basic Shooter](../basic-shooter/). Guidance gets thinner. Pay
     attention to the ball-path layout, 3D-printed pulleys with metal
     inserts, nut strips, and block motors.
   - [Exercise 4 — Telescoping Hook](https://frcdesign.org/learning-course/stage1/1c/exercise4/).
     A two-stage telescoping climber. Nested moving parts, GreyT bearing
     blocks, and a MAXPlanetary. Watch clearances and print tolerances on
     the crush block.
   - [Exercise 5 — Flipped Gearbox](https://frcdesign.org/learning-course/stage1/1c/exercise5/).
     Re-orient a gearbox to fit a tight package. Practice flipping and
     re-mating a power transmission without rebuilding it from scratch.
   - [Exercise 6 — Direction Swap](https://frcdesign.org/learning-course/stage1/1c/exercise6/).
     Add an idler or extra stage to reverse output direction without
     moving the motor.
   - [Exercise 7 — Vertical Rollers](https://frcdesign.org/learning-course/stage1/1c/exercise7/).
     Rollers standing vertically for centering or feeding. Same mates,
     different gravity.
   - [Exercise 8 — Indexer Centering](https://frcdesign.org/learning-course/stage1/1c/exercise8/).
     A centering indexer that funnels a game piece to the middle.
     Combines rollers, structure, and layout geometry.

3. **Sanity-check motion and clearances.** For every assembly, drag what is
   supposed to spin or slide. Belts should not cut through plates. Rollers
   should not collide with structure. If two valid approaches exist, pick
   one and keep going — do not stall waiting for a "right" answer.

4. **Write one design note.** Pick any exercise from 3–8 and write a few
   sentences: *What did you do when the slides stopped spelling out a
   feature, and why is that choice defensible?* If you used the solutions
   document, say what you looked up and what you already had.

5. **Hand it to a mentor.** Share `Stage 1C — YourName` or export
   screenshots of all eight finished assemblies plus the note. If your team
   exported these tickets, paste the link and move the issue to In Review.

## Acceptance Criteria

- [ ] A copy of the Stage 1C exercises document exists in your Onshape
      account and a mentor has a shareable link (or equivalent screenshots).
- [ ] Exercises 1–8 are complete in that copy, each with a layout-driven
      part studio and an assembly.
- [ ] Layout sketches are fully constrained; Origin Cube is the first
      feature in the studios that the course asks you to start that way.
- [ ] No overlapping solids; custom parts and important features are named.
- [ ] A short written note explains one judgment call from Exercises 3–8.

## Resources

- [Stage 1C introduction](https://frcdesign.org/learning-course/stage1/1c/introduction/)
- [Exercise Overview (copy the document here)](https://frcdesign.org/learning-course/stage1/1c/exercise-overview/)
- [Exercise 1: Flat Intake](https://frcdesign.org/learning-course/stage1/1c/exercise1/)
- [Exercise 2: Dead Axle Rollers](https://frcdesign.org/learning-course/stage1/1c/exercise2/)
- [Exercise 3: Ball Shooter](https://frcdesign.org/learning-course/stage1/1c/exercise3/)
- [Exercise 4: Telescoping Hook](https://frcdesign.org/learning-course/stage1/1c/exercise4/)
- [Exercise 5: Flipped Gearbox](https://frcdesign.org/learning-course/stage1/1c/exercise5/)
- [Exercise 6: Direction Swap](https://frcdesign.org/learning-course/stage1/1c/exercise6/)
- [Exercise 7: Vertical Rollers](https://frcdesign.org/learning-course/stage1/1c/exercise7/)
- [Exercise 8: Indexer Centering](https://frcdesign.org/learning-course/stage1/1c/exercise8/)
- [Onshape Learning Center](https://learn.onshape.com/)
- [Power Transmission](../power-transmission/)
- [Onshape Fundamentals](../onshape-fundamentals/)

## Notes

- These are deliberately under-specified. If two valid approaches exist,
  pick one and note why — that judgment is the skill.
- Reuse Tube Converter, Robot Shaft, Belt & Chain Gen, and Origin Cube
  everywhere. Speed comes from leaning on them, not from redrawing hex
  shafts by hand.
- Do not ship these practice mechanisms onto a competition robot without a
  design review. They teach CAD, not a legal, robust, game-winning intake.
- The next ticket ([Top-Down Design Methodology](../design-methodology/))
  is Stage 1D: one master layout sketch driving a swerve drivebase.
