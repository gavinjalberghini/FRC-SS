---
layout: mechanical-lesson
title: Riveting & Fastened Assembly
subtitle: Pop rivets and rivet tools, plus bolted assembly best practices for strong, serviceable joints.
permalink: /learning/mechanical/riveting-assembly/
role: veteran
order: 10
size: 2
time: "1–2 hrs"
---

## Description

Cut, drilled, finished parts still have to become a robot. FRC uses
two everyday joints: **blind (pop) rivets** for a permanent, light
gusset-to-tube connection, and **bolts** for anything you will take
apart, adjust, or service. This ticket is how a rivet actually clamps,
how to pull one square, and how not to build a bolted joint you cannot
reach in the pit.

[Shop Safety & PPE](../shop-safety/) is still required. Rivet tools
are not saws, but you will drill holes — glasses on, gloves off at
the drill, work clamped. You already know fastener families from
[Fasteners & Hardware](../fasteners-hardware/) and you have clearance
holes from [Drilling & Tapping](../drilling-tapping/).

A **blind rivet** installs from one side, which is the whole point
when the back of a tube is closed. You put the rivet body through
aligned holes. The tool pulls the **mandrel**. The mandrel head
expands the backside of the rivet into a shop-head, then **snaps
off**. The parts are clamped. That clamp is **permanent**. To undo
it you drill the rivet out, which also opens the hole a little. Do
not rivet a gearbox side plate you will want to service at an event.

Size the rivet to the **hole** and the **grip**. The common FRC
pattern is **1/8 in rivets in ~1/8 in holes** (often a #30 bit —
confirm on the rivet package). Grip range is the *total* thickness
of the stack: a 1/16 in gusset on 1/16 in tube wall is 1/8 in of
grip, not "a short rivet." A rivet meant for 1/8–1/4 in grip on a
3/8 in stack will not set. A rivet that is too long for a thin
stack looks ugly and may not clamp. Aluminum rivets in aluminum
structure are the default; steel rivets in thin tube can crush the
wall.

If the holes do not line up, clamp and re-drill as a pair. A rivet
will not pull two misaligned holes into true — it will freeze the
mistake.

Technique:

1. Deburr and line up the holes. Clamp so the parts cannot shift.
2. Load the mandrel in the matching nosepiece.
3. Insert the rivet fully. Hold the tool **square**.
4. Squeeze (or trigger the pneumatic) until the mandrel snaps.
5. Check the shop-head on the back. Pick up the spent mandrel —
   those things find drivetrain chain.

A pneumatic riveter is the same process with less hand pain. Fingers
stay off the nose.

Bolted joints are how you keep a robot repairable. Clearance hole on
the pass-through side, **nylock** or a tapped hole on the other.
Leave wrench access. Do not bury a #10-32 under a bellypan with no
cutout. Do not overtighten into aluminum — you already stripped a
practice hole if you ignored the fastener ticket. Thread locker
where the drawing says so, not as a personality.

## Prerequisites

- [Shop Safety & PPE](../shop-safety/) signed off.
- [Fasteners & Hardware](../fasteners-hardware/) and
  [Drilling & Tapping](../drilling-tapping/) completed.

## What you'll learn

- How a blind rivet clamps two parts, and why that is permanent.
- How to pick diameter and grip and pull a square rivet.
- How to build one bolted joint you could actually service.

## Tasks

1. **Watch a rivet set before you set one.** Watch
   [Blind Pop Rivets Explained and How to Install Them](https://www.youtube.com/watch?v=sQ5LwjxDl5Y).
   Then skim AndyMark
   [Hardware](https://andymark.com/collections/hardware) (rivets) or
   McMaster
   [rivets](https://www.mcmaster.com/products/rivets/) far enough to
   see diameter vs grip. Write the grip range printed on the rivets
   *this shop* uses for gussets.

2. **Match rivet to hole.** On scrap 1/16 in plate or a leftover
   gusset and a piece of tube, drill (or use existing) holes that
   match the rivet. A 1/8 in rivet should be snug — if it falls
   through, the hole is too big and the rivet will spin. Deburr.
   Clamp the stack.

3. **Set rivets.** Install at least **three** rivets with a hand
   riveter, square, mandrels collected. If the shop has a pneumatic
   riveter, set **two more** with that tool after a mentor shows the
   trigger. Inspect the back: the shop-head should sit down, not
   look like a loose mushroom. Mark the coupon with your name.

4. **Drill one out.** On purpose, drill out one practice rivet the
   way you would in the pit (correct bit, both layers supported).
   Say why you would not do this to a plate you still need. This is
   the "permanent" lesson, not vandalism.

5. **Build a serviceable bolted joint.** Two scraps, #10-32 or
   1/4-20 as the mentor assigns: clearance on one side, nylock or
   tapped hole on the other, washer if the hole is slotted. Tighten
   so it does not rattle and so you can still remove it with the
   hex key that lives in the pit kit. Point to the tool access. If
   you cannot reach the hex, redesign the stack with the mentor —
   that is the whole point.

## Acceptance Criteria

- [ ] You stated, in your own words, how a mandrel sets a blind
      rivet and why the joint is permanent.
- [ ] You wrote the shop's gusset-rivet diameter and grip range from
      the package.
- [ ] A named coupon has at least three square hand-set rivets
      (plus two pneumatic if the shop has the tool). Mandrels are
      in the trash, not on the floor.
- [ ] One practice rivet was drilled out on purpose.
- [ ] A bolted sample joint uses the assigned size, a lock, and
      visible tool access. A mentor removed and reinstalled the
      screw.

## Resources

- [Blind Pop Rivets Explained (YouTube)](https://www.youtube.com/watch?v=sQ5LwjxDl5Y)
- [AndyMark: Hardware](https://andymark.com/collections/hardware)
- [McMaster-Carr: Rivets](https://www.mcmaster.com/products/rivets/)
- [AndyMark: 1/4-20 thread rivet nut](https://andymark.com/products/1-4-20-thread-rivet-nut) —
  different tool; useful when you need threads in sheet
- [REV ION: Introduction to Structure](https://docs.revrobotics.com/ion-build/structure/introduction-to-structure)
- [WPILib: Hardware Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/index.html)
- [Chief Delphi](https://www.chiefdelphi.com/) — search "rivet
  vs bolt" when a design review gets religious

## Notes

- Mandrels left in a drive gearbox will find the chain. Sweep.
- A leaning rivet (tool not square) looks set from the front and
  is loose on the back. Always look at the shop-head.
- Rivet-nuts (nutserts) are not pop rivets. They need their own
  installer and a correct hole. Practice on scrap; a spinning
  rivet-nut in a finished bellypan is a bad afternoon.
- Level 2 ends here. Next is
  [Power Transmission & Drivetrains](../power-transmission-drivetrains/):
  gears, belts, chain, shafts, and a gearbox that has to spin by
  hand before anyone enables a motor.
