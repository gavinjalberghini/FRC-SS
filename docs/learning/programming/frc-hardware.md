---
layout: lesson
title: FRC Hardware & Firmware
subtitle: Get to know the robot's electronics and how to keep their firmware and tools up to date.
permalink: /learning/programming/frc-hardware/
role: programmer
order: 4
size: 2
time: "1–2 hrs"
---

## Overview

Software runs on hardware, and FRC robots use a specific set of electronics. This
lesson familiarizes you with the common devices, how to update their firmware,
and how to install the software you'll need on your computer. Knowing the hardware
makes debugging far easier — many "code" problems are really wiring, firmware, or
configuration problems.

## Prerequisites

- None, though it helps to have done [Git Fundamentals](../git/) first.

## What you'll learn

- The roles of the main control-system components.
- Where to find official documentation for each device.
- How to update firmware and install the FRC development tools.

## Steps & acceptance criteria

- [ ] Read the documentation for the core control-system devices:
  - [ ] [roboRIO](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/imaging-your-roborio.html) — the robot's main controller.
  - [ ] [Robot radio](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/radio-programming.html) — networking between robot and driver station.
- [ ] Read about the common motor controllers, power, and pneumatics devices:
  - [ ] [CTRE devices (Phoenix)](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
  - [ ] [REV Power Distribution Hub (PDH)](https://docs.revrobotics.com/ion-control/pdh/overview)
  - [ ] [REV Mini Power Module (MPM)](https://docs.revrobotics.com/ion-control/mpm/overview)
  - [ ] [REV Pneumatic Hub (PH)](https://docs.revrobotics.com/ion-control/ph/overview)
- [ ] Read about common sensors and coprocessors:
  - [ ] [Limelight](https://docs.limelightvision.io/)
  - [ ] [PhotonVision](https://docs.photonvision.org/en/latest/)
- [ ] Install the FRC development tools on your computer:
  - [ ] [FRC Game Tools](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/frc-game-tools.html) (Driver Station, roboRIO Imaging Tool).
- [ ] Where possible, update each device to its latest firmware following the
      vendor's instructions.

## Resources

- [WPILib: Zero to Robot](https://docs.wpilib.org/en/stable/docs/zero-to-robot/introduction.html) — start-to-finish robot setup.
- [CTRE Phoenix documentation](https://v6.docs.ctr-electronics.com/en/stable/index.html)
- [REV Robotics documentation](https://docs.revrobotics.com/)

## Notes

- Firmware mismatches are a common source of "device not found" or erratic
  behavior. When something misbehaves, checking firmware versions is a good early
  step.
- Configuring a device's settings on the device itself (rather than only in code)
  keeps those settings consistent no matter which laptop deploys the code.
