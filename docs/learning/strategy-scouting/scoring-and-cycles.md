---
layout: strategy-lesson
title: Scoring, Cycles & Penalties
subtitle: Break the game into cycles, points-per-second, and the penalties that erase a good match.
permalink: /learning/strategy-scouting/scoring-and-cycles/
role: scout
order: 2
size: 2
time: "1–2 hrs"
---

## Description

Most FRC games are cycle games wearing different costumes. A **cycle** is a
repeatable loop: acquire a game piece (or reach a scoring position), score
it, return to a state where you can start again. This ticket turns the
scoring table from
[Reading the Game](../reading-the-game/)
into cycle math — and into respect for the fouls that make that math
worthless.

**Points per second** is the comparison that survives highlight videos. A
5-point action that takes 4 seconds beats a 10-point action that takes 20,
until endgame, when the clock is the constraint. Endgame is usually a
one-shot with a huge swing. Treat it as its own cycle with a hard deadline
and a setup cost (align, climb, wait for a partner).

REBUILT (2026) makes this concrete and slightly awkward: fuel in an active
hub is 1 point each, so a "cycle" at Einstein is a burst of shots, not a
single ball. Mid-pack robots still take visible trips. If you are on a
later game with discrete pieces (coral, notes, cubes), count pieces. The
worksheet is the same: start condition, end condition, time, points,
failure modes.

