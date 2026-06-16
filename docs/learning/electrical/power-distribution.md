---
layout: electrical-lesson
title: Power Distribution
subtitle: The battery, main breaker, and Power Distribution Hub — how power flows and how channels are protected.
permalink: /learning/electrical/power-distribution/
role: technician
order: 3
size: 2
time: "1 hr"
---

## Overview

The Power Distribution Hub (PDH) — or the older Power Distribution Panel (PDP) —
is the heart of the robot's power system. It takes one big input from the
battery and splits it into many protected outputs. This lesson explains how the
distribution system is organized so you can wire to it correctly and read it
when something trips.

## Prerequisites

- [Electrical Safety](../electrical-safety/).
- [The FRC Control System](../control-system/).

## What you'll learn

- How the battery, Anderson connector, and main breaker connect to the PDH.
- The difference between high-current and fused channels.
- How channel breakers and fuses are sized and why.
- How to read the PDH's status/trouble lights.

## Unit 1 — Battery to PDH

1. The battery connects to the robot through an **Anderson SB50 connector**.
2. The **positive** lead runs through the **120A main breaker**, then to the
   PDH's main positive input.
3. The **negative** lead runs straight to the PDH's main negative input.
4. Heavy current uses thick wire — typically **6 AWG** for the main leads.

The main breaker is both protection *and* the robot's on/off switch.

## Unit 2 — Channels

The PDH provides two kinds of outputs:

- **High-current channels** accept replaceable **40A (or 30A) breakers** and
  feed motor controllers. The white graphics on the hub show which breaker pairs
  with which terminal pair.
- **Fused channels** accept small automotive **mini-fuses** (e.g. 10A) and feed
  low-current electronics like the roboRIO and radio. Some channels are
  *non-switchable* (always on) — use these for devices that must never be cut.

Match the breaker/fuse to the wire and the device, and stay within the rules in
the current game manual.

## Unit 3 — Reading the PDH

The PDH has a status LED and per-channel indicators. In normal operation the
lights are healthy/green; a tripped channel, low battery, or fault will show a
different pattern. You'll learn the full code chart in
[Status Lights & Fault Codes](../status-lights-fault-codes/).

## Steps & acceptance criteria

- [ ] Identify the main positive/negative inputs and the main breaker connection.
- [ ] Explain which channels you'd use for a motor controller vs. the roboRIO.
- [ ] Select a correct breaker/fuse size for a given wire and device (per the rules).
- [ ] Locate the CAN terminals and termination switch on the PDH.

## Resources

- [REV Power Distribution Hub overview](https://docs.revrobotics.com/ion-control/pdh/overview)
- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html) — the PDH wiring steps.
- [CTRE Power Distribution Panel](https://docs.ctr-electronics.com/) (for robots using the older PDP).

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — document your team's standard channel assignments (which breaker/fuse goes in which channel for which subsystem) so wiring is consistent year to year.</p>
</div>
