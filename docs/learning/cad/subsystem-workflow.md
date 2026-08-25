---
layout: cad-lesson
title: Subsystem Workflow
subtitle: Package the battery, electronics, bellypan, and bumpers into a finished drivebase.
permalink: /learning/cad/subsystem-workflow/
role: veteran
order: 6
size: 2
time: "2–3 hrs"
---

## Description

A drivetrain is not done when the frame exists. It needs a battery, a
control system, a bellypan those things mount to, and bumpers that satisfy
the game manual. This ticket applies the Stage 1D top-down workflow to
**finishing** the drivebase you already started — the last Designer /
early Veteran step before Stage 2 mechanisms.

This is **Stage 1E** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage1/1e/introduction/).
You keep working in your `Stage 1D Robot` document (or a copy). The
battery holder and electronics do not re-sketch the whole robot; they
reference parts that already reference the layout, so a frame change still
propagates.

The subsystem workflow FRCDesign wants you to feel in your hands:

1. Layout sketches in the layout studio.
2. Derive them into the subsystem part studio.
3. Model structure (tubes, plates) from that derive.
4. Insert into the subsystem assembly, group, fasten Origin Cube to the
   origin, then finish hardware.
5. Insert that assembly into the top-level robot.
6. Come back and **detail** — battery, electronics, pocketing, bumpers —
   without abandoning the origin or the group.

Detailing is where robots actually get used. A beautiful frame you cannot
wire, cannot swap a battery in 30 seconds, or cannot bumper-color-swap
between finals is not a finished subsystem.

Constraints that are easy to forget in CAD:

- The battery is about 13 lb. Low and centered wins tip-resistance. A
  strap that can be opened with gloves matters as much as the plate.
- Electronics (PDH/PDP, main breaker, RoboRIO or SystemCore, radio, motor
  controllers) need reach, wire routes, and inspection access. Work with
  an electrician, not around them.
- Bellypan pocketing can save several pounds and cost hours of machining
  (or fab-house dollars). It is optional on purpose.
- Bumper rules (height, coverage, corner protection, construction, color)
  change every year. Model to the **current**
  [FRC game manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system),
  not last season's memory.

This site does not track whether you finished. Your Onshape document lives
in your account. Mentors review a share link.

## Prerequisites

- [Top-Down Design Methodology](../design-methodology/) completed. You
  need the Stage 1D layout, drivetrain studio, and assemblies to detail.
- A current-season game manual tab open when you model bumpers.

## What you'll learn

- The six-step subsystem workflow, by adding details to a drivebase you
  already own.
- How to package a battery and a control system so they are low, serviceable,
  and legal.
- How pocketing trades weight against manufacturing time.
- How to model bumpers and a mounting scheme as their own studio and
  assembly so they can be hidden in the top-level robot.

## Tasks

