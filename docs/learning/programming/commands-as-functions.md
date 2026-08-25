---
layout: lesson
title: Commands as Functions
subtitle: Use lambdas and method references to build inline commands the scheduler can run.
permalink: /learning/programming/commands-as-functions/
role: veteran
order: 9
size: 1
time: "~45 min"
---

## Description

The command-based framework is built on passing **functions** around:
you hand a small function to a `Command`, and the scheduler calls it
later — when the command is scheduled, not when Java evaluates the
line that builds it. If that sentence is fuzzy, every
`Commands.runOnce` and every `() -> drive.withVelocityX(...)` you
copy from a vendor example will feel like magic, and you will put
side effects in the wrong place.

You already write methods from [Java Fundamentals](../java-fundamentals/)
Unit 9 and you already bind buttons in
[Reading Driver Input](../driver-input/). This ticket is the missing
piece: the difference between **calling** `resetEncoders()` and
**passing** `drivetrain::resetEncoders`. The next ticket,
[Match State & Alliance Color](../alliance-color/), will ask you to
pass *another* kind of later-evaluated thing (`Optional`, suppliers).
Get functions-as-data first.

The easy mistakes: writing `Commands.runOnce(drivetrain.resetEncoders())`
(that calls it *now* and passes the return value, usually `void`,
which does not compile — or worse, compiles if it returns something
you did not mean); capturing a loop index in a lambda and wondering
why every button does the last thing; assuming the lambda body runs
when `RobotContainer` constructs.

You will bind one lambda command and one method-reference command in
simulation and explain, in a comment a mentor can read, why the body
does not run at the line it is written. That comment lives in
`frc-learning` with the rest of your WPILib notes. This site does
not track it.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/), especially methods
  (Unit 9). You should be able to write a `void` method and a method
  that returns a value.
- [Reading Driver Input](../driver-input/) — a command-based example
  project you can run in the simulator.

## What you'll learn

- The difference between calling a function and passing a function.
- How to pass work with a method reference (`obj::method`) or a
  lambda (`() -> ...`).
- Java's "effectively final" capture rule, and which functional
  interfaces WPILib uses constantly.

## Passing versus calling

Calling a function runs its code now. **Passing** a function hands
it to other code to run *later*. Seeing a function's name in source
does not always mean it runs on that line. `Commands.runOnce(...)`
builds a command object and returns it. The function inside runs
when the scheduler runs that command — typically because a trigger
fired or `autonomousCommand.schedule()` ran.

