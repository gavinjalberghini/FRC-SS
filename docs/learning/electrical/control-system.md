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

## Description

Before you wire anything, you need a mental map of the whole control system:
what each device is, what it does, and how **power** and **signals** flow
between them. A technician who can only recite part numbers guesses. A
technician who can trace two flows — energy from the battery, commands from
the driver-station laptop — can point at the failing layer before they pick
up a tool.

This ticket is the identification half of Level 1 on the electronics side.
You will stand in front of a real robot or a spare control board, name every
core device, and photograph the board with labels. You will not crimp, fuse,
or enable anything yet. The robot stays in the safe state you demonstrated
in [Electrical Safety](../electrical-safety/).

Two flows matter:

- **Power** always starts at the 12 V battery, goes through the 120 A main
  breaker, lands on the Power Distribution Hub or Panel (PDH/PDP), and then
  splits onto protected channels. High-current channels feed motor
  controllers. Fused low-current channels feed the roboRIO, radio, and
  similar electronics. If a device is dead, you walk that path backwards:
  device → channel → breaker/fuse → PDH input → main breaker → battery.
- **Signal** starts at the driver-station laptop, goes over Wi-Fi (or a
  tether) to the radio, then Ethernet to the roboRIO. The roboRIO talks to
  motor controllers and the pneumatics module over the **CAN bus** (or,
  on older/simple setups, PWM). Sensors talk back to the roboRIO so code
  can react.

The Robot Signal Light (RSL) is the one light inspectors and FTA volunteers
look at from across the field. Per
[WPILib's status-light reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html):
solid ON means the robot is powered and disabled; blinking means it is
enabled; off means the robot is off, the roboRIO is unpowered, or the RSL
is not wired. You will read every other LED in
[Status Lights & Fault Codes](../status-lights-fault-codes/); today you
only need to find the RSL and say what those three states mean.

This site does not track whether you finished. If your team exported these
tickets into its own GitHub, close this issue there once a mentor accepts
the criteria below.

## Prerequisites

- [Electrical Safety](../electrical-safety/) completed (safe-state demo
  signed off).
- A real robot, last year's robot, or a spare control board with the core
  devices mounted. A photograph of someone else's robot is a last resort,
  not the assignment.

## What you'll learn

- The job of each core control-system device, by pointing at it.
- How power flows from the battery to an actuator.
- How commands flow from the driver station to a motor controller.
- The difference between a high-current PDH channel and a fused
  low-current channel.

## Tasks

1. **Read the official map.** Skim
   [WPILib: Hardware Component Overview](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html)
   and the first half of
   [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
   (stop before you are tempted to start wiring). You are collecting names
   and jobs, not building a board.

2. **Name every core device on a real robot.** With the robot in the safe
   state (battery unplugged, pressure vented, on blocks), point to and
   name each of the following. If your team uses the older PDP or PCM,
   say so — the job is the same even when the plastic is different.

   | Device | Job |
   | --- | --- |
   | **12 V battery** | The only legal source of electrical energy on the robot. Always live. |
   | **Main breaker (120 A)** | Master cutoff between battery and everything else; also the on/off switch. |
   | **PDH / PDP** | Splits battery power into protected channels. |
   | **roboRIO** | Runs team code and talks to every other device. |
   | **Radio (e.g. VH-109)** | Wireless link between the robot and the driver station. |
   | **Motor controllers** (SPARK MAX, Talon FX, …) | Take roboRIO commands and drive motors. |
   | **Robot Signal Light (RSL)** | Required light: solid = powered/disabled, blinking = enabled. |
   | **Pneumatics module (PH/PCM)** | Controls the compressor and solenoids (you will open this up in the pneumatics tickets). |

   Keep the scratch note from the safety ticket. Add one line per device:
   *name — job — where it lives on this robot*.

3. **Trace power out loud.** Starting at the battery, walk a mentor along
   the path to one motor: Anderson → 120 A breaker (positive only;
   negative runs straight to the PDH) → PDH main inputs → a high-current
   channel + branch breaker → motor-controller **power** input → motor
   leads. Then walk the fused path: PDH low-current channel → roboRIO
   (10 A, non-switchable — the game manual says so). Say which path would
   be dead if the main breaker were off, and which path would still be
   dead if only one 40 A branch breaker were tripped.

4. **Trace signal out loud.** Walk the other flow: driver-station laptop
   → radio → Ethernet → roboRIO → CAN (yellow = high, green = low) or PWM
   → the same motor controller. Point at the CAN daisy-chain if the robot
   has one. You do not need to terminate a bus yet; that is
   [Power Distribution](../power-distribution/) and
   [roboRIO Ports](../roborio-ports/). You need to know the chain exists.

5. **Photograph the board.** Take one well-lit photo of the control board
   (or the robot's electronics belly). On a printed copy or in a simple
   editor, label every device from Task 2. This labeled photo is the
   artifact a mentor reviews. If your team keeps student work in a
   personal `frc-learning` repo or a shared drive, put it there. This
   website will not store it.

6. **Read the RSL line.** Open
   [WPILib: Status Light Quick Reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html)
   and read only the RSL table. Tell a mentor the three RSL states
   without looking. You will come back to this page in ticket 10; do not
   memorize the PDH rainbow today.

## Acceptance Criteria

- [ ] On a real robot or spare board, you pointed to and named the
      battery, main breaker, PDH/PDP, roboRIO, radio, at least one motor
      controller, the RSL, and the pneumatics module (if the robot has
      one).
- [ ] You traced the power path from the battery to a motor and the fused
      path from the PDH to the roboRIO, and you explained the difference
      between a high-current channel and a fused channel.
- [ ] You traced the signal path from the driver station to a motor
      controller (radio → Ethernet → roboRIO → CAN or PWM).
- [ ] A labeled photo of the control board exists and a mentor can read
      every label without asking you which blob is which.
- [ ] You stated the three RSL states (solid / blinking / off) from
      memory.

## Resources

- [WPILib: Hardware Component Overview](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html)
- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
- [WPILib: Zero to Robot](https://docs.wpilib.org/en/stable/docs/zero-to-robot/introduction.html)
- [WPILib: Status Light Quick Reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html)
- [REV Power Distribution Hub overview](https://docs.revrobotics.com/ion-control/pdh/overview)
- [CTRE Phoenix 6 hardware reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
- [FRC Competition Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)

## Notes

- If a device has no power, you trace toward the PDH, then the breaker,
  then the battery. If a device has power but does not listen, you trace
  the signal path. Mixing those two hunts is how pits lose an hour.
- The pneumatics module is on this map so you can find it. You do not
  build or pressurize anything until
  [Pneumatics 2](../pneumatics-construction/), and you do not do the
  force math until
  [Pneumatics 3](../pneumatics-troubleshooting/).
- The next ticket ([Power Distribution](../power-distribution/)) is the
  close-up of the PDH: main inputs, channel types, breaker sizing, CAN
  terminals, and the termination switch.
