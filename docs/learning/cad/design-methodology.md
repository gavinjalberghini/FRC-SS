---
layout: cad-lesson
title: Top-Down Design Methodology
subtitle: Drive a whole project from a master layout sketch through part studios to a top-level assembly.
permalink: /learning/cad/design-methodology/
role: veteran
order: 5
size: 2
time: "2–3 hrs"
---

## Description

Up to now you have modeled parts and small mechanisms. This ticket teaches
the **workflow** that ties a whole robot together: **top-down design**.

In **bottom-up** design you model each part in isolation and assemble last.
That works for a single gusset. It fails for a robot, because the intake,
elevator, and drive must share space, origins, and mounting faces. In
**top-down** design you define the overall layout first and let parts
inherit from it. Change the layout, and everything downstream updates.
FRC teams use this because the layout is the single source of truth for
frame size, pivot points, and mechanism travel.

This is **Stage 1D** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage1/1d/top-down-design/).
You will create a new document (not only a copy), build a master layout
for a swerve drivebase, derive that layout into a drivetrain part studio,
assemble it, and drop the drivetrain plus a public scoring mechanism into
a top-level robot assembly.

The Onshape mechanics behind "top-down":

- A **main layout sketch** (sometimes called a master sketch) is a set of
  light, fully constrained sketches: side profile, top outline, wheel
  boxes, tube locations. It does *not* include every bolt hole.
- **Derive** brings those sketches into another part studio. Tube lengths
  and plate outlines reference the derived geometry, so a frame-width
  change is one dimension, not twenty.
- **Origin Cube** is the first feature in the layout studio, the drivetrain
  studio, and the assemblies. Fasten cube-to-origin and every document
  shares one point. That same point is what software teams export to
  AdvantageScope. CAD origin and code origin should match.
- A **top-level assembly** inserts subsystem assemblies (not loose parts)
  and mates *their* origin cubes. You are assembling robots from
  subsystems, the way the shop will.

If a number appears twice, you have already lost. Drive it from the layout
once.

This site does not track whether you finished. The `Stage 1D Robot`
document lives in your Onshape account. Mentors review a share link.

## Prerequisites

- [Practice Mechanisms](../practice-mechanisms/) completed (Stage 1C,
  including Origin Cube habits).
- You can copy or insert a public Onshape document by URL. Stage 1D's
  top-level assembly uses a linked 1678 scoring mechanism.

## What you'll learn

- The difference between top-down and bottom-up, and why FRC robots are
  laid out top-down.
- How to build a parametric main layout sketch (side + top) with Origin
  Cube and no redundant dimensions.
- How Derive, Extrude Individual, and Tube Converter turn that layout into
  named frame parts.
- How a drivetrain assembly and a top-level robot assembly stay aligned
  through origin-cube mates.

## Tasks