Oracle's
[Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
is the language reference. WPILib's
[Treating Functions as Data](https://docs.wpilib.org/en/stable/docs/software/basic-programming/functions-as-data.html)
is the same idea with robot-shaped examples. Read both. Type the
WPILib examples; do not only highlight them.

## Method references

If you already have a method with the right shape, refer to it with
`::`:

```java
// Build a command that calls drivetrain.resetEncoders() when scheduled
Command resetCmd = Commands.runOnce(drivetrain::resetEncoders, drivetrain);
```

`runOnce` wants a `Runnable` — no parameters, no return value — so
`resetEncoders()` must have that shape or it will not compile. The
second argument is the subsystem requirement: the scheduler will not
run two commands that both own `drivetrain` at once.

## Lambda expressions

If you do not have a named method, write the function inline:

```java
// One-line lambda: brackets, return, and semicolon can be omitted
Command driveHalf = Commands.runOnce(
    () -> drivetrain.arcadeDrive(0.5, 0.0),
    drivetrain);
```

`() ->` is the (empty) parameter list; what follows is the body.
When the body needs the *current* joystick value every loop, you
will write `Commands.run(() -> ..., drivetrain)` instead of
`runOnce`. That is still a lambda. It is just called more than once.

## Capturing variables

A lambda can use variables from the surrounding code (a "capture").
In Java you can only capture variables that are **effectively
final** (never reassigned). The object a reference points to can
still change its internal state — you just cannot repoint the
reference. To capture a changing primitive, wrap it in an object
(or read it from the joystick / a `DoubleSupplier` every call,
which is what drive requests do).

If you build commands inside a `for` loop and each lambda uses the
loop index, you will fight this rule. Build them from a list of
named objects instead.

## Functional interfaces you will keep meeting

- `Runnable` — no args, no return (`runOnce`, `run`)
- `Supplier<T>` — no args, returns a value (many "get measurement"
  hooks)
- `Consumer<T>` — takes a value, no return
- `BooleanSupplier` — triggers and `until(...)`

You do not need to implement these as classes. A lambda or a method
reference that matches the shape is enough.

## Tasks

1. **Read the two official pages.** Read
   [Treating Functions as Data](https://docs.wpilib.org/en/stable/docs/software/basic-programming/functions-as-data.html)
   and
   [Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
   through "Target Typing." Skim
   [Command-based programming](https://docs.wpilib.org/en/stable/docs/software/commandbased/index.html)
   so `Commands.runOnce` has a home. In
   `wpilib/commands-as-functions.md`, write three sentences: calling
   versus passing; what `::` means; what `() ->` means.

2. **Bind a lambda command.** In your command-based sim project,
   create a command with `Commands.runOnce` (or `InstantCommand`)
   using a **lambda** that prints a message that includes the word
   `lambda`. Bind it to a button you did not use in the driver-input
   ticket. Enable teleop in
   [simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)
   and confirm the message prints **only** when you press the
   button — not when `RobotContainer` constructs. Paste the console
   line into the notes.

3. **Bind a method-reference command.** Add a small method on an
   existing subsystem (or on `RobotContainer`) such as
   `public void logReset() { System.out.println("reset via ::"); }`.
   Build `Commands.runOnce(this::logReset)` (or
   `subsystem::logReset` with the right requirements). Bind it to a
   second button. Confirm it runs on press.

4. **Write the comment the ticket is for.** Above the lambda bind,
   add a comment of at least three lines that explains why the
   lambda body does **not** run at the line where it is written,
   and when it *does* run. A mentor should be able to read only
   that comment and know you did not treat `runOnce` as
   `resetEncoders()`.

5. **Break capture on purpose, then fix it.** In a scratch `main`
   or a short `java/LambdaCapture.java` in `frc-learning`, try to
   compile a lambda that increments an `int count` from outside
   and prints it. Write down the compiler error. Then fix it the
   way the Oracle page describes (array of one, `AtomicInteger`,
   or stop incrementing and pass a supplier). Commit that file
   with a comment of what you learned. This is not robot code; it
   is so the rule is not abstract.

6. **Open a pull request** with the markdown notes, the capture
   experiment, and the robot-sim Java change.

## Acceptance Criteria

- [ ] `wpilib/commands-as-functions.md` explains calling versus
      passing, `::`, and `() ->` in your own words.
- [ ] Simulation: a lambda `runOnce` prints only on a button press,
      not at startup. Sample output is in the notes.
- [ ] Simulation: a method-reference command prints on a second
      button.
- [ ] A three-line (or longer) comment above the lambda bind
      explains delayed execution.
- [ ] `java/LambdaCapture.java` (or equivalent) shows a capture
      compile error you hit and the fix, with a comment.
- [ ] A pull request is open or was merged after review.

## Resources

- [WPILib: Treating Functions as Data](https://docs.wpilib.org/en/stable/docs/software/basic-programming/functions-as-data.html)
- [WPILib: Command-based programming](https://docs.wpilib.org/en/stable/docs/software/commandbased/index.html)
- [WPILib: Binding Commands to Triggers](https://docs.wpilib.org/en/stable/docs/software/commandbased/binding-commands-to-triggers.html)
- [Oracle: Lambda Expressions](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
- [Oracle: Method References](https://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html)
- [WPILib: Robot Simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)

## Notes

- `Commands.runOnce(drivetrain.resetEncoders(), drivetrain)` is the
  classic compile fail. You wanted `drivetrain::resetEncoders`.
- Drive defaults are often `Commands.run(() -> ..., drivetrain)`:
  the lambda runs every scheduler cycle while the default command
  is scheduled. That is how a stick becomes motion. The signs from
  [the coordinate system ticket](../coordinate-system/) still
  belong *inside* that lambda.
- Next: [Match State & Alliance Color](../alliance-color/). You will
  read an `Optional` every loop instead of caching alliance in a
  constructor — same "do not do it too early" instinct as lambdas.
