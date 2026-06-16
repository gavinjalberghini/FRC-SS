---
layout: lesson
title: Phoenix Tuner X
subtitle: Configure, test, and diagnose CTRE devices without writing code.
permalink: /learning/programming/phoenix-tuner/
role: programmer
order: 5
size: 2
time: "~1 hr"
---

## Overview

Phoenix Tuner X is CTRE's companion app for updating, configuring, analyzing, and
directly controlling their devices (motor controllers, CANcoders, etc.). It lets
you test hardware and tune settings quickly — without deploying robot code — which
makes it one of the fastest ways to confirm wiring and diagnose problems.

## Prerequisites

- [FRC Hardware & Firmware](../frc-hardware/) — know what the devices are.
- Access to a robot (or test bench) with CTRE devices on the CAN bus.

## What you'll learn

- How to connect to a robot and browse its CTRE devices.
- How to identify a specific device by blinking it.
- How to drive a motor manually and plot its position and velocity.

## Steps & acceptance criteria

- [ ] Read through the [Phoenix Tuner X documentation](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/index.html)
      to understand the available configuration and testing features.
- [ ] Open Phoenix Tuner X while connected to a device and explore the interface
      and device settings.
- [ ] **Blink** a device to confirm you're looking at the correct physical unit.
- [ ] Select a motor and control its movement using a **voltage** command.
- [ ] Plot the motor's **position** and **velocity** on the graph while you drive it.

## A naming & ID convention (recommended)

Consistent device IDs and names make code and debugging far clearer. One scheme
that works well for swerve robots:

- IDs are **two-digit numbers**. The tens digit identifies the module, the ones
  digit identifies the device on that module:
  - Tens: front-left `1`, front-right `2`, back-left `3`, back-right `4`,
    non-module devices `0` or `5`.
  - Ones: drive motor `1`, angle/steer motor `2`, CANcoder `3`, other `4`–`9`.
- Names use `camelCase`, with the module first, then the function — e.g.
  `frontLeftDrive`, `frontLeftAngle`, `frontLeftCAN` (keep "CAN" capitalized).

## Resources

- [Phoenix Tuner X documentation](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/index.html)
- [CTRE Phoenix 6 documentation](https://v6.docs.ctr-electronics.com/en/stable/index.html)

## Notes

- Configuring settings in Phoenix Tuner X (rather than only in code) makes them
  consistent across every computer that deploys to the robot.
- Phoenix Tuner X is mainly a *speed* tool — it shortens the test/diagnose loop so
  you aren't redeploying code just to check a wire or a direction.
