---
layout: cad-lesson
title: Basic Shooter
subtitle: Model a flywheel shooter while learning rigidity, trajectory, exit velocity, compression, and spin.
permalink: /learning/cad/basic-shooter/
role: veteran
order: 7
size: 2
time: "2–3 hrs"
---

## Overview

This is your first full mechanism. As a Veteran Designer you model the mechanisms
that win matches and learn the engineering concepts behind them. First up: a
**flywheel shooter**. You'll learn why a shooter is built the way it is, then model
it with a layout sketch, part studio, and assembly.

This lesson covers **Stage 2A** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/).

## Prerequisites

- All Designer lessons completed.

## How to work through it

- [ ] Read the engineering concepts first — they explain the design decisions.
- [ ] Build the layout sketch, part studio, then assembly in order.
- [ ] Check that the flywheel spins freely and the game piece path is clear.

## Engineering concepts

- **Structure rigidity.** A shooter pushes hard on the game piece; a flexy frame
  steals energy and ruins consistency. Build it stiff.
- **Ball trajectory.** The launch angle and height set where the game piece lands.
  Design the geometry around the target.
- **Exit velocity.** Faster flywheel surface speed = farther/faster shot. Set the
  flywheel diameter and reduction to hit your target velocity.
- **Compression & wrap.** The game piece must be squeezed (compression) against the
  wheel over enough contact area (wrap) to transfer energy without slipping.
- **Spin control.** Differential wheel speeds (top vs. bottom) add backspin/topspin
  to stabilize the shot.
- **Friction & efficiency.** Wheel material and surface finish determine grip;
  bearings and alignment determine how much motor power actually reaches the piece.

## Unit 1 — Layout sketch

Sketch the shooter's key geometry: flywheel position and diameter, the feed path,
the compression gap, and the launch angle. This drives the whole model.

## Unit 2 — Part studio

Model the structure, flywheel(s), shafts, and hood referencing the layout. Use the
Robot Shaft FeatureScript for shafts and Tube Converter for structure.

## Unit 3 — Assembly

Insert the motor and parts, mate the flywheel so it spins freely, and verify the
game piece path and compression. Confirm the structure is rigid where the load is.

## Resources

- [Stage 2A: Basic Shooter (source)](https://frcdesign.org/learning-course/)

## Notes

- Compression is the number-one tuning variable on a real shooter — model it as an
  adjustable gap so you can iterate.
- A shooter is only as consistent as its rigidity and its feed; design both
  deliberately.
