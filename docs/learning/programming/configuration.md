---
layout: lesson
title: "Tunable Config: Units, Preferences & Deploy Files"
subtitle: Type-safe units, dashboard-tunable Preferences, and files in the deploy directory.
permalink: /learning/programming/configuration/
role: veteran
order: 11
size: 2
time: "1 hr"
---

## Description

Robot code is full of numbers: wheel diameters, PID gains, setpoints,
path files. Three WPILib tools keep those numbers from turning into
3 a.m. mysteries. The **Units library** tags a value with a dimension
so you cannot add inches to seconds by accident. **Preferences**
store a tunable on the roboRIO so you can change it from a dashboard
without redeploying. The **deploy directory** ships files (JSON,
PathPlanner paths, vision configs) next to the code so simulation
and the robot use the same path helper.

You just learned that alliance color is a bad thing to cache in
[Match State & Alliance Color](../alliance-color/). This ticket is
the opposite instinct: measurements and config *should* be explicit,
named, and loaded from one place. The next ticket,
[Debugging & Performance](../debugging/), will warn you that
`Distance` objects created every loop become garbage-collection
stalls. Read both before you sprinkle `Inches.of` inside
`periodic`.

The easy mistakes: mixing `3` (inches?) with `3` (meters?) in a
swerve constructor; typoing a Preference key so the dashboard
edits a *new* empty key while code reads the old one; putting a
path file on the desktop and wondering why the roboRIO cannot see
it; using `new File("src/main/deploy/...")` which works on a
laptop and fails on the robot.

You will compute a wheel circumference with Units, change a
Preference from the dashboard in simulation, and read a deploy
file back. Artifacts go in `frc-learning`. This site does not
store the JSON you deploy.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/) through classes.
- A command-based example or the sim project from
  [Reading Driver Input](../driver-input/).
- [Match State & Alliance Color](../alliance-color/) so you do not
  "configure" alliance as a Preference (do not).

## What you'll learn

- How to write a measurement once in inches and convert it
  explicitly to meters at the API boundary.
- How to init and read a Preference, and why the key is a
  constant.
- Where `src/main/deploy/` goes on the roboRIO and how
  `Filesystem.getDeployDirectory()` keeps sim and robot aligned.

## The Units library

The Units library tags a value with its dimension so the compiler
catches mistakes. You cannot add a distance to a time. Conversions
are explicit:

```java
import static edu.wpi.first.units.Units.*;

Distance wheelDiameter = Inches.of(3);
Distance perRotation   = wheelDiameter.times(Math.PI);
double meters          = perRotation.in(Meters);
```

Arithmetic on measures creates **new objects**. For constants
computed once, that is fine. For values recomputed every loop,
prefer `MutableMeasure` (see
[Java Garbage Collection](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-gc.html)
and the next ticket) so you are not allocating a pile of
`Distance` objects at 50 Hz.

Official page:
[The Java Units Library](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-units.html).

Prefer Units at the edges of your code (configuration, dashboard
labels, comments you would have written as "inches"). Convert to
bare doubles only when an API will not take a `Measure`.

## Robot Preferences

`Preferences` stores values in the roboRIO's flash so you can tune
them live from SmartDashboard or Shuffleboard without rebuilding.
Initialize defaults once, then read them when you mean to pick up
a change:

```java
public static final String kArmPKey = "ArmP";
public static final double kDefaultArmKp = 50.0;

// Initialize the key with a default if it does not exist yet
Preferences.initDouble(kArmPKey, kDefaultArmKp);

// Read it later (second argument is the fallback if missing)
double armKp = Preferences.getDouble(kArmPKey, kDefaultArmKp);
```

Keep keys in named constants. A typo silently creates a second,
empty preference, and you will tune the wrong number for an hour.

