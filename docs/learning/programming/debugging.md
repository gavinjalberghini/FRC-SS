---
layout: lesson
title: "Debugging & Performance: Test Mode, Stacktraces & GC"
subtitle: Use Test mode, read stack traces to find bugs, and avoid garbage-collection stalls.
permalink: /learning/programming/debugging/
role: veteran
order: 12
size: 2
time: "1 hr"
---

## Overview

Code breaks — the skill is finding *why* fast. This lesson covers three tools:
**Test mode** for safely exercising mechanisms, **reading stack traces** to locate
crashes, and understanding **Java garbage collection** so your robot loop doesn't
stutter.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/) (especially exceptions).

## What you'll learn

- How to add and use Test-mode code.
- How to read a Java stack trace to find the line that crashed.
- Why creating many short-lived objects can cause loop overruns.

## Test mode

Selecting **Test** in the Driver Station runs `testInit()` once and
`testPeriodic()` each tick (alongside `robotPeriodic()`). It's a safe place to
exercise individual mechanisms or check sensors before wiring them into teleop or
autonomous. (LiveWindow, which shows sensors/actuators on the dashboard, is
**disabled by default** since 2024 and can be re-enabled.)

## Reading a stack trace

When robot code crashes you'll see `Unhandled exception` in the console with a
stack trace. Read it top-down — the top of the stack is where it failed:

```text
Error at frc.robot.Robot.robotInit(Robot.java:23): Unhandled exception: java.lang.NullPointerException
        at frc.robot.Robot.robotInit(Robot.java:23)
        at edu.wpi.first.wpilibj.TimedRobot.startCompetition(TimedRobot.java:107)
        ...
```

That tells you: the exception was a `NullPointerException`, in `robotInit`, at
`Robot.java` line **23**. Start there. Three very common cases:

- **NullPointerException** — you used an object that was declared but never
  `new`'d. Fix: initialize it before use.
- **ArithmeticException: / by zero** — an integer division had a `0` denominator.
  Fix: use a non-zero value, guard with `if`, or use `double`.
- **HAL: Resource already allocated** — two devices share the same port (or a
  subsystem was constructed twice). Fix: give each device its own port / make the
  subsystem a single instance.

When asking others for help, share your code link **and** the full stack trace.

## Garbage collection & object creation

Java reclaims unused objects automatically, but while the collector runs, **your
robot program pauses**. Creating lots of short-lived objects every loop can cause
occasional freezes or **loop overruns**. To avoid it: minimize per-loop object
creation, reuse objects (e.g. `MutableMeasure` from the
[Configuration](../configuration/) lesson), and prefer primitives/arrays in hot paths.

## Steps & acceptance criteria

- [ ] Read the WPILib pages on [Using Test Mode](https://docs.wpilib.org/en/stable/docs/software/basic-programming/using-test-mode.html),
      [Reading Stacktraces](https://docs.wpilib.org/en/stable/docs/software/basic-programming/reading-stacktraces.html),
      and [Java Garbage Collection](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-gc.html).
- [ ] In a simulation project, add a line to `testInit()`/`testPeriodic()` that
      prints a message, and confirm it runs when you enable **Test** mode.
- [ ] Deliberately cause a `NullPointerException` (declare an object but don't
      initialize it, then use it), read the stack trace, identify the failing line,
      and fix it.
- [ ] In a comment, explain one change you could make to a per-loop calculation to
      avoid creating new objects every iteration.

## Resources

- [WPILib: Using Test Mode](https://docs.wpilib.org/en/stable/docs/software/basic-programming/using-test-mode.html)
- [WPILib: Reading Stacktraces](https://docs.wpilib.org/en/stable/docs/software/basic-programming/reading-stacktraces.html)
- [WPILib: Java Garbage Collection](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-gc.html)

## Notes

- A good debugging habit: when something breaks, ask "what changed since it last
  worked?" Frequent commits make that question easy to answer.
- The single-step debugger (in VS Code) lets you pause and inspect variable values
  right before a crash — invaluable when the stack trace alone isn't enough.