Penalties are negative cycles. In 2026 a **MINOR FOUL** is 5 points to the
opponent and a **MAJOR FOUL** is 15 — Table 6-6 in
[Section 6.6 Violations](https://firstfrc.blob.core.windows.net/frc2026/Manual/HTML/2026GameManual.htm).
A foul that costs as much as two of your cycles is not "aggressive
defense." It is a strategy error. Disable, yellow, and red cards are
match-loss events. Design them out. Human-player errors count; strategy
includes the people off the robot.

This site does not store your cycle table. Keep it with the game brief
from the last ticket. You will hand the ranked cycles to
[Robot Priorities](../robot-priorities/)
so the must / should / won't list is about math, not vibes.

## Prerequisites

- [Reading the Game](../reading-the-game/)
  completed (scoring table in your notes, one-page brief).
- A stopwatch (phone clock is fine) and the Einstein Finals 1 video you
  already watched.

## What you'll learn

- How to define a cycle for this season's game so two scouts mean the
  same loop.
- How to compare actions by points per second, including setup cost and
  endgame deadlines.
- Which penalties erase a good match, and how to write them next to the
  cycle they cancel.

## Tasks

1. **Name at least two scoring cycles.** Using your scoring table from
   the last ticket and
   **Section 6.5** /
   **Table 6-4**
   in the
   [2026 Game Manual](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
   (or this year's table), write a row for each cycle:

   - **Name** (example: "hub cycle," "tower climb," "human-player feed").
   - **Start condition** — where the piece is, where the robot is.
   - **End condition** — scored, and the robot ready to start again.
   - **Points** if it succeeds (match points, and ranking points if any).
   - **Failure modes** — drop, jam, miss, dead robot, inactive hub.

   You need at least two scoring cycles plus endgame as its own row.
   If you cannot describe start and end in one sentence each, you cannot
   time it later.

2. **Watch a specific match and time cycles.** Re-open
   [2026 Einstein Finals 1](https://www.youtube.com/watch?v=EjF9we707DA)
   and
   [the TBA breakdown](https://www.thebluealliance.com/match/2026cmptx_f1m1).
   Pick **one** robot (write the team number). With a stopwatch:

   - Time three visible scoring bursts or trips for that robot (acquire
     → score → ready again). If the robot never leaves the hub, time
     "start shooting → stop shooting → start again."
   - Time the endgame action if they attempt the tower, or write "no
     attempt" and the clock when they would have had to start.

   Write optimistic time (best of the three) and realistic time (median).
   Einstein fuel volume is not countable by eye; you are measuring *loop
   time*, not official score. TBA's fuel totals are the alliance sanity
   check, not your per-robot count.

3. **Compute points per second.** For each cycle row:

   ```text
   pps = points_if_success / realistic_time_seconds
   ```

   Add a **setup cost** column: extra seconds before the first cycle
   (align, cross a bump, wait for a shift). Rank the cycles plus endgame
   by realistic pps. Then write one sentence on an action that looks
   impressive on video but loses on math — a long climb that is late, a
   far shot with a low hit rate, a mechanism that only works after a
   20-second align.

4. **List three fouls that erase one good cycle.** Read
   **Section 6.6** and skim **Section 7 Game Rules (G)** for contact,
   zone, and scoring-element rules (in 2026,
   [G407](https://firstfrc.blob.core.windows.net/frc2026/Manual/HTML/2026GameManual.htm)
   "only score while in your alliance zone" is a classic). For each of
   three fouls, write: rule number, points given to the opponent, and
   which of your cycles it cancels. Include at least one human-player or
   card-level event.

5. **Sanity-check against public data — do not outsource the table.**
   Open the same match on
   [The Blue Alliance](https://www.thebluealliance.com/match/2026cmptx_f1m1)
   and look up one of the six teams on
   [Statbotics](https://www.statbotics.io/)
   (team search, then the 2026 season). Write two sentences: what TBA's
   score breakdown tells you that your stopwatch cannot, and what your
   stopwatch tells you that EPA cannot (a jam, a missed climb, a robot
   that stopped trying). Public models complement your notes. They do
   not replace a cycle table.

6. **Optional discrete-piece drill.** If REBUILT bursts feel too fuzzy,
   repeat Task 2 on a prior discrete-piece match your mentor names, or
   pick a Week 1–3 qualification match on
   [TBA events](https://www.thebluealliance.com/events)
   that has video and count scored pieces for one robot. Same worksheet.
   The point is the habit, not Einstein's score.

## Acceptance Criteria

- [ ] A cycle table exists with at least two scoring cycles plus endgame.
      Each row has start, end, points, optimistic time, realistic time,
      setup cost, failure modes, and points per second.
- [ ] One named robot from Einstein Finals 1 (or a mentor-approved
      substitute) has three timed loops written down.
- [ ] Cycles are ranked by realistic points per second, and one
      "impressive on video, loses on math" action is explained in a
      sentence.
- [ ] Three fouls are listed with rule numbers and the cycle they erase.
- [ ] Two sentences exist on what TBA/Statbotics add versus what only
      your timing shows.
- [ ] A mentor can read the table without you narrating it.

## Resources

- [2026 Game Manual (PDF)](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
- [2026 Game Manual (HTML) — Section 6](https://firstfrc.blob.core.windows.net/frc2026/Manual/HTML/2026GameManual.htm)
- [FRC Q&A](https://frc-qa.firstinspires.org/)
- [The Blue Alliance](https://www.thebluealliance.com/)
- [TBA: 2026 Einstein Finals 1](https://www.thebluealliance.com/match/2026cmptx_f1m1)
- [Einstein Final 1 (YouTube)](https://www.youtube.com/watch?v=EjF9we707DA)
- [Statbotics](https://www.statbotics.io/)
- [Statbotics: the EPA model](https://www.statbotics.io/blog/epa)
- [Chief Delphi: zone play in Rebuilt](https://www.chiefdelphi.com/t/how-important-is-zone-play-going-to-be/511023)
- [Reading the Game](../reading-the-game/)
- [Robot Priorities](../robot-priorities/)

## Notes

- If you cannot time it, you cannot prioritize it. A guess with a
  stopwatch on video beats a confident opinion with no clock.
- Endgame pps is a trap if you forget the deadline. A 30-point climb
  that starts at 0:04 is zero points.
- TBA final score is an alliance number. It will not tell you which
  robot of the three did the work. That is why you still watch.
- Next:
  [Robot Priorities](../robot-priorities/).
  Bring this table. Must / should / won't is how the table becomes a
  robot.
