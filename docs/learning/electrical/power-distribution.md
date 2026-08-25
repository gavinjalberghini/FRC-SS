---
layout: electrical-lesson
title: Power Distribution
subtitle: The battery, main breaker, and Power Distribution Hub — how power flows and how channels are protected.
permalink: /learning/electrical/power-distribution/
role: technician
order: 3
size: 2
time: "1 hr"
---

## Description

The Power Distribution Hub (PDH) — or the older Power Distribution Panel
(PDP) — is the heart of the robot's power system. It takes one big input
from the battery and splits it into many protected outputs. This ticket
is the close-up of the device you pointed at in
[The FRC Control System](../control-system/). You will read the silkscreen,
pick a legal breaker for a given wire, and find the CAN terminals and
termination switch. You will not energize a half-wired channel "just to
see." The battery stays off the robot until a mentor says the demo is
safe.

Power on an FRC robot is a tree, not a suggestion:

1. The battery connects through an **Anderson SB50** (or another SB-type
   housing the manual allows — pink/red SB50 is what you can borrow at
   an event).
2. The **positive** lead runs through the **120 A main breaker**, then
   to the PDH's main positive input. The **negative** lead runs straight
   to the PDH's main negative input. Heavy current uses thick copper —
   typically **6 AWG**. The game manual (R609 in 2026) names the devices
   that must sit on that 6 AWG run and the legal 120 A breaker part
   numbers. The manual wins.
3. From there the hub fans out. **High-current channels** accept
   replaceable 40 A (or 30 A) ATO breakers and feed motor controllers.
   The white graphics on a PDH show which breaker pairs with which
   terminal pair. **Low-current / fused channels** accept small ATM/APM
   fuses or breakers (the roboRIO is a 10 A, **non-switchable** channel —
   again, the manual) and feed the roboRIO, radio, and similar
   electronics. Some channels are always on; the switchable one is for
   things like LEDs that you actually want to turn off.

A breaker is sized to trip *before* the wire downstream of it overheats.
That is the same physics as [Electrical Safety](../electrical-safety/):
the breaker is the fuse for the copper, not a suggestion of how much
current you wish you had. Upsizing a 40 A breaker on 18 AWG "because the
motor tripped" is how insulation cooks. Match breaker, wire, and device,
then check the current game manual. If this ticket, a vendor page, and
the manual disagree, the **manual wins**.

The PDH also sits on the CAN bus. It has CAN terminals and a termination
switch. A healthy bus is a single daisy-chain with 120 Ω at each end —
usually the roboRIO at one end and the PDH (jumper ON) at the other.
You will wire CAN for real in later tickets; today you find the switch
and say whether it should be on.

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a mentor
accepts the criteria below.

## Prerequisites

- [Electrical Safety](../electrical-safety/) completed.
- [The FRC Control System](../control-system/) completed (you can already
  point at the PDH and trace battery → breaker → hub).
- A PDH or PDP you can hold or stand over, plus the team's copy of the
  current game manual (or the PDF linked below).

## What you'll learn

- How the battery, Anderson connector, and main breaker connect to the
  PDH, including which lead goes through the breaker.
- The difference between high-current and fused / low-current channels,
  and which one the roboRIO is allowed to use.
- How to pick a breaker or fuse that matches the wire *and* the rules.
- Where the CAN terminals and termination switch live, and how to read
  the PDH's status LED at a glance.

## Tasks

