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

## Description

In [Pneumatics 1](../pneumatics-identification/) you learned to *name*
the parts. Now you learn what each one *does* in the air path, how the
control module is wired, and how to assemble a board an inspector can
walk. This is the construction level: you cut tube square, land CAN and
solenoid voltage correctly, leak-check, and demonstrate a
double-solenoid plus double-acting cylinder cycle.

Air is stored work. The compressor does `P·ΔV` work on each stroke. The
tanks hold that energy. The regulator spends it at a lower, legal
working pressure. The solenoid aims it. The cylinder turns it into
force. The relief valve and the vent plug are how the system loses on
purpose instead of failing. The **current game manual** (section 8.8 /
R8xx) sets the stored-pressure cap (**120 PSI** in recent seasons),
the working-pressure regulator, legal parts, and the required gauges
and relief valve. The FIRST pneumatics manual is a teaching PDF. If
the two disagree, the **game manual wins**.

The robot — and the practice board — stay in the safe state whenever
you are cutting tube or landing wire: battery off, **vent plug open
until gauges read zero**, then work. You pressurize only with a mentor
watching, and you vent again before anyone breaks a fitting.

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a
mentor accepts the criteria below.

## Prerequisites

- [Pneumatics 1: Component Identification](../pneumatics-identification/)
  completed (you can name every part and tell solenoids and switches
  apart).
- [Wiring Craftsmanship](../wiring-craftsmanship/) completed (ferrules,
  tug tests, labels, strain relief).
- A practice pneumatics board or a robot the lead will let you build
  on, plus the current game manual.

## What you'll learn

- The purpose of each component in the air path, in order.
- How a solenoid is built, how 12 V vs. 24 V is selected, and how to
  actuate one by hand.
- How to wire a Pneumatic Hub or Pneumatics Control Module: CAN,
  power, compressor, pressure switch, solenoids.
- How to assemble, leak-check, and demo a complete, inspectable
  board.

## Tasks

