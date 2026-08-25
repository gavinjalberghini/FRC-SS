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

## Description

A robot is only as good as the driver's control over it. WPILib reads
USB controllers through `GenericHID` and the ready-made subclasses
`Joystick`, `XboxController`, and `PS4Controller`. Each axis is a
double from **-1 to 1**. Buttons are not "how hard," they are pressed
or not — and in command-based code you almost never poll them yourself.
You bind them to commands with **triggers**.

This is the first veteran WPILib lab. You have Java from
[Java Fundamentals](../java-fundamentals/) and a board habit from
[Kanban & Agile Practices](../kanban-agile/). You do **not** need a
physical robot. The simulator plus the Driver Station (or the sim GUI)
is enough. The easy mistakes are: reading the stick every loop in
`teleopPeriodic` after the team already uses command-based bindings;
using `getAButton()` (held) when you wanted `getAButtonPressed()`
(edge); and assuming USB port 0 is "the driver's stick" after someone
plugged in a keyboard.

You will print an axis, bind a button to a command, and write down
what you saw in `frc-learning`. The next ticket, the
[Field Coordinate System](../coordinate-system/), explains why so many
teams negate those axis values. Do this ticket first so you have
numbers on the screen before you argue about signs.

This site does not track the sim demo. A mentor does — via a PR and,
if they ask, a shared screen.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/) through methods (Unit 9)
  at minimum. Exercises 1–7 on a branch is the bar.
- [Kanban & Agile Practices](../kanban-agile/) so this lab can be a
  real issue on a board if the team works that way.
- WPILib VS Code installed
  ([setup guide](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html)).
- A USB controller, or willingness to use keyboard/sim controls. No
  physical robot required.

## What you'll learn

- How to construct a controller object tied to a Driver Station USB
  port, and how to see live axis values.
- The difference between a level button read and an edge read, and
  why command-based code uses triggers instead of either.
- How to bind a button to a command in `RobotContainer` and prove it
  in simulation.

## Reading axes and buttons

A controller is created with the USB port index shown in the Driver
Station:

```java
XboxController controller = new XboxController(0); // port 0
double forward = -controller.getLeftY();           // axes range -1..1
```

Axes are read continuously. Buttons are usually read with the
`Pressed` / `Released` "edge" methods so an action happens **once**
per press rather than every loop while held:

```java
if (controller.getAButtonPressed()) {
  // runs once, the moment A is pressed
}
```

The POV (the directional hat / D-pad) returns an angle in degrees, or
`-1` when not pressed. It is hard to hit an exact angle, so do not
require 47° to mean "intake."

## The command-based way: binding triggers

In command-based code you bind a button to a command in
`RobotContainer` instead of polling it. A `CommandXboxController`
exposes each button as a `Trigger`:

```java
CommandXboxController controller = new CommandXboxController(0);

// While A is held, run the intake; stop it when released.
controller.a().whileTrue(intake.runIntakeCommand());

// Press B once to toggle an arm position.
controller.b().onTrue(arm.toggleCommand());
```

`whileTrue` versus `onTrue` is the held-versus-edge distinction,
expressed as scheduler behavior rather than an `if` in periodic.
[Commands as Functions](../commands-as-functions/) will explain the
`()` -> lambda you will start seeing in examples. For this ticket,
copy a pattern from the docs and make it print.

## Tasks

