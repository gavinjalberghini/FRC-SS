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

## Description

Code breaks. The skill is finding *why* fast enough that driver
practice still happens. This ticket is three tools that save a
build-season week: **Test mode** so you can exercise one mechanism
without running teleop; **reading a stack trace** so a
`NullPointerException` is a line number instead of a vibe; and
**garbage collection** so a clever Units one-liner does not stall
the 20 ms loop.

You just put numbers in the right places in
[Tunable Config](../configuration/). This ticket is what you do
when those numbers — or a `null` subsystem — go wrong. The next
ticket, [Code a Robot](../code-a-robot/), is the capstone: you
will generate swerve, tune a PID, and follow a path. You will
crash. You will want this ticket's habits before that one, not
during it.

The easy mistakes: enabling LiveWindow on a mechanism that
commands motors the instant Test mode starts; reading only the
bottom of a stack trace (that is WPILib's `startCompetition`);
creating `new Translation2d()` every loop and calling the
resulting overrun "CAN bus issues"; asking for help with "it
doesn't work" and no trace.

You will add Test-mode prints, cause and fix an NPE, and write
one allocation change. Artifacts go in `frc-learning`. This site
does not collect stack traces. The team's issue does, if they
exported the ticket.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/), especially
  exceptions (Units 11 and 16).
- [Tunable Config](../configuration/) so `MutableMeasure` is not
  a surprise.
- A sim-capable WPILib project from the earlier veteran labs.

## What you'll learn

- Where Test mode runs (`testInit` / `testPeriodic`) and why it
  exists.
- How to read a Java stack trace from the top: exception type,
  *your* class, *your* line.
- Why per-loop object allocation pauses the robot, and one
  concrete change that avoids it.

## Test mode

Selecting **Test** on the Driver Station runs `testInit()` once
and `testPeriodic()` each tick (alongside `robotPeriodic()`). It
is a safe place to jog one motor, print one sensor, or run a
sysid routine without your teleop default commands fighting you.