1. **Read the air path, then the rules.** Read
   [FIRST Pneumatics Manual](https://www.firstinspires.org/hubfs/web/program/frc/resources/pneumatics-manual.pdf)
   through the high-pressure vs. working-pressure figures and the
   leak-test notes. Then read the current
   [game manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
   Pneumatic System section
   ([2026 PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf),
   section 8.8) for required parts and pressure numbers. Write the
   stored cap, the working-pressure idea, and "manual wins" on the
   build sheet you will keep next to the board.

2. **Walk the air path out loud.** On the parts tray or a drawing,
   put the components in this order and say what each one *does*
   (not just its name):

   1. **Compressor** pressurizes air (a piston with one-way valves).
   2. **Accumulator(s)** store it; more tanks = fewer compressor
      cycles and a longer recharge — you will quantify that in
      [Pneumatics 3](../pneumatics-troubleshooting/).
   3. **Air pressure switch / analog sensor** tells the module when
      the high side is at the legal limit (**120 PSI** stored max
      unless the current manual says otherwise) so the compressor
      stops.
   4. **Safety relief valve** vents if pressure ever exceeds its
      rating — mounted as close to the compressor output as
      possible.
   5. **Regulator** drops working pressure (commonly to ~60 PSI)
      for the actuator side.
   6. **Solenoid** directs air to a **cylinder**.
   7. **Flow controls** set cylinder speed; **gauges** show both
      sides; the **vent plug** purges the system for service.

3. **Take a solenoid apart with your eyes.** Most FRC solenoids
   have three pieces: the **wire and connector**, the **coil**
   (12 V *or* 24 V — read the coil, do not assume), and the
   **body**. Single solenoids spring back; double solenoids hold
   the last position. The control module switches the **negative**
   side; supply is common positive.

   **Manual actuation:** find the small button behind the coil and
   press it with a blunt tool to fire the valve without code. Some
   valves have a slotted screw you can twist to lock them open.
   Practice this on a **vented** board. It is how you later
   isolate "no air" from "no electrical."

4. **Read the official wiring page for your module.** One of:

   - [WPILib: Wiring Pneumatics — REV Pneumatic Hub](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-pneumatics-ph.html)
     and
     [REV: Wiring the Pneumatic Hub](https://docs.revrobotics.com/ion-control/ph/gs/wiring)
   - [WPILib: Wiring Pneumatics — CTRE PCM](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-pneumatics-pcm.html)

   Then land, on a vented board, with
   [craftsmanship](../wiring-craftsmanship/) habits:

   - **Power in** from a PDH low-current channel (REV recommends
     a 20 A breaker on a **non-switchable** side channel for a PH
     that drives a compressor — then check the game manual).
   - **CAN in/out**, yellow = high, green = low, 18–22 AWG. Either
     PH/PCM CAN connector can be in or out. The PH does **not**
     come with a terminator; it sits in the middle of the chain
     unless you add one.
   - **Compressor output** on the module's compressor terminals
     (18 AWG or larger if you extend).
   - **Pressure switch / analog sensor** on the matching port.
     Digital switch polarity usually does not matter; analog
     three-wire sensors do — see the REV wiring page.
   - **Solenoid outputs** as numbered pairs. Set the **12 V / 24 V
     switch or jumper** to match the coils **before** you apply
     power. All solenoids on one PH must be the same voltage.
   - The module runs compressor safety independently of user
     code. That is the point of the "little brain."

5. **Build the board like an inspector will see it.** Follow the
   **current game manual** for required components and ratings
   (high-side parts rated for the stored pressure, working-side
   parts rated for working pressure). Then:

   - Route hose so it does not pinch, kink, or rub a chain.
     Tight bends are orifices. Orifices are leaks you cannot
     hear.
   - Cut tube **square**. A diagonal cut is a leak at a
     press-fit. Push until the tube bottoms, then tug.
   - Label the regulator, both gauges (HIGH / WORKING), the vent
     plug, and the solenoid channels.
   - Leak-check: pressurize with a mentor watching, listen, then
     use soapy water on fittings. A bubble is a redo, not a
     "we'll tape it." Vent before you pull a fitting.

6. **Demonstrate.** For a mentor playing inspector: show the
   relief valve, vent plug, both gauges, legal stored/working
   numbers from the manual, the 12 V/24 V setting, and a working
   **double solenoid + double-acting cylinder** cycle (code or
   manual override). Then vent to zero before anyone leaves the
   board.

7. **Hand it in.** If your team exported these tickets, attach a
   labeled photo of the finished board and the name of the mentor
   who walked the inspection demo. Move the issue to In Review.
   This website will not store the photo.

## Acceptance Criteria

- [ ] You explained the purpose of each component in the air path,
      in order, without reading this page.
- [ ] You identified a solenoid's three parts and coil voltage, and
      you manually actuated it on a vented board.
- [ ] A PCM or PH is wired: CAN, power, compressor, pressure
      sensor/switch, and at least one solenoid at the matching
      12 V/24 V setting. Joints passed a tug test.
- [ ] A complete board with one double solenoid and one
      double-acting cylinder is assembled with square-cut tube,
      no audible leak after a soapy-water check, and labels an
      inspector can read.
- [ ] You demonstrated the board (relief, vent, gauges, cycle)
      and then vented it to zero. You stated the current manual's
      stored and working pressure limits and said the manual
      wins.

## Resources

- [FIRST Pneumatics Manual](https://www.firstinspires.org/hubfs/web/program/frc/resources/pneumatics-manual.pdf)
- [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [2026 Game Manual PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
- [WPILib: Wiring Pneumatics — REV PH](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-pneumatics-ph.html)
- [WPILib: Wiring Pneumatics — CTRE PCM](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-pneumatics-pcm.html)
- [WPILib: Pneumatics APIs](https://docs.wpilib.org/en/stable/docs/software/hardware-apis/pneumatics/index.html)
- [REV Pneumatic Hub overview](https://docs.revrobotics.com/ion-control/ph/overview)
- [REV: Wiring the Pneumatic Hub](https://docs.revrobotics.com/ion-control/ph/gs/wiring)
- [REV PH status LEDs](https://docs.revrobotics.com/ion-control/ph/status-led)

## Notes

- Always **vent** with the pressure vent plug before opening the
  system. "I think it's empty" is how fittings become projectiles.
- Performance math (cylinder force, stored volume, strokes per
  charge) is
  [Pneumatics 3: Calculations & Troubleshooting](../pneumatics-troubleshooting/).
  Build first; then you will have numbers to compare to reality.
- The next ticket, [roboRIO Ports](../roborio-ports/), is the
  serial-bus half of the control system: CAN termination, I2C,
  SPI, RS-232, MXP, and the two buttons on the roboRIO.