1. **Read the methodology page.** Open
   [Top Down Design](https://frcdesign.org/learning-course/stage1/1d/top-down-design/).
   Write two sentences you will hand to a mentor: *Top-down means …* and
   *We use one origin because …*.

2. **Create the document and the layout sketch.** Follow
   [Layout Sketch](https://frcdesign.org/learning-course/stage1/1d/layout-sketch/)
   in a **new** Onshape document named `Stage 1D Robot — YourName`. Create
   a part studio called `Main Layout Sketch`, insert Origin Cube first, and
   build the side and top layouts from the slides:

   - Side profile of the drive tubes, 1.75" off the ground for MK4i, plus
     the 4.625" wheel clearance box.
   - Top outline that *equals* the side-layout tube length (no second
     width dimension).
   - 2×1 outer tubes, 2×2 cross tube, and MK4i 4.25" corner offsets,
     patterned with a circular pattern.

   Name the sketches and folder them. They must be fully constrained.
   Notice the top sketch can be fully defined with **no** raw dimensions
   if it references the side sketch.

3. **Model the drivetrain part studio.** Follow
   [Part Studio](https://frcdesign.org/learning-course/stage1/1d/part-modeling/).
   New folder `Drivetrain`, new studio `Drivetrain`. Origin Cube first,
   then **Derive** the layout sketches. Extrude Individual + Tube Converter
   for the tubes (2×1 at 1/8" wall, 2×2 at 1/16" as the page specifies).
   Model the bellypan from the layout, fillet with Fillet All Edges, add
   patterned mounting holes. Set the bellypan material to Aluminum 6061.
   Name every part.

4. **Assemble the drivetrain.** Follow
   [Assembly](https://frcdesign.org/learning-course/stage1/1d/assembly-modeling/).
   Insert the studio, group the rigid parts with the Origin Cube, fasten
   the cube to the assembly origin. Insert simplified MK4i modules from
   FRCDesignLib, circular-pattern them, and rivet the bellypan. Leave the
   three holes per side empty for the gusset bolts in the next task. Name
   replicates and folder instances.

5. **Add the gussets and remaining hardware.** Follow
   [Adding More Components](https://frcdesign.org/learning-course/stage1/1d/adding-components/).
   Sketch a 1/8" gusset in the drivetrain studio (manually define holes or
   project only one, then pattern — do not chain every tube hole). Insert
   the new part, **edit the existing Group** so it stays where it was
   modeled. Add bolts through the reserved bellypan holes, rivet the
   gusset, mirror to the other side. Organize the instance tree.

6. **Build the top-level assembly.** Follow
   [Top Level Assembly](https://frcdesign.org/learning-course/stage1/1d/top-level-assembly/).
   New assembly `Top Level Robot Assembly`. Insert the drivetrain and
   fasten its origin cube to this assembly's origin. Insert the 1678 2023
   scoring mechanism from the document button / URL on that page and
   fasten *its* origin cube the same way. That is the whole trick.

7. **Write one design note and share.** In a few sentences: *If the drive
   side length changed by an inch, which sketches and features would
   update, and what did you refuse to hard-code so that would work?* Share
   `Stage 1D Robot — YourName` (or screenshots of the layout, drivetrain
   assembly, and top-level assembly) with a mentor. If your team exported
   these tickets, paste the link and move the issue to In Review.

## Acceptance Criteria

- [ ] A document you own (`Stage 1D Robot — YourName` or similar) is
      shareable with a mentor.
- [ ] `Main Layout Sketch` exists, starts with Origin Cube, and is fully
      constrained; the top outline is driven by the side layout rather than
      a second independent width.
- [ ] The drivetrain part studio derives that layout; tubes and bellypan
      are named; no overlapping solids.
- [ ] The drivetrain assembly is origin-cube-mated, with modules, rivets,
      and gussets organized into folders.
- [ ] A top-level assembly contains the drivetrain and the linked scoring
      mechanism, each fastened through its origin cube.
- [ ] A short written note explains one layout-driven choice and what
      would update if the frame size changed.

## Resources

- [Top Down Design](https://frcdesign.org/learning-course/stage1/1d/top-down-design/)
- [Layout Sketch](https://frcdesign.org/learning-course/stage1/1d/layout-sketch/)
- [Part Studio](https://frcdesign.org/learning-course/stage1/1d/part-modeling/)
- [Assembly](https://frcdesign.org/learning-course/stage1/1d/assembly-modeling/)
- [Adding More Components](https://frcdesign.org/learning-course/stage1/1d/adding-components/)
- [Top Level Assembly](https://frcdesign.org/learning-course/stage1/1d/top-level-assembly/)
- [Document Setup (multi-document robots)](https://frcdesign.org/best-practices/document-setup/)
- [Onshape Learning Center](https://learn.onshape.com/)
- [Practice Mechanisms](../practice-mechanisms/)

## Notes

- Resist redimensioning a part by hand. If a number appears twice, drive
  it from the layout once.
- The layout sketch is a planning tool as much as a CAD artifact. Sketch
  it before you commit to tube length or bellypan outline.
- FRCDesign's later stages split a real robot across several documents
  (concept, subsystems, main). Stage 1D stays in one document so you learn
  the references first. Read
  [Document Setup](https://frcdesign.org/best-practices/document-setup/)
  when you start a competition robot.
- The next ticket ([Subsystem Workflow](../subsystem-workflow/)) is Stage
  1E: battery, electronics, bellypan pocketing, and bumpers on this same
  drivebase.