1. **Read the hub, then the rules.** Open
   [REV: Power Distribution Hub overview](https://docs.revrobotics.com/ion-control/pdh/overview)
   (20 high-current 40 A channels, 3 low-current 15 A channels, 1
   switchable low-current channel). If the robot uses a PDP, use
   [WPILib's hardware overview](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html)
   for the older panel. Then open the current
   [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
   Power Distribution section
   ([2026 PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf),
   section 8.6). Write four rule numbers on a scratch note: main 6 AWG
   run, 120 A breaker, roboRIO 10 A non-switched feed, and "one
   breaker/fuse per circuit."

2. **Walk the battery-to-PDH run on the robot.** With the robot in the
   safe state, put a finger on: battery positive → SB50 → 120 A breaker
   → PDH main positive; battery negative → SB50 → PDH main negative.
   Confirm the main leads are 6 AWG copper (or larger) and that every
   lug and breaker terminal is insulated. Game manual R607 (2026) wants
   those terminals covered at all times. Say out loud why the breaker is
   only in the positive lead.

3. **Pick channels like an inspector.** Standing at the PDH, answer
   these three prompts to a mentor, then write the answers on the
   scratch note:

   - A SPARK MAX or Talon FX driving a drivetrain motor: which kind of
     channel, and which breaker (typically 40 A, never above what the
     wire and the manual allow)?
   - The roboRIO: which kind of channel, which fuse/breaker, and why it
     must be **non-switchable**?
   - The radio: fused low-current, sized per the current radio and
     manual — look it up, do not guess.

   Follow
   [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
   for the official channel pictures. If a vendor "getting started"
   page and the manual disagree, the manual wins.

4. **Find CAN and the terminator.** Point at the PDH CAN terminals
   (yellow = high, green = low). Find the termination switch or jumper.
   Read
   [WPILib: CAN Wiring Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/can-wiring-basics.html).
   Tell a mentor whether *this* robot's PDH should have termination ON
   (PDH at the end of the daisy-chain) or OFF (PDH in the middle, with
   a 120 Ω resistor at the real end). You do not rewire the bus today.

5. **Read the status LED once.** Open
   [REV: PDH status LED patterns](https://docs.revrobotics.com/ion-control/pdh/status-led)
   or the PDH table on
   [WPILib: Status Light Quick Reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html).
   Write three lines: solid green, solid blue, and orange/blue blink
   (low battery). You will memorize the full rainbow in
   [Status Lights & Fault Codes](../status-lights-fault-codes/). Today
   you only need to know that "green and communicating" is the healthy
   case, and that a red **channel** LED means that channel has no
   voltage (tripped or missing breaker).

6. **Hand the note to a mentor.** The scratch note plus a finger-point
   tour of inputs, one high-current channel, one fused channel, and the
   CAN terminator is the review. If your team exported these tickets,
   attach a photo of the labeled PDH (or the note) and move the issue
   to In Review.

## Acceptance Criteria

- [ ] You identified the PDH/PDP main positive and negative inputs and
      showed how the 120 A breaker sits only in the positive lead.
- [ ] You explained which channels you would use for a motor controller
      versus the roboRIO, including the 10 A non-switchable rule.
- [ ] You selected a legal breaker or fuse for a given wire and device
      and cited the game-manual rule that backs the choice. You said
      the manual wins.
- [ ] You located the CAN terminals and the termination switch, and you
      stated whether termination should be ON or OFF on this robot.
- [ ] You stated what a healthy PDH status LED looks like and what a
      red channel LED means.

## Resources

- [REV Power Distribution Hub overview](https://docs.revrobotics.com/ion-control/pdh/overview)
- [REV PDH status LED patterns](https://docs.revrobotics.com/ion-control/pdh/status-led)
- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
- [WPILib: CAN Wiring Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/can-wiring-basics.html)
- [WPILib: Hardware Component Overview](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html)
- [WPILib: Robot Battery Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/robot-battery.html)
- [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [2026 Game Manual PDF](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)

## Notes

- The main breaker is protection *and* the on/off switch. It still does
  not replace unplugging the Anderson when your hands are in the
  wiring.
- Channel numbers matter later when programmers read PDH current. Label
  them when you start building in
  [Wiring Craftsmanship](../wiring-craftsmanship/).
- The next ticket,
  [Pneumatics 1: Component Identification](../pneumatics-identification/),
  is the same skill on the air side: name every part by sight before
  you build a board. You do not pressurize anything there either.
