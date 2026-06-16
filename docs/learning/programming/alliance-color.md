---
layout: lesson
title: Match State & Alliance Color
subtitle: Read the alliance color safely and act on it during a match.
permalink: /learning/programming/alliance-color/
role: veteran
order: 10
size: 1
time: "~30 min"
---

## Overview

Lots of robot behavior depends on which alliance you're on — field-oriented
driving, which AprilTags to expect, autonomous side, LED colors, and more. WPILib
exposes this through `DriverStation.getAlliance()`. The catch: the color **isn't
known until the Driver Station connects**, so your code has to handle the
"no color yet" case.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/) and [Commands as Functions](../commands-as-functions/).

## What you'll learn

- How to read the alliance color.
- Why it returns an `Optional`, and how to handle all three cases.
- When the alliance color is (and isn't) available.

## Reading the alliance color

`getAlliance()` returns an `Optional<Alliance>` — there are **three** cases to
handle: red, blue, and not-known-yet:

```java
Optional<Alliance> ally = DriverStation.getAlliance();
if (ally.isPresent()) {
  if (ally.get() == Alliance.Red) {
    // red action
  } else if (ally.get() == Alliance.Blue) {
    // blue action
  }
} else {
  // no color yet — pick a safe default
}
```

## Timing matters

- The color is **not** available in constructors or `robotInit()` — don't assume
  it there.
- It **is** typically available by `autonomousInit()` / `teleopInit()`.
- It can **change** (or appear to) before you connect to the field, so when you
  rely on it for driving, re-check it **every loop** rather than caching it once.

## Steps & acceptance criteria

- [ ] Read the WPILib [Get Alliance Color](https://docs.wpilib.org/en/stable/docs/software/basic-programming/alliancecolor.html)
      page.
- [ ] In a simulation project, set your alliance on the Driver Station **Operation**
      tab, then print a different message for red, blue, and "no color yet."
- [ ] Confirm the "no color yet" branch runs if you read the alliance too early
      (e.g. in the constructor) — then move the read to `teleopInit()` and confirm
      it reports the correct color.

## Resources

- [WPILib: Get Alliance Color](https://docs.wpilib.org/en/stable/docs/software/basic-programming/alliancecolor.html)
- [WPILib: Driver Station](https://docs.wpilib.org/en/stable/docs/software/driverstation/index.html)

## Notes

- At a competition the Field Management System sets your alliance automatically;
  off the field, you choose it in the Driver Station.
- Combine this with the [Coordinate System](../coordinate-system/) lesson to invert
  driver X/Y when you're on the red alliance using a fixed blue field origin.
