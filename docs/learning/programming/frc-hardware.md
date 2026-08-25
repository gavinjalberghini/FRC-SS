---
layout: lesson
title: FRC Hardware & Firmware
subtitle: Get to know the robot's electronics and how to keep their firmware and tools up to date.
permalink: /learning/programming/frc-hardware/
role: programmer
order: 4
size: 2
time: "1–2 hrs"
---

## Description

Software runs on hardware, and FRC robots use a specific, small set of
electronics. The roboRIO runs your code. The radio carries packets between
that code and the Driver Station. Motor controllers, a power hub, sensors,
and maybe a vision coprocessor do the rest. If you cannot name those devices
and say what each one is for, every "code bug" you meet will take twice as
long — because many of them are wiring, firmware, or a stale image.

This ticket comes after [Java Fundamentals](../java-fundamentals/) on
purpose. You now know how a program starts. You do not yet know *where* it
starts on a robot. The easy mistake is to skip the hardware walk and jump
straight into VS Code. Then a Talon with last year's firmware, a radio that
was never programmed, or two devices sharing a CAN ID looks like a Java
problem, and you will debug the wrong layer for an hour.

You will read official docs, install the FRC Game Tools on a computer you
can use in the shop, and write a short hardware map into `frc-learning`.
Where the team has a robot or a test board, you will also help update
firmware — with a mentor, not by guessing at a "Format Target" button.

The next ticket, [Phoenix Tuner X](../phoenix-tuner/), is how you talk to
CTRE devices without deploying code. This ticket is the map of what those
devices *are*.

This site does not track whether you finished. Put the write-up in your
`frc-learning` repo and close the team's exported issue only after a mentor
walks the robot (or a labeled photo set) with you.

## Prerequisites

- [Git Fundamentals](../git/) so you have `frc-learning` to put notes in.
  Java Units 1–8 from [Java Fundamentals](../java-fundamentals/) are
  strongly recommended; you do not need every exercise finished.
- Access to the shop, a labeled photo of the team's robot, or last year's
  robot. A mentor should be present for any firmware or imaging step.
- A Windows computer for the
  [FRC Game Tools](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/frc-game-tools.html)
  (Driver Station and roboRIO Imaging Tool are Windows-only). macOS and
  Linux are fine for WPILib VS Code; they are not a substitute for Game
  Tools on imaging day.

## What you'll learn

- The job of each core control-system device, in the order power and
  signals actually flow.
- Where the official manual for each common vendor device lives, so you
  stop asking a senior for a PDF they bookmarked in 2022.
- How to install FRC Game Tools and what "update the firmware" actually
  means before you touch a robot.

## Tasks