Official page:
[Setting Robot Preferences](https://docs.wpilib.org/en/stable/docs/software/basic-programming/robot-preferences.html).

Preferences survive deploys. That is the point. It is also how a
stale gain from last week comes back to haunt you. If a value
must match the committed code, it is a constant or a deploy file,
not a Preference.

## The deploy directory

Files in `src/main/deploy/` are copied to the roboRIO at
`/home/lvuser/deploy` when you deploy. Use it for config and for
path files (PathPlanner, Choreo). Read them with `Filesystem` so
the same call works on the robot **and** in simulation:

```java
File deployDir = Filesystem.getDeployDirectory();
```

Official page:
[Robot Project Deploy Directory](https://docs.wpilib.org/en/stable/docs/software/basic-programming/deploy-directory.html).

PathPlanner's generated paths belong here (or in the location
that vendor's WPILib integration expects — read
[PathPlanner lib getting started](https://pathplanner.dev/pplib-getting-started.html)
when you reach [Autonomous Paths](../autonomous/)). Do not check
in a hardcoded `/Users/you/Downloads/auto.path`.

## Tasks

1. **Read the three WPILib pages.** Read
   [Units](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-units.html),
   [Preferences](https://docs.wpilib.org/en/stable/docs/software/basic-programming/robot-preferences.html),
   and
   [Deploy directory](https://docs.wpilib.org/en/stable/docs/software/basic-programming/deploy-directory.html)
   all the way through. In `wpilib/configuration.md`, write one
   paragraph each: when you would use Units, when Preferences,
   when a deploy file. Include one example of a number that
   should **not** be a Preference (alliance color is a valid
   example).

2. **Compute distance per rotation.** In the sim project (or a
   small class under `frc-learning/wpilib/`), use the Units
   library to take a wheel diameter in **inches**, compute
   circumference, and print it in **meters**. Use a diameter you
   would actually put on a module (look at the team's wheel, or
   use 4.0 inches and say so). Paste the program output in the
   notes. Commit the Java.

3. **Tune one Preference in simulation.** `initDouble` a key such
   as `DemoP`. Read it in `robotPeriodic` or a command and print
   it (or send it to
   [SmartDashboard](https://docs.wpilib.org/en/stable/docs/software/dashboards/smartdashboard/smartdashboard-intro.html)).
   Change the value on the dashboard or Preferences table, and
   confirm the next print shows the new number **without**
   redeploying. Screenshot the dashboard and the console into
   `wpilib/configuration/`.

4. **Ship and read a deploy file.** Create
   `src/main/deploy/learning-config.json` (or `.txt`) with a
   short JSON object — for example `{"intake": "practice"}`.
   Read it with `Filesystem.getDeployDirectory()`, print the
   contents in sim, and paste that printout. If the file is
   missing, your code should print a clear error, not an NPE.

5. **Key-constant habit.** In the notes, quote the Preference
   **constant** you used (`kArmPKey` or similar) and write one
   sentence on what happens if someone types the string literal
   `"ArmP "` with a trailing space in the dashboard.

6. **Open a pull request** with notes, screenshots, the Units
   snippet, and the deploy file.

## Acceptance Criteria

- [ ] `wpilib/configuration.md` explains Units vs Preferences vs
      deploy files, including one number that must not be a
      Preference.
- [ ] Java using the Units library prints distance-per-rotation
      in meters from an inch diameter. Output is in the notes.
- [ ] A Preference is initialized, edited from the dashboard in
      simulation, and the new value is observed without
      redeploying. Screenshot is in the repo.
- [ ] A file in `src/main/deploy/` is read via
      `Filesystem.getDeployDirectory()` and its contents are
      printed. Missing-file behavior is not a crash.
- [ ] Preference keys used in code are named constants.
- [ ] A pull request is open or was merged after review.

## Resources

- [WPILib: The Java Units Library](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-units.html)
- [WPILib: Setting Robot Preferences](https://docs.wpilib.org/en/stable/docs/software/basic-programming/robot-preferences.html)
- [WPILib: Robot Project Deploy Directory](https://docs.wpilib.org/en/stable/docs/software/basic-programming/deploy-directory.html)
- [WPILib: SmartDashboard intro](https://docs.wpilib.org/en/stable/docs/software/dashboards/smartdashboard/smartdashboard-intro.html)
- [WPILib: Java Garbage Collection](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-gc.html)
- [PathPlanner: library getting started](https://pathplanner.dev/pplib-getting-started.html)

## Notes

- Prefer Units at the edges; convert to doubles at APIs that do
  not accept measures. Do not allocate new measures in a hot
  loop — that is the next ticket.
- Preference keys in named constants avoid typos that silently
  create empty preferences.
- Deploy files are how PathPlanner autos get onto the roboRIO.
  You will use this again in [Autonomous Paths](../autonomous/).
- Next: [Debugging & Performance](../debugging/). Bring a
  project that can crash on purpose.
