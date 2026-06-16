---
layout: cad-lesson
title: Onshape Fundamentals
subtitle: Part studios, plates, and assemblies — the core CAD skills, built around FRC-relevant exercises.
permalink: /learning/cad/onshape-fundamentals/
role: designer
order: 2
size: 3
time: "Self-paced (multi-week)"
---

## Overview

This is the largest lesson in the curriculum and the foundation for everything
after it. You'll learn sketching, part modeling, multi-part modeling, and
assemblies through a series of FRC-relevant exercises. Work through the exercises
**in order** — each one builds on the previous, and you're encouraged to
experiment to figure out how each feature works.

This lesson covers **Stage 1A** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage1/1a/section1-setup/).
Before starting, make sure the required part library and FeatureScripts are added
(see [Getting Started](../getting-started/)).

## Prerequisites

- [Getting Started with Onshape](../getting-started/) completed.
- The Stage 1A exercise document copied into your own Onshape account.

## How to work through it

- [ ] Copy the provided Stage 1A document into your account.
- [ ] Do every exercise in order using the page-navigation buttons.
- [ ] Check that your CAD makes physical sense — parts shouldn't overlap.
- [ ] Aim for **fully constrained** sketches (everything turns black).

## Background — Box tubes

Box tube provides the primary structure of an FRC robot, from the drivetrain to
the superstructure. From the side a box tube is a simple **rectangle**. Tubing is
named by its cross-section size, spoken aloud:

- **1×1** ("one-by-one")
- **2×1** ("two-by-one")
- **2×2** ("two-by-two")

The workflow is always the same: sketch the rectangle, **extrude** it as a solid
block, then run **Tube Converter** to hollow it out and add the hole pattern.

## Section 1 — Part Studio Fundamentals

- **Exercise 0: Navigation.** Learn to orbit, pan, zoom, and use the view cube.
- **Exercise 1: First Tubes.** Sketch a rectangle, extrude it, and convert it to a
  box tube. Get comfortable with the sketch → extrude → tube workflow.
- **Exercise 2: More Tubes (cross rails).** Add cross rails to a drivetrain. Pick
  the right extrude setting so parts land in the right place, then change the part
  **appearance** so the model looks clean. Make sure parts don't overlap.
- **Exercise 3: Sketch Basics.** Practice sketch constraints and dimensions; build
  fully-constrained sketches that turn black.
- **Exercise 4: Drivetrain Frame.** Sketch and extrude a full drivetrain frame,
  then tube-convert it. **Mirror across both X and Y axes** using construction
  lines — never draw both sides by hand. Use the origin as the center reference and
  avoid overdimensioning.
- **Exercise 5: Box Frame.** Build a rectangular box frame.
- **Exercise 6: Triangle Frame.** Build an angled/triangular frame to practice
  non-orthogonal geometry.

## Section 2 — Plates

Plates are flat parts (often aluminum or polycarbonate) that tie tubes together
and mount components.

- **Exercise 1: Plate Workflow.** The standard way to model a plate from a face.
- **Exercise 2: Gusset.** Model a gusset that joins two tubes.
- **Exercise 3: Superstructure Gussets & Plate.** Combine multiple gussets and a
  plate into a superstructure connection.
- **Exercise 4: Motor Mounting.** Create a plate with the correct bolt pattern to
  mount a motor.

## Section 3 — Assemblies

An assembly brings finished parts together and defines how they move with **mates**.

- **Exercise 1: Rivets.** Use rivets to fasten parts; learn fastened mates.
- **Exercise 2: Swerve Drive.** Insert and mate a swerve module.
- **Exercise 3: Gusset Setup.** Position gussets in the assembly.
- **Exercise 4: Full Frame.** Assemble the complete drivetrain frame.
- **Exercise 5: Finishing the Frame.** Final fasteners, checks, and cleanup so the
  drivebase is competition-ready.

## Resources

- [Stage 1A: Onshape Fundamentals (source)](https://frcdesign.org/learning-course/stage1/1a/section1-setup/)
- [Using the Tube Converter FeatureScript](https://onshape4frc.com/blog/using-tube-converter/)
- [Onshape Learning Center](https://learn.onshape.com/)

## Notes

- A fully-constrained sketch (all black) is the goal — it won't shift unexpectedly
  later.
- Always sanity-check against real life: if two tubes overlap in CAD, they'll
  collide on the real robot.
- Use symmetry (mirror/pattern) instead of redrawing geometry; it's faster and
  easier to edit.
