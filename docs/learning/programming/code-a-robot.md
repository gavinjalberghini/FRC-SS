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

## Description

This is the capstone of the veteran track and a qualification for
leadership: take a robot from an empty project to one that drives
under a stick and follows a one-meter autonomous path. It is
intentionally **not** a paste-from-chatbot tutorial. You are
expected to be resourceful — official docs, last year's repo, Tuner
X, and every ticket before this one. Mentors will answer specific
questions. They will not pair-program the entire drivetrain while
you watch.

You have Java, hardware, Tuner X, driver input, coordinates,
commands-as-functions, alliance color, config, and debugging. This
ticket is those skills on one chassis. The easy mistakes are all
schedule mistakes: generating swerve with guessed wheel radius;
skipping CANcoder zeroing; tuning steer PID on the carpet with
people around the frame; jumping to a six-note auto before the
robot can track a meter of straight line.

The next ticket, [Autonomous Paths](../autonomous/), goes deeper on
PathPlanner and Choreo. You still need **one** working path here,
on hardware, so that ticket is not theoretical. After autonomous,
the lead track starts at
[Researching Robot Code](../researching-robot-code/).

Work the Java in a repo you control (a fork, a personal robot
project, or a clearly named folder). Document the process in
`frc-learning` so a mentor can review the *engineering*, not just
watch a drive-by. This site does not store your video. The team's
exported issue should get the link.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/),
  [FRC Hardware & Firmware](../frc-hardware/), and
  [Phoenix Tuner X](../phoenix-tuner/) completed — you can blink
  devices and command a motor with voltage.
- [The Field Coordinate System](../coordinate-system/) and
  [Debugging & Performance](../debugging/) strongly recommended.
  You will get a sign wrong and you will get a stack trace.
