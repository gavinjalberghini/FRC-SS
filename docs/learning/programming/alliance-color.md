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

## Description

A lot of robot behavior depends on which alliance you are on:
field-oriented driving, which AprilTags you trust, which auto side
you load, LED color, even which human-player station you face.
WPILib exposes this through `DriverStation.getAlliance()`. The
catch: the color **is not known until the Driver Station has told
the robot**, so the API returns an `Optional`. There are three
cases — red, blue, and not-yet — and code that only handles two of
them will pick a silent default in the pit and a surprising one on
the field.

You now have axes from [the coordinate system ticket](../coordinate-system/)
and delayed execution from
[Commands as Functions](../commands-as-functions/). This ticket is
the other "do not do it in the constructor" lesson. Caching
alliance in `robotInit()` is how field-relative drive works in the
shop (you set blue on the DS) and inverts the wrong way at a
regional (FMS assigns red after you already cached). The next
ticket, [Tunable Config](../configuration/), is about numbers you
*should* store. Alliance is not one of them.

The easy mistakes: calling `ally.get()` without `isPresent()`;
assuming `robotInit` is late enough; inverting odometry *and*
driver input *and* the path, then calling it "alliance handling."
Invert one documented frame, on purpose, every loop.

You will prove the three branches in simulation and write the
answers in `frc-learning`. This site does not track the sim. A
mentor should see the three printouts.

## Prerequisites

- [Java Fundamentals](../java-fundamentals/) (methods, and ideally
  the Optional idea — if `Optional` is new, Oracle's
  [Optional is in the API docs](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html);
  you only need `isPresent` / `get` / `orElse` here).
- [Commands as Functions](../commands-as-functions/) so you are not
  also fighting lambdas.
- [The Field Coordinate System](../coordinate-system/) so "invert
  driver X/Y on red" means something.

## What you'll learn

- How to read alliance color and handle red, blue, and unknown.
- When the value is available (`autonomousInit` / `teleopInit`,
  and again every loop if you drive field-relative) and when it
  is not (constructors, `robotInit`).
- How this connects to a fixed blue field origin.

## Reading the alliance color

`getAlliance()` returns an `Optional<Alliance>`. Handle all three
cases:

```java
Optional<Alliance> ally = DriverStation.getAlliance();
if (ally.isPresent()) {
  if (ally.get() == Alliance.Red) {
    // red action
  } else if (ally.get() == Alliance.Blue) {
    // blue action
  }
} else {
  // no color yet — pick a safe default and do not pretend you know
}
```

A slightly tighter shape, once you are comfortable with
`Optional`:

```java
boolean red = DriverStation.getAlliance()
    .orElse(Alliance.Blue) == Alliance.Red;
```

That still **chooses a default** when unknown. Make the default
explicit in a comment. "Pretend we are blue until FMS speaks" is
a team decision, not a hidden `orElse`.

## Timing matters

- The color is **not** available in constructors or reliably in
  `robotInit()`. Do not assume it there.
- It **is** typically available by `autonomousInit()` and
  `teleopInit()`.
- It can **change** (or appear to) before you connect to the
  field. When field-relative drive depends on it, re-read it
  **every loop** rather than caching once in a field.
- At a competition the Field Management System sets alliance.
  Off the field, you choose it on the Driver Station Operation
  tab. Simulation has the same control.

Official page:
[Get Alliance Color](https://docs.wpilib.org/en/stable/docs/software/basic-programming/alliancecolor.html).

## Tasks

1. **Read the WPILib page.** Read
   [Get Alliance Color](https://docs.wpilib.org/en/stable/docs/software/basic-programming/alliancecolor.html)
   and skim
   [Driver Station](https://docs.wpilib.org/en/stable/docs/software/driverstation/index.html)
   enough to find the Operation tab's alliance control. In
   `wpilib/alliance-color.md`, write when you would *not* call
   `getAlliance()` and what you do instead.

2. **Print three branches in simulation.** In your command-based
   sim project, add code that prints a different message for red,
   blue, and "no color yet." Put the read in `teleopPeriodic` or
   a default command — not in a constructor. Use the Driver
   Station / sim GUI to set alliance. Capture all three lines of
   output in the notes (unknown may require reading once at
   startup before the DS is connected, or logging from
   `robotInit` on purpose for this experiment).

3. **Prove the early-read trap.** Temporarily read alliance in a
   constructor or at the top of `robotInit` and print the
   Optional. Confirm you can see empty / unknown if you start the
   robot code before the DS alliance is applied. Then **remove**
   that constructor read so it does not ship as "the" alliance.
   Write one paragraph: what you saw, and where the read lives
   now.

4. **Write the field-origin plan.** In the same markdown file,
   answer:

   - We use a fixed blue field origin (PathPlanner / Choreo
     default). The driver wants "push stick away from you" to
     mean "away from the driver station wall." What do you invert
     on red, and what do you leave alone?
   - Name one other feature (LEDs, auto chooser, vision tag
     filter) that should key off alliance, and whether it may be
     read once in `teleopInit` or must be re-read every loop.

5. **Open a pull request** with the notes and the sim Java. Ask
   a mentor to look at the three printouts and the field-origin
   answer.

## Acceptance Criteria

- [ ] `wpilib/alliance-color.md` states when `getAlliance()` is
      not valid and what a safe unknown default means on this
      team.
- [ ] Simulation output (pasted) shows three distinct messages:
      red, blue, and unknown / empty Optional.
- [ ] You demonstrated an early read that was empty or wrong,
      then moved the real read out of the constructor. The
      paragraph is in the notes.
- [ ] The field-origin question has a written answer that
      inverts driver field-relative input (or an equivalent
      documented approach), not "invert everything."
- [ ] A second feature (LEDs, auto, vision) is named with a
      once-versus-every-loop choice.
- [ ] A pull request is open or was merged after review.

## Resources

- [WPILib: Get Alliance Color](https://docs.wpilib.org/en/stable/docs/software/basic-programming/alliancecolor.html)
- [WPILib: Driver Station](https://docs.wpilib.org/en/stable/docs/software/driverstation/index.html)
- [WPILib: Coordinate System](https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html)
- [PathPlanner: GUI getting started](https://pathplanner.dev/gui-getting-started.html)
  — field origin used by paths
- [Java 17: Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html)

## Notes

- At a competition FMS sets alliance. In the shop you set it.
  Forgetting to set it in the shop looks like "unknown" or a
  stale default — not like a CAN fault.
- Combine this with [the coordinate system](../coordinate-system/)
  to invert driver X/Y on red when the field origin is blue.
  Do not invert the path file *and* the odometry *and* the stick
  unless a mentor has walked the frames with you.
- Next: [Tunable Config](../configuration/) — units, Preferences,
  and deploy files. Those *are* safe to set early. Alliance is
  not.
