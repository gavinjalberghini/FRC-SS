---
layout: cad-lesson
title: Onshape Fundamentals
subtitle: Part studios, plates, and assemblies — the core CAD skills, built around FRC-relevant exercises.
permalink: /learning/cad/onshape-fundamentals/
role: designer
order: 2
size: 3
time: "Self-paced (multi-week)"
---

## Description

This is the largest ticket in the CAD track and the foundation for everything
after it. You will learn sketching, part modeling, multi-part modeling, and
assemblies by doing FRC-relevant exercises — box tubes, gussets, motor plates,
rivets, and a swerve frame — not by watching a generic CAD tour.

The work lives in **Stage 1A** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage1/1a/section1-setup/).
This ticket teaches the Onshape ideas those pages assume, then sends you to
the exact section and exercise pages. Do the exercises **in order**. Each one
expects the previous one. FRCDesign wants you to experiment until a feature
"works"; that is the pedagogy, not a missing instruction.

Three habits matter more than any single tool:

- **Fully constrained sketches.** A sketch is done when every line and
  circle is black, not blue. Blue geometry can drag later and silently move
  a hole. Dimensions and constraints (coincident, equal, horizontal, tangent,
  midpoint) lock intent. The origin and construction lines are references,
  not decoration.
- **Part studios vs assemblies.** You model custom parts next to each other
  in a **part studio**, referencing faces and edges so holes line up. You
  then insert those parts, plus buyable COTS parts from FRCDesignLib, into
  an **assembly** and **mate** them. A fastened mate is a bolt. A revolute
  mate is a pivot. Do not try to "assemble" inside a part studio by
  overlapping solids.
- **No overlapping solids.** If two tubes occupy the same volume in CAD,
  they collide on the robot. Extrude as **New** when you mean a second part.
  **Add** merges bodies. That one dropdown is the most common beginner
  mistake in Stage 1A.

Box tube is the structural language of FRC. From the side it is a rectangle.
Sizes are spoken as **1×1**, **2×1**, and **2×2**. The workflow is always
sketch the rectangle, **extrude** it as a solid, then run **Tube Converter**
to hollow it and punch the standard hole pattern. Never draw both sides of a
symmetric frame by hand — **mirror** across construction lines through the
origin.

This site does not track whether you finished. Copy the Stage 1A document
into **your** Onshape account and keep it there. Mentors review a share
link, not a progress bar on this website.

## Prerequisites

- [Getting Started with Onshape](../getting-started/) completed (Education
  account, FRCDesignApp, and the named FeatureScripts).
- Tube Converter must already appear on your toolbar. Exercise 1 uses it.

## What you'll learn

- How to orbit, pan, and zoom a part studio, and how folders and tabs
  organize a copied exercise document.
- How sketches, constraints, and dimensions capture design intent, and why
  black geometry is the goal.
- How to model box-tube frames with sketch → extrude → Tube Converter, and
  how to add plates and gussets that reference those tubes.
- How assemblies, fastened mates, and FRCDesignLib fasteners turn a studio
  into something a shop could build.

## Tasks

