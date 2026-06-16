---
layout: cad-lesson
title: Cascade Elevator
subtitle: Model a cascade elevator with elevator blocks, chain attachment, rigging, cable clamps, and a gearbox.
permalink: /learning/cad/cascade-elevator/
role: lead
order: 10
size: 3
time: "3–4 hrs"
---

## Overview

The capstone of the curriculum: a **cascade elevator** that extends multiple stages to
reach high while packaging small. Elevators are precise, fast, and mechanically
rich — they tie together structure, bearings, power transmission, and rigging.
This is the most involved mechanism in the curriculum.

This lesson covers **Stage 2D** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/).

## Prerequisites

- All earlier mechanism lessons completed.

## How to work through it

- [ ] Study each engineering concept — elevators are unforgiving of mistakes.
- [ ] Build the layout, part studio, then assembly.
- [ ] Verify each stage extends smoothly and the rigging stays tensioned.

## Engineering concepts

- **Elevator blocks.** The blocks (with bearings or slides) that ride in the rails
  and constrain each stage to move only up and down. Alignment here is everything.
- **Chain attachment.** How the driven chain attaches to the carriage so the motor
  can pull it up and down. The attachment must be strong and not introduce slop.
- **Rigging.** A **cascade** elevator uses cables/belts routed over pulleys so that
  driving one stage extends all stages together, multiplying travel. Get the
  routing right or the stages won't move proportionally.
- **Cable clamp.** Cables must be clamped securely at their ends — a slipping clamp
  drops the whole elevator.
- **Cable ends.** Properly terminated cable ends (swaged/clamped) prevent fraying
  and failure under repeated load.
- **Gearbox.** The elevator gearbox sets lift speed and torque, and must hold
  position (or have a brake) so the elevator doesn't fall under gravity.

## Unit 1 — Layout sketch

Define the number of stages, retracted and fully-extended heights, rail and block
positions, and the cable/chain routing. The rigging geometry is the trickiest part
— sketch it carefully.

## Unit 2 — Part studio

Model the rails, carriage, elevator blocks, pulleys, and gearbox referencing the
layout. Support bearings and align rails precisely.

## Unit 3 — Assembly

Mate the stages so each slides freely, route the rigging, add the gearbox, and
verify smooth, proportional extension across the full range with tension
maintained.

## Resources

- [Stage 2D: Cascade Elevator (source)](https://frcdesign.org/learning-course/)

## Notes

- Cascade rigging multiplies both travel **and** the consequences of a mistake —
  double-check that every stage moves the right amount.
- Plan for the elevator holding position against gravity from the start (brake or
  self-locking ratio); it's hard to add later.

## What's next

You've reached the end of the curriculum. Keep going: take on independent robot
and mechanism projects, get design feedback from teammates and mentors, study
strong public CAD from other teams, and keep sharpening your engineering and
strategic judgement. See the [CAD & Design Hub](../) for the full roadmap.
