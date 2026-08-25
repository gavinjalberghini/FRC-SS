---
layout: cad-lesson
title: Cascade Elevator
subtitle: Model a cascade elevator with elevator blocks, chain attachment, rigging, cable clamps, and a gearbox.
permalink: /learning/cad/cascade-elevator/
role: lead
order: 10
size: 3
time: "3–4 hrs"
---

## Description

This is the capstone of the CAD track: a **cascade elevator** that extends
several stages to reach high while packaging small. Elevators are precise,
fast, and mechanically unforgiving. They tie together structure, bearings,
power transmission, and **rigging** — the cables or belts that make stages
move together.

This is **Stage 2D** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage2/2d/introduction/).
Read the comparison of cascade vs continuous first. Then copy the provided
document and build layout, part studio, and assembly. If a stage binds or
a clamp slips in CAD, it will drop a mechanism on the field.

Two rigging families show up in FRC:

- **Cascade.** Each stage moves the same distance relative to its parent.
  Drive the first moving stage (usually with chain) and the rigging
  multiplies travel through the rest. Center of mass rises earlier.
  Intermediate stages can carry climb loads. Adding a fourth stage makes
  the cable routing much harder.
- **Continuous.** One long run; stage order depends on friction. Extra
  stages are easier to add. Gearbox needs less reduction for the same
  carriage speed, but holding and sequencing get messier.

This ticket is cascade. The motor does not magically move every tube —
**chain** pulls stage one, and **cables/belts over pulleys** make stage
two (and three) follow.

Ideas you must be able to point to:

- **Elevator blocks.** Bearing blocks that ride in the rails and constrain
  each stage to slide, not twist. Alignment here is everything. Most teams
  buy WCP or TTB blocks rather than milling their own. Block stack height
  sets the spacing between stages.
- **Chain attachment.** The driven chain must bolt to stage one without
  slop. A chain comb (the reference uses TTB) is a COTS way to do that.
  A floppy clamp is backlash you will feel at the carriage.
- **Rigging.** Sketch the cable path *before* you place crossmembers. The
  clamp-plate tube and the motor sit where the routing demands, not where
  they look symmetric. Get the routing wrong and stages will not move in
  proportion.
- **Cable clamp and cable ends.** A slipping clamp drops the elevator.
  Terminate ends (swage, clamp) so the cable cannot fray out of a loop.
  Model the clamp as a real part with bolts, not a coincident sketch line.
- **Gearbox.** Lift speed vs stall vs **holding against gravity**. Plan a
  ratio or a brake from the start. Adding a brake after the plates are
  cut is miserable. Cascade can use force on an intermediate stage for
  climb; do not ignore that if the course's reference leans on it.

CAD-wise this is still layout → derive/reference → studio → flexible
assembly. Origin Cube still comes first. Stages **slider** or cylindrical
mates; do not fasten the carriage to the base. Drag the full travel with
rigging tension visually intact.

This site does not track whether you finished. The elevator document lives
in your Onshape account. Mentors review a share link.

## Prerequisites

- All earlier CAD tickets completed, especially
  [Dead Axle Pivot](../dead-axle-pivot/) and
  [Slapdown Intake](../slapdown-intake/) so moving assemblies and origin
  cubes are routine.
- Stage 1C Exercise 4 (telescoping hook) is the linear-motion preview;
  an elevator is that idea with rigging.

## What you'll learn

- How cascade rigging differs from continuous, and what that does to
  travel, COM, and gearbox choice.
- How elevator blocks, chain attachment, and cable clamps turn a stack of
  tubes into a constrained mechanism.
- How to sketch rigging paths so stage motion stays proportional.
- How to assemble sliding stages, route hardware, and verify full-height
  extension without collisions.

## Tasks

