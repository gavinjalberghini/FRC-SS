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

## Overview

Unskilled technicians jump randomly from device to device, prioritizing the
parts they're most comfortable with. Level 3 technicians follow a **disciplined,
repeatable process** that finds the real fault quickly without breaking working
hardware. This lesson teaches that process and the team protocols that make
troubleshooting a coordinated, safe activity.

## Prerequisites

- [Status Lights & Fault Codes](../status-lights-fault-codes/).
- All Level 1 and Level 2 lessons.

## What you'll learn

- A step-by-step troubleshooting procedure.
- How to swap and verify a suspect device.
- Team protocols for safe, communicated troubleshooting.

## Unit 1 — The troubleshooting procedure

1. **Mentally isolate the subsystem** that's failing.
2. **Check the trouble/signal lights** for a clue (you learned these last lesson).
3. **Start closest to the affected device** (motor, solenoid, sensor). Have a
   programmer check the code for that item while you check the hardware side.
4. **Check every input to that device** — power, signal, and air — looking for
   loose, weak, broken, or poorly crimped/soldered connections.
5. **Move up the subsystem**, branching and checking at each point, until you
   reach a **known-good item** — a device that serves multiple things where the
   *others* still work.

The goal is to converge on the fault, not to randomly replace parts.

## Unit 2 — Resolving the problem

Once a probable bad device is identified:

1. **Quick-swap an identical part.** Communicate the swap to all subsystem leads
   so they can make any needed changes (CAN IDs, config) during the swap.
2. **Check it, check it again, then check it once more** after the swap.
3. If hardware fixes don't resolve it, **communicate everything the hardware team
   tried** to the lead programmer — the issue may be in code.

## Unit 3 — Team troubleshooting protocols

Troubleshooting is a team activity with a verbal protocol:

1. Call out: **"I'm troubleshooting ______"** (pneumatics / electrical /
   drivetrain).
2. A **second person** with certification in that area "hovers" and assists.
3. The **primary** verbalizes what they're checking and what they're thinking.
4. The **secondary** listens and only speaks up if a step or trouble spot was
   missed. (If no certified secondary is available, a mentor steps in.)

This catches mistakes, trains newer members, and keeps everyone safe.

## Steps & acceptance criteria

- [ ] Walk through the 5-step procedure on a staged fault without skipping steps.
- [ ] Correctly identify a "known-good item" in a subsystem.
- [ ] Perform a communicated device swap and re-verify.
- [ ] Run the verbal troubleshooting protocol as both primary and secondary.

## Resources

- [WPILib: Preemptive Troubleshooting](https://docs.wpilib.org/en/stable/docs/hardware/hardware-basics/robot-preemptive-troubleshooting.html)
- [WPILib: Driver Station / diagnostics](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html)

## Notes

<div class="callout">
  <div class="callout-icon">📌</div>
  <p>Placeholder — adapt the verbal protocol to your team's roles and document who the certified "secondary" can be for each subsystem.</p>
</div>
