---
layout: mechanical-lesson
title: Fasteners & Hardware
subtitle: Screws, bolts, nuts, rivets, and thread sizes — what to use where, and how threads work.
permalink: /learning/mechanical/fasteners-hardware/
role: fabricator
order: 3
size: 1
time: "45–60 min"
---

## Description

A competition robot is held together by hundreds of screws. The wrong one
is not a style choice — it is a joint that backs out in a playoff or a
head you cannot reach with the hex key in the pit. This ticket is a
hardware walk, not a lecture. You already can mark a line from
[Measurement & Layout](../measurement-layout/). You still do not run a
machine unless [Shop Safety & PPE](../shop-safety/) is signed off, and
you will not need one here.

FRC almost always means **socket-head cap screws (SHCS)** driven with a
hex (Allen) key. The tall cylindrical head is strong and fits in a
counterbore. **Button heads** sit lower and look cleaner on a visible
panel; they are weaker, so they are the wrong choice for a high-load
gearbox through-bolt. **Flat heads** need a countersink so they sit
flush. Mix those three up and you will either stick up into a belt or
crush a thin plate.

Threads are a diameter plus a pitch. Read them that way every time.

**#10-32** is a numbered screw about 0.190 in across, with **32 threads
per inch** (fine / UNF). It is the default FRC structural screw. REV
MAXTube, AndyMark punched tube, and most gussets are laid out on a 1/2 in
grid of **#10 clearance holes**. Fine pitch puts more threads into a
1/16 in tube wall, which is why a #10-32 nylock through a gusset actually
holds. Typical hex keys: **5/32 in** on a #10-32 SHCS and **1/8 in**
on a #10-32 button head. Confirm on the fastener — do not guess and
cam out.

**1/4-20** is a 1/4 in (0.250 in) diameter screw with **20 threads per
inch** (coarse / UNC). Use it where the load is ugly: bumper mounts,
chassis-to-bellypan, some motor and gearbox through-bolts. Coarse thread
is faster to run and more damage-tolerant. It also removes more material
when you drill a 1×1 tube, so it is overkill for a light polycarb guard.
Typical hex: **3/16 in** for a 1/4-20 SHCS, **5/32 in** for a button
head.

A bolt and a nut (or a tapped hole) must match **both** numbers.
A #10-32 screw will not live in a #10-24 nut, and a 1/4-20 will
not live in a #10-32 hole. That mismatch is how bins get poisoned
and how a "quick repair" shreds a thread at an event. Metric callouts
show up on some COTS gearboxes and electronics (**M3 × 0.5**,
**M4 × 0.7**). If the drawing says metric, stay metric.

**Nylock** nuts have a nylon insert that resists vibration. Use them
anywhere a plain nut would rattle off — which, on a robot, is almost
everywhere. **Nutserts / rivet nuts** put threads into thin sheet when
you cannot reach the back. **Rivets** are permanent; they have their own
ticket later. **Standoffs and spacers** set a distance between two
plates so a shaft or a belt can pass.

