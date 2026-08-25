---
layout: lesson
title: Phoenix Tuner X
subtitle: Configure, test, and diagnose CTRE devices without writing code.
permalink: /learning/programming/phoenix-tuner/
role: programmer
order: 5
size: 2
time: "~1 hr"
---

## Description

Phoenix Tuner X is CTRE's companion app for updating, configuring, analyzing,
and directly controlling Phoenix devices — Talon FX / Kraken motor
controllers, CANcoders, Pigeon 2, CANivore. It lets you test hardware and
tune settings **without deploying robot code**. That is the fastest way to
answer "is it the wire, the ID, the invert, or the Java?"

You just finished [FRC Hardware & Firmware](../frc-hardware/), so you can
name the devices on the CAN bus. This ticket is how you *talk* to the CTRE
ones. The easy mistakes are all the same: driving a mechanism that is not
on blocks, blinking the wrong motor because two IDs collided, or changing
config on a laptop and assuming the robot kept it. Tuner X is a power tool.
Treat it like a drill, not like a website.

This is the last programmer-track ticket. After it, the veteran track starts
with [Kanban & Agile Practices](../kanban-agile/) — how the team tracks
work — and then [Reading Driver Input](../driver-input/). You do not need
Tuner X to write Java, but you will need it the first time a swerve module
refuses to steer. Learn the app on a calm afternoon, not on Thursday night
before an event.

Work still lives in `frc-learning` (notes, screenshots, the ID table). The
demonstration lives on a robot or test board with a mentor watching. This
site does not track either one.

## Prerequisites

- [FRC Hardware & Firmware](../frc-hardware/) — you know what the devices
  are and Game Tools / Driver Station can launch.
- Access to a robot or test bench with CTRE devices on the CAN bus, **and
  a mentor**. Mechanisms on blocks. No one standing in the sweep of an arm
  or a swerve module.
- Phoenix Tuner X installed from the store for your OS. Official install
  and platform notes are in
  [Phoenix Tuner X](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/index.html).

## What you'll learn

- How to connect Tuner X to a roboRIO (including a fresh image that has no
  robot program yet).
- How to identify a physical device by blinking it, and how to give it a
  unique ID and a name a human can read.
- How to command a motor with voltage and plot position and velocity so
  you can see "it moves" without writing a subsystem.

## A naming and ID convention (recommended)

Consistent device IDs and names make code and debugging far clearer. One
scheme that works well for swerve robots:

- IDs are **two-digit numbers**. The tens digit identifies the module, the
  ones digit identifies the device on that module:

  - Tens: front-left `1`, front-right `2`, back-left `3`, back-right `4`,
    non-module devices `0` or `5`.
  - Ones: drive motor `1`, angle/steer motor `2`, CANcoder `3`, other
    `4`–`9`.

- Names use `camelCase`, with the module first, then the function — e.g.
  `frontLeftDrive`, `frontLeftAngle`, `frontLeftCAN` (keep "CAN"
  capitalized).

If the team already has a convention, **use the team's**. Write it down
either way. [Code a Robot](../code-a-robot/) will ask you to generate
swerve against whatever IDs are on the hardware.

## Tasks

