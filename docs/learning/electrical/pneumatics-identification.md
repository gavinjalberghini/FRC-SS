---
layout: electrical-lesson
title: "Pneumatics 1: Component Identification"
subtitle: Recognize every part of an FRC pneumatic system by sight, from the compressor to press-fit connectors.
permalink: /learning/electrical/pneumatics-identification/
role: technician
order: 4
size: 1
time: "45–60 min"
---

## Overview

Pneumatics use compressed air to move mechanisms. Before you can build or
troubleshoot a pneumatic system, you have to know the parts on sight. This is the
identification level — memorize the name of each component and pay close
attention to the **physical differences** between parts that look similar.

## Prerequisites

- [Electrical Safety](../electrical-safety/).

## What you'll learn

- The name and appearance of every base pneumatic component.
- How to tell visually similar parts apart (single vs. double solenoids, analog
  vs. digital pressure switches).

## Unit 1 — The base components

Learn to recognize each of these by sight:

- **Pneumatics Control Module / Pneumatic Hub (PCM/PH)** — the "little brain"
  that controls the safety parts of the system independently of the roboRIO.
- **Compressor** — a motor-driven piston that pulls in air and pushes it out at
  higher-than-atmospheric pressure.
- **Accumulator (air tank)** — a reservoir where compressed air builds up. More
  tanks means the compressor cycles on/off less often.
- **Air pressure switch** — senses high-side pressure and signals when the system
  reaches its limit (FRC max = **120 PSI**).
- **Safety relief valve** — a mechanical valve designed to vent if pressure
  exceeds its rating; mounted as close to the compressor output as possible.
- **Gauge** — shows the pressure (in PSI) in that part of the system. A system
  can have several gauges.
- **Regulator** — lowers the pressure between two segments of the circuit
  (typically down to ~60 PSI on the working side).
- **Pressure vent plug** — manually vents/purges the system so it's safe to work
  on.
- **Flow control** — restricts airflow to slow a cylinder's motion in one
  direction.
- **Solenoids (single & double)** — electrically operated valves that direct
  air. (See Unit 2.)
- **Cylinder (piston)** — uses air to push a rod in and out of a cylindrical body.
- **Tubing** — ¼ inch (outside diameter) air line.
- **Press-fit connectors** — push-to-connect fittings that join tubing to
  components.

## Unit 2 — Telling similar parts apart

- **Single vs. double solenoid.** A *single* solenoid has one coil and springs
  back when de-energized; a *double* solenoid has two coils and stays in its last
  position. Count the coils/connectors.
- **Analog vs. digital pressure switch.** The analog version can report the
  actual pressure to the driver station; the digital (binary) version only
  reports whether the system is at max pressure.
- **Cylinder sizing.** Cylinders are described by **bore** (body diameter) and
  **stroke** (how far the rod travels).

## Steps & acceptance criteria

- [ ] Name every component above when shown a real part or photo.
- [ ] Correctly distinguish a single from a double solenoid.
- [ ] Correctly distinguish an analog from a digital pressure switch.
- [ ] Pass your team's Pneumatics Level 1 identification check.

## Resources

- [FRC Pneumatics Manual (FIRST)](https://firstfrc.blob.core.windows.net/frc2017/pneumatics-manual.pdf)
- [REV Pneumatic Hub overview](https://docs.revrobotics.com/ion-control/ph/overview)
- [WPILib: Pneumatics](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/pneumatics/index.html)

## Notes

- This lesson is purely identification. *Why* each part exists and how to build a
  board comes next in [Pneumatics 2: Purpose & Construction](../pneumatics-construction/).

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — add labeled photos of your team's actual pneumatic parts bin so members study the exact components they'll handle.</p>
</div>