1. **Copy the Stage 1A document.** Open
   [1A: Introduction and Setup](https://frcdesign.org/learning-course/stage1/1a/section1-setup/).
   Read the box-tube intro. Use the **Stage 1A Document** button on that
   page and copy the document into your account (the page includes a short
   copy tutorial). Rename the copy something like
   `Stage 1A — YourName`. All Section 1–3 exercises happen inside this copy.
   Do not model in the public original.

2. **Learn the view and the tabs.** Complete
   [Exercise 0: Navigation](https://frcdesign.org/learning-course/stage1/1a/section1-exercise0/)
   in your copy. Right-drag orbits, middle-drag or Ctrl+right-drag pans,
   scroll zooms, and the view cube snaps to a face. Open the Section 1
   folder and confirm you can find the Exercise 1 part studio. A part
   studio, an assembly, and a drawing are different **tab types** in the
   same document.

3. **Do every Section 1 exercise in order.** Use the next-page arrows on
   FRCDesign, not a skip list. In your copied document:

   - [Exercise 1: First Tubes](https://frcdesign.org/learning-course/stage1/1a/section1-exercise1/)
     — Sketch a rectangle, extrude it as **New**, run Tube Converter.
     Change length and watch the tube follow.
   - **Exercise 2: More Tubes (cross rails).** Add cross rails. Pick the
     extrude end condition so parts land in the right place. Change part
     **appearance**. Confirm tubes do not overlap.
   - **Exercise 3: Sketch Basics.** Practice constraints and dimensions
     until the sketch turns black. If a line stays blue, you are missing a
     coincident, equal, or dimension — do not leave it.
   - **Exercise 4: Drivetrain Frame.** Sketch and extrude a full drivetrain
     frame, then tube-convert it. **Mirror across both X and Y** using
     construction lines through the origin. Do not draw both sides by hand.
     Avoid over-dimensioning; symmetry should close the sketch.
   - **Exercise 5: Box Frame.** Build a rectangular box frame.
   - **Exercise 6: Triangle Frame.** Build an angled / triangular frame so
     non-orthogonal geometry is not a surprise later.

   After each studio, name the parts (`Left rail`, `Front cross`, not
   `Part 3`). Orbit the model and look for overlapping solids.

4. **Do every Section 2 (plates) exercise.** Start at
   [Exercise 1: Plate Workflow](https://frcdesign.org/learning-course/stage1/1a/section2-exercise1/).
   A plate exists to put holes where you need them; the outline is the
   string you wrap around those holes. The workflow is: holes first
   (bearings, bolts, motor patterns), then center-point arcs and tangent
   lines for the perimeter.

   - [Exercise 1: Plate Workflow](https://frcdesign.org/learning-course/stage1/1a/section2-exercise1/)
     — A simple two-bearing plate.
   - [Exercise 2: Gusset](https://frcdesign.org/learning-course/stage1/1a/section2-exercise2/)
     — A gusset that joins two tubes. Use **Use / Project** (`U`) to copy
     holes from the tube. Do **not** use a gusset FeatureScript; the point
     is the plate workflow.
   - [Exercise 3: Superstructure Gussets & Plate](https://frcdesign.org/learning-course/stage1/1a/section2-exercise3/)
     — Several gussets plus a large plate. Use **linear pattern** and
     **mirror**; project at most one hole per tube.
   - [Exercise 4: Motor Mounting](https://frcdesign.org/learning-course/stage1/1a/section2-exercise4/)
     — A plate with the CIM-class 2" bolt circle and 1.25" boss clearance.

5. **Do every Section 3 (assemblies) exercise.** Start at
   [Exercise 1: Rivets](https://frcdesign.org/learning-course/stage1/1a/section3-exercise1/).
   Insert parts from the studio, then insert COTS hardware from
   FRCDesignLib. A **fastened mate** locks two mate connectors together.

   - [Exercise 1: Rivets](https://frcdesign.org/learning-course/stage1/1a/section3-exercise1/)
     — Fasten rivets through gusset holes.
   - [Exercise 2: Swerve Drive](https://frcdesign.org/learning-course/stage1/1a/section3-exercise2/)
     — Insert and mate an MK4i module. Use **Replicate** for rivets and
     a circular pattern for modules.
   - [Exercise 3: Gusset Setup](https://frcdesign.org/learning-course/stage1/1a/section3-exercise3/)
     — Model the remaining gusset that the next assembly needs.
   - **Exercise 4: Full Frame.** Assemble the complete drivetrain frame.
   - **Exercise 5: Finishing the Frame.** Final fasteners, checks, and
     cleanup so the drivebase looks like something you would send to a
     mentor, not a pile of unnamed instances.

6. **Sanity-check and write one design note.** Orbit every finished studio
   and assembly. Sketches should be black. Parts should be named. Solids
   should not overlap. In a short note (a few sentences in the share
   comment, or a text tab in the document), answer: *Where did you use
   mirror or pattern instead of redrawing, and why does that matter when
   the frame width changes?*

7. **Hand it to a mentor.** Share `Stage 1A — YourName` (Onshape **Share**,
   view or comment) or export screenshots of the finished Section 3 frame
   plus one fully constrained sketch. If your team exported these tickets,
   paste the link on this issue and move it to In Review.

## Acceptance Criteria

- [ ] A copy of the Stage 1A document exists in your Onshape account and a
      mentor has a shareable link (or equivalent screenshots).
- [ ] Section 1 Exercises 0–6, Section 2 Exercises 1–4, and Section 3
      Exercises 1–5 are complete in that copy, in order.
- [ ] Sketches that define parts are fully constrained (black geometry).
- [ ] No overlapping solids where two tubes or plates occupy the same
      volume.
- [ ] Custom parts have readable names, not `Part 1` / `Part 2`.
- [ ] A short written note explains one use of mirror or pattern and why
      you chose it.

## Resources

- [Stage 1A setup (copy the document here)](https://frcdesign.org/learning-course/stage1/1a/section1-setup/)
- [Exercise 0: Navigation](https://frcdesign.org/learning-course/stage1/1a/section1-exercise0/)
- [Exercise 1: First Tubes](https://frcdesign.org/learning-course/stage1/1a/section1-exercise1/)
- [Section 2 Exercise 1: Plate Workflow](https://frcdesign.org/learning-course/stage1/1a/section2-exercise1/)
- [Section 2 Exercise 2: Gusset](https://frcdesign.org/learning-course/stage1/1a/section2-exercise2/)
- [Section 2 Exercise 3: Superstructure Gussets](https://frcdesign.org/learning-course/stage1/1a/section2-exercise3/)
- [Section 2 Exercise 4: Motor Mounting](https://frcdesign.org/learning-course/stage1/1a/section2-exercise4/)
- [Section 3 Exercise 1: Rivets](https://frcdesign.org/learning-course/stage1/1a/section3-exercise1/)
- [Section 3 Exercise 2: Swerve Drive](https://frcdesign.org/learning-course/stage1/1a/section3-exercise2/)
- [Section 3 Exercise 3: Gusset Setup](https://frcdesign.org/learning-course/stage1/1a/section3-exercise3/)
- [Using the Tube Converter FeatureScript](https://onshape4frc.com/blog/using-tube-converter/)
- [Onshape Learning Center](https://learn.onshape.com/)
- [Onshape Fundamentals pathway](https://learn.onshape.com/learn/learning-path/onshape-fundamentals)
- [Getting Started with Onshape](../getting-started/)

## Notes

- A fully constrained sketch will not drift when a teammate edits a nearby
  dimension. Blue geometry is unfinished work.
- Always sanity-check against real life: overlapping tubes in CAD become a
  collision on the robot.
- Use symmetry (mirror / pattern) instead of redrawing. It is faster today
  and editable in week six.
- If Tube Converter or FRCDesignLib is missing, stop and return to
  [Getting Started](../getting-started/). Do not reinvent box tube by
  shelling a block by hand.
- The next ticket ([Power Transmission](../power-transmission/)) is Stage
  1B: motors, shafts, gears, belts, and three gearbox exercises.