1. **Read the workflow and project overview.** Open
   [Subsystem Workflow Introduction](https://frcdesign.org/learning-course/stage1/1e/introduction/)
   and
   [Project Overview](https://frcdesign.org/learning-course/stage1/1e/project-overview/).
   Confirm you are detailing **your** Stage 1D document (make a copy named
   `Stage 1E — YourName` if you want to keep a clean 1D snapshot). Use the
   1E reference document on the overview page as a visual target, not as
   something to insert and call finished.

2. **Exercise 1 — Battery holder.** Read
   [Battery Mounting](https://frcdesign.org/learning-course/stage1/1e/battery-mounting/)
   and complete
   [Exercise 1: Battery Holder](https://frcdesign.org/learning-course/stage1/1e/exercise1/).
   Place the battery low on the bellypan. Model a holder that locks it and
   still allows a fast match swap (strap cutout, not a bolted lid). Name
   the plate and spacers; assign materials; insert the battery from
   FRCDesignLib.

3. **Exercise 2 — Mounting electronics.** Read
   [Electronics](https://frcdesign.org/learning-course/stage1/1e/electronics/)
   and complete
   [Exercise 2: Mounting Electronics](https://frcdesign.org/learning-course/stage1/1e/exercise2/).
   Lay out PDH, main breaker, RoboRIO (or the current controller the page
   uses), and an IMU so everything is reachable and wires have a path to
   the battery and breaker. The Electronic Mounting FeatureScript is
   allowed here. Fasteners and hole sizes are on that exercise page — use
   them. Leave service clearance; do not sit the radio under a bellypan
   you cannot reach.

4. **Exercise 3 — Bellypan pocketing.** Complete
   [Exercise 3: Bellypan Pocketing](https://frcdesign.org/learning-course/stage1/1e/exercise3/).
   Pocket with Part Lighten (or Vent) using a diamond rib pattern. Keep
   material under mounts and along load paths. If your team would not
   machine this bellypan, still do the exercise — then write why you would
   skip it on a real robot.

5. **Exercise 4 — Bumpers.** Complete
   [Exercise 4: Bumpers](https://frcdesign.org/learning-course/stage1/1e/exercise4/).
   Add a bumper profile to the main layout (the page recommends 3/4"
   ground clearance and a 1/4" frame gap as a starting point — check this
   year's manual). New part studio and assembly in the drivetrain folder;
   derive the layout; sweep a block bumper. Insert that assembly into the
   drivetrain so it can be hidden as one unit.

6. **Exercise 5 — Bumper mounting.** Complete
   [Exercise 5: Bumper mounting](https://frcdesign.org/learning-course/stage1/1e/exercise5/)
   (follow the next-page arrow from Exercise 4 if the title differs
   slightly). Design a mount that is secure in a hit and quick to remove
   for an alliance-color swap. If the current manual changed bumper
   construction, model to the manual and note the difference.

7. **Write one design note and share.** In a few sentences pick one:
   *battery location*, *electronics access*, or *pocketing vs solid
   bellypan* — and defend the choice against weight, rules, or pit-lane
   time. Share the document (or screenshots of the finished drivebase:
   frame, modules, battery, electronics, bellypan, bumpers) with a mentor.
   If your team exported these tickets, paste the link and move the issue
   to In Review.

## Acceptance Criteria

- [ ] A shareable Onshape document contains the detailed Stage 1E
      drivebase (your 1D document or a named 1E copy).
- [ ] Exercises 1–5 are complete: battery holder, electronics, bellypan
      pocketing, bumpers, and bumper mounting.
- [ ] Layout-driven sketches are fully constrained; new parts are named;
      no overlapping solids (battery through the bellypan, bumpers through
      the frame, and so on).
- [ ] Electronics and battery are assembled with hardware, not floating
      in space.
- [ ] Bumpers live in their own studio/assembly and appear in the
      drivetrain or top-level assembly.
- [ ] A short written note defends one packaging choice (battery,
      electronics, or pocketing).

## Resources

- [Stage 1E introduction](https://frcdesign.org/learning-course/stage1/1e/introduction/)
- [Project Overview](https://frcdesign.org/learning-course/stage1/1e/project-overview/)
- [Battery Mounting](https://frcdesign.org/learning-course/stage1/1e/battery-mounting/)
- [Exercise 1: Battery Holder](https://frcdesign.org/learning-course/stage1/1e/exercise1/)
- [Electronics](https://frcdesign.org/learning-course/stage1/1e/electronics/)
- [Exercise 2: Mounting Electronics](https://frcdesign.org/learning-course/stage1/1e/exercise2/)
- [Exercise 3: Bellypan Pocketing](https://frcdesign.org/learning-course/stage1/1e/exercise3/)
- [Exercise 4: Bumpers](https://frcdesign.org/learning-course/stage1/1e/exercise4/)
- [Exercise 5: Bumper Mounting](https://frcdesign.org/learning-course/stage1/1e/exercise5/)
- [FRC game manual, Q&A, and field drawings](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [Onshape Learning Center](https://learn.onshape.com/)
- [Top-Down Design Methodology](../design-methodology/)

## Notes

- Read this season's bumper and electronics rules before you call the
  model done. Construction, height, and control-system hardware change.
- Service access is a real constraint. A package you cannot reach to reset
  a breaker is a bad package.
- Pocketing is optional on a competition bellypan. Doing the exercise is
  not optional; skipping it on a real robot is a team decision you should
  be able to explain.
- The next ticket ([Basic Shooter](../basic-shooter/)) is Stage 2A: your
  first full mechanism, with engineering concepts in front of the CAD.
