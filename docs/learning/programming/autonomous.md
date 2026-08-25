---
layout: lesson
title: Autonomous Paths
subtitle: Design autonomous routines with PathPlanner and Choreo.
permalink: /learning/programming/autonomous/
role: veteran
order: 14
size: 2
time: "1–2 hrs"
---

## Description

The autonomous period is a lot of points and zero driver skill.
It is also where "we will tune it at the event" goes to die. Two
tools dominate FRC path design right now: **PathPlanner** (human-
friendly paths and full autos with named commands) and **Choreo**
(a solver that emits time-optimal trajectories). Many teams use
both — PathPlanner can even consume Choreo output.

You already followed a one-meter line in
[Code a Robot](../code-a-robot/). This ticket is how you design
routines that are more than a straight line: waypoints, rotation
targets, constraint zones, event markers, and the difference
between a *path* and an *auto*. The easy mistakes: one giant path
that cannot be reused; event markers that fire on the wrong
waypoint; ignoring bumpers when you hug a reef; never running
the auto with the same battery and floor you will see on Saturday.

This is the last veteran ticket. The lead track starts with
[Researching Robot Code](../researching-robot-code/) — other
teams' autos are one of the first things you will steal
ideas from, so you need the vocabulary here first.

You will build a PathPlanner auto that uses the listed features,
and a Choreo path that uses that tool's equivalents. They do not
have to win a regional. They do have to exist as files a mentor
can open, plus a short write-up in `frc-learning`. Hardware time
is bonus if the robot is still available; the ticket can be
signed on files plus a sim replay if a mentor agrees. This site
does not store `.auto` files.

## Prerequisites

- [Code a Robot](../code-a-robot/) — you have generated swerve
  and followed at least one path on a real drivetrain (or a
  mentor-signed exception if the robot was down — say so in
  the notes).
