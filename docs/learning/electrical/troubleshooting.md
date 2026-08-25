---
layout: electrical-lesson
title: Systematic Troubleshooting & Team Protocols
subtitle: A repeatable method for isolating faults, plus the team protocols that keep troubleshooting safe and fast.
permalink: /learning/electrical/troubleshooting/
role: lead
order: 11
size: 2
time: "1–2 hrs"
---

## Description

Unskilled technicians jump from device to device, starting with the
parts they already know how to swap. Level 3 technicians follow a
**disciplined, repeatable process** that finds the real fault without
breaking working hardware. This ticket is that process, plus the verbal
protocol that keeps two people and a live robot from surprising each
other.

You already have the dictionary
([Status Lights & Fault Codes](../status-lights-fault-codes/)), the
power tree ([Power Distribution](../power-distribution/)), the signal
tree ([The FRC Control System](../control-system/),
[roboRIO Ports](../roborio-ports/)), and the craft standard
([Wiring Craftsmanship](../wiring-craftsmanship/)). Troubleshooting is
those tickets used in order, not a new kind of magic.

The physics does not change when you are in a hurry. A short still
melts metal. A half-seated Anderson still browns the roboRIO. A CAN
pair with one loose ferrule still takes down every device past the
break. The safe state still comes first: if you are going to pull
connectors, **battery off, pressure vented, robot on blocks**, then
announce before power comes back.

You will write a fault tree for the most common pit sentence — **"the
robot won't enable"** — and you will walk a staged fault without
skipping steps. The website will not grade the tree. A mentor will.

This site does not track whether you finished. If your team exported
these tickets into its own GitHub, close this issue there once a
mentor accepts the criteria below.

## Prerequisites

- [Status Lights & Fault Codes](../status-lights-fault-codes/)
  completed (pit card in your pocket).
- All Technician and Veteran tickets (safety through pneumatics
  construction). You cannot isolate a subsystem you cannot name.
- A mentor willing to stage a safe fault (loose CAN, tripped
  breaker, unplugged RSL, DS not set to the right team number —
  not a dead short).

## What you'll learn

- A five-step troubleshooting procedure that converges on a fault
  instead of replacing parts at random.
- How to swap a suspect device once, communicate the swap, and
  re-verify three times.
- The verbal protocol that makes troubleshooting a two-person,
  safe activity.

## Tasks