1. **Read the official Tuner X pages.** Read
   [Phoenix Tuner X](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/index.html),
   [Connecting Tuner](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/connecting.html),
   and at least skim
   [Controlling Devices](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/controlling-devices.html)
   and
   [Plotting](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/plotting.html).
   Watch
   [CyberKnights: Phoenix Tuner X basics](https://www.youtube.com/watch?v=tyMGkEOPRbo)
   (about 15 minutes) once through before you plug into a robot. Write five
   bullets in `hardware/tuner-x.md` in `frc-learning`: how you connect,
   what a temporary diagnostic server is, what Blink does, what Voltage
   control does, and what you must never do with an unconstrained mechanism.

2. **Connect.** Open the Driver Station, then Tuner X. Point Tuner at the
   robot (Driver Station preset, USB `172.22.11.2`, or team `10.TE.AM.2`).
   If the device list is empty on a freshly imaged roboRIO, use **Run
   Temporary Diagnostic Server** as the connecting guide describes — do
   not invent a new robot project just to see devices. Screenshot the
   device list into `hardware/tuner-x/` in the repo (blur nothing; IDs
   are not secrets).

3. **Blink until you are sure.** Pick one motor controller. Use Blink.
   Walk to the robot and confirm the LEDs you expected are the ones
   flashing. If they are not, stop and fix the ID map before you command
   anything. Repeat for a CANcoder or Pigeon if the robot has one. Add a
   row to an ID table in `hardware/tuner-x.md`: Tuner name, CAN ID,
   physical location ("front-left steer", "pigeon in bellypan").

4. **Drive one motor with voltage.** With that mechanism on blocks and a
   mentor present, enable as Tuner X's controlling-devices page requires,
   select **Voltage** (not a closed-loop mode you have not tuned), and
   move the motor a small amount in both directions. Then stop and
   disable. You are proving the wire, the invert, and the ID — not
   showing off speed.

5. **Plot position and velocity.** Open the plotter, add **position** and
   **velocity** for the motor you just moved, and command it again. Save
   or screenshot the plot into `hardware/tuner-x/`. In the markdown file,
   write two sentences: did position increase when you commanded positive
   voltage, and does that match the mechanical "forward" the team uses?
   If it does not, that is an invert you will need later — record it now.

6. **Optional, if the team is updating firmware.** Update **one** device
   (or one group of the same type) to the firmware Tuner recommends,
   following the in-app prompts and a mentor. Write the from/to versions
   in the notes. Do not batch-update the whole robot five minutes before
   driver practice.

7. **Commit and review.** Branch, commit `hardware/tuner-x.md` plus
   screenshots, open a pull request, and demonstrate Blink + a voltage
   move to a mentor on the real hardware.

## Acceptance Criteria

- [ ] `hardware/tuner-x.md` in `frc-learning` lists connect method, Blink,
      voltage control, plotting, and a safety note about unconstrained
      mechanisms.
- [ ] A screenshot of the Tuner X device list is in the repo.
- [ ] You blinked a device and a mentor agreed you were looking at the
      correct physical unit.
- [ ] You commanded one motor with a voltage output, both directions,
      mechanism on blocks, mentor present.
- [ ] A position/velocity plot (screenshot) is in the repo, with two
      sentences on whether positive voltage matched mechanical forward.
- [ ] An ID/name table for the devices you touched is written down. It
      matches the team convention or the swerve scheme above.
- [ ] A pull request with the notes is open or was merged after review.

## Resources

- [Phoenix Tuner X documentation](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/index.html)
- [Connecting Tuner](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/connecting.html)
- [Controlling Devices](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/controlling-devices.html)
- [Plotting](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/plotting.html)
- [CTRE Phoenix 6 documentation](https://v6.docs.ctr-electronics.com/en/stable/index.html)
- [CTRE hardware reference](https://v6.docs.ctr-electronics.com/en/stable/docs/hardware-reference/index.html)
- [CyberKnights: Phoenix Tuner X basics (YouTube)](https://www.youtube.com/watch?v=tyMGkEOPRbo)
- [FRC: Using the CTRE Swerve Generator (YouTube)](https://www.youtube.com/watch?v=3QqltCdH_Qk)
  — preview of the generator you will use in
  [Code a Robot](../code-a-robot/); you do not run it yet

## Notes

- Configuring settings in Tuner X (rather than only in code) makes them
  consistent across every computer that deploys to the robot. Persist
  configs you mean to keep; a laptop is not the source of truth if you
  never wrote them to the device.
- Tuner X is a *speed* tool. It shortens the test loop so you are not
  redeploying code to check a wire or a direction. It is not a substitute
  for robot code at a match.
- Temporary diagnostic server is for empty roboRIOs. If the team already
  has a robot program, connect normally and do not "fix" a working
  diagnostics install.
- Never enable a drivetrain on the floor "just to see the plot." Blocks
  or a cart with wheels off the ground.
- Programmer track ends here. Veteran track starts at
  [Kanban & Agile Practices](../kanban-agile/).
