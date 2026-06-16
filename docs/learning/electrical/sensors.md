---
layout: electrical-lesson
title: Sensors & Signal Inputs
subtitle: Limit switches, encoders, gyros, and rangefinders — by function and by how they talk to the roboRIO.
permalink: /learning/electrical/sensors/
role: veteran
order: 7
size: 2
time: "1–2 hrs"
---

## Overview

Sensors let the robot perceive its environment and its own mechanisms. A robot
that can sense where its arm is, how far it has driven, or which way it's facing
can do tasks faster and more reliably — and protect itself from breaking. This
lesson categorizes sensors two ways: by **what they measure** and by **how they
communicate** with the roboRIO. Those two views drive design and wiring,
respectively.

## Prerequisites

- [The FRC Control System](../control-system/) and [Wiring Craftsmanship](../wiring-craftsmanship/).

## What you'll learn

- Common sensor types grouped by function.
- The communication protocols sensors use to reach the roboRIO.
- How to wire and locate sensors physically.

## Unit 1 — Sensors by function

- **Proximity / limit switches** — detect presence or an end-of-travel. Types
  include mechanical limit switches, magnetic, inductive, and photoelectric.
- **Distance sensors** — ultrasonic, triangulating rangefinders, and LIDAR.
- **Shaft rotation sensors** — **encoders** (count rotation/position) and
  **potentiometers** (absolute angle over a limited range).
- **Accelerometers** — measure acceleration.
- **Gyroscopes** — measure rotation/heading (a robot's heading gyro is critical
  for swerve and autonomous).

Many brushless motor controllers include a built-in encoder, so you get position
feedback "for free" over CAN.

## Unit 2 — Sensors by communication protocol

How a sensor talks to the roboRIO determines how you wire and program it:

- **Analog input** — outputs a voltage proportional to the reading (e.g. a
  potentiometer or analog pressure sensor).
- **Digital input (DIO)** — on/off signals (limit switches) and pulse-based
  signals (quadrature encoders).
- **Serial bus** — CAN, I2C, SPI, or RS-232 for richer/digital devices. (Ports
  are covered in [roboRIO Ports & Communication Protocols](../roborio-ports/).)

Analog and digital inputs are simple to support; serial-bus sensors are more
capable but more involved.

## Unit 3 — Wiring & placement

- Respect the sensor's voltage (many DIO/I2C devices are **3.3V** — don't feed
  them 5V or 12V).
- Keep signal wires away from motor-power wires to reduce noise.
- Mount sensors rigidly; a limit switch that flexes gives false readings.
- Protect wires at the sensor with strain relief, just like power wiring.

## Steps & acceptance criteria

- [ ] Match three common sensors to what they measure.
- [ ] State which communication category each uses (analog, digital, or serial).
- [ ] Wire a limit switch to a DIO port and an analog sensor to an analog input.
- [ ] Explain why signal and power wiring should be routed separately.

## Resources

- [WPILib: Sensor Overview — Hardware](https://docs.wpilib.org/en/stable/docs/hardware/sensors/sensor-overview-hardware.html)
- [WPILib: Sensor Overview — Software](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/sensors/index.html)
- [WPILib: roboRIO ports / DIO](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/roborio-pinout.html)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — list the sensors your team commonly uses (gyro model, encoders, limit switches) and your standard wiring/port assignments for each.</p>
</div>
