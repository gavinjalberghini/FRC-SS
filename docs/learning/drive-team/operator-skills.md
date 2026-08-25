---
layout: drive-lesson
title: Operator Skills
subtitle: Mechanism timing, button discipline, and coordinating with the driver without talking over them.
permalink: /learning/drive-team/operator-skills/
role: veteran
order: 5
size: 2
time: "1–2 hrs"
---

## Description

The operator’s job is to make mechanisms boring: same button, same
timing, same result. Fancy one-off sequences are how you miss in elims.
This ticket is timing, bindings, and how two people share one robot
without a debate.

You already ran timed cycles in
[Driving Fundamentals](../driving-fundamentals/). Those times included
the operator even if one person held both sticks. Officially, FIRST
calls both of you
[DRIVERs](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
(Table 6-1). The playbook still splits the jobs: the driver delivers
pose; the operator delivers the mechanism. If the pose is wrong, do not
fire and blame the driver after.

One voice to the driver still holds. The operator does not narrate.
Short cues only: "ready," "scoring," "jam," "stowed." If you need a
paragraph, the binding or the robot is wrong. Mentors do not grab the
operator's controller to "just hit score." They can ask you to walk the
bindings out loud. Software should make illegal or self-destructive
combos hard. You still need to know what a stuck button does.

This site does not track who is starting at operator. Hours in the
practice log beat a claim that you "know the buttons." If your team
exported these tickets, close this issue there once a mentor accepts the
criteria below.

## Prerequisites

- [Driving Fundamentals](../driving-fundamentals/) — you have a written
  cycle drill and a log.
- [The Driver Station](../driver-station/) — USB order is the order you
  practiced, not "whatever plugged in."
- A robot (or a mechanism on a cart) whose intake, score, stow, and
  climb bindings you can actually press. A binding sheet from
  programming if one exists.

## What you'll learn

- How to bind and practice mechanisms as drills, not vibes.
- When to act versus when to wait for the driver.
- How to fail a cycle without failing the next one.
- A three-word vocabulary you will reuse in
  [In-Match Communication](../in-match-communication/).

## Tasks

1. **Watch mechanism timing in a real match.** Watch
   [Einstein Final 1 — 2026 FIRST Championship](https://www.youtube.com/watch?v=EjF9we707DA)
   and pick one robot with a visible second student on a controller. For
   three cycles, mark when the mechanism moves relative to when the
   drivetrain stops. Write one sentence: *The operator waited for pose*
   or *The operator fired while still moving* and what happened. You
   are training your eyes, not judging world champions.

2. **Walk the bindings in the dark.** With the robot disabled (or the
   controller unplugged from the DS), hold the operator controller and
   recite out loud, without looking at the buttons:

   - intake
   - score / launch / dump (use your robot's word)
   - stow
   - climb
   - cancel / panic (whatever stops a stuck command)
   - what a held or stuck button does

   Then plug in, open the DS
   [USB Devices tab](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html),
   and confirm this controller is in the slot the code expects. Walk
   the list again with a mentor watching your thumbs, not the robot.
   One action per control when you can. Mode-shift only if you practice
   it weekly. Do not rematch bindings the morning of an event without a
   practice block after.

3. **Write the operator half of the cycle drill.** Add four lines to the
   drill card from [Driving Fundamentals](../driving-fundamentals/):

   - **Ready:** what the operator says when the mechanism can legally
     fire.
   - **Fire rule:** pose must be good; if not, do not fire.
   - **Jam recovery:** cancel, stow, clear the piece if the rules
     allow, get to the next start pose. Do not hold a failing command.
   - **Time budget:** the driver may not sit still more than a defined
     number of seconds for your recovery (agree on a number; 3 and 5
     are common).

   This is the start of the communication script. Keep it to those
   four lines.

4. **Run ten score attempts with a driver.** Timed. Same start pose
   every time. A third person logs make / miss and the cause (pose,
   binding, jam, brownout, "I guessed"). The coach may say the clock
   ("60," "endgame") and nothing else. Mentors stay off both
   controllers. If you brown out, back off as
   [The Driver Station](../driver-station/) taught; that cycle is a
   miss with cause "brownout."

5. **Demonstrate a jam recovery.** Have a partner create a safe, legal
   jam (or call "jam" and pretend if you cannot jam safely). Cancel,
   stow, clear if allowed, next start pose. The drivetrain may pause
   no longer than the time budget on the card. Tell the coach once.
   Then the next cycle. Do not hold a funeral for the missed shot.

6. **Lock a three-word vocabulary with your driver.** Agree on exactly
   three words you will use in a practice match (recommended: **ready**,
   **jam**, **stowed**). Write them on the role map. Run one short
   practice match using *only* those words plus the coach's clock
   calls. If you talk more than that, the robot is driving you.

## Acceptance Criteria

- [ ] You can recite the binding map (intake, score, stow, climb,
      cancel, stuck-button) without looking at the controller. A mentor
      heard it.
- [ ] Ten score attempts are logged with make/miss and cause. The
      session used the written fire rule.
- [ ] You demonstrated a jam recovery that kept the drivetrain pause
      under the agreed time. Mentor-checkable on a field or mock field.
- [ ] A three-word vocabulary is written on the role map and was used
      in a practice match with no extra chatter.
- [ ] USB order on the DS matches the practiced operator slot.

## Resources

- [WPILib: FRC Driver Station — USB Devices](https://docs.wpilib.org/en/stable/docs/software/driverstation/driver-station.html)
- [WPILib: Reading Buttons on Joysticks](https://docs.wpilib.org/en/stable/docs/software/basic-programming/joystick.html)
  (if you need to talk to programming about a binding)
- [Programming: Reading Driver Input](../../programming/driver-input/)
- [Einstein Final 1 (YouTube)](https://www.youtube.com/watch?v=EjF9we707DA)
- [2026 Game Manual Table 6-1](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
- [Driving Fundamentals](../driving-fundamentals/)
- [In-Match Communication](../in-match-communication/) — next place
  this vocabulary grows
- [Human Player](../human-player/) — next ticket

## Notes

- If one student is both driver and operator, still walk the binding
  map. Mode-shift under stress is how you climb in the first shift.
- "Software will prevent that" is not a binding. Know the failure.
- The human player is not a fourth voice. Their signal comes in
  [Human Player](../human-player/).
- The next ticket is the outpost. Operators who ignore it still jam
  when a piece arrives late.
