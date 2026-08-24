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

## Overview

Most FRC games are cycle games wearing different costumes. A cycle is a
repeatable loop: acquire a game piece, score it, return. This lesson is how
to turn the scoring table into cycle math — and how to respect the fouls
that make that math worthless.

## Prerequisites

- [Reading the Game](../reading-the-game/)

## What you'll learn

- How to define a cycle for this season’s game.
- How to compare actions by points per second, not points per highlight.
- Which penalties are strategy and which are just losing.

## Unit 1 — Name the cycles

For each scoring action, write:

- **Start condition** (where the piece is, where the robot is).
- **End condition** (scored, and the robot ready to start again).
- **Likely time** for a practiced team vs. a mid-pack team.
- **Failure modes** (drop, jam, miss, dead robot).

If you cannot time it, you cannot prioritize it. Use a stopwatch on video
from a similar past game if this year’s field is not built yet.

## Unit 2 — Points per second

A 5-point action that takes 4 seconds beats a 10-point action that takes
20 — until endgame, when the clock is the constraint.

- Compute optimistic and realistic cycle times.
- Add **setup cost**: a mechanism that only works after a long climb or a
  precise align.
- Endgame is usually a one-shot with a huge swing. Treat it as its own
  cycle with a hard deadline.

## Unit 3 — Penalties as negative cycles

- A foul that costs as much as two cycles is not “aggressive defense.” It
  is a strategy error.
- Disable and yellow/red cards are match-loss events. Design them out
  (bumper rules, zone rules, contact).
- Human-player errors count. Strategy includes the people off the robot.

## Steps & acceptance criteria

- [ ] Define at least two scoring cycles with start, end, and a time
      estimate.
- [ ] Rank those cycles plus endgame by points per second under a realistic
      time.
- [ ] List three fouls that would erase one good cycle.
- [ ] Explain one action that looks impressive on video but loses on math.

## Resources

- [FRC Game Manual](https://www.firstinspires.org/resource-library/frc/competition-manual-qa-system)
- [Statbotics](https://www.statbotics.io/) — how cycle-like metrics show up in real results.
- [Robot Priorities](../robot-priorities/)