- Access to a swerve robot (or last year's) you may deploy to,
  **with a mentor**, robot on blocks until the first drive check
  passes.
- Phoenix Tuner X, WPILib VS Code, FRC Game Tools, and a
  controller. PathPlanner installed from
  [pathplanner.dev](https://pathplanner.dev/home.html).

## What you'll learn

- The end-to-end loop: IDs and firmware → generated swerve →
  deploy → driver feel → PID → a one-meter path.
- How to use the CTRE Swerve Project Generator instead of
  hand-writing module geometry the first time.
- How to write down a PID tune so the next person can repeat it.

## Generating swerve code — order of operations

A reliable order when standing up a new swerve drivetrain. Do not
skip ahead to PathPlanner.

1. **Identify and ID every device.** With the robot safely on
   blocks, connect Phoenix Tuner X, blink each device to locate
   it, and assign IDs and names using the team convention (or the
   scheme in [Phoenix Tuner X](../phoenix-tuner/)). Update
   firmware as needed. Write the ID table *before* you generate
   code. Two modules sharing a steer ID will generate a project
   that compiles and steers like a haunted shopping cart.

2. **Measure the drivetrain.** Find the module manufacturer and
   type, then look up **wheel radius** and **gear ratio** from
   the module spec sheet — not from memory, not from another
   team's 2023 repo. Measure the distances between modules
   (center-to-center of the CANcoders, or the official
   dimension the generator asks for). Write the numbers in
   `robot/swerve-bringup.md` with units.

3. **Generate the project** in the
   [CTRE Swerve Project Generator](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/tuner-swerve/index.html)
   with the Driver Station open. Follow the on-screen steps
   carefully, especially wheel alignment when zeroing CANcoders.
   Watch
   [FRC: Using the CTRE Swerve Generator](https://www.youtube.com/watch?v=3QqltCdH_Qk)
   once before you click through, then do it on *this* robot.
   The generator is not a suggestion. It encodes invert,
   coupling, and encoder offsets that are miserable to invent.

4. **Add driver feel.** In the drive request, apply a small
   **deadband** and a smoothing curve so tiny stick movements
   do not cause jitter. A cubic curve is a common choice. The
   signs must match [the coordinate system](../coordinate-system/)
   — do not "fix invert" by cubing an already-wrong axis.

   ```java
   drivetrain.applyRequest(() ->
     drive.withVelocityX(
             Math.abs(joystick.getLeftY()) < 0.075
                 ? 0
                 : Math.pow(joystick.getLeftY(), 3) * MaxSpeed)
         .withVelocityY(
             Math.abs(joystick.getLeftX()) < 0.075
                 ? 0
                 : Math.pow(joystick.getLeftX(), 3) * MaxSpeed)
         .withRotationalRate(
             Math.abs(joystick.getRightX()) < 0.075
                 ? 0
                 : -Math.pow(joystick.getRightX(), 3) * MaxAngularRate)
   );
   ```

   Confirm each HID axis mapping against a forward push and a
   CCW twist before you call the cubics "done."

5. **Test and adjust.** Verify wheels drive **forward together**
   on a slight forward push (still on blocks — look at tread
   direction). Confirm rotation directions. Then, with a mentor
   and a clear floor, put the robot down and tune speeds,
   deadbands, and PIDs to the drive team's liking. If driving
   is inverted, flip the **one** affected axis and record it. If
   it jitters with no input, increase the deadband. If one
   corner steers opposite, it is almost always invert or
   encoder offset, not "the PID."

## Tuning a PID (drive or steer)

Read
[Introduction to PID](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-pid.html)
before you drag sliders. A usable shop procedure:

1. Start with the generator / vendor defaults. Plot the
   relevant sensor in Tuner X
   ([Plotting](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/plotting.html)).
2. Change **one** gain at a time. Write the old value down
   before you change it.
3. For a steer module: command a step heading and look for
   overshoot and settle time. Increase P until it responds,
   add D if it oscillates, use I only if a constant error
   remains and you understand windup.
4. Screenshot or export the plot for "before" and "after."
   Put both in `robot/pid/`.

If you cannot explain what P does in a sentence, you are not
tuning — you are gambling.

## A one-meter path

Install PathPlanner, read
[PathPlanner home](https://pathplanner.dev/home.html) and
[library getting started](https://pathplanner.dev/pplib-getting-started.html),
and look at CTRE's Phoenix 6 example that already wires
PathPlanner to generated swerve (the swerve-generator video
points at this). Build a path that is **one meter forward**,
nothing else. Deploy. Run it on a taped meter on the floor.

Tune path-following / odometry gains only after the robot
drives straight in teleop and the wheel radius is correct. A
robot that tracks 0.8 m when you asked for 1.0 m is usually
geometry or wheel radius, not "needs more P."

## Tasks

1. **Create the robot project.** Follow
   [Creating a robot program](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/creating-robot-program.html)
   only if the generator does not already emit a full project.
   Use last year's code and WPILib docs as references, not as
   something to copy blindly. The project must live in a Git
   repo you own or a clearly agreed team branch — not unreviewed
   commits on the competition `main` the night before a week 1
   event.

2. **Bring up hardware and generate swerve.** Complete steps 1–3
   in "Generating swerve code" above. Commit or attach the ID
   table and the measurements. Deploy
   ([Deploying robot code](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/deploying-robot-code.html)).
   On blocks, use Tuner X or teleop to confirm each module
   steers and drives.

3. **Add driver feel and pass the stick test.** Complete steps
   4–5. A driver (or you, with a mentor) must be able to
   translate field- or robot-relative, rotate, and stop without
   the robot twitching at rest. Write the deadband, the curve,
   and every invert you changed in `robot/swerve-bringup.md`.

4. **Tune one PID loop.** Drive or steer. Document the process
   in `robot/pid/README.md`: what you commanded, starting
   gains, ending gains, and before/after plots or a screen
   recording. Read the PID intro page first.

5. **Follow a one-meter path.** Create the PathPlanner path,
   integrate it, run it, measure how far the robot actually
   went. Tune until it is "reasonable" — a mentor defines
   that, but "left the tape entirely" is not it. Record a
   short video or a sequence of photos plus the measured
   error.

6. **Write the README.** In the robot repo (and a summary in
   `frc-learning/robot/README.md`): what you did, what was
   hard, what you would change next time, and links to the
   PID plots and the path file. Open a pull request. Ask a
   mentor to watch the meter path or the recording.

## Acceptance Criteria

- [ ] A Git repo contains the generated (and then modified)
      swerve project. A mentor can find the commit.
- [ ] An ID/name table and measured wheel radius, gear ratios,
      and module translations are written down with units.
- [ ] CANcoders were zeroed per the generator steps. You can
      say how you aligned the wheels.
- [ ] Teleop drive works on the floor: forward is forward,
      rotation direction is documented, deadband stops twitch.
- [ ] One PID (drive or steer) has before/after gains and a
      plot or recording in `robot/pid/`.
- [ ] A PathPlanner path of about one meter forward runs on
      the robot. Measured error is written down. A mentor
      accepted "reasonable."
- [ ] `robot/README.md` (or the project README) covers what
      you did, what was hard, and what you would change.
- [ ] A pull request was reviewed. You did not force-push over
      someone else's competition code to "finish the ticket."

## Resources

- [WPILib: Creating a robot program](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/creating-robot-program.html)
- [WPILib: Deploying robot code](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/deploying-robot-code.html)
- [CTRE Swerve Project Generator](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/tuner-swerve/index.html)
- [Phoenix Tuner X](https://v6.docs.ctr-electronics.com/en/stable/docs/tuner/index.html)
- [FRC: Using the CTRE Swerve Generator (YouTube)](https://www.youtube.com/watch?v=3QqltCdH_Qk)
- [CyberKnights: Phoenix Tuner X basics (YouTube)](https://www.youtube.com/watch?v=tyMGkEOPRbo)
- [WPILib: Introduction to PID](https://docs.wpilib.org/en/stable/docs/software/advanced-controls/introduction/introduction-to-pid.html)
- [WPILib: Coordinate System](https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html)
- [PathPlanner documentation](https://pathplanner.dev/home.html)
- [PathPlanner: library getting started](https://pathplanner.dev/pplib-getting-started.html)
- [CTRE Phoenix 6 examples](https://github.com/CrossTheRoadElec/Phoenix6-Examples)

## Notes

- Start before you feel ready and write down what you try. That
  habit is what leadership looks for in the next track.
- Ask specific questions when stuck. Show the ID table, the
  measurement, and the last plot — not "swerve is broken."
- Wheel radius wrong by 5% is a path that looks "almost" right
  forever. Measure.
- Alliance-colored field drive is still the
  [alliance color](../alliance-color/) ticket. Do not skip it
  because the generator defaulted to blue in the shop.
- Next: [Autonomous Paths](../autonomous/). You will build
  real autos with events and constraints. You need this
  meter-long proof first.