1. **Learn the control system as a system.** Read WPILib's
   [Hardware Component Overview](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html)
   and
   [Introduction to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
   all the way through. Then read
   [Control System Software](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-software.html)
   so you know which laptop tools exist (Driver Station, Imaging Tool,
   WPILib VS Code, vendor utilities). In `frc-learning`, create
   `hardware/control-system.md` and write, in your own words, the power
   path (battery → main breaker → PDH → devices) and the signal path
   (Driver Station → radio → roboRIO → CAN/PWM → actuators). Ten sentences
   is enough if they are accurate.

2. **Read the brain and the radio.** Follow
   [Imaging your roboRIO](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/imaging-your-roborio.html)
   and
   [Programming your Radio](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/radio-programming.html)
   far enough that you can explain *when* you image a roboRIO (new season,
   corrupted image, new team number) versus when you only set a team
   number. You are not required to image a roboRIO alone. Add a short
   "roboRIO and radio" section to `hardware/control-system.md` that
   answers: what is an image, what is firmware, and why a USB-B cable
   shows up in every imaging guide.

3. **Read the devices your team actually uses.** Open each of these and
   skim until you can point at the physical object (or a photo) and name
   it:

   - [CTRE Phoenix hardware reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
     (Talon FX / Kraken, CANcoder, Pigeon, CANivore if you have one)
   - [REV Power Distribution Hub](https://docs.revrobotics.com/ion-control/pdh/overview)
   - [REV Mini Power Module](https://docs.revrobotics.com/ion-control/mpm/overview)
   - [REV Pneumatic Hub](https://docs.revrobotics.com/ion-control/ph/overview)
     (skip only if the team has no pneumatics — say so in the write-up)
   - [Limelight docs](https://docs.limelightvision.io/) and
     [PhotonVision docs](https://docs.photonvision.org/en/latest/)
     — you configure cameras in a later ticket; here you only need "this
     is a coprocessor on the robot network"

   Add a table or bullet list to `hardware/devices.md`: device name,
   vendor, what it does, and the URL you used. If the team uses SPARK MAX
   or SPARK Flex, add
   [REV SPARK MAX](https://docs.revrobotics.com/brushless/spark-max/overview)
   as well.

4. **Install the FRC development tools.** On a Windows machine you can
   bring to the shop, install
   [FRC Game Tools](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/frc-game-tools.html).
   Confirm the Driver Station and the roboRIO Imaging Tool launch. If you
   have not already, install
   [WPILib VS Code](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html)
   on the computer you write code on. Write the versions you installed
   (Game Tools year, WPILib year) into `hardware/tools.md`.

5. **Walk a real robot with a mentor.** With the robot disabled and on
   blocks or a cart, point to: battery, main breaker, PDH, roboRIO, radio,
   RSL, at least one motor controller, and at least one sensor or
   coprocessor. Say what happens if that device is unplugged. If the team
   is updating firmware this week, watch or help with **one** vendor
   update — CTRE through Tuner X in the next ticket, REV through the
   [REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client),
   roboRIO through the Imaging Tool. Do not format a roboRIO without a
   mentor.

6. **Commit the notes.** On a branch in `frc-learning`, commit
   `hardware/control-system.md`, `hardware/devices.md`, and
   `hardware/tools.md`. Open a pull request titled for this ticket and
   ask a mentor to review the write-up. If your team exported these
   tickets, paste the PR URL on the issue.

## Acceptance Criteria

- [ ] `hardware/control-system.md` in your `frc-learning` repo describes
      the power path and the signal path in your own words, and explains
      image versus firmware for the roboRIO.
- [ ] `hardware/devices.md` lists the team's real devices (or last year's)
      with vendor, role, and a documentation URL for each.
- [ ] FRC Game Tools is installed on a Windows computer you can use, and
      `hardware/tools.md` records the Game Tools and WPILib versions.
- [ ] On a robot or a labeled photo set, you pointed to battery, breaker,
      PDH, roboRIO, radio, RSL, a motor controller, and one sensor or
      coprocessor and said what each does. A mentor was present.
- [ ] You did not image or factory-reset a control-system device alone.
- [ ] A pull request with the hardware notes is open or was merged after
      review.

## Resources

- [WPILib: Zero to Robot](https://docs.wpilib.org/en/stable/docs/zero-to-robot/introduction.html)
- [WPILib: Hardware Component Overview](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-hardware.html)
- [WPILib: Control System Software](https://docs.wpilib.org/en/stable/docs/controls-overviews/control-system-software.html)
- [WPILib: Intro to FRC Robot Wiring](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-1/intro-to-frc-robot-wiring.html)
- [WPILib: Imaging your roboRIO](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/imaging-your-roborio.html)
- [WPILib: Programming your Radio](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-3/radio-programming.html)
- [WPILib: FRC Game Tools](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/frc-game-tools.html)
- [WPILib: VS Code setup](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html)
- [CTRE Phoenix v6 hardware reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
- [REV Power Distribution Hub](https://docs.revrobotics.com/ion-control/pdh/overview)
- [REV Mini Power Module](https://docs.revrobotics.com/ion-control/mpm/overview)
- [REV Pneumatic Hub](https://docs.revrobotics.com/ion-control/ph/overview)
- [REV Hardware Client](https://docs.revrobotics.com/rev-hardware-client)
- [REV SPARK MAX](https://docs.revrobotics.com/brushless/spark-max/overview)
- [Limelight documentation](https://docs.limelightvision.io/)
- [PhotonVision documentation](https://docs.photonvision.org/en/latest/)
- [FIRST Resource Library](https://www.firstinspires.org/resource-library)

## Notes

- Firmware mismatches are a common source of "device not found" or
  erratic motion. When something misbehaves, checking firmware versions
  is an early step, not a last resort.
- Configuring a device on the device (Tuner X, REV Hardware Client)
  rather than only in code keeps those settings consistent no matter
  which laptop deploys. That is the whole next ticket.
- CAN IDs must be unique on a bus. Two Talons set to ID 1 is not a Java
  compile error. It is a robot that lies to you.
- The roboRIO image is **not** the same as roboRIO firmware. The Imaging
  Tool's docs say this; believe them before you click Reformat.
- Next: [Phoenix Tuner X](../phoenix-tuner/). Bring the device list you
  just wrote.
