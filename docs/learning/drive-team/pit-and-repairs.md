---
layout: drive-lesson
title: Pit Crew & Between-Match Repairs
subtitle: Diagnose fast, fix what matters, and get back in queue without making it worse.
permalink: /learning/drive-team/pit-and-repairs/
role: veteran
order: 9
size: 2
time: "1–2 hrs"
---

## Description

The pit is an emergency room with a schedule. The next match will arrive
whether the robot is ready or not. This ticket is triage: what to fix,
what to leave, and how to stop a helpful crowd from turning a 4-minute
job into a 20-minute one.

You already have a [pre-match card](../pre-match-checklist/) and you
already know comms versus brownout from
[The Driver Station](../driver-station/). When the robot comes off the
field, the drive team owes the pit a **30-second report** — symptom, not
theory — then they get out of the way. Debugging-by-committee starts
with six people holding Allen keys.

One technician leads. Others fetch; they do not invent a second
diagnosis. Disconnect the battery before hands go in. Vent pneumatics.
See [Electrical Safety](../../electrical/electrical-safety/). Mentors
may advise. They do not take the driver sticks to "test it quickly" if
a student can enable. They also do not weld a new idea onto a robot
that has to queue in eight minutes.

If you cannot finish before queue, you go with a known limitation and a
match-plan change — not a half-finished gearbox. The coach updates the
one-sentence plan. Practice hours on timed repairs beat a shop legend
about how fast you *could* change a belt.

This site does not track repairs. If your team exported these tickets,
attach the timed-repair notes and close the issue once a mentor accepts
the criteria below.

## Prerequisites

- [Pre-Match Checklist](../pre-match-checklist/) — battery and bumper
  swap times already written.
- [Electrical: Systematic Troubleshooting](../../electrical/troubleshooting/)
  if you will touch electrical; otherwise a technician who has.
- [Electrical Safety](../../electrical/electrical-safety/).
- A practice robot you are allowed to make a known, safe "failure" on
  (loose chain, unplugged stick, tired battery — not a cut wire).

## What you'll learn

- How to take a 30-second report from the drive team.
- How to triage against the match clock.
- How to keep the pit safe and quiet enough to work.
- Which five spares you will not travel without.

## Tasks

1. **Watch what a dead robot looks like after the fact.** Skim
   [Driver Station Log File Viewer](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station-log-viewer.html)
   so you know that brownouts, comms drops, and FMS-connected matches
   leave a log. You do not need to master the viewer in this ticket.
   Write one line on the 30-second report card: *If they say comms or
   brownout, pull the DS log before you guess.* Then read
   [roboRIO Brownouts](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-brownouts.html)
   for the 12V fault counter you already pointed at.

2. **Write the 30-second report script.** One card, three lines the
   driver or coach says when the robot comes off the field:

   - **What failed** (symptom, not theory): "intake dead," "browned out
     twice," "left rear module clicking."
   - **When it started** (auto, shift 2, last cycle).
   - **Can we play the next match if that thing stays broken?** yes /
     yes with a plan change / no.

   Then they leave the robot. The lead technician repeats the three
   lines out loud so the pit heard the same report. Practice this
   script after a practice "failure" in Task 4.

3. **Triage against a clock.** Write three buckets on the back of the
   card:

   - **Must fix to play**
   - **Nice to fix**
   - **Wait for a longer window**

   Using the battery-swap and bumper-swap times from the pre-match
   card, plus one more timed repair (belt, chain, or module — pick
   what *your* robot actually breaks), decide which bucket each
   repair is in for a typical 8–15 minute cycle. If you do not know
   the event cycle time, use 10 minutes. Write the number.

4. **Run a timed known repair with one lead.** Safety first: battery
   disconnected, pneumatics vented, glasses on. Time a real repair you
   already measured or the new belt/chain/module. One person leads.
   Others fetch only what the lead names. No second diagnosis. When
   the repair is done, reconnect, run the
   [pre-match card](../pre-match-checklist/) through battery and
   enable-on-blocks. Write the total time (repair + card). If it does
   not fit between matches, that repair is "wait" or "no-go," not
   "we'll try."

5. **Run a troubleshooting pass with a silent pit.** Plant a safe
   failure (unplugged encoder, USB stick swapped, bumper strap, radio
   power). Drive team gives the 30-second report. Lead technician
   works. Everyone else is quiet unless they are fetching. A mentor
   watches for crowd size and for hands in a live robot. Stop if
   safety slips. The
   [electrical troubleshooting](../../electrical/troubleshooting/)
   ticket is the method; this ticket is the room.

6. **List the five spares you will not go to an event without.** Be
   specific (belts of *this* width, bumper hardware, batteries,
   a swerve module, radio power lead — your robot, not a generic
   list). Put the list on the cart or in the pit bible. Food,
   homework, and visitors belong behind the tape, not on the robot.

## Acceptance Criteria

- [ ] A 30-second report script exists and was used after a practice
      failure. A mentor heard the three lines.
- [ ] At least one known repair is timed, including the re-run of the
      pre-match card, and is assigned to must / nice / wait.
- [ ] A troubleshooting pass ran with one lead and a silent pit.
      Mentor-checkable in the shop.
- [ ] Five named spares are written down.
- [ ] You can state the battery-disconnect rule without looking at this
      page.

## Resources

- [WPILib: Driver Station Log Viewer](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station-log-viewer.html)
- [WPILib: roboRIO Brownouts](https://docs.wpilib.org/en/stable/docs/software/roborio-info/roborio-brownouts.html)
- [WPILib: Driver Station Errors/Warnings](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station-errors-warnings.html)
- [Electrical: Troubleshooting](../../electrical/troubleshooting/)
- [Electrical: Electrical Safety](../../electrical/electrical-safety/)
- [Mechanical: Assembly, Tolerances & Maintenance](../../mechanical/assembly-tolerances-maintenance/)
- [2026 Game Manual — G301 cycle times, section 6.3](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
- [Inspection & the Technician](../inspection-technician/) — next
  ticket

## Notes

- A half-finished gearbox in queue is how you miss the match *and*
  inspection. Known limitation plus a plan change is a legal robot.
  An open gearbox is not.
- Re-inspection exists. A "quick weld" or a new mechanism can put you
  back in line. The next ticket owns that question.
- Tools have homes. A floor full of parts is how you miss a fastener
  and the match.
- The next ticket ([Inspection & the Technician](../inspection-technician/))
  is how you stay legal after you fix it.
