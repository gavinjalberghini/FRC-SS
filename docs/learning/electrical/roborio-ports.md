---
layout: electrical-lesson
title: roboRIO Ports & Communication Protocols
subtitle: CAN, I2C, SPI, RS-232, MXP, and the user/reset buttons — what each port does and when to use it.
permalink: /learning/electrical/roborio-ports/
role: lead
order: 9
size: 2
time: "1–2 hrs"
---

## Overview

The roboRIO is the robot's main controller, and it has a lot of specialty ports.
Level 3 technicians understand every port — not just the ones they use most — so
they can wire unusual devices and reason about communication problems. This
lesson is a tour of the roboRIO's ports and the protocols they speak.

## Prerequisites

- [The FRC Control System](../control-system/) and [Sensors & Signal Inputs](../sensors/).

## What you'll learn

- The communication protocols available on the roboRIO and their wiring.
- What the onboard buttons and the MXP expansion port do.
- A habit of researching real-world uses for each port.

## Unit 1 — CAN

The **CAN bus** is the communications backbone of the robot. It connects the
roboRIO to the PDH, motor controllers, and the pneumatics module on a single
daisy-chained pair.

- **Yellow = HIGH, Green = LOW.** Newer roboRIOs print the color names on the
  connector.
- The bus must be **terminated** at both ends (the PDH has a termination switch).

## Unit 2 — Serial protocols

- **I2C (Inter-Integrated Circuit)** — a 2-wire bus where many devices share the
  lines, each with a unique address. Pins: Ground, Power (**3.3V**), System
  Clock, System Data. roboRIO is master; devices are slaves.
- **SPI (Serial Peripheral Interface)** — a faster bus that talks to up to 4
  devices using a shared clock/data set plus a per-device Chip Select. Signals:
  SCK (clock), MOSI (master out/slave in), MISO (master in/slave out). Often used
  for onboard gyros.
- **RS-232 (UART)** — a basic, relatively slow but very universal serial link.
  Pins: Ground, Receive, Transmit.

## Unit 3 — Expansion & buttons

- **MXP (myRIO Expansion Port)** — accepts specialty add-on boards that expand
  the roboRIO's I/O. Screw points secure the board.
- **Reset button** — held for 5 seconds, reboots the FPGA and processor.
- **User button** — a general-purpose button readable in code (**not**
  debounced).

## Unit 4 — "Research Usage"

For each specialty port, find one real example of a team or device using it
(e.g. a navX gyro on SPI/I2C, a sensor on RS-232). Being able to point to a
concrete use cements what the port is for.

## Steps & acceptance criteria

- [ ] Name every port on the roboRIO and the protocol it uses.
- [ ] State the wire/pin meaning for CAN, I2C, SPI, and RS-232.
- [ ] Explain what the reset and user buttons do.
- [ ] Research and present one real-world device that uses each specialty port.

## Resources

- [WPILib: roboRIO pinout / accessing the I/O](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/roborio-pinout.html)
- [WPILib: CAN devices](https://docs.wpilib.org/en/stable/docs/software/can-devices/index.html)
- [NI roboRIO User Manual](https://www.ni.com/docs/en-US/bundle/roborio-frc-2/page/manual.html)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — record which roboRIO ports your team actually uses each season and for which device, so the next technician can trace them quickly.</p>
</div>
