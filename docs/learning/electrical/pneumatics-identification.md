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

## Description

Pneumatics use compressed air to move mechanisms. Air is just another way
to store and spend energy — same idea as the battery, different physics.
Pressure in a tank is stored work. A cylinder turns that pressure into
force (`force = pressure × area`). A leak spends the store for nothing. A
relief valve is the pneumatic cousin of a breaker: it opens so the tank
does not become a projectile.

Before you can build or troubleshoot a pneumatic system, you have to know
the parts on sight. This ticket is identification only. You will hold (or
be shown) every base component, name it, and call out the **physical
differences** between parts that look similar — single vs. double
solenoids, analog vs. digital pressure switches. You will find the
pressure vent plug on a real robot or practice board and, with a mentor,
vent the system as you already did in
[Electrical Safety](../electrical-safety/). You will not build a board,
fire a cylinder, or do the force math. Those are
[Pneumatics 2](../pneumatics-construction/) and
[Pneumatics 3](../pneumatics-troubleshooting/).

The **current game manual wins** on every pressure number. Recent manuals
(section 8.8 / R8xx) cap stored pressure at **120 PSI** and require a
primary relieving regulator that drops working pressure (commonly to
**60 PSI**). The FIRST pneumatics manual is a teaching document and says
so on page one: it does **not** supersede the game manual. If a vendor
page, a 2017 PDF, this ticket, and the manual disagree, the **manual
wins**.

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a mentor
accepts the criteria below.

## Prerequisites

- [Electrical Safety](../electrical-safety/) completed (you already
  vented a system once as part of safe state).
- [The FRC Control System](../control-system/) completed so you can
  find the pneumatics module on the board.
- A parts tray, spare pneumatics board, or a robot you can walk around.
  Photos are a backup, not the assignment.

## What you'll learn

- The name and appearance of every base pneumatic component.
- How to tell visually similar parts apart (single vs. double solenoids,
  analog vs. digital pressure switches).
- Where stored pressure lives (high side) versus where work happens
  (regulated side), and why the vent plug is part of safe state.

## Tasks

1. **Read the official picture, then the rules.** Skim
   [FIRST Robotics Competition Pneumatics Manual](https://www.firstinspires.org/hubfs/web/program/frc/resources/pneumatics-manual.pdf)
   through the high-pressure vs. working-pressure diagram. Then open the
   current
   [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
   Pneumatic System section
   ([2026 PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf),
   section 8.8). Write the stored-pressure cap, the working-pressure
   idea, and the sentence "the game manual wins" on a scratch note. Peek
   at
   [WPILib: Pneumatics APIs](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/pneumatics/index.html)
   only far enough to see that PCM and PH are both legal "little brains."

2. **Name every base component by sight.** With a mentor or a labeled
   tray, identify each of the following on a real part or a robot.
   Say the name, then one sentence about what it *looks like* (count
   ports, coils, gauges — do not recite a catalog):

   - **Pneumatics Control Module / Pneumatic Hub (PCM/PH)** — the
     module that runs compressor safety and solenoids, on CAN,
     independently enough that a dead user-code process should not
     leave you with an unregulated compressor.
   - **Compressor** — a motor-driven piston that pulls in air and
     pushes it out above atmospheric pressure.
   - **Accumulator (air tank)** — a reservoir. More tanks means the
     compressor cycles on and off less often.
   - **Air pressure switch** — senses high-side pressure and signals
     when the system is at its limit (FRC stored max = **120 PSI**,
     unless the current manual says otherwise).
   - **Safety relief valve** — a mechanical valve that vents if
     pressure exceeds its rating; mounted as close to the compressor
     output as possible.
   - **Gauge** — shows PSI in that part of the system. A legal system
     has more than one (high side and working side).
   - **Regulator** — lowers pressure between two segments (typically
     down to ~60 PSI on the working side).
   - **Pressure vent plug** — the manual dump. This is how you make
     the system safe to work on.
   - **Flow control** — restricts airflow to slow a cylinder in one
     direction.
   - **Solenoids (single and double)** — electrically operated valves
     that direct air. See Task 3.
   - **Cylinder (piston)** — uses air to push a rod in and out.
     Described by **bore** (body diameter) and **stroke** (how far
     the rod travels).
   - **Tubing** — ¼ inch outside-diameter air line in typical FRC
     kits.
   - **Press-fit / push-to-connect fittings** — join tubing to
     components.

3. **Tell similar parts apart.** Do this with hardware in your hands,
   not from memory of a slide:

   - **Single vs. double solenoid.** A *single* solenoid has one coil
     and springs back when de-energized. A *double* solenoid has two
     coils and stays in its last position. Count the coils and
     electrical connectors.
   - **Analog vs. digital pressure switch / sensor.** The analog
     version can report the actual pressure (a voltage you can plot).
     The digital (binary) switch only reports whether the high side
     is at the cutoff. The PH has ports for both — see
     [REV: Pneumatic Hub overview](https://docs.revrobotics.com/ion-control/ph/overview).

4. **Find and use the vent plug.** On a robot or practice board that
   may still have residual pressure, locate the pressure vent plug
   *before* you touch fittings. With a mentor, open it and wait until
   the gauges read zero. This is the same safe-state step you already
   owe every time you work on the robot. You are not cutting tubing
   or firing solenoids today.

5. **Pass the identification check.** Have a mentor or lead hold up
   (or point at) parts in a different order than Task 2. You name
   them. Misses go back on the tray and you try again — this is a
   sight test, not a vocabulary quiz. If your team has a written
   Pneumatics Level 1 check, this ticket *is* that check.

6. **Hand it in.** If your team exported these tickets, note who
   watched the identification check and move the issue to In Review.
   This website will not store the sign-off.

## Acceptance Criteria

- [ ] You named every component in Task 2 when shown a real part or
      a robot (not only a diagram).
- [ ] You distinguished a single solenoid from a double solenoid by
      counting coils, and you distinguished an analog pressure sensor
      from a digital pressure switch.
- [ ] You found the pressure vent plug and, with a mentor, vented the
      system to zero before anyone handled fittings.
- [ ] You stated the stored-pressure cap and the working-pressure idea
      from the current game manual, and you said the manual wins over
      the pneumatics teaching PDF.
- [ ] A mentor signed the team's Pneumatics Level 1 identification
      check, or the equivalent verbal check if the team has no sheet.

## Resources

- [FIRST Robotics Competition Pneumatics Manual](https://www.firstinspires.org/hubfs/web/program/frc/resources/pneumatics-manual.pdf)
  — teaching document; does not supersede the game manual
- [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [2026 Game Manual PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
  — section 8.8 Pneumatic System
- [REV Pneumatic Hub overview](https://docs.revrobotics.com/ion-control/ph/overview)
- [WPILib: Pneumatics](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/pneumatics/index.html)
- [WPILib: Wiring Pneumatics — REV PH](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-pneumatics-ph.html)
  — pictures only; you wire this in Pneumatics 2

## Notes

- This lesson is purely identification. *Why* each part exists in the
  air path, how to square-cut tubing, and how to wire the PH/PCM are
  [Pneumatics 2: Purpose & Construction](../pneumatics-construction/).
- Force, volume, and recharge math wait for
  [Pneumatics 3](../pneumatics-troubleshooting/). Do not size a
  cylinder from a vibe.
- The next ticket, [Wiring Craftsmanship](../wiring-craftsmanship/),
  leaves air and goes back to copper: gauge, strip, crimp, ferrule,
  label, strain-relief. You will use those habits on the pneumatics
  module when you build the board.
