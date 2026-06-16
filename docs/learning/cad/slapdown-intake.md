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

## Overview

A **slapdown intake** flips down to grab game pieces off the floor and folds back
up inside the frame. It combines a pivot (which you learned in the last lesson)
with rollers. This lesson covers the engineering rules that make intakes reliable,
then walks you through modeling one.

This lesson covers **Stage 2C** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/).

## Prerequisites

- [Dead Axle Pivot](../dead-axle-pivot/) completed.

## How to work through it

- [ ] Internalize the intake golden rules before designing.
- [ ] Build the layout, part studio, then assembly.
- [ ] Check that it folds inside the frame and grabs pieces reliably.

## Engineering concepts

- **Intake golden rules.** Intakes should be wide, fast, forgiving of alignment,
  and able to pull a piece in even when it's not perfectly positioned. Reliability
  beats cleverness.
- **Robustness.** Intakes take the most abuse on the robot — they hit the floor,
  walls, and other robots. Design them to survive impacts and to deflect rather
  than break.
- **Pivot.** The deploy/retract pivot needs enough torque to slap down quickly and
  enough strength to take hits. Reuse the dead-axle pivot patterns.
- **Rollers.** Compliant rollers grip and pull pieces in. Spacing and compression
  against the piece (and against a hard surface) determine how well they grab.
- **Zombie axles.** A "zombie axle" is a roller axle supported only on one end (or
  poorly captured) that flexes and causes problems — avoid them by supporting
  roller axles properly on both ends.

## Unit 1 — Layout sketch

Define the deployed and retracted positions, the roller positions and diameters,
the pivot, and the path a game piece takes into the robot. Confirm it folds inside
the frame perimeter.

## Unit 2 — Part studio

Model the rollers, the pivoting frame, structure, and the drive for both the pivot
and the rollers. Support every roller axle on both ends.

## Unit 3 — Assembly

Mate the pivot and rollers, add motors and power transmission, and verify the
intake deploys, grabs, and retracts without collisions.

## Resources

- [Stage 2C: Slapdown Intake (source)](https://frcdesign.org/learning-course/)

## Notes

- An intake that works 95% of the time loses matches — design for the worst-case
  approach angle, not the ideal one.
- Watch for zombie axles: if a roller shaft is only held at one end, fix it before
  it costs you a piece on the field.
