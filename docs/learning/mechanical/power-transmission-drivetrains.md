---
layout: mechanical-lesson
title: Power Transmission & Drivetrains
subtitle: Gears, belts, chain, shafts, and bearings — how motor power becomes robot motion.
permalink: /learning/mechanical/power-transmission-drivetrains/
role: lead
order: 11
size: 3
time: "Multi-session"
---

## Description

A motor spins too fast and with the wrong kind of force for most
mechanisms. **Power transmission** is how that spin becomes a wheel,
an arm, or an intake roller you can actually use. This is the
mechanical-build twin of the CAD lesson
[Power Transmission & Gearboxes](../../cad/power-transmission/). CAD
teaches you to model the ratio. This ticket teaches you to *assemble*
it so it spins by hand without grinding.

You need [Shop Safety & PPE](../shop-safety/) signed off before you
touch a press, a drill, or a powered chassis. You need the veteran
tickets — especially
[Riveting & Fastened Assembly](../riveting-assembly/) and
[Fasteners & Hardware](../fasteners-hardware/) — because a gearbox is
just parts and #10-32s until it is a gearbox.

Three ways to send rotation somewhere else:

- **Gears** mesh tooth to tooth. Compact, stiff, no stretch. They
  need the correct **center distance**. Too close and they bind and
  howl. Too far and they slop and chew the tips. FRC gears are
  usually **20 DP** (diametral pitch): pitch diameter in inches is
  teeth ÷ 20. A 20T and a 60T want 1 in + 3 in = 4 in center to
  center. Different DP or different tooth profiles do not mesh.
  Meshing gears reverse direction.
- **Timing belts** (GT2, HTD, RT25) run on toothed pulleys. Quiet,
  light, no grease flung at electronics. They need **alignment**
  (pulleys in one plane) and **tension** (firm, not guitar-string).
  Too tight cooks bearings; too loose skips under load.
