---
layout: electrical-lesson
title: Status Lights & Fault Codes
subtitle: Read the roboRIO, PDH, motor controller, and pneumatics status LEDs to pinpoint faults fast.
permalink: /learning/electrical/status-lights-fault-codes/
role: lead
order: 10
size: 2
time: "1–2 hrs"
---

## Overview

Every major device on the robot reports its state through LEDs. A Level 3
technician can glance at a robot and read its "trouble lights" to narrow a
problem in seconds instead of guessing. This lesson covers the roboRIO's status
LEDs and how to look up fault codes for the PDH, motor controllers, and the
pneumatics module.

## Prerequisites

- [The FRC Control System](../control-system/) and [roboRIO Ports](../roborio-ports/).

## What you'll learn

- What each roboRIO LED means.
- How to interpret motor controller and pneumatics module status LEDs.
- The habit of confirming "lights should match" before digging deeper.

## Unit 1 — roboRIO LEDs

- **Status** — self-test/boot health. Repeated blink patterns indicate problems:
  2 blinks = likely failed upgrade; 3 = safe mode; 4 = repeated crashes (often
  out of memory); steady/irrecoverable = call NI.
- **Power** — Green = OK; Red = a voltage rail is shorted/overcurrent; Blinking
  Red = over 16V applied (outputs disabled); Yellow = **brownout** under ~6V
  (outputs disabled); Off = voltage out of range.
- **Mode** — Off = outputs disabled; Green = autonomous; Yellow = teleop; Red =
  test/unknown.
- **Comm** — Solid Red = no code; Blinking Red = E-Stop; Green = connected to
  driver station.
- **RSL** — mirrors the Robot Signal Light's connection status.

## Unit 2 — Power Distribution Hub / Panel

The PDH/PDP status LED reports healthy operation vs. faults (no communication,
sticky faults, low battery). On the older PDP, the trouble lights "should always
match except in bootloader mode." Look up the exact chart in the vendor docs.

## Unit 3 — Motor controllers

Controllers like the Talon FX/SRX and SPARK MAX use LED **color and blink
pattern** to show enabled/disabled, direction, brushed/brushless mode, CAN
status, and faults. Memorize the codes for the controllers your team runs, and
keep the vendor's LED chart handy.

## Unit 4 — Pneumatics module (PCM/PH)

The control module's status LEDs report power, CAN communication, compressor
state, and solenoid faults (e.g. a shorted solenoid). A healthy module and a
fault-state module look different at a glance.

## Steps & acceptance criteria

- [ ] Interpret every roboRIO LED state from memory.
- [ ] Look up and explain the fault codes for your team's motor controllers.
- [ ] Explain the PCM/PH status LED states.
- [ ] Given a robot showing a brownout or "no code" light, state what it means.

## Resources

- [NI roboRIO User Manual — LED states](https://www.ni.com/docs/en-US/bundle/roborio-frc-2/page/manual.html)
- [CTRE Phoenix — status LED references](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
- [REV — SPARK MAX & Pneumatic Hub LED references](https://docs.revrobotics.com/)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — print or paste the exact LED/fault-code charts for the specific roboRIO, controllers, and pneumatics module your team uses, since codes vary by device and firmware.</p>
</div>
