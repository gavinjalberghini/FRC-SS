---
layout: electrical-lesson
title: Status Lights & Fault Codes
subtitle: Read the roboRIO, PDH, motor controller, and pneumatics status LEDs to pinpoint faults fast.
permalink: /learning/electrical/status-lights-fault-codes/
role: lead
order: 10
size: 2
time: "1–2 hrs"
---

## Description

Every major device on the robot reports its state through LEDs. A Level
3 technician can glance at a robot and read those lights to narrow a
problem in seconds instead of swapping parts they are comfortable with.
This ticket is the dictionary. The next ticket,
[Systematic Troubleshooting](../troubleshooting/), is the method that
uses the dictionary. Do not skip this one and "just debug."

You already know where the devices live
([The FRC Control System](../control-system/)) and what the ports are
([roboRIO Ports](../roborio-ports/)). Today you learn what they say
when they are unhappy. The official charts win over memory and over
this page. Firmware revisions change colors. When a vendor page and
a printed pit card disagree, open the current vendor page.

A useful habit: **lights should match the story you believe.** If you
think the robot is disabled and connected, the RSL is solid, the
roboRIO Comm LED is green, and Mode is off. If any one of those
disagrees, believe the lights and fix the story. The RSL, from
[WPILib's status-light reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html):
solid ON = powered and disabled; blinking = enabled; off = robot off,
roboRIO unpowered, or RSL not wired.

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a
mentor accepts the criteria below.

## Prerequisites

- [The FRC Control System](../control-system/) and
  [roboRIO Ports & Communication Protocols](../roborio-ports/)
  completed.
- A powered robot or spare board a mentor will let you read (on
  blocks, battery connected only for the LED walk). Keep
  [Electrical Safety](../electrical-safety/) habits.

## What you'll learn

- What each roboRIO LED means, from the current WPILib chart — not
  from last year's pit lore.
- How to look up PDH, SPARK MAX, Talon FX, and PH/PCM LED codes
  instead of guessing.
- The habit of confirming "lights should match" before you pull a
  connector.

## Tasks

1. **Print or pin the official chart.** Open
   [WPILib: Status Light Quick Reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html)
   and keep it open for the whole ticket. Skim the
   [NI roboRIO user manual](https://www.ni.com/docs/en-US/bundle/roborio-frc-2/page/manual.html)
   LED section if you want photographs. You will still be asked to
   recall the roboRIO table without the page.

2. **roboRIO LEDs, from the current chart.** Stand at a roboRIO and
   map each lamp. The rows below match WPILib's latest table — if
   the page has changed, the page wins.

   - **Power** — Green = power is good. Amber = brownout protection
     tripped, outputs disabled. Red = power fault; check user rails
     for a short. Off or an unexpected color means voltage is not
     where the controller wants it.
   - **Status** — On while booting, then should go off. 2 blinks =
     software error, reimage. 3 blinks = safe mode (restart; reimage
     if it stays). 4 blinks = software crashed twice without a
     reboot (reboot; reimage if it stays). Constant flash or solid
     on = unrecoverable; that is an NI conversation, not a "swap
     the radio" conversation.
   - **Comm** — Off = no communication with the driver station.
     Solid red = DS communication, **no user code** running.
     Blinking red = E-stop. Solid green = good DS communications.
   - **Mode** — Off = outputs disabled (disabled, brownout, etc.).
     **Orange** = autonomous enabled. **Green** = teleop enabled.
     **Red** = test enabled. (If you learned "green means auto" in
     an older shop, unlearn it. The chart is orange / green / red.)
   - **RSL** — mirrors the Robot Signal Light: solid = disabled,
     blinking = enabled, off = unpowered or unwired.

   Cover the page and say all five to a partner. Uncover. Repeat
   the ones you missed.

3. **PDH / PDP.** Open
   [REV: PDH status LED patterns](https://docs.revrobotics.com/ion-control/pdh/status-led)
   (firmware 21.1.7+) and the PDH/PDP tables on the WPILib chart.

   - PDH **status**: solid green = communicating with the roboRIO;
     solid blue = powered, no main comm; orange/blue blink = low
     battery; orange/yellow = CAN fault. Learn those four plus
     "look up the rest."
   - PDH **channel** LED: off = channel has voltage and is fine;
     solid red = no voltage, active fault (tripped or missing
     breaker); blink red = sticky fault.
   - Older **PDP**: green = no fault (strobe vs. slow tells
     enabled vs. disabled); orange = sticky fault; red = no CAN.
     Special states (red/orange damaged, green/orange bootloader,
     no LED = no power or reversed polarity) are on the WPILib
     page. On the PDP, the two trouble lights "should always
     match except in bootloader mode."

4. **Motor controllers your team actually runs.** Open the chart
   for each:

   - [REV SPARK MAX status LEDs](https://docs.revrobotics.com/brushless/spark-max/status-led)
     — idle color is motor type + brake/coast (you used this in
     [Motors](../motors-controllers/)); green/red while driving;
     orange-plus-another-color slow blinks are faults (12 V
     missing, CAN, gate driver).
   - [CTRE Talon FX status lights](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/talonfx/index.html)
     — off = no power; alternating red = no valid CAN/PWM;
     simultaneous orange blink = valid CAN, disabled; solid
     orange = enabled, neutral; green/red blink rate = duty
     cycle.

   Write a five-line "pit card" for *your* controllers only. You
   do not memorize a Victor you do not own.

5. **Pneumatics module.** Open
   [REV: PH status LEDs](https://docs.revrobotics.com/ion-control/ph/status-led)
   (or the PCM table on the WPILib chart). Status colors follow
   the same family as the PDH (green = comm, blue = no comm,
   orange mixes = faults). Compressor LED green = compressor on.
   Solenoid channel LED green = that channel is on. A shorted
   coil looks different from a healthy idle — that is the point
   of looking before you replace the compressor.

6. **Read a live robot.** With a mentor, power a robot on blocks
   (announce first). Walk Power, Status, Comm, Mode, RSL, PDH,
   one motor controller, and the PH/PCM. For each, say the color
   and what it means *right now*. Then have the mentor describe
   two hypotheticals you must answer without the robot: a
   **brownout** (Power amber, outputs dead, Mode off) and **no
   user code** (Comm solid red, DS connected). Those two answers
   feed the fault tree in the next ticket.

7. **Hand in the pit card.** A mentor covers the WPILib page and
   asks the roboRIO table plus one controller and the PH/PDH.
   If your team exported these tickets, attach the pit card and
   move the issue to In Review.

## Acceptance Criteria

- [ ] You interpreted every roboRIO LED (Power, Status, Comm, Mode,
      RSL) from memory using the current WPILib meanings, including
      orange = autonomous and solid-red Comm = no user code.
- [ ] You looked up and explained the fault codes for the motor
      controllers this team actually runs (SPARK MAX and/or Talon
      FX), with the vendor page open, then closed.
- [ ] You explained the PH or PCM status, compressor, and solenoid
      LEDs.
- [ ] Given a robot (or a verbal prompt) showing brownout or "no
      code," you stated what the lights mean and what you would
      check next — without swapping a random part.
- [ ] A one-page pit card exists for this team's devices.

## Resources

- [WPILib: Status Light Quick Reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html)
- [NI roboRIO User Manual](https://www.ni.com/docs/en-US/bundle/roborio-frc-2/page/manual.html)
- [REV PDH status LEDs](https://docs.revrobotics.com/ion-control/pdh/status-led)
- [REV SPARK MAX status LEDs](https://docs.revrobotics.com/brushless/spark-max/status-led)
- [REV PH status LEDs](https://docs.revrobotics.com/ion-control/ph/status-led)
- [CTRE Talon FX hardware / LED reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/talonfx/index.html)
- [CTRE Phoenix 6 hardware reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
- [WPILib: Driver Station](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html)

## Notes

- Status-blink lore drifts. "2 blinks means failed upgrade" may
  have been true on a roboRIO you owned in 2018. The current
  WPILib line is "software error, reimage." Trust the page you
  opened today.
- The next ticket,
  [Systematic Troubleshooting & Team Protocols](../troubleshooting/),
  is a 5-step hunt plus a verbal protocol. You will write a
  fault tree for "robot won't enable" using these lights. Bring
  the pit card.