LiveWindow, which used to throw sensors and actuators onto the
dashboard automatically, is **disabled by default** since 2024
because it surprised people with motion. Re-enable it only if
you mean to, and only with the robot on blocks. Official page:
[Using Test Mode](https://docs.wpilib.org/en/stable/docs/software/basic-programming/using-test-mode.html).

Test mode is not "teleop but spooky." If you put full drive code
in `testPeriodic`, you have missed the point.

## Reading a stack trace

When robot code crashes you will see `Unhandled exception` in
the console with a stack trace. Read it **top-down**. The top
frames are where it failed:

```text
Error at frc.robot.Robot.robotInit(Robot.java:23): Unhandled exception: java.lang.NullPointerException
        at frc.robot.Robot.robotInit(Robot.java:23)
        at edu.wpi.first.wpilibj.TimedRobot.startCompetition(TimedRobot.java:107)
        ...
```

That says: `NullPointerException`, in `robotInit`, at
`Robot.java` line **23**. Start there. Ignore the WPILib frames
until your frame does not exist (then you found a library bug,
which is rare).

Three very common cases:

- **NullPointerException** — you used an object that was
  declared but never `new`'d, or a subsystem getter returned
  null. Fix: initialize before use; do not call methods on
  something you never constructed.
- **ArithmeticException: / by zero** — integer division had a
  `0` denominator. Fix: guard, or use `double`.
- **HAL: Resource already allocated** — two devices share a
  port, or a subsystem was constructed twice. Fix: one
  instance, unique ports / CAN IDs. Tuner X from
  [Phoenix Tuner X](../phoenix-tuner/) is how you confirm the
  ID side.

When you ask for help, send the **full** stack trace and a link
to the commit. Official page:
[Reading Stacktraces](https://docs.wpilib.org/en/stable/docs/software/basic-programming/reading-stacktraces.html).

The VS Code debugger can pause on that line:
[Debugging a Robot Program](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/debugging-robot-program.html).
Use it when the trace is not enough.

## Garbage collection and object creation

Java reclaims unused objects automatically. While the collector
runs, **your robot program pauses**. Creating lots of
short-lived objects every loop (new `Translation2d`, new
`Distance`, string concatenation for NT) causes occasional
freezes and **loop overruns**.

Minimize per-loop allocation. Reuse objects (`MutableMeasure`
from the Units library). Prefer primitives and arrays on hot
paths. Official page:
[Java Garbage Collection](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-gc.html).

A loop overrun is a real match problem: the scheduler slips,
odometry jumps, a command finishes late. It will not always
show up as an exception.

## Tasks

1. **Read the three WPILib pages.** Read
   [Using Test Mode](https://docs.wpilib.org/en/stable/docs/software/basic-programming/using-test-mode.html),
   [Reading Stacktraces](https://docs.wpilib.org/en/stable/docs/software/basic-programming/reading-stacktraces.html),
   and
   [Java Garbage Collection](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-gc.html).
   Skim
   [Debugging a Robot Program](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/debugging-robot-program.html)
   so you know where the debug button lives. In
   `wpilib/debugging.md`, write when you would use Test mode
   instead of teleop, and what line of a stack trace you read
   first.

2. **Add Test-mode output.** In your sim project, print a clear
   message from `testInit()` and a counter or sensor line from
   `testPeriodic()`. Enable **Test** in the Driver Station /
   sim GUI. Confirm teleop does *not* print those lines.
   Paste both the Test output and a sentence that you checked
   teleop.

3. **Cause, read, and fix an NPE.** Declare an object (a
   `Command`, a `XboxController`, a custom class — anything)
   without initializing it, then use it so the program throws.
   Copy the **full** stack trace into
   `wpilib/debugging/npe-trace.txt`. Highlight (in the markdown
   file) the exception type and the **your-code** line. Then
   initialize the object and confirm the crash is gone. Commit
   both the broken-trace file and the fix. Do not leave the
   NPE on `main`.

4. **Name an allocation fix.** In a comment on a periodic
   method (or in the markdown file if you do not want to churn
   drive code), explain **one** change that avoids creating
   new objects every iteration — for example, reuse a
   `MutableMeasure`, cache a `Translation2d`, or stop building
   log strings with `+` in a loop. Point at a real line in
   your project or at the Units example from the previous
   ticket.

5. **Practice the help packet.** In `wpilib/debugging.md`,
   write the three things you will include the next time you
   ask a mentor about a crash: repo link + commit, full
   stack trace, what changed since it last worked. Frequent
   commits from [Git Fundamentals](../git/) make that last
   question answerable.

6. **Open a pull request.** A mentor should be able to read
   the saved stack trace and point at the same line you did.

## Acceptance Criteria

- [ ] `wpilib/debugging.md` says when Test mode is the right
      mode and which stack-trace line you read first.
- [ ] Enabling Test in simulation prints your `testInit` /
      `testPeriodic` messages; teleop does not.
- [ ] `wpilib/debugging/npe-trace.txt` contains a real
      `NullPointerException` stack trace you caused. The
      notes name the class and line. The crash is fixed on
      the branch you want reviewed.
- [ ] One written allocation change (comment or markdown)
      names a per-loop object you would stop creating.
- [ ] The "help packet" three-liner is in the notes.
- [ ] A pull request is open or was merged after review.

## Resources

- [WPILib: Using Test Mode](https://docs.wpilib.org/en/stable/docs/software/basic-programming/using-test-mode.html)
- [WPILib: Reading Stacktraces](https://docs.wpilib.org/en/stable/docs/software/basic-programming/reading-stacktraces.html)
- [WPILib: Java Garbage Collection](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-gc.html)
- [WPILib: Debugging a Robot Program](https://docs.wpilib.org/en/stable/docs/software/vscode-overview/debugging-robot-program.html)
- [WPILib: The Java Units Library](https://docs.wpilib.org/en/stable/docs/software/basic-programming/java-units.html)
  — `MutableMeasure` for hot loops
- [Oracle: Exceptions](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html)

## Notes

- When something breaks, ask "what changed since it last
  worked?" Frequent commits make that question cheap.
- The single-step debugger in VS Code lets you inspect
  variables on the line before the crash. Use it when the
  trace is not enough — not as a substitute for reading the
  trace.
- HAL resource errors are often "I constructed Drive twice"
  or "Tuner X ID 1 is also in Constants as 1 for a different
  motor." Check hardware before rewriting kinematics.
- Next: [Code a Robot](../code-a-robot/). That ticket expects
  you to generate swerve, tune PID, and follow a meter of
  path. Bring Test mode and a willingness to read traces.
