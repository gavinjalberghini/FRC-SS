---
layout: mechanical-lesson
title: Power Transmission & Drivetrains
subtitle: Gears, belts, chain, shafts, and bearings — how motor power becomes robot motion.
permalink: /learning/mechanical/power-transmission-drivetrains/
role: lead
order: 11
size: 3
time: "Multi-session"
---

## Overview

Almost every mechanism moves because a motor's power is transmitted through
gears, belts, or chain and supported by shafts and bearings. Understanding power
transmission lets you assemble gearboxes and drivetrains correctly and diagnose
them when they bind or skip. This is the mechanical-build counterpart to the CAD
curriculum's power-transmission lesson.

## Prerequisites

- All of Level 1 and Level 2.

## What you'll learn

- How gears, belts, and chain transmit power and change speed/torque.
- What gear ratio means and how it trades speed for torque.
- How shafts and bearings support rotating parts.
- The basics of assembling a gearbox and a drivetrain.

## Unit 1 — Gears, belts, and chain

- **Gears** mesh tooth-to-tooth — compact and rigid, but need correct **center
  distance** so they mesh without binding or slop.
- **Belts** (timing/GT2) run quietly over pulleys and need correct **tension** and
  alignment.
- **Chain** (#25, #35) runs over sprockets, tolerates more distance and dirt, and
  needs **tension** (often via a tensioner or adjustable mount).

## Unit 2 — Gear ratio, speed, and torque

A **gear ratio** compares input to output teeth. A **reduction** (small driving a
large gear) trades **speed for torque** — slower output, more force. Most FRC
mechanisms reduce a fast motor down to a usable speed with high torque.

- Reduction = (driven teeth) ÷ (driving teeth).
- Stacked **stages** multiply: a 4:1 then 3:1 gearbox is 12:1 overall.
- More torque = more force at the mechanism; less speed = slower motion.

## Unit 3 — Shafts & bearings

- **Shafts** (round or hex) carry the rotating load; hex shafts positively drive
  hex-bore gears/sprockets.
- **Bearings** support shafts with low friction; they press into bores and must be
  **square and fully seated**.
- **Retaining** features (shaft collars, retaining rings, spacers) keep parts
  located on the shaft.

## Unit 4 — Assembly basics

- Set the correct **center distance** for gears and **tension** for belt/chain —
  too tight binds and wears, too loose skips.
- Make sure shafts spin **freely** by hand before powering — bind means
  misalignment or an unseated bearing.
- Confirm gears/sprockets are **aligned** in the same plane.

## Steps & acceptance criteria

- [ ] Explain the difference between gear, belt, and chain transmission.
- [ ] Calculate the overall ratio of a two-stage reduction and state its effect on
      speed and torque.
- [ ] Identify shafts, bearings, and retaining hardware in a gearbox.
- [ ] Assemble a gearbox/drive stage that spins freely with correct mesh/tension.

## Resources

- [CAD Curriculum: Power Transmission & Gearboxes]({{ '/learning/cad/power-transmission/' | relative_url }})
- [WPILib: Hardware Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/index.html)
- Vendors: [WCP](https://wcproducts.com/), [REV Robotics](https://www.revrobotics.com/), [AndyMark](https://www.andymark.com/)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — document your team's standard drivetrain (e.g. swerve modules or a kit chassis), the gearboxes you use, and your assembly checklists.</p>
</div>