- **Chain** (#25 everyday, #35 when the load is rude) runs on
  sprockets. It likes dirt less than marketing claims, but it
  tolerates distance and debris better than a belt. Tension with a
  sliding mount or a tensioner. #25 is what REV ION and a lot of
  WCP structure are pitched around.

**Ratio** is driven teeth ÷ driving teeth. A 12T pinion on a 60T
gear is 5:1: the output is slower and has about 5× the torque
(minus efficiency). Stack stages: 4:1 then 3:1 is **12:1** overall.
Almost every FRC arm or elevator is a reduction. Shooters sometimes
run near 1:1 or even a small step-up. If you cannot say what a
ratio does to speed and torque, do not bolt the gearbox together
yet. FRCDesign's
[gear basics](https://frcdesign.org/learning-course/stage1/1b/gears/)
and REV's
[introduction to motion](https://docs.revrobotics.com/ion-build/motion/introduction-to-motion)
are the written versions of this paragraph.

**Shafts** carry the rotation. **1/2 in hex** is the FRC default
because the shape *is* the key — a hex-bore sprocket cannot slip
the way a round shaft plus a missing set screw can. WCP ThunderHex
and similar profiles exist so a bearing can live on a hex shaft.
**Bearings** take the radial load so the shaft is not spinning in
raw aluminum. Press them **square and fully seated**. A cocked
bearing is a gearbox that feels "almost fine" until it welds
itself at an event. **Collars, snap rings, and spacers** keep
things located on the shaft. Missing a spacer is how a gear walks
out of mesh.

Assembly rule that saves motors: **spin it by hand before anyone
enables.** Bind means misalignment, an unseated bearing, a screw
in a gear's path, or center distance that is wishful. Skip this
and you will smell varnish.

This site does not track your gearbox. The mentor spins it.

## Prerequisites

- [Shop Safety & PPE](../shop-safety/) signed off.
- Veteran tickets through
  [Riveting & Fastened Assembly](../riveting-assembly/) completed.
  If your team groups by "Level 1 / Level 2," that means all of
  both.

## What you'll learn

- How gears, belts, and chain differ, and when this shop uses each.
- How to compute a single-stage and a two-stage ratio and say what
  it does to speed and torque.
- How to identify shaft, bearing, and retaining hardware in a real
  gearbox.
- How to assemble (or rebuild) a stage that spins freely.

## Tasks

1. **Read the motion docs.** Read REV
   [Introduction to Motion](https://docs.revrobotics.com/ion-build/motion/introduction-to-motion)
   and FRCDesign
   [Gear Basics](https://frcdesign.org/learning-course/stage1/1b/gears/).
   Skim WCP
   [FRC Build System](https://docs.wcproducts.com/welcome/frc-build-system)
   (belts, chain, gears). Write four lines you will keep: when you
   would pick gears vs belt vs #25 vs #35.

2. **Do the ratio on paper.** A mentor (or last year's gearbox)
   gives you tooth counts. Compute:

   - single-stage ratio (driven ÷ driving)
   - two-stage overall (multiply the stages)
   - what that does to output **speed** and **torque** versus the
     motor

   Example you should be able to do cold: 12T driving 36T, then
   15T driving 45T. Overall? Speed? Torque? Check yourself against
   [ReCalc](https://www.reca.lc/) or the JVN calculator if the
   team uses it — after you do the multiply by hand.

3. **Walk a real gearbox.** Pull a COTS gearbox or an old robot
   stage off the shelf (AndyMark, WCP, REV, VEX-style — whatever
   you have). With a mentor, point to:

   - input (motor / pinion)
   - each stage's driving and driven gear
   - output shaft
   - bearings (are they seated?)
   - how the gears are retained (collar, snap ring, bolt-through)

   Do not power it.

4. **Assemble or rebuild one stage.** On a practice block, a GreyT
   / WCP / REV kit, or a stripped drivetrain module the team can
   spare:

   - press or seat bearings square
   - set center distance or belt/chain tension to the vendor spec
     or the CAD
   - align sprockets/pulleys/gears in one plane
   - spin the output **by hand**

   It should turn smoothly with no grind, no scrape, and no
   "tight spot" once per rev. If it binds, find it. Do not "free
   it up with a motor."

5. **Look at a drivetrain.** On the current or last robot, name
   the transmission type (West Coast, swerve, other), the wheel
   count, and how power gets from motor to wheel. You are not
   designing a new chassis here. You are proving you can see the
   parts. CAD students can compare to
   [Power Transmission & Gearboxes](../../cad/power-transmission/).

## Acceptance Criteria

- [ ] Four written lines state when this shop would use gears,
      belt, #25, and #35.
- [ ] Hand-calculated single-stage and two-stage ratios, with
      speed/torque effect, checked by a mentor (calculator only
      after the hand math).
- [ ] You pointed to input, stages, output, bearings, and
      retention on a real gearbox.
- [ ] A practice stage or kit gearbox spins freely by hand with
      correct mesh or tension. A mentor spun it too.
- [ ] You named the team's drivetrain type and the path from
      motor to wheel on a real chassis.

## Resources

- [REV ION: Introduction to Motion](https://docs.revrobotics.com/ion-build/motion/introduction-to-motion)
- [REV: FRC Robot Basics Guide (PDF)](https://www.revrobotics.com/content/docs/FRC-Robot-Basics-Guide.pdf)
- [FRCDesign: Gear Basics](https://frcdesign.org/learning-course/stage1/1b/gears/)
- [FRCDesign Learning Course](https://frcdesign.org/learning-course/)
- [WCP FRC Build System](https://docs.wcproducts.com/welcome/frc-build-system)
- [YETI: Power Transmission Basics](https://wiki.yetirobotics.org/books/design-process/page/power-transmission-basics)
- [ReCalc](https://www.reca.lc/)
- [CAD curriculum: Power Transmission & Gearboxes](../../cad/power-transmission/)
- [WPILib: Hardware Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/index.html)
- [AndyMark](https://www.andymark.com/) / [REV](https://www.revrobotics.com/) /
  [WCP](https://wcproducts.com/) — vendor gearbox user guides for
  the kit you actually assembled

## Notes

- Never reach into a chained or belted mechanism that might be
  enabled. Battery out, like electrical's safe state.
- Grease is not "more is better." Follow the gearbox manual. Extra
  grease on an open chain becomes a sanding compound.
- The last ticket,
  [Assembly, Tolerances & Maintenance](../assembly-tolerances-maintenance/),
  is how this gearbox stays serviceable through a district event,
  not just on the bench the night you built it.