1. **Read the engineering pages, then copy the document.** Start at
   [Cascade Elevator Introduction](https://frcdesign.org/learning-course/stage2/2d/introduction/)
   and read:

   - [Elevator Blocks](https://frcdesign.org/learning-course/stage2/2d/elevator-blocks/)
   - [Chain Attachment](https://frcdesign.org/learning-course/stage2/2d/chain-attachment/)
   - [Rigging](https://frcdesign.org/learning-course/stage2/2d/rigging/)

   Follow the next-page arrows through cable clamp, cable ends, and
   gearbox pages. Copy the Stage 2D reference / exercise document into
   your account as `Stage 2D Elevator — YourName`. In your scratch note,
   write one sentence: *Cascade means each stage … relative to its
   parent.* You will paste that into the mentor note.

2. **Unit 1 — Layout sketch.** On the Stage 2D layout-sketch page, define
   stage count, retracted height, fully extended height, rail and block
   positions, chain run, and cable/belt routing. The rigging geometry is
   the hard part — do not skip it to "make tubes first." Origin Cube
   first. Fully constrain the sketch. If a pulley location is arbitrary,
   mark it as a variable you would prototype.

3. **Unit 2 — Part studio.** Follow the Stage 2D part-studio page. Model
   rails, carriage, elevator blocks (insert or derive COTS blocks when
   the course says to), pulleys, clamps, and the gearbox, all referencing
   the layout. Align rails. Seat bearings. Name every stage and clamp.
   No overlapping solids — stacked tubes that occupy the same volume will
   not slide.

4. **Unit 3 — Assembly.** Follow the Stage 2D assembly page. Mate stages
   so each **slides** on its rails. Route the rigging. Add the gearbox
   and chain attachment. Drag from stowed to full height. Stages should
   extend in proportion; the carriage should not leap while a mid-stage
   sits still. Check hardstops and cable wrap at both ends.

5. **Write one design note.** In a few sentences: *How does your gearbox
   hold against gravity (ratio, brake, or both), and what happens if the
   first-stage chain clamp slips?* If you would pick continuous rigging
   for a different robot, say why cascade is still the right lesson.

6. **Hand it to a mentor.** Share `Stage 2D Elevator — YourName` or export
   screenshots of the black layout (routing visible), the named studio,
   and the assembly at retracted and extended height. If your team
   exported these tickets, paste the link and move the issue to In Review.

## Acceptance Criteria

- [ ] A shareable Onshape document contains your Stage 2D cascade
      elevator.
- [ ] Layout, part studio, and assembly work from the FRCDesign Stage 2D
      pages is complete in that document.
- [ ] The layout sketch is fully constrained and shows stage heights plus
      rigging paths, not only a stack of rectangles.
- [ ] Custom parts and stages are named; no overlapping solids; blocks and
      clamps are real assembled parts.
- [ ] Stages slide through the designed travel; extension looks
      proportional; rigging stays routed at both ends.
- [ ] A short written note includes the cascade sentence from Task 1 and
      defends a hold-against-gravity or clamp choice.

## Resources

- [Stage 2D introduction](https://frcdesign.org/learning-course/stage2/2d/introduction/)
- [Elevator Blocks](https://frcdesign.org/learning-course/stage2/2d/elevator-blocks/)
- [Chain Attachment](https://frcdesign.org/learning-course/stage2/2d/chain-attachment/)
- [Rigging](https://frcdesign.org/learning-course/stage2/2d/rigging/)
- [FRCDesign Learning Course](https://frcdesign.org/learning-course/)
- [Onshape Learning Center](https://learn.onshape.com/)
- [Slapdown Intake](../slapdown-intake/)
- [Power Transmission](../power-transmission/)
- [CAD & Design Hub](../)

## Notes

- Cascade rigging multiplies travel **and** the cost of a mistake.
  Double-check that every stage moves the right amount before you call it
  done.
- Plan holding against gravity from the first layout (brake or a ratio
  that can stall safely). It is hard to add after plates exist.
- COTS elevator blocks exist because alignment is a manufacturing problem.
  Inventing your own slides is a research project, not a first elevator.
- You have reached the end of this curriculum. Keep going: independent
  robot and mechanism projects, design reviews with teammates and
  mentors, public CAD from other teams, and the rest of the
  [FRCDesign course and handbook](https://frcdesign.org/). See the
  [CAD & Design Hub](../) for the full roadmap.
