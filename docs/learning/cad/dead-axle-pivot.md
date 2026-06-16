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

## Overview

Many mechanisms pivot: arms, wrists, intakes. This lesson teaches the **dead axle**
pivot — where the axle is fixed and the arm rotates on bearings around it (as
opposed to a "live" axle that spins). You'll learn the engineering trade-offs, then
model the pivot.

This lesson covers **Stage 2B** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/).

## Prerequisites

- All Designer lessons completed; [Basic Shooter](../basic-shooter/) recommended first.

## How to work through it

- [ ] Read the engineering concepts and relate each to a part of the pivot.
- [ ] Build the layout, part studio, then assembly.
- [ ] Verify the arm rotates freely with no binding and minimal play.

## Engineering concepts

- **Strength.** A pivot carries large bending loads, especially at the joint.
  Support the axle on both sides and use enough material at the pivot.
- **Friction.** Bearings at the pivot keep rotation smooth; avoid metal-on-metal
  rubbing that wastes power and wears parts.
- **Power transmission.** The arm is usually driven by a gearbox through chain,
  belt, or gears. Choose a reduction that holds position and moves at the speed you
  need.
- **Tensioning.** Chain and belt drives need adjustable tension — design in a way
  to take up slack (e.g., a tensioner or slotted mount).
- **Backlash.** Slop in gears/chain lets the arm wiggle at the end of travel. Less
  backlash = more precise positioning; tighten the drivetrain where precision
  matters.

## Unit 1 — Layout sketch

Define the pivot center, arm length, range of motion, and where the gearbox and
chain/belt run. The pivot point is the anchor for everything.

## Unit 2 — Part studio

Model the dead axle, the rotating arm with bearings, structure, and the drive.
Make sure the axle is captured and the bearings seat properly.

## Unit 3 — Assembly

Mate the arm to rotate about the dead axle, add the gearbox and chain/belt, and
verify the full range of motion with no collisions and minimal backlash.

## Resources

- [Stage 2B: Dead Axle Pivot (source)](https://frcdesign.org/learning-course/)

## Notes

- Dead axles are common because they're strong and let you put bearings in the
  rotating part instead of supporting a spinning shaft across a long span.
- Always check the *full* sweep of the arm in the assembly — collisions usually
  hide at the extremes of travel.
