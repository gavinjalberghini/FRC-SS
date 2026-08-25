---
layout: mechanical-lesson
title: Assembly, Tolerances & Maintenance
subtitle: Build to tolerance, align mechanisms, and keep the robot serviceable through a season.
permalink: /learning/mechanical/assembly-tolerances-maintenance/
role: lead
order: 12
size: 2
time: "2–3 hrs"
---

## Description

A pile of in-spec parts can still be a robot that binds, drives
crooked, and drops a chain in quarterfinals. This is the capstone:
fit, alignment, service access, and the boring checklist that keeps
a machine alive. You already assembled a stage in
[Power Transmission & Drivetrains](../power-transmission-drivetrains/).
You already know how a rivet differs from a nylock from
[Riveting & Fastened Assembly](../riveting-assembly/).
[Shop Safety & PPE](../shop-safety/) is still the rule if you pick
up a tool — pit repairs are how people skip glasses.

A **tolerance** is how far a dimension may miss the number and
still work. `2.000 ± 0.005 in` is a bearing bore or a gear center,
not a bumper board. Tight tolerances cost time. Call them only
where the physics cares. A **clearance fit** slides (a #10 in a
clearance hole, a shaft in a slip-fit collar). A **press /
interference fit** is slightly too big and is pressed (a bearing
in a plate). If two parts will not go together, **measure both**
before you hit them. Forcing a press-fit bearing in at an angle is
how you size the bore up and ruin the plate.

Alignment is why frames get squared on a table with a large square,
not "by eye on the cart." A chassis that is a parallelogram will
never track. Shafts that are not parallel will walk belts off and
wear sprockets into mushrooms. Gears and sprockets must be
**coplanar**. The test is still the one from the last ticket: cycle
every mechanism **by hand** with the battery off. If you cannot
move it, a motor will not magically fix it — it will brown out or
cook.

Serviceability is a design choice you make with a hex key in your
hand. Can you reach the fastener? Is it a bolt where you will swap
a worn roller, or a rivet because that gusset should not move?
Are the #10-32s and 1/4-20s in labeled bins in the pit, or in one
shared coffee can? Electrical will thank you if wires and pneumatic
hose are not pinched under the bellypan you have to drop every
event. Coordinate; do not "just drill another hole" through a
CAN run.

Maintenance is a loop, not a vibe. Before and after a practice
block or a match: fasteners, chain/belt tension, bearing play,
cracks, and anything that changed since the last checklist. Re-torque
what backs out. Thread locker where the build called for it, not
after the third time the same screw lands on the carpet. Log
repeat failures so CAD can change the part instead of you changing
the same bolt forever.

This website does not store your checklist. Tape it in the pit
box. The team's board, if they exported tickets, is where this
one closes.

## Prerequisites

- [Shop Safety & PPE](../shop-safety/) signed off.
- [Power Transmission & Drivetrains](../power-transmission-drivetrains/)
  completed, plus the veteran fabrication tickets it depends on.

## What you'll learn

- How to talk about tolerance, clearance, and press fit on a real
  part, not as vocabulary.
- How to square and free up a mechanism by hand.
- How to write a pre-match mechanical list this team will actually
  use.

## Tasks

1. **Measure a fit instead of arguing about it.** Find one clearance
   fit and one press or snug fit on the robot or a spare plate
   (bearing in a bore, hex shaft in a bearing, bolt in a hole).
   Measure with calipers. Write the two numbers and which kind of
   fit each is. If a part does not assemble, measure *before*
   persuading it with a hammer.

2. **Square and cycle a mechanism.** With a mentor, pick a
   subsystem you are allowed to touch (intake, elevator carriage,
   a spare gearbox, a practice chassis). Check:

   - a reference face with a square
   - shaft parallelism / sprocket or pulley plane
   - free motion by hand, battery disconnected

   Fix one real issue if you find one (spacer, loose bearing, belt
   tension, a screw in the path). If it is already perfect, have
   the mentor introduce a known fault (loose tension, missing
   spacer) and you find it.

3. **Critique service access.** Walk the current robot (or last
   year's). Find one joint that is hard to service. Write: fastener
   type, why it is painful, and one change (bolt instead of rivet,
   cutout, different head, labeled spare). You do not have to
   implement it this ticket unless a mentor wants the work —
   the write-up is the evidence.

4. **Write the pit checklist.** One page, this team's robot, not a
   generic internet list. Include at least:

   - fasteners on drivetrain, bumpers, and the highest-load joint
   - chain or belt tension on every loop that can skip
   - bearing play on the output that failed last year (ask)
   - bumpers on/off hardware
   - "battery out / glasses on" as line one

   Put it in the pit box or the team's drive folder. Electrical's
   [Systematic Troubleshooting](../../electrical/troubleshooting/)
   is the same mindset for wires — do not invent a second culture.

5. **Run the list once.** Do a real pre-practice or dummy
   "pre-match" inspection with a mentor using *your* list. Mark
   what you found. Change the list if a line was useless or a
   failure mode was missing.

## Acceptance Criteria

- [ ] Two caliper measurements exist, labeled clearance vs
      press/snug, on real hardware.
- [ ] You squared and hand-cycled a mechanism and either fixed a
      fault or found a mentor-planted one.
- [ ] A written serviceability note names one bad joint and one
      concrete change.
- [ ] A one-page mechanical checklist for *this* robot lives in
      the pit box or team folder, and you used it once with a
      mentor.
- [ ] Shop-safety habits were intact (glasses, battery out when
      hands are in mechanisms).

## Resources

- [WPILib: Hardware Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/index.html)
- [WPILib: Preemptive troubleshooting](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/preemptive-troubleshooting.html)
- [Electrical: Systematic Troubleshooting](../../electrical/troubleshooting/)
- [FIRST Safety Manual (PDF)](https://www.firstinspires.org/hubfs/web/program/all/safety-manual.pdf?hsLang=en)
- [Chief Delphi](https://www.chiefdelphi.com/) — search "pit
  checklist" or "reliability"
- [REV ION: Introduction to Motion](https://docs.revrobotics.com/ion-build/motion/introduction-to-motion)
- [FRC Game Manual / Q&A](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system) —
  bumper and fastener rules change; read the year you are in

## Notes

- A checklist nobody runs is decoration. Assign who holds it on
  drive team.
- If a failure repeats, the fix is a design change, not a stronger
  word at the next torque pass.
- This is the last mechanical ticket. You are not "done learning."
  You are allowed to build, and you are expected to hand the next
  new student [Shop Safety & PPE](../shop-safety/) before they
  touch a saw.
