---
layout: drive-lesson
title: The Driver Station
subtitle: Enable, comms, brownouts, and the screens you actually watch during a match.
permalink: /learning/drive-team/driver-station/
role: crew
order: 2
size: 2
time: "1–2 hrs"
---

## Description

The Driver Station (DS) is how the robot is enabled, how you see brownouts,
and how you know you still have comms. Drivers who only watch the field
miss the warning that precedes a dead robot. This ticket is the DS you
must be fluent in before you care about fancy HUDs.

You already named the seats in [Drive Team Roles](../drive-team-roles/).
The laptop is not a sixth seat. It is a tool the driver and operator
share, that the technician can restart, and that the coach does not
drive. Mentors still do not grab a controller — or the mouse — to "just
enable it" for you. If a student cannot set up the DS in the shop, they
cannot set it up on a field that is yelling at them.

On the field the
[Field Management System (FMS)](https://www.firstinspires.org/resources/library/frc/technical-resources)
owns enable. You plug Ethernet into the assigned driver station, the DS
shows **FMS Connected**, and you wait. Mashing enable early does nothing
useful and tells the FTA you have not practiced. Off the field, *you*
own enable, disable, and e-stop. Know where all three live before anyone
puts the robot on the ground.

In a match you have time for three glances: the field, the clock (or the
coach's endgame cue), and the DS status pane — comms, battery, brownout,
sticky faults. Practice those glances with the robot on blocks. A
first-time DS user on the field is a risk.

This site does not track whether you finished the walk. If your team
exported these tickets, close this issue there once a mentor accepts the
criteria below.

## Prerequisites

- [Drive Team Roles](../drive-team-roles/) completed (you know who stands
  where and who does not touch the sticks).
- Access to a Driver Station laptop with the current
  [FRC Game Tools](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/first-driver-station.html)
  installed, and a practice robot or a robot on blocks. If the competition
  robot is down, a kitbot or last year's drive base is enough.
- Safety glasses. Battery connected only when a mentor or technician
  agrees the robot is safe to enable.

## What you'll learn

- The plug-in order, enable / disable / e-stop flow, and what **FMS
  Connected** changes.
- What comms loss and brownout look like on the DS, and what the driver
  does in each case.
- Which DS tabs matter in a match versus in the shop.
- How to set up the DS for a practice drive without a mentor touching
  the laptop.

## Tasks

1. **Read the official DS pages.** Read
   [FRC Driver Station Powered by NI LabVIEW](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html)
   through the Operation, Diagnostics, Setup, USB Devices, and CAN/Power
   tabs. Then skim
   [Driver Station (Operator Console) Best Practices](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station-best-practices.html)
   through "Before Each Match." Write five labels on a sticky note you
   will put on the laptop bezel (or a card you keep with the DS):

   - team number (Setup tab)
   - enable / disable
   - e-stop (Space on the DS; physical button on the field)
   - battery voltage
   - comms / "No Robot Communication"

   You are not decorating the laptop. You are building muscle memory for
   the three-glance habit.

2. **Walk a real Driver Station.** With a mentor watching and the robot
   on blocks or on a cart with wheels chocked:

   - Confirm the laptop is on the current Game Tools, team number is
     correct, and the DS application is in focus.
   - Plug joysticks into the USB ports you will use at the event. Open
     the USB Devices tab and confirm each stick appears in the slot you
     practiced with. Press F1 if a stick is missing.
   - Connect to the robot (tether or practice radio). Wait until the
     status string is not "No Robot Communication."
   - Point to battery voltage, the brownout / 12V fault counter on the
     CAN/Power tab, and the comms fault counter.
   - Point to **Enable**, **Disable**, and the e-stop path (Space bar in
     the shop; the field e-stop button in a station you have seen in a
     photo or at an event).
   - Enable in teleop. Disable. Do not enable autonomous on the ground
     unless the coach has cleared the space.

   A mentor does not click for you. If you get stuck, they talk; they do
   not grab the trackpad.

3. **Learn comms loss versus brownout.** Read
   [roboRIO Brownout and Understanding Current Draw](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-brownouts.html)
   through the brownout identification section. Then write two short
   scripts on the same card as Task 1:

   - **Comms drop:** the robot is a brick. Do not invent stick inputs.
     Say "comms" once to the coach. Hands still. The technician and FTA
     path starts. You do not reboot the DS during a live match unless
     the FTA tells you to.
   - **Brownout:** voltage sags, the voltage background goes red, the
     status string can read "Voltage Brownout," and the 12V fault
     counter climbs. Mechanisms die first. Back off current — usually
     drivetrain — instead of holding full stick into a stall.

   Battery choice is a drive-team decision as much as an electrical one.
   A tired battery is a strategy error. You will put voltage on the
   [pre-match card](../pre-match-checklist/) later.

4. **Watch FMS take the controls.** Watch
   [Einstein Final 1 — 2026 FIRST Championship](https://www.youtube.com/watch?v=EjF9we707DA)
   and look at the alliance stations, not the robots, for 30 seconds of
   teleop. Notice: Ethernet to the shelf, laptop open, people not
   mashing the keyboard after the match has started. Then read the
   [FMS Whitepaper](https://fms-manual.readthedocs.io/en/latest/fms-whitepaper/fms-whitepaper.html)
   introduction (the first two sections are enough) so you know why
   enable greys out on the field. Write one sentence: *On the field, FMS
   enables the robot; in the shop, I do.*

5. **Practice the three glances.** Enable the robot on blocks. Have a
   teammate call "field," "clock," "DS" at random for two minutes. Each
   time, look at that thing and say what you see (a landmark, a time or
   "no clock in the shop," voltage and comms). The coach-in-training
   stands where you can hear them. One voice. If you stare at the robot
   bumpers the whole time, you fail the glance drill even if the robot
   is fine.

6. **Set up a practice drive without help.** From a cold laptop — lid
   closed, sticks unplugged — set up the DS, connect, confirm USB order,
   and enable teleop. Time it. Write the time on the role map from
   [Drive Team Roles](../drive-team-roles/). If it is more than a few
   minutes, do it again until it is boring. Boring is the goal.

## Acceptance Criteria

- [ ] You can point to enable, disable, e-stop (Space and the field
      button), battery voltage, comms status, and the 12V / brownout
      counter on a real DS while a mentor watches.
- [ ] You set up the DS for a practice drive without a mentor touching
      the laptop.
- [ ] You can explain comms loss versus brownout in two sentences and
      say what the *driver* does in each case (not what software should
      do).
- [ ] You can state what **FMS Connected** means: the field owns enable;
      you wait.
- [ ] The three-glance habit (field, clock, DS) has been practiced with
      the robot enabled on blocks.

## Resources

- [WPILib: FRC Driver Station](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html)
- [WPILib: Driver Station index](https://docs.wpilib.org/en/stable/docs/software/driverstation/index.html)
- [WPILib: Operator Console Best Practices](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station-best-practices.html)
- [WPILib: Installing the FIRST Driver Station](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/first-driver-station.html)
- [WPILib: roboRIO Brownouts](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-brownouts.html)
- [WPILib: Driver Station Log Viewer](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station-log-viewer.html)
- [FIRST Technical Resources — FMS Whitepaper](https://www.firstinspires.org/resources/library/frc/technical-resources)
- [FMS Whitepaper](https://fms-manual.readthedocs.io/en/latest/fms-whitepaper/fms-whitepaper.html)
- [Electrical: Power Distribution](../../electrical/power-distribution/)
- [Electrical: Status Lights & Fault Codes](../../electrical/status-lights-fault-codes/)
- [Match Flow & Field Rules](../match-flow-rules/) — next ticket

## Notes

- Space bar is e-stop in the DS. It is not a joke and it is not "disable
  but faster." After an e-stop the robot stays down until the DS is
  reset the way the docs describe. On the field, the physical e-stop and
  A-stop buttons are part of the station; A-stop disables for the rest
  of auto only.
- Dedicate a laptop to driving if you can. The best-practices page is
  blunt: no programming, no hotel gaming, no random USB devices. A
  hinged Ethernet port will fail you in queue. Use a port saver.
- Do not deploy code while connected to FMS. The
  [Game Manual, section 5.12](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
  says so.
- The next ticket ([Match Flow & Field Rules](../match-flow-rules/)) is
  the clock and the rules that make a legal enable matter.
