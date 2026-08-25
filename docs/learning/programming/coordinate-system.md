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

## Description

Getting the coordinate system right is one of the highest-leverage
things a programmer can do. Many teams intuitively assume +Y is
forward because that is how a math class graph looks, or because a
joystick's "Y" is the vertical stick. WPILib does not use that
convention. If you guess, you will spend the season chasing bugs in
driving, pose estimation, and path following that are all the same
bug: a sign.

You just learned how to **read** a stick in
[Reading Driver Input](../driver-input/). This ticket is what those
numbers *mean* on the robot and on the field. The next two tickets —
[Commands as Functions](../commands-as-functions/) and
[Match State & Alliance Color](../alliance-color/) — will use this.
Alliance color is how you flip driver-relative field drive when you
are on red and the field origin stays blue.

The easy mistakes: assuming +Y is forward; forgetting that a joystick
forward is **negative** Y; mixing robot-relative and field-relative
without writing down which; inverting a gyro that is already CCW+
"because PathPlanner looked mirrored." Write the axes down. Then
negate on purpose.

Work goes in `frc-learning` as a labeled sketch and a short sim note.
This site does not grade the sketch. A mentor should be able to tell
from it whether you will break kinematics.

## Prerequisites

- [Reading Driver Input](../driver-input/) — you can print an axis
  and run a drive example in simulation.

## What you'll learn

- WPILib's robot convention (NWU): +X forward, +Y left, +Z up, CCW+
  rotation.
- The joystick convention (NED) and why "forward on the stick" is
  not "+Y on the robot."
- How to label swerve module translations from the robot center with
  the correct signs.

## The robot coordinate system (NWU)

WPILib uses **North-West-Up**:

- **+X** points **forward**.
- **+Y** points **left**.
- **+Z** points **up**.
- Rotation is **counter-clockwise positive** (CCW+): 0° is +X
  (forward), 90° is +Y (left). The range is `(-180°, 180°]`.

The common mistake is assuming +Y points forward. It does not.
**+X is forward.** Getting this wrong breaks kinematics,
field-oriented driving, and path planning. Read the official page
until that sentence is boring:
[Coordinate System](https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html).

## The joystick coordinate system (NED)

Joysticks use **North-East-Down**, and the values you read are
rotations around axes, not "robot translations" yet. In practice:

- Pushing the stick **forward** gives a **negative Y** value.
- Pushing the stick **right** gives a **positive X** value.

The robot wants "forward = positive X." The stick gives "forward =
negative Y." So you **negate** (and you swap which HID axis maps to
which robot axis) when you feed the drivetrain:

```java
// Arcade drive: forward speed, then turn rate
myDrive.arcadeDrive(-driveStick.getY(), -driveStick.getX());
```

That is not a superstition. It is a change of frame. If a robot
drives backward, flip **one** documented sign and record it. Do not
flip three and hope.

## Watch out for sensors

- Some gyros and IMUs report **clockwise-positive** rotation (the
  opposite of WPILib). You may need to invert their values — always
  verify rotation is CCW+ in the robot frame.
- Many encoders and IMUs read **continuously** (past 180° they
  report 181°, not -179°). Make sure your wrapping matches the
  sensor. WPILib `Rotation2d` exists so you stop writing your own
  wrap function at 1 a.m.
- PathPlanner and Choreo document a **field** origin. Most current
  FRC tooling uses a fixed blue-alliance origin. When you are on
  red, you invert the *driver's* field-relative X/Y (or rotate the
  pose), not the field's AprilTag map. That is
  [Alliance Color](../alliance-color/).

## Tasks

1. **Read the spec, not a meme.** Read
   [WPILib: Coordinate System](https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html)
   completely, including the joystick and field notes. If you will
   touch PathPlanner this season, also open
   [PathPlanner: getting started](https://pathplanner.dev/gui-getting-started.html)
   and find how that tool draws the field origin. Write
   `wpilib/coordinates.md` in `frc-learning`.

2. **Write the axes in your own words.** In that file, without
   copying WPILib's table, state:

   - robot +X, +Y, +Z, and positive rotation
   - what a joystick reports when you push forward and when you
     push right
   - why `arcadeDrive(-getY(), -getX())` is a common first line

3. **Prove it in simulation.** In the drive example from the
   previous ticket (or a fresh WPILib arcade/swerve example), push
   the stick **forward** and confirm the simulated robot moves
   **forward**. If it does not, add the documented negation — do
   not also invert turn "for luck." Then push the stick to rotate
   and confirm CCW on the robot when you command positive rotation
   (or document the HID mapping you used). Paste a sentence of
   what you saw into the markdown file.

4. **Sketch a swerve chassis.** On paper or in a drawing tool,
   sketch a rectangle, mark the robot front, and label each
   module's translation from the **robot center** as `(x, y)` in
   meters with **WPILib signs** (front-left is +X and +Y). Include
   the four corners. Photograph or export the sketch into
   `wpilib/coordinates/` and embed or link it from the markdown.
   Wrong signs here are how generated swerve code steers like a
   crab.

5. **Answer two trap questions** in the same file:

   - A teammate says "just invert the gyro, PathPlanner is
     mirrored." What do you check before you invert anything?
   - You are writing field-relative drive for a fixed blue origin.
     What should change when the Driver Station says you are red?
     (You may point at the next ticket; you still have to say
     *what* changes — driver input or the world.)

6. **Open a pull request** with the write-up and the sketch. A
   mentor should be able to reject a sketch that puts +Y forward.

## Acceptance Criteria

- [ ] `wpilib/coordinates.md` states robot +X/+Y/+Z and CCW+ in
      your own words.
- [ ] The same file states joystick forward and joystick right in
      HID units, and explains the common arcadeDrive negations.
- [ ] Simulation: stick forward moves the robot forward; rotation
      direction is written down and matches the convention you
      claim.
- [ ] A swerve sketch labels all four module `(x, y)` translations
      from center with WPILib signs. Front is marked.
- [ ] The two trap questions have written answers.
- [ ] A pull request is open or was merged after a mentor looked
      at the sketch.

## Resources

- [WPILib: Coordinate System](https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html)
- [WPILib: Robot Simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)
- [PathPlanner: GUI getting started](https://pathplanner.dev/gui-getting-started.html)
- [WPILib: Joysticks](https://docs.wpilib.org/en/stable/docs/software/basic-programming/joystick.html)

## Notes

- For field-relative driving you also choose a **field** origin.
  Most tools (PathPlanner, Choreo) use a fixed blue origin. When
  your alliance is red, you invert the driver's field X/Y — which
  is exactly what [Alliance Color](../alliance-color/) covers.
- `Rotation2d.fromDegrees(90)` is left, not "north on a paper map,"
  unless your paper map is the robot.
- Next: [Commands as Functions](../commands-as-functions/). The
  `() ->` in drive requests is the next idea. The signs you just
  wrote still apply inside that lambda.
