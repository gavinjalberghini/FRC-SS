---
layout: electrical-lesson
title: The FRC Control System
subtitle: Meet every device on the robot — roboRIO, PDH/PDP, radio, breakers, and the RSL — and how they connect.
permalink: /learning/electrical/control-system/
role: technician
order: 2
size: 2
time: "1–2 hrs"
---

## Overview

Before you wire anything, you need a mental map of the whole control system:
what each device is, what it does, and how power and signals flow between them.
This lesson is the "identification" half of Level 1 for the electronics side —
the goal is to recognize every device on sight and explain its job.

## Prerequisites

- [Electrical Safety](../electrical-safety/).

## What you'll learn

- The role of each core control-system component.
- How power flows from the battery to actuators.
- How control signals flow from the driver station to the robot.

## Unit 1 — The core devices

| Device | Job |
| --- | --- |
| **12V Battery** | Stores energy; the only power source on the robot. |
| **Main breaker (120A)** | Master cutoff between battery and everything else. |
| **Power Distribution Hub / Panel (PDH/PDP)** | Splits battery power into protected channels for every device. |
| **roboRIO** | The robot's main controller — runs your code and talks to all devices. |
| **Radio (e.g. VH-109)** | Wireless link between the robot and the driver station. |
| **Motor controllers** (SPARK MAX, Talon, etc.) | Take signals from the roboRIO and drive the motors. |
| **Robot Signal Light (RSL)** | Required light showing robot state (solid = enabled-ready, blinking = enabled). |
| **Pneumatics module (PCM/PH)** | Controls the compressor and solenoids (covered in the pneumatics lessons). |

## Unit 2 — How power flows

Battery → **main breaker** → **PDH** → branch channels:

- **High-current channels** (with 40A breakers) feed motor controllers.
- **Fused low-current channels** feed the roboRIO, radio, and other electronics.

Every device's power comes from the PDH. If a device has no power, you trace it
back toward the PDH, then the breaker, then the battery.

## Unit 3 — How signals flow

- The **driver station** laptop sends commands over Wi-Fi/Ethernet to the
  **radio**.
- The radio passes them over Ethernet to the **roboRIO**.
- The roboRIO sends control signals over the **CAN bus** (or PWM) to motor
  controllers and the pneumatics module.
- Sensors send data *back* to the roboRIO so your code can react.

Understanding these two flows — power and signal — is what lets you guess where
a problem is before you even pick up a tool.

## Steps & acceptance criteria

- [ ] Point to and name every core device on a real (or pictured) robot.
- [ ] Trace the power path from the battery to a motor.
- [ ] Trace the signal path from the driver station to a motor controller.
- [ ] Explain the difference between a high-current and a fused channel on the PDH.

## Resources

- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
- [WPILib: Zero to Robot](https://docs.wpilib.org/en/stable/docs/zero-to-robot/introduction.html)
- Vendor docs: [REV Power Distribution Hub](https://docs.revrobotics.com/ion-control/pdh/overview), [CTRE](https://docs.ctr-electronics.com/)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — paste a labeled photo or diagram of your team's standard control-system layout here so new members can match the table above to real hardware.</p>
</div>