1. **Read the WPILib pages.** Read
   [Joysticks](https://docs.wpilib.org/en/stable/docs/software/basic-programming/joystick.html)
   and
   [Binding Commands to Triggers](https://docs.wpilib.org/en/stable/docs/software/commandbased/binding-commands-to-triggers.html)
   all the way through. Skim
   [What is "command-based" programming?](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html)
   if the word "scheduler" is new. Write four sentences in
   `wpilib/driver-input.md` in `frc-learning`: what an axis range is,
   what USB port means, what `whileTrue` does, what `onTrue` does.

2. **See live HID values.** Open the Driver Station
   ([Game Tools](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/frc-game-tools.html)
   if you still need it) and the **USB Devices** tab. Plug in a
   controller. Move every stick and press every face button. Screenshot
   the tab with a stick deflected into `wpilib/driver-input/`. Note
   which physical port is `0`. If you are on a machine without Game
   Tools, use the
   [simulation GUI](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)
   joystick view after Task 3 and say so in the notes.

3. **Create or open a command-based example.** In WPILib VS Code,
   create a new robot project
   ([Creating a robot program](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/creating-robot-program.html))
   using a **command-based** Java template, or clone a WPILib example
   that already has a drivetrain. Put the project **outside** the
   team's robot repo. A folder such as `frc-learning/wpilib/driver-input-sim/`
   is fine if the repo can hold it; otherwise keep the project local
   and commit only the notes plus the one Java file you changed.

4. **Print one axis and one edge.** In simulation
   ([Robot Simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)),
   print one axis (for example left Y) and the result of an edge read
   (`getAButtonPressed()` or a `Trigger` equivalent) to the console
   or NetworkTables. Enable teleop in the sim. Push the stick, tap the
   button. Confirm the button line appears **once per tap**, not every
   cycle while held. Paste a few lines of console output into
   `wpilib/driver-input.md`.

5. **Bind a command to a trigger.** In `RobotContainer`, bind a
   button to `Commands.runOnce(() -> System.out.println("intake"),
   /* no subsystem */)` or an `InstantCommand` that prints a message.
   Follow the trigger-binding doc. Press the button in simulation and
   confirm the message. Commit that Java change (or the whole example
   project) on a branch.

6. **Write the gotchas.** In the same markdown file, answer in your
   own words: when does the Driver Station rescan USB? What happens if
   two controllers are swapped? Why is polling `getAButton()` in
   `teleopPeriodic` a bad habit on a command-based robot?

7. **Open a pull request.** Ask a mentor to read the notes and, if
   they want, watch the sim bind once.

## Acceptance Criteria

- [ ] `wpilib/driver-input.md` explains axis range, USB port,
      `whileTrue`, and `onTrue` in your own words.
- [ ] A screenshot of USB Devices (or the sim joystick view) shows a
      deflected axis.
- [ ] Simulation prints an axis value and an edge-triggered button
      event. Sample output is in the notes.
- [ ] A button is bound to a command in `RobotContainer` (or
      equivalent). Pressing it in sim prints a message **once per
      press** for `onTrue`, or while held for `whileTrue` — and the
      notes say which you used.
- [ ] The notes answer USB rescan, swapped controllers, and why
      periodic polling is the wrong default.
- [ ] A pull request with the notes (and the Java change) is open or
      was merged after review.

## Resources

- [WPILib: Joysticks](https://docs.wpilib.org/en/stable/docs/software/basic-programming/joystick.html)
- [WPILib: Binding Commands to Triggers](https://docs.wpilib.org/en/stable/docs/software/commandbased/binding-commands-to-triggers.html)
- [WPILib: What is command-based?](https://docs.wpilib.org/en/stable/docs/software/commandbased/what-is-command-based.html)
- [WPILib: Robot Simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)
- [WPILib: Creating a robot program](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/creating-robot-program.html)
- [WPILib: FRC Game Tools](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/frc-game-tools.html)
- [WPILib: HID controllers in simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)

## Notes

- The Driver Station only re-scans for controllers while **disabled**
  (or when you press F1). At competition you cannot disable on the
  field, so check USB order in the queue. A forgotten second
  controller bumping the driver to port 1 is a real match loss.
- Many teams negate axis values when driving. The next lesson, the
  [Field Coordinate System](../coordinate-system/), is exactly why —
  do not invent a fourth sign flip "until it feels right" without
  reading that page.
- Prefer `CommandXboxController` (or the matching Command* class) in
  new code. Raw `XboxController` plus `if` in periodic is how
  command-based projects rot.
