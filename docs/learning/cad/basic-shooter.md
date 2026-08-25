---
layout: cad-lesson
title: Basic Shooter
subtitle: Model a flywheel shooter while learning rigidity, trajectory, exit velocity, compression, and spin.
permalink: /learning/cad/basic-shooter/
role: veteran
order: 7
size: 2
time: "2–3 hrs"
---

## Description

This is your first full **mechanism**. Stage 1 taught you to model. Stage 2
teaches you to *decide*, then model. A **flywheel shooter** is the usual
way FRC robots score when they cannot physically reach the goal: a spinning
wheel (or pair of wheels) grabs a game piece and throws it.

This ticket is **Stage 2A** of the
[FRCDesign.org Learning Course](https://frcdesign.org/learning-course/stage2/2a/introduction/).
Read the engineering pages first. They explain why the reference shooter
looks the way it does. Then copy or follow the provided document and build
the layout sketch, part studio, and assembly. Stage 2 is less click-by-click
than Stage 1; the pages tell you what to model and why, not every
constraint.

The ideas you must be able to defend:

- **Rigidity.** A shooter that flexes while it fires steals energy and
  sprays shots. Thick side plates, support tubes, and standoffs are not
  cosmetics. If the flywheels can walk relative to the hood, you do not
  have a shooter — you have a noise maker.
- **Trajectory.** Exit angle and height set where the piece lands. The
  layout sketch includes the goal geometry (or a field reference) so the
  hood angle is a decision, not a guess.
- **Exit velocity.** Surface speed is `wheel RPM × circumference` (and
  related through diameter). Larger diameter at lower RPM is often more
  efficient than spinning a small wheel to death. Two CIM-class brushless
  motors are common. Inertia (extra flywheel mass) helps recovery between
  shots and hurts spin-up — pick on purpose.
- **Compression and wrap.** The piece must be squeezed against the wheel
  (compression) over enough contact arc (wrap) to transfer energy without
  slipping. Too little and it chatters; too much and the motor stalls or
  the piece deforms. Softer pieces need more compression; hard pieces
  often want compliant wheels or a foam backing.
- **Spin.** Different top and bottom (or hood vs floor) speeds add backspin
  or topspin. Backspin can stabilize a ball; the layout should show both
  wheel diameters and their relationship to the path.
- **Friction and efficiency.** Wheel compound and surface decide grip.
  Bearings, alignment, and belt wrap decide how much motor power actually
  reaches the piece. Belts for flywheel reductions should use generous
  pulleys and real tooth engagement so they do not skip.

CAD-wise this is Stage 1D again: a fully constrained layout of wheels,
compression circles, and the ball path, then plates and shafts that
**derive** or reference that layout, then an assembly origin-cubed to the
origin so the flywheel can spin.

This site does not track whether you finished. The shooter document lives
in your Onshape account. Mentors review a share link.

## Prerequisites

- All Designer tickets completed: [Getting Started](../getting-started/),
  [Onshape Fundamentals](../onshape-fundamentals/),
  [Power Transmission](../power-transmission/),
  [Practice Mechanisms](../practice-mechanisms/).
- [Subsystem Workflow](../subsystem-workflow/) completed so you have a
  drivebase habit (layout → studio → assembly) before a moving mechanism.
- Stage 1C Exercise 3 (the practice shooter) is useful warm-up, not a
  substitute.

## What you'll learn

- Why rigidity, compression, wrap, and surface speed dominate shooter
  consistency.
- How to capture flywheel diameter, compression gap, feed path, and launch
  angle in one layout sketch.
- How to model structure, shafts, and hood from that layout using Tube
  Converter, Robot Shaft / Shaft Generator, and Belt & Chain Gen.
- How to mate a flywheel so it spins and still check that the game-piece
  path is clear.

## Tasks

1. **Read the engineering pages before you model.** Start at
   [Basic Shooter Introduction](https://frcdesign.org/learning-course/stage2/2a/introduction/)
   and read:

   - [Structure & Rigidity](https://frcdesign.org/learning-course/stage2/2a/structure-rigidity/)
   - [Ball Trajectory](https://frcdesign.org/learning-course/stage2/2a/ball-trajectory/)
   - [Exit Velocity](https://frcdesign.org/learning-course/stage2/2a/exit-velocity/)
   - [Compression & Wrap](https://frcdesign.org/learning-course/stage2/2a/compression-wrap/)

   Follow any remaining concept pages the next-arrow offers (spin, friction).
   Copy the Stage 2A / reference document from those pages into your
   account as `Stage 2A Shooter — YourName`. Use the reference part studio's
   rollback bar as a teacher, not as a file to submit.

2. **Unit 1 — Layout sketch.** Complete
   [Layout Sketch](https://frcdesign.org/learning-course/stage2/2a/layout-sketch/)
   in your document. Sketch flywheel diameter, the concentric compression
   circle, the game-piece path, hood wheels, feed wheels, and a launch
   angle tied to a field reference. Origin Cube first. The sketch is not
   done until it is **black**. If you must constrain something arbitrarily
   to close it, say so in your note.

3. **Unit 2 — Part studio.** Complete
   [Part Studio](https://frcdesign.org/learning-course/stage2/2a/part-studio/).
   Model structure, flywheels, shafts, and hood from the layout. Use Robot
   Shaft (or Shaft Generator) and Tube Converter. Mirror the main plate
   instead of redrawing the far side. Name parts (`Left plate`, `Flywheel
   shaft`, not `Part 7`). No overlapping solids.

4. **Unit 3 — Assembly.** Complete
   [Assembly](https://frcdesign.org/learning-course/stage2/2a/assembly/).
   Insert the studio (green check, then group; fasten Origin Cube to the
   origin). Add motors, pulleys, and hardware from FRCDesignLib. Mate the
   flywheel so it **revolves** freely. Drag it. Confirm the game-piece path
   and compression gap are still what the layout promised.

5. **Write one design note.** In a few sentences: *What compression (or
   wrap, or flywheel diameter) did you use, and what would you prototype
   first if this were going on a real robot?* Compression is the usual
   number-one tuning variable — treat it as a decision, not a copied
   dimension.

6. **Hand it to a mentor.** Share `Stage 2A Shooter — YourName` or export
   screenshots of the black layout, the named part studio, and the spinning
   assembly. If your team exported these tickets, paste the link and move
   the issue to In Review.

## Acceptance Criteria

- [ ] A shareable Onshape document contains your Stage 2A shooter (copy
      you own, not the public original).
- [ ] Layout, part studio, and assembly pages on FRCDesign are complete in
      that document.
- [ ] The layout sketch is fully constrained; flywheel, compression, path,
      and launch geometry are visible.
- [ ] Custom parts are named; no overlapping solids; structure looks like
      it could take flywheel load without the plates floating.
- [ ] The flywheel mates spin; the game-piece path is clear in the
      assembly.
- [ ] A short written note defends one shooter choice (compression, wrap,
      diameter, or rigidity).

## Resources

- [Stage 2A introduction](https://frcdesign.org/learning-course/stage2/2a/introduction/)
- [Structure & Rigidity](https://frcdesign.org/learning-course/stage2/2a/structure-rigidity/)
- [Ball Trajectory](https://frcdesign.org/learning-course/stage2/2a/ball-trajectory/)
- [Exit Velocity](https://frcdesign.org/learning-course/stage2/2a/exit-velocity/)
- [Compression & Wrap](https://frcdesign.org/learning-course/stage2/2a/compression-wrap/)
- [Layout Sketch](https://frcdesign.org/learning-course/stage2/2a/layout-sketch/)
- [Part Studio](https://frcdesign.org/learning-course/stage2/2a/part-studio/)
- [Assembly](https://frcdesign.org/learning-course/stage2/2a/assembly/)
- [Onshape Learning Center](https://learn.onshape.com/)
- [Practice Mechanisms (Exercise 3 shooter)](../practice-mechanisms/)
- [Power Transmission](../power-transmission/)

## Notes

- Model compression as a dimension you could change, not a magic number
  buried in a plate outline. You will iterate it on a prototype.
- A shooter is only as consistent as its rigidity *and* its feed. Design
  both. A perfect flywheel with a random indexer still misses.
- Use belts (not a tiny pinion on a huge gear) for high-RPM flywheel
  reductions when the course says so; skipping teeth at shooter speed is
  a match-losing failure.
- The next ticket ([Dead Axle Pivot](../dead-axle-pivot/)) is Stage 2B:
  a rotating arm on a fixed axle, with backlash and tensioning added to
  the same layout → studio → assembly loop.
