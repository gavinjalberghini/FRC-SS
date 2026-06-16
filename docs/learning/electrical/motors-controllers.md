---
layout: electrical-lesson
title: Motors & Motor Controllers
subtitle: Brushed vs. brushless motors, CAN vs. PWM control, and wiring controllers from the PDH to the motor.
permalink: /learning/electrical/motors-controllers/
role: veteran
order: 6
size: 2
time: "1–2 hrs"
---

## Overview

Motors are how the robot does work, and motor controllers are how the roboRIO
tells them what to do. This lesson covers the common motors and controllers, the
difference between brushed and brushless, and how to wire a controller correctly
from power input to motor output.

## Prerequisites

- [Power Distribution](../power-distribution/) and [Wiring Craftsmanship](../wiring-craftsmanship/).

## What you'll learn

- The difference between brushed and brushless motors.
- Common FRC motors and the controllers that drive them.
- CAN vs. PWM control signaling.
- How to wire a motor controller's power input and motor output.

## Unit 1 — Brushed vs. brushless

- **Brushed motors** (e.g. CIM, BAG, 775) use physical brushes to switch current.
  Simple 2-wire control.
- **Brushless motors** (e.g. NEO, Kraken, Falcon) are more efficient and powerful
  for their size but need a controller that electronically commutates them, plus
  often a sensor feedback connection.

Many modern controllers can run either type — but you must configure the
controller for the correct mode (e.g. SPARK MAX defaults to brushless; hold the
mode button to switch to brushed).

## Unit 2 — Common controllers

| Controller | Vendor | Notes |
| --- | --- | --- |
| **SPARK MAX / SPARK Flex** | REV | Brushed or brushless (NEO). CAN or PWM. |
| **Talon FX (integrated)** | CTRE | Built into Kraken/Falcon brushless motors. CAN. |
| **Talon SRX / Victor SPX** | CTRE | Brushed. CAN or PWM. |

## Unit 3 — CAN vs. PWM

- **CAN bus** is the preferred control method: a single daisy-chained data bus
  carries commands *and* rich feedback (current, temperature, faults, sensor
  data) for many devices. Each device needs a unique CAN ID.
- **PWM** is a simpler one-signal-per-controller method with no feedback. Used
  for basic or legacy setups.

Most competitive robots run nearly everything on CAN.

## Unit 4 — Wiring a controller

1. **Power input** (`V+ / V−` or red/black, *not* `M+/M−`) goes to a
   high-current PDH channel protected by a 40A breaker.
2. **Motor output** goes to the motor leads, red-to-red / black-to-black, using
   Wago 221 or equivalent connectors.
3. **CAN** in/out daisy-chains to the next device (yellow = high, green = low).
4. Confirm the controller's mode LED matches the motor type before enabling.

<div class="callout">
  <div class="callout-icon">⚠️</div>
  <p>Double-check that the red power wire goes to <strong>V+</strong>, never <strong>M+</strong>. Swapping power and motor terminals is a classic, damaging mistake.</p>
</div>

## Steps & acceptance criteria

- [ ] State whether a given motor is brushed or brushless and what mode its
      controller needs.
- [ ] Explain the trade-offs between CAN and PWM control.
- [ ] Wire a motor controller end to end (power in, motor out, CAN) with correct
      polarity and terminals.
- [ ] Verify a controller's status LED indicates the correct mode.

## Resources

- [CTRE Phoenix Hardware Reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
- [REV SPARK MAX documentation](https://docs.revrobotics.com/brushless/spark-max/overview)
- [WPILib: CAN devices](https://docs.wpilib.org/en/stable/docs/software/can-devices/index.html)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — list the specific motors and controllers your team standardizes on, plus your CAN ID numbering scheme.</p>
</div>
