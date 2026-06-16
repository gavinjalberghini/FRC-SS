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

## Overview

The autonomous period is worth a lot of points, and it all comes down to a robot
following planned paths on its own. Two tools dominate FRC autonomous path design:
**PathPlanner** and **Choreo**. This lesson introduces both so you can choose the
right one and build a working path.

## Prerequisites

- [Code a Robot](../code-a-robot/) — you'll integrate paths into a real drivetrain.

## What you'll learn

- The core concepts shared by path-planning tools.
- How to build a path and an auto in PathPlanner.
- How to build a trajectory in Choreo and when to prefer it.

## Steps & acceptance criteria

- [ ] In **PathPlanner**, read the relevant docs and understand what each of these
      does and when to use it:
  - [ ] Waypoints
  - [ ] Event markers
  - [ ] Rotation targets
  - [ ] Global constraints
  - [ ] Constraint zones
  - [ ] The path optimizer
  - [ ] The difference between a *path* and an *auto*
- [ ] Create a path and an auto in PathPlanner that use all of the features above.
      (It doesn't have to accomplish anything specific.)
- [ ] In **Choreo**, read the relevant docs and understand:
  - [ ] Pose, translation, and empty waypoints
  - [ ] Constraint zone types (max velocity vs. acceleration; angular acceleration; stop points)
  - [ ] Event markers
  - [ ] Generating and saving paths
- [ ] Create a path in Choreo that uses all of the features above.

## PathPlanner vs. Choreo

- **PathPlanner** is great for quickly laying out human-friendly paths and full
  autonomous routines (autos) with event markers and named commands.
- **Choreo** generates time-optimal trajectories using a solver, which can squeeze
  out extra performance for tightly constrained motions.
- Many teams use both — and PathPlanner can even consume Choreo trajectories.

## Resources

- [PathPlanner documentation](https://pathplanner.dev/home.html)
- [PathPlanner: editing paths & autos](https://pathplanner.dev/gui-editing-paths-and-autos.html)
- [Choreo documentation](https://choreo.autos/)
- [Choreo: editing paths](https://choreo.autos/usage/editing-paths/)

## Notes

- Build your autonomous early and test it often — auto bugs are hard to spot the
  morning of a competition.
