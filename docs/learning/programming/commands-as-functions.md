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

## Overview

The command-based framework is built on passing **functions** around: you hand a
small function to a `Command`, and the scheduler calls it later. Understanding how
Java treats "functions as data" — through **method references** and **lambda
expressions** — is the key that makes command-based code click.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/) (especially methods).

## What you'll learn

- The difference between *calling* a function and *passing* a function.
- How to pass a function with a method reference or a lambda.
- The rules for capturing variables in a Java lambda.

## Passing vs. calling

Calling a function runs its code now. **Passing** a function hands it to other
code to run *later*. Seeing a function's name in code doesn't always mean it runs
right then — `Commands.runOnce(...)` builds a command and returns it; the function
inside only runs when the command is scheduled.

## Method references

If you already have a method with the right shape, refer to it with `::`:

```java
// Build a command that calls drivetrain.resetEncoders() when scheduled
Command resetCmd = Commands.runOnce(drivetrain::resetEncoders, drivetrain);
```

`runOnce` wants a `Runnable` — a function with **no parameters and no return
value** — so `resetEncoders()` must have that shape, or it won't compile.

## Lambda expressions

If you don't have a named method, write the function inline with a lambda:

```java
// One-line lambda: the brackets, return, and semicolon can be omitted
Command driveHalf = Commands.runOnce(() -> drivetrain.arcadeDrive(0.5, 0.0), drivetrain);
```

`() ->` is the (empty) parameter list; what follows is the body.

## Capturing variables

A lambda can use variables from the surrounding code (a "capture"). In Java you
can only capture variables that are **effectively final** (never reassigned). The
object a reference points to can still change its internal state — you just can't
repoint the reference. To capture a changing primitive, wrap it in an object.

## Steps & acceptance criteria

- [ ] Read the WPILib [Treating Functions as Data](https://docs.wpilib.org/en/stable/docs/software/basic-programming/functions-as-data.html)
      page.
- [ ] In a command-based example running in simulation, create an `InstantCommand`
      (via `Commands.runOnce`) using a **lambda** that prints a message, and bind it
      to a button. Confirm the message prints only when you press the button.
- [ ] Create a second command using a **method reference** to an existing method.
- [ ] Explain, in a comment, why the lambda body does **not** run at the line where
      it's written.

## Resources

- [WPILib: Treating Functions as Data](https://docs.wpilib.org/en/stable/docs/software/basic-programming/functions-as-data.html)
- [WPILib: Command-based programming](https://docs.wpilib.org/en/stable/docs/software/commandbased/index.html)

## Notes

- Common functional interfaces you'll meet: `Runnable` (no args, no return),
  `Supplier<T>` (no args, returns a value), `Consumer<T>` (takes a value, no
  return), and `BooleanSupplier` (used by triggers).
