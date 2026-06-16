---
layout: lesson
title: The Field Coordinate System
subtitle: Understand WPILib's robot, joystick, and field axes — and why you negate inputs.
permalink: /learning/programming/coordinate-system/
role: veteran
order: 8
size: 1
time: "~45 min"
---

## Overview

Getting the coordinate system right is one of the highest-leverage things a
programmer can do. Many teams intuitively assume a different convention than
WPILib uses, then spend the season chasing bugs in driving, pose estimation, and
path following. A few minutes here saves hours later.

## Prerequisites

- [Reading Driver Input](../driver-input/).

## What you'll learn

- WPILib's robot coordinate convention (NWU).
- The joystick convention (NED) and why it's different.
- Why driver inputs are usually negated.

## The robot coordinate system (NWU)

WPILib uses **North-West-Up**:

- **+X** points **forward**.
- **+Y** points **left**.
- **+Z** points **up**.
- Rotation is **counter-clockwise positive** (CCW+): 0° is +X (forward), 90° is +Y
  (left). The range is `(-180°, 180°]`.

> **Common mistake:** assuming +Y points forward. It doesn't — **+X is forward.**
> Getting this wrong breaks kinematics, field-oriented driving, and path planning.

## The joystick coordinate system (NED)

Joysticks use **North-East-Down**, and the values are *rotations* around axes, not
translations. In practice:

- Pushing the stick **forward** gives a **negative Y** value.
- Pushing the stick **right** gives a **positive X** value.

Because the robot wants "forward = positive X" but the stick gives "forward =
negative Y," you **negate** the joystick values when feeding them to the drivetrain:

```java
// Arcade drive: forward speed, then turn rate
myDrive.arcadeDrive(-driveStick.getY(), -driveStick.getX());
```

## Watch out for sensors

- Some gyros/IMUs report **clockwise-positive** rotation (the opposite of WPILib).
  You may need to invert their values — always verify rotation is CCW+.
- Many encoders/IMUs read **continuously** (past 180° they report 181°, not -179°).
  Make sure your code handles wrapping the same way your sensor does.

## Steps & acceptance criteria

- [ ] Read the WPILib [Coordinate System](https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html)
      page.
- [ ] In your own words, write down which direction +X, +Y, and positive rotation
      point for the **robot**, and for the **joystick**.
- [ ] In a drive example running in simulation, push the stick forward and confirm
      the robot moves forward (add the negation if it doesn't). Do the same for turning.
- [ ] Sketch a swerve robot and label the (x, y) translation of each module from
      the robot center, using the correct signs.

## Resources

- [WPILib: Coordinate System](https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html)
- [WPILib: Robot Simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)

## Notes

- For field-relative driving you'll also choose a **field** origin convention
  (most tools, like PathPlanner and Choreo, use a fixed "blue origin"). When your
  alliance is red, you invert the driver's X/Y — which is exactly what the
  [Alliance Color](../alliance-color/) lesson covers.
