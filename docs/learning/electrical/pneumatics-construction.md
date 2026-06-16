---
layout: electrical-lesson
title: "Pneumatics 2: Purpose & Construction"
subtitle: What each pneumatic part does, how to wire the PCM/PH, and how to build and test a complete board.
permalink: /learning/electrical/pneumatics-construction/
role: veteran
order: 8
size: 3
time: "Multi-session"
---

## Overview

In Pneumatics 1 you learned to *name* the parts. Now you'll learn what each one
*does* and how they connect into a working system — then build a complete,
inspectable pneumatics board. This is the construction level: you assemble,
route hose, wire the control module, and demonstrate the board for an inspector.

## Prerequisites

- [Pneumatics 1: Component Identification](../pneumatics-identification/).
- [Wiring Craftsmanship](../wiring-craftsmanship/).

## What you'll learn

- The purpose of each component in the air path.
- How a solenoid is built and how to actuate it manually.
- How to wire the Pneumatics Control Module / Pneumatic Hub.
- How to assemble and test a complete board.

## Unit 1 — The air path

Air flows through the system in order:

1. **Compressor** pressurizes air (a piston with one-way valves).
2. **Accumulator(s)** store it; more tanks = fewer compressor cycles.
3. **Air pressure switch** turns the compressor off at the FRC max of **120 PSI**
   (high-pressure side).
4. **Safety relief valve** vents if pressure ever exceeds the rating — mounted as
   close to the compressor output as possible.
5. **Regulator** drops the working pressure (commonly to ~60 PSI) for the
   actuator side.
6. **Solenoid** directs air to a **cylinder**, which moves the mechanism.
7. **Flow controls** fine-tune cylinder speed; **gauges** show pressure; the
   **vent plug** purges the system for service.

## Unit 2 — Solenoids in depth

A solenoid is an electrically operated valve. Most FRC solenoids have three
parts:

1. **Wire & connector**
2. **Coil assembly** (12V *or* 24V)
3. **Solenoid body**

- **Single** solenoids spring back to one position; **double** solenoids hold
  their last commanded position.
- The control module switches the **negative** side; the supply is common
  positive.
- **Manual actuation:** find the small button behind the coil and press it with a
  blunt tool to fire the valve temporarily; some have a slotted screw you can
  twist to lock it open. This is invaluable for testing without code.

## Unit 3 — Wiring the control module (PCM/PH)

- **CAN in/out:** the module sits on the CAN bus; either CAN connector can be in
  or out — just match colors (yellow = high, green = low). Use 18–16 AWG.
- **Power in** comes from the PDH; the **compressor** output drives the
  compressor.
- **Solenoid outputs** are paired; set the **12V or 24V jumper/switch** to match
  your coils (one or the other — never assume).
- The module also reads the **pressure sensor(s)** and runs the compressor safety
  logic independently of the roboRIO.

## Unit 4 — Build & test

1. Assemble the board following the **current game manual** layout (electronics
   included).
2. Route hose neatly — avoid tight bends, pinches, and wraps that cause pressure
   loss.
3. Make press-fit connections with **square-cut** tube ends for airtight seals.
4. Leak-check, then demonstrate the board for an inspector: show the relief
   valve, vent plug, gauges, and a working double-solenoid + double-acting
   cylinder cycle.

## Steps & acceptance criteria

- [ ] Explain the purpose of each component in the air path.
- [ ] Manually actuate a solenoid and identify its 3 parts and voltage.
- [ ] Correctly wire a PCM/PH: CAN, power, compressor, pressure switch, and one
      solenoid at the right voltage.
- [ ] Build a complete, leak-free board with one double solenoid and one
      double-acting cylinder, and pass an inspection demo.

## Resources

- [FRC Pneumatics Manual (FIRST)](https://firstfrc.blob.core.windows.net/frc2017/pneumatics-manual.pdf)
- [REV Pneumatic Hub documentation](https://docs.revrobotics.com/ion-control/ph/overview)
- [WPILib: Pneumatics](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/pneumatics/index.html)

## Notes

- Always **vent the system** with the pressure vent plug before working on it.
- Performance math (cylinder force, recharge rate) is covered in
  [Pneumatics 3: Calculations & Troubleshooting](../pneumatics-troubleshooting/).

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — document your team's standard board layout, hose colors/routing rules, and the inspection checklist you use before competition.</p>
</div>
