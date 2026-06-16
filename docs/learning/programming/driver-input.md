---
layout: lesson
title: Reading Driver Input
subtitle: Read joysticks and controllers, and bind buttons to actions in command-based code.
permalink: /learning/programming/driver-input/
role: veteran
order: 7
size: 2
time: "30–60 min"
---

## Overview

A robot is only as good as the driver's control over it. WPILib reads driver
input through the `GenericHID` class and its ready-made subclasses —
`Joystick` (flight sticks), `XboxController`, and `PS4Controller`. Each controller
axis ranges from **-1 to 1**, and buttons can be read as pressed, released, or
held. In command-based code, you usually bind buttons to commands using
**triggers** rather than polling them yourself.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/).
- A WPILib install with the robot **simulator** (no physical robot required).

## What you'll learn

- How to construct a controller object tied to a Driver Station USB port.
- The difference between reading axes and reading buttons.
- How to bind a button to a command with a `Trigger`.

## Reading axes and buttons

A controller is created with the USB port index shown in the Driver Station:

```java
XboxController controller = new XboxController(0); // port 0
double forward = -controller.getLeftY();           // axes range -1..1
```

Axes are read continuously. Buttons are usually read with the `Pressed` /
`Released` "edge" methods so an action happens **once** per press rather than
every loop while held:

```java
if (controller.getAButtonPressed()) {
  // runs once, the moment A is pressed
}
```

> The POV (the directional hat / D-pad) returns an angle in degrees, or `-1` when
> not pressed. It's hard to hit an exact angle, so avoid requiring precise POV angles.

## The command-based way: binding triggers

In command-based code you bind a button to a command in `RobotContainer` instead
of polling it. A `CommandXboxController` exposes each button as a `Trigger`:

```java
CommandXboxController controller = new CommandXboxController(0);

// While A is held, run the intake; stop it when released.
controller.a().whileTrue(intake.runIntakeCommand());

// Press B once to toggle an arm position.
controller.b().onTrue(arm.toggleCommand());
```

## Steps & acceptance criteria

- [ ] Read the WPILib [Joysticks](https://docs.wpilib.org/en/stable/docs/software/basic-programming/joystick.html)
      page and open the **USB Devices** tab of the Driver Station to see live axis
      and button values for a connected controller.
- [ ] In a WPILib example project (such as a drive example) running in simulation,
      print one axis value and one button's `pressed` state to the console.
- [ ] Read [Binding Commands to Triggers](https://docs.wpilib.org/en/stable/docs/software/commandbased/binding-commands-to-triggers.html)
      and bind a button to a simple command (for example, an `InstantCommand` that
      prints a message). Confirm it runs when you press the button in simulation.

## Resources

- [WPILib: Joysticks](https://docs.wpilib.org/en/stable/docs/software/basic-programming/joystick.html)
- [WPILib: Binding Commands to Triggers](https://docs.wpilib.org/en/stable/docs/software/commandbased/binding-commands-to-triggers.html)
- [WPILib: Robot Simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)

## Notes

- The Driver Station only re-scans for controllers while **disabled** (or when you
  press F1). At competition you can't disable on the field, so check your USB order
  before each match.
- Many teams negate axis values when driving — the next lesson, the
  [Field Coordinate System](../coordinate-system/), explains exactly why.
