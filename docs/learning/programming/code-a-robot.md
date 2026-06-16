---
layout: lesson
title: Code a Robot
subtitle: A full zero-to-robot build — swerve generation, PID tuning, and path following.
permalink: /learning/programming/code-a-robot/
role: veteran
order: 13
size: 3
time: "Multi-session"
---

## Overview

This is the capstone of the veteran track and a qualification for leadership: take
a robot from an empty project to one that drives and follows an autonomous path.
It is intentionally **not** a step-by-step tutorial. You're expected to be
resourceful — lean on official docs, existing robot codebases, and the earlier
lessons to fill in the gaps.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/), [FRC Hardware & Firmware](../frc-hardware/),
  and [Phoenix Tuner X](../phoenix-tuner/).
- Access to a swerve robot (or last year's robot) you can deploy to.

## What you'll learn

- The end-to-end robot deployment cycle.
- How to generate and tune a swerve drivetrain.
- How to tune a PID loop and follow a planned path.

## Steps & acceptance criteria

- [ ] **Zero to robot.** Create a robot project in WPILib (VS Code) in your own
      repository. Use existing robot codebases and the WPILib docs as references.
- [ ] **Generate swerve.** Use the [CTRE Swerve Project Generator](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/tuner-swerve/index.html)
      to produce a swerve configuration for the robot (see the device ID/naming
      convention in the [Phoenix Tuner X lesson](../phoenix-tuner/)).
- [ ] **Tune a PID loop.** Tune a drive or steer PID and document your process,
      including before/after values and graphs where possible.
- [ ] **Follow a path.** Create a [PathPlanner](https://pathplanner.dev/) path,
      integrate it into the robot code, run a 1-meter-forward test, and tune the
      odometry PIDs until the robot follows it with reasonable precision.
- [ ] **Document & submit.** Record a short demo (or screenshots + write-up) and
      put your code in a repository with a README covering what you did, what was
      hard, and what you'd change next time.

## Reference: generating swerve code

A reliable order of operations when standing up a new swerve drivetrain:

1. **Identify & ID every device.** With the robot safely on blocks, connect
   Phoenix Tuner X, blink each device to locate it, and assign IDs and names using
   a consistent convention. Update firmware as needed.
2. **Measure the drivetrain.** Find the module manufacturer/type, then look up
   the wheel radius and gear ratio from the module's spec sheet. Measure the
   distances between modules (center-to-center of the CANcoders).
3. **Generate the project** in the CTRE swerve tool with the Driver Station open,
   following the on-screen steps carefully (especially wheel alignment when
   zeroing the CANcoders).
4. **Add driver feel.** In the drive request, apply a small **deadband** and a
   smoothing curve so tiny stick movements don't cause jitter. A cubic curve is a
   common choice:

   ```java
   drivetrain.applyRequest(() ->
     drive.withVelocityX(Math.abs(joystick.getLeftY()) < 0.075 ? 0 : Math.pow(joystick.getLeftY(), 3) * MaxSpeed)
          .withVelocityY(Math.abs(joystick.getLeftX()) < 0.075 ? 0 : Math.pow(joystick.getLeftX(), 3) * MaxSpeed)
          .withRotationalRate(Math.abs(joystick.getRightX()) < 0.075 ? 0 : -Math.pow(joystick.getRightX(), 3) * MaxAngularRate)
   );
   ```

5. **Test & adjust.** Verify wheels drive forward together on a slight forward
   push, confirm rotation directions, then tune speeds, deadbands, and PIDs to
   the drive team's liking. If driving is inverted, flip the sign on the affected
   axis; if it's jittery with no input, increase the deadband.

## Resources

- [WPILib: Creating a robot program](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/creating-robot-program.html)
- [CTRE Swerve Project Generator](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/tuner-swerve/index.html)
- [WPILib: PID control](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-pid.html)
- [PathPlanner documentation](https://pathplanner.dev/home.html)

## Notes

- Start before you feel ready and document what you try — that habit is exactly
  what leadership looks for.
- Ask specific questions when stuck, but show what you've already attempted first.