1. **Read the official "fix it before it breaks" pages.** Read
   [WPILib: Preemptive Troubleshooting](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/preemptive-troubleshooting.html)
   (battery connections, secured SB50, tug tests, whiskers) and
   [WPILib: Wiring Best Practices](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-best-practices.html).
   Skim
   [WPILib: Driver Station](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html)
   far enough to know where the DS reports comms, code, E-stop,
   and joystick. CTRE's
   [CAN bus troubleshooting](https://v6.docs.ctr-electronics.com/en/stable/docs/troubleshooting/canbus-troubleshooting.html)
   is the page you open when a row of motor LEDs goes red.

2. **Memorize the five-step hunt — then use it, in order.**

   1. **Mentally isolate the subsystem** that is failing (enable,
      drive, one mechanism, radio, pneumatics). If you cannot
      name the subsystem, you are not troubleshooting yet.
   2. **Read the lights** you learned last ticket. RSL, roboRIO
      Comm/Power/Mode, PDH, the nearest motor controller, PH.
      Write what you see *before* you touch a wire.
   3. **Start closest to the affected device** (motor, solenoid,
      sensor, "the enable path"). Have a programmer check the
      code and the Driver Station for that item while you check
      hardware.
   4. **Check every input to that device** — power, signal, and
      air — for loose, weak, broken, or badly crimped joints.
      Tug. Look for whiskers. Jostle the harness the way CTRE
      describes.
   5. **Move up the subsystem** until you reach a **known-good
      item**: a device that serves multiple things, where the
      *others* still work. If three motors on the same PDH are
      fine and the fourth is dead, the PDH is probably not the
      fault. If nothing on CAN answers, the bus or the roboRIO
      is.

   The goal is to converge, not to empty the spare-parts drawer.

3. **Write a fault tree for "robot won't enable."** One page,
   your own words, that a mentor can watch you walk. Start from
   the symptom and branch on *observations*, not vibes. A
   minimum tree includes:

   - Safe state / on blocks / announce — you do not enable a
     robot on the cart in a crowd.
   - **RSL off** vs. solid vs. blinking. Off → roboRIO power,
     RSL wiring, main breaker, battery / Anderson / 6 AWG lugs.
   - **roboRIO Power** amber (brownout / battery / main leads)
     vs. red (user-rail short) vs. green.
   - **Comm off** (radio, Ethernet, DS IP / team number, Wi-Fi)
     vs. **Comm solid red** (no user code — deploy, crash,
     Status blinks) vs. **Comm blinking red** (E-stop) vs.
     green.
   - **Mode stays off** when the DS says enable → brownout,
     E-stop, DS not actually enabling, or a disabled-by-fault
     controller path.
   - Battery voltage under load, main breaker, and the "lights
     should match" check from last ticket.

   You may draw boxes or write nested bullets. You may not write
   "check everything." Put this page in the team's learning repo
   or a pit binder. This website will not store it.

4. **Walk a staged fault.** A mentor stages one problem (examples:
   DS not connected, a tripped branch breaker, CAN unplugged at
   one controller, RSL unplugged). You:

   - Call out **"I'm troubleshooting electrical"** (or
     pneumatics / drivetrain).
   - Run the five steps out loud. A certified secondary (or the
     mentor) hovers and only speaks if you skip a step.
   - Stop at the known-good item. Name it.
   - Fix only the fault you found. Re-check lights. Check
     again. Check once more.

5. **Practice a communicated swap.** If the staged fault is a
   device, quick-swap an identical spare. Tell every subsystem
   lead what changed (CAN ID, firmware, "this SPARK is now
   brushed"). After the swap: check, check again, check once
   more. If hardware is now clean and the symptom remains, walk
   to the lead programmer with a list of what you tried — not
   "code is broken" as a first sentence.

6. **Run the verbal protocol from both seats.**

   1. Primary: **"I'm troubleshooting ______."**
   2. A second certified person hovers.
   3. Primary verbalizes what they are checking and what they
      think.
   4. Secondary speaks only to catch a missed step or a safety
      miss. If no certified secondary exists, a mentor sits
      there.

   Do it once as primary and once as secondary. This is how you
   avoid two people enabling a robot that still has a hand in
   it.

7. **Hand in the tree.** A mentor reads the "won't enable" page
   and watches one staged hunt. If your team exported these
   tickets, attach the fault tree and move the issue to In
   Review.

## Acceptance Criteria

- [ ] You walked the five-step procedure on a staged fault
      without skipping "read the lights" or "name the known-good
      item."
- [ ] You correctly identified a known-good item in that
      subsystem (something that still works and shares a power
      or signal parent with the failure).
- [ ] You performed a communicated device swap (or explained why
      the staged fault did not need one) and re-verified three
      times.
- [ ] You ran the verbal protocol as primary and as secondary.
- [ ] A written fault tree for "robot won't enable" exists,
      branches on RSL / roboRIO Comm / Power / Mode / battery,
      and a mentor can follow it without you narrating.

## Resources

- [WPILib: Preemptive Troubleshooting](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/preemptive-troubleshooting.html)
- [WPILib: Wiring Best Practices](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/wiring-best-practices.html)
- [WPILib: Status Light Quick Reference](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/status-lights-ref.html)
- [WPILib: Driver Station](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html)
- [CTRE: CAN bus troubleshooting](https://v6.docs.ctr-electronics.com/en/stable/docs/troubleshooting/canbus-troubleshooting.html)
- [REV PDH troubleshooting](https://docs.revrobotics.com/ion-control/pdh/troubleshooting)
- [REV SPARK MAX troubleshooting](https://docs.revrobotics.com/brushless/spark-max/troubleshooting)

## Notes

- If you cannot say the subsystem in one word, you are not ready
  to pull a connector.
- The last ticket,
  [Pneumatics 3: Calculations & Troubleshooting](../pneumatics-troubleshooting/),
  applies this same hunt to air — plus the force and volume math
  that tells you whether the system was ever going to keep up
  with the match.