Grip length matters. You want roughly one diameter of thread engagement
(a #10 wants about 0.19 in of useful thread) without bottoming in a
blind hole. Overtighten aluminum and you strip it. Seat the hex key
fully, keep it square, and stop when the joint is snug plus a controlled
final turn — not when your shoulder is involved.

This site does not track which bin you identified. The mentor does.

## Prerequisites

- [Shop Safety & PPE](../shop-safety/) signed off.
- [Measurement & Layout](../measurement-layout/) completed. You will use
  a tape or calipers to check screw length.

## What you'll learn

- How to name SHCS, button head, flat head, nylock, and a rivet on sight.
- What **#10-32** and **1/4-20** each number means, and what each size
  is for on an FRC robot.
- How to pick a locking method and drive a screw without stripping it.

## Tasks

1. **See the two sizes in the wild.** Open AndyMark's
   [Hardware](https://andymark.com/collections/hardware) collection and
   find both a
   [1/4-20 fastener kit](https://andymark.com/products/1-4-20-fasteners-hardware-kit)
   and the #10 / screws bins your shop actually stocks. Then read REV's
   note that ION structure is
   [#10 hardware](https://docs.revrobotics.com/ion-build/structure/introduction-to-structure).
   Write two sentences you will say to a mentor: *#10-32 is for …*
   and *1/4-20 is for …*.

2. **Walk the fastener wall.** With a mentor or a veteran, stand at the
   hardware organizer. Pull one of each into an egg carton or a labeled
   cup:

   - #10-32 SHCS
   - #10-32 button head
   - 1/4-20 SHCS
   - nylock nut (#10-32 or 1/4-20 — say which)
   - a pop rivet
   - one metric screw if the shop has a COTS gearbox or radio mount
     that uses it

   Put each back in the **correct** bin. If two sizes share a bin, tell
   a mentor — that bin is a future failure.

3. **Read a thread callout.** Using a thread gauge, the bin label, or
   McMaster's
   [thread charts](https://www.mcmaster.com/products/thread-charts/),
   decode `#10-32 × 1.25 SHCS` and `1/4-20 × 0.75 BHCS` out loud:
   diameter, pitch (TPI), length, and head style. Measure one screw's
   length with calipers (under the head for a socket head; overall
   conventions vary — ask how *this* shop calls length).

4. **Drive one screw correctly.** Seat the matching hex key or driver
   bit fully in a #10-32 SHCS. Drive it into a spare nut or a tapped
   scrap until it is snug. No cam-out, no rounded hex, no "plus a
   grunt." If you strip it, you do the task again on a new screw — the
   damaged one is now a teaching object, not robot hardware.

5. **Pick a joint.** A mentor shows you three sample joints (or three
   photos of last year's robot): a gusset on tube, a bumper mount, and
   a polycarb cover. For each, you name fastener family, size, and lock
   (nylock, thread locker, or rivet) and say *why*. You are not building
   the joint yet — that is
   [Riveting & Fastened Assembly](../riveting-assembly/).

## Acceptance Criteria

- [ ] Two written sentences, in your words, state what #10-32 is for and
      what 1/4-20 is for, including what each number means (diameter and
      TPI).
- [ ] You pulled SHCS, button head, nylock, and a rivet from the shop
      bins, named each, and returned each to the correct bin. A mentor
      watched the return.
- [ ] You decoded a #10-32 and a 1/4-20 callout (diameter, pitch,
      length, head) out loud.
- [ ] You drove a #10-32 SHCS with a fully seated hex key and did not
      strip the socket.
- [ ] You assigned fastener + lock + reason for three sample joints.

## Resources

- [AndyMark: Hardware](https://andymark.com/collections/hardware)
- [AndyMark: 1/4-20 Fasteners Hardware Kit](https://andymark.com/products/1-4-20-fasteners-hardware-kit)
- [REV ION: Introduction to Structure](https://docs.revrobotics.com/ion-build/structure/introduction-to-structure)
- [McMaster-Carr: Thread charts](https://www.mcmaster.com/products/thread-charts/)
- [McMaster-Carr: Socket head cap screws](https://www.mcmaster.com/products/socket-head-cap-screws/)
- [WCP FRC Build System](https://docs.wcproducts.com/welcome/frc-build-system)
- [WPILib: Hardware Basics](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/index.html)
- [Chief Delphi](https://www.chiefdelphi.com/) — search "nylock" or
  "hardware organization" for pit-bin war stories

## Notes

- #10-24 exists. It is not #10-32. If a nut feels like it starts then
  grinds, stop. You are cross-threading or mixing pitch.
- Thread locker (Loctite-style) is not a substitute for a nylock on a
  joint you will take apart every weekend. Use what the build calls for.
- The next ticket, [Materials & Stock](../materials-stock/), is what
  those fasteners go *into*: 1×1 tube is not 2×1 tube, and polycarbonate
  is not a cutting board.