- PathPlanner and Choreo installed. Start at
  [pathplanner.dev](https://pathplanner.dev/home.html) and
  [choreo.autos](https://choreo.autos/).
- [Tunable Config](../configuration/) so you know why those
  files live under deploy.

## What you'll learn

- Shared ideas: waypoints, constraints, events, and "path
  versus auto."
- How to build a PathPlanner path *and* an auto that uses
  markers, rotations, global constraints, a zone, and the
  optimizer.
- How to build a Choreo trajectory with pose/translation
  waypoints, constraint types, and events — and when you
  would pick the solver over drawing.

## PathPlanner versus Choreo

- **PathPlanner** is fast for human-shaped paths and for
  stitching a full autonomous routine (an *auto*) out of
  paths plus named commands (intake, shoot, wait).
- **Choreo** generates time-optimal trajectories with a
  solver. It shines when the motion is tightly constrained
  (arrive here, stopped, facing that heading, as fast as
  physics allows).
- Many teams draw structure in one tool and polish in the
  other. Read both docs before you pick a religion.

Official starting points:

- [PathPlanner: editing paths and autos](https://pathplanner.dev/gui-editing-paths-and-autos.html)
- [Choreo: editing paths](https://choreo.autos/usage/editing-paths/)

Field origin is still the one you wrote down in
[the coordinate system ticket](../coordinate-system/) and
[alliance color](../alliance-color/). A beautiful auto that
assumes the wrong origin is a taxi into the opposing barge.

## PathPlanner ideas you must be able to explain

Read the editing-paths page and click through the GUI until
these are not just words:

- **Waypoints** — poses the robot should pass through or
  stop at. The path is not "the line you see" if the holonomic
  rotation is independent.
- **Event markers** — "at this point along the path, run this
  named command." Wrong placement is an intake that opens in
  the other alliance's zone.
- **Rotation targets** — holonomic heading separate from the
  translation spline.
- **Global constraints** — max velocity / acceleration the
  whole path respects unless a zone overrides them.
- **Constraint zones** — slower (or different) limits on a
  stretch (near a game piece, near a wall).
- **Path optimizer** — PathPlanner's pass that reshapes the
  path under constraints. Run it, then look at the result;
  do not assume the first draw is what the robot will do.
- **Path versus auto** — a path is a trajectory. An auto is
  a sequence: paths, named commands, waits, decisions. You
  need both.

## Choreo ideas you must be able to explain

From [editing paths](https://choreo.autos/usage/editing-paths/)
and the rest of the Choreo usage docs:

- **Pose, translation, and empty waypoints** — when the
  solver may choose heading versus when you lock a full pose.
- **Constraint zone types** — max velocity versus
  acceleration, angular acceleration, stop points. These are
  not the same knob.
- **Event markers** — same job as PathPlanner's, different
  UI.
- **Generate and save** — a Choreo path you never generated
  is a drawing. Save where the robot project will actually
  load it (deploy / vendor instructions).

## Tasks

1. **Read PathPlanner.** Read
   [home](https://pathplanner.dev/home.html),
   [editing paths and autos](https://pathplanner.dev/gui-editing-paths-and-autos.html),
   and
   [library getting started](https://pathplanner.dev/pplib-getting-started.html).
   In `auto/pathplanner-notes.md`, write one or two sentences
   for each feature in the list above (waypoints through
   path-versus-auto). Use your own words. Cite the heading
   you used if you need to look it up again.

2. **Build a PathPlanner path and an auto.** Create a path
   that uses **all** of: multiple waypoints, a rotation
   target, a global constraint you changed from default, a
   constraint zone, an event marker, and a pass through the
   optimizer. Create an **auto** that includes that path plus
   at least one named command or wait so it is not only a
   single path. Commit the `.path` / `.auto` files (and the
   project settings that name the robot size) into the robot
   repo or into `frc-learning/auto/pathplanner/`. Screenshot
   the GUI into `auto/pathplanner/`.

3. **Read Choreo.** Read
   [Choreo documentation](https://choreo.autos/) and
   [editing paths](https://choreo.autos/usage/editing-paths/).
   In `auto/choreo-notes.md`, write one or two sentences
   each for: pose versus translation versus empty waypoints;
   the constraint types listed above; event markers;
   generate-and-save.

4. **Build a Choreo path.** Create a trajectory that uses
   those waypoint types, at least two constraint kinds, an
   event marker, and a successful generate/save. Commit the
   saved file and a GUI screenshot to
   `frc-learning/auto/choreo/` (or the robot deploy folder
   with a pointer in the notes).

5. **Write the choice.** In `auto/README.md`, answer: for
   *this* team's next real auto, would you start in
   PathPlanner, Choreo, or both, and why? Name one risk of
   your choice (for example, "solver will ignore the pretty
   line I drew" or "hand-drawn path will leave time on the
   table").

6. **Run something if the robot is up.** If you still have
   the Code a Robot drivetrain, run either the PathPlanner
   auto in sim
   ([WPILib simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html))
   or a short hardware replay. Write the result. If the
   robot is not available, say so; a mentor can still sign
   the files.

7. **Open a pull request** with the notes, screenshots, and
   path files. If the team exported this ticket, attach the
   PR.

## Acceptance Criteria

- [ ] `auto/pathplanner-notes.md` defines waypoints, event
      markers, rotation targets, global constraints,
      constraint zones, the optimizer, and path versus auto
      in your own words.
- [ ] A PathPlanner path file uses all of those features
      (optimizer run included). Screenshots are in the repo.
- [ ] A PathPlanner auto file sequences that path with at
      least one named command or wait.
- [ ] `auto/choreo-notes.md` covers waypoint kinds,
      constraint types, events, and generate/save.
- [ ] A generated Choreo trajectory is saved in the repo
      with a screenshot.
- [ ] `auto/README.md` picks a starting tool for the team's
      next auto and names a risk.
- [ ] A pull request is open or was merged after review.

## Resources

- [PathPlanner documentation](https://pathplanner.dev/home.html)
- [PathPlanner: editing paths and autos](https://pathplanner.dev/gui-editing-paths-and-autos.html)
- [PathPlanner: library getting started](https://pathplanner.dev/pplib-getting-started.html)
- [Choreo documentation](https://choreo.autos/)
- [Choreo: editing paths](https://choreo.autos/usage/editing-paths/)
- [WPILib: Robot Simulation](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/introduction.html)
- [WPILib: Coordinate System](https://docs.wpilib.org/en/stable/docs/software/basic-programming/coordinate-system.html)
- [CTRE Phoenix 6 examples](https://github.com/CrossTheRoadElec/Phoenix6-Examples)
  — swerve + PathPlanner / Choreo samples

## Notes

- Build autonomous early and test it often. Auto bugs hide
  until the field is carpet and the battery is tired.
- Named commands in an auto must exist in code. A marker
  that calls `intake` when no `intake` command is registered
  is a silent no-op or a crash — read the lib getting-started
  page for how your version registers names.
- Bumper size in the GUI is not decoration. Wrong bumpers
  make every "near the reef" zone a lie.
- Veteran track ends here. Lead track starts at
  [Researching Robot Code](../researching-robot-code/).
