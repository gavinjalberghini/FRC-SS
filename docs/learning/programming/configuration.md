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

## Overview

Robot code is full of numbers: gains, setpoints, measurements, and config. This
lesson covers three WPILib tools that make those numbers safer and easier to
change: the **Units library** (so you never mix up inches and meters), **Robot
Preferences** (so you can tune values from the dashboard without redeploying), and
the **deploy directory** (for config and path files that ship with your code).

## Prerequisites

- [Java Fundamentals](../java-fundamentals/).

## What you'll learn

- How to make measurements type-safe with the Units library.
- How to store and edit tunable values with Preferences.
- Where to put files your robot needs at runtime.

## The Units library

The Units library tags a value with its dimension so the compiler catches
mistakes (you can't add a distance to a time, and conversions are explicit):

```java
import static edu.wpi.first.units.Units.*;

Distance wheelDiameter = Inches.of(3);
Distance perRotation   = wheelDiameter.times(Math.PI);
double meters          = perRotation.in(Meters); // explicit conversion to a bare double
```

> Arithmetic on measures creates **new objects**. For values computed once
> (constants), that's fine. For values recomputed every loop, prefer `MutableMeasure`
> to avoid creating lots of short-lived objects (see the [Debugging & Performance](../debugging/) lesson).

## Robot Preferences

`Preferences` stores values in the roboRIO's flash so you can tune them live from
SmartDashboard/Shuffleboard without rebuilding. Initialize defaults once, then
read them when needed:

```java
public static final String kArmPKey = "ArmP";
public static final double kDefaultArmKp = 50.0;

// Initialize the key with a default if it doesn't exist yet (e.g. in a constructor)
Preferences.initDouble(kArmPKey, kDefaultArmKp);

// Read it later (second argument is the fallback if the key is missing)
double armKp = Preferences.getDouble(kArmPKey, kDefaultArmKp);
```

## The deploy directory

Files in `src/main/deploy/` are copied to the roboRIO at `/home/lvuser/deploy`
when you deploy. Use it for config files and path files (PathPlanner/Choreo). Read
them with the `Filesystem` class so the path works on the robot **and** in
simulation:

```java
File deployDir = Filesystem.getDeployDirectory();
```

## Steps & acceptance criteria

- [ ] Read the WPILib pages on the [Units library](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-units.html),
      [Robot Preferences](https://docs.wpilib.org/en/stable/docs/software/basic-programming/robot-preferences.html),
      and the [Deploy directory](https://docs.wpilib.org/en/stable/docs/software/basic-programming/deploy-directory.html).
- [ ] Using the Units library, compute a wheel's distance-per-rotation from a
      diameter in inches and print it in meters.
- [ ] In a simulation project, store one tunable value in `Preferences`, edit it on
      the dashboard, and confirm your code reads the new value.
- [ ] Put a small text or JSON file in `src/main/deploy/`, then read it back using
      `Filesystem.getDeployDirectory()` and print its contents.

## Resources

- [WPILib: The Java Units Library](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-units.html)
- [WPILib: Setting Robot Preferences](https://docs.wpilib.org/en/stable/docs/software/basic-programming/robot-preferences.html)
- [WPILib: Robot Project Deploy Directory](https://docs.wpilib.org/en/stable/docs/software/basic-programming/deploy-directory.html)

## Notes

- Prefer the Units library at the edges of your code (configuration, dashboards)
  and convert to bare doubles only when talking to APIs that don't accept units.
- Keep Preference **keys** in named constants to avoid typos that silently create
  new, empty preferences.
