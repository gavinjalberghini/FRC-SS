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

## Overview

Almost every mechanism on a robot moves because a motor's power is transmitted
through gears, belts, or chains. This lesson teaches the engineering behind power
transmission and then walks you through modeling real gearboxes in Onshape.

This lesson covers **Stage 1B** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/).

## Prerequisites

- [Onshape Fundamentals](../onshape-fundamentals/) completed.

## How to work through it

- [ ] Read each concept and find the parts it describes in the part library.
- [ ] Build each gearbox exercise in your copied document.
- [ ] Calculate the reduction by hand and verify it against your model.

## Unit 1 — Motors

FRC motors (e.g., Kraken, NEO, Falcon, CIM) convert electrical power into
rotation. Key specs are **free speed** (max RPM with no load), **stall torque**
(max torque at zero speed), and **current draw**. Mechanisms are designed around
the motor's power curve.

## Unit 2 — Shafts and bearings

- **Shafts** transmit rotation. Common types are round (with retaining features)
  and **hex** (1/2" hex is standard — it transmits torque through its shape).
- **Bearings** let a shaft spin freely while supporting it. They press into a bore
  or mount in a bearing block. Every rotating shaft needs to be supported, usually
  at two points.

## Unit 3 — Torque and speed

Gearing trades **speed for torque** (or vice versa). A *reduction* multiplies
torque and divides speed:

\[ \text{ratio} = \frac{\text{driven teeth}}{\text{driving teeth}} \]

A 4:1 reduction gives 4× the torque at 1/4 the speed. Choosing the right reduction
is the heart of mechanism design — too fast and it stalls, too slow and it wastes
the motor.

## Unit 4 — Gear basics

- Gears mesh tooth-to-tooth and must share the same **diametral pitch (DP)** —
  20 DP and 32 DP are common in FRC.
- The distance between two gear centers depends on their tooth counts and DP, so
  gear placement drives your layout sketch.
- Meshing gears spin in **opposite** directions.

**Exercise 1 — Simple gearbox.** Model a single-stage gearbox: a pinion on the
motor driving a larger gear on the output shaft. Verify the center distance and
the reduction.

**Exercise 2 — Two-stage gearbox.** Add a second reduction stage to multiply the
ratio. Practice stacking gears and supporting the intermediate shaft on bearings.

## Unit 5 — Belts and pulleys

- Timing belts (e.g., GT2) run on toothed **pulleys** and transmit power with no
  slip across a distance.
- Belt length must match the **center distance** between pulleys; the
  Belt & Chain Gen FeatureScript helps you size and visualize them.
- Belts are quiet and light but can't transmit as much torque as chain.

## Unit 6 — Chain and sprockets

- Roller chain (#25, #35) runs on **sprockets** for high-torque transmission over
  distance (common on drivetrains and arms).
- Chain needs **tensioning** — too loose and it skips, too tight and it binds.

**Exercise 3 — Gear and belt gearbox.** Combine a gear stage and a belt stage in
one gearbox to practice mixing transmission types.

## Resources

- [Stage 1B: Power Transmission (source)](https://frcdesign.org/learning-course/)
- [Belt & Chain Gen FeatureScript](https://onshape4frc.com/)
- [WCP / REV / AndyMark gear and pulley catalogs](https://www.wcproducts.com/)

## Notes

- Always write down your target reduction *before* picking gears — design the math
  first, then the geometry.
- Leave room for bearings and retaining features when you place shafts; a gear
  that meshes perfectly but can't be supported is useless.
