---
layout: strategy-lesson
title: Designing a Scouting System
subtitle: Decide what to collect, who collects it, and whether a sheet or an app will survive a Friday night.
permalink: /learning/strategy-scouting/scouting-system-design/
role: scout
order: 4
size: 2
time: "1–2 hrs"
---

## Description

A scouting system is a product used by tired people in a loud stands. If it
needs a 20-minute training or a perfect network, it will fail at the first
event. This ticket is how to choose *what* to collect and *how*, before you
fall in love with a form.

You already named an alliance role and a must / should / won't list in
[Robot Priorities](../robot-priorities/).
Those decisions tell you which *other* robots you care about. First pick,
second pick, defense assignment, auto coordination — each proposed field
on the sheet must change one of those decisions. If it does not, it is
decoration.

Typical quantitative set for almost any FRC game: auto success, cycle
count or scoring actions (defined the way you defined a cycle in
[Scoring, Cycles & Penalties](../scoring-and-cycles/)),
endgame result, major fouls, disabled. Everything else is optional until
the core is reliable. A perfect metric on 12 teams is worse than a crude
metric on 40.

**Paper** survives dead phones and venue Wi-Fi. It is slower to aggregate.
**Apps** (QRScout, custom forms, TBA-backed tools) aggregate fast and fail
when the tablet dies. A hybrid is common: app first, paper backup, one
person entering. Pick for the people you have, not the demo you saw on
Chief Delphi. Read
[What do you expect from a scouting app?](https://www.chiefdelphi.com/t/what-do-you-expect-from-a-scouting-app/506324)
far enough to steal the requirement "data available when the coach needs
it," not far enough to start a rewrite of someone else's stack.

Staffing is part of the design. Every match needs enough scouts to cover
six robots without one person watching two. Pit scouting is a different
shift from match scouting; the next two tickets split them. A scout lead
sits where they can see the field *and* the incoming data.

This website does not store scouting databases and does not become your
event app. Design the schema here; keep the filled sheets on paper or in
a tool your team owns. You will *use* the paper sheet in
[Pit Scouting](../pit-scouting/)
and
[Match Scouting](../match-scouting/).

## Prerequisites

- [Robot Priorities](../robot-priorities/)
  completed (role sentence and must / should / won't).
- The cycle definitions from
  [Scoring, Cycles & Penalties](../scoring-and-cycles/).

## What you'll learn

- How to pick metrics that change alliance decisions, and how to reject
  the rest.
- Paper vs. app trade-offs, including the Friday-night failure mode you
  are accepting.
- How to staff scouting so it does not eat the pit.

## Tasks

1. **Write the decision list first.** Before any columns, write the four
   decisions this system must support at an event:

   - Who is our first pick?
   - Who is our second pick / third robot?
   - Whom do we defend or avoid in our own matches?
   - How do we coordinate auto and endgame with partners?

   If a later field does not map to one of these, cut it.

2. **Draft a metric list (the schema).** For each proposed field, write
   one line: **field name — type (number / enum / yes-no / text) —
   decision it changes — can a trained scout record it in real time?**
   Start from this minimum and add only what you will use:

   - team number, match number, alliance color, scout name
   - auto: success / fail / pieces or action, plus "left starting zone"
     if the game cares
   - teleop: cycle count *or* scoring bursts, using *your* cycle
     definition (one sentence)
   - endgame: result enum (none / park / level 1 / 2 / 3 — adapt to
     this year)
   - flags: disabled, no-show, major foul, yellow/red card
   - one short text box, not a novel

   That list *is* the scouting schema. Keep it to one side of a sheet.
   High-volume games (REBUILT fuel) cannot be counted as individual
   pieces; Chief Delphi's
   [Scouting Methods](https://www.chiefdelphi.com/t/scouting-methods/511265)
   thread is full of +5/+10 and balls-per-second ideas. Pick a
   definition you can train in ten minutes.

3. **Build a paper sheet.** On literal paper (or a printed one-pager),
   lay out the schema so a scout can fill it without reading a legend
   mid-match. Large checkboxes, a cycle tally that can be hashed, team
   number at the top in huge type, a "I lost the robot" box. Time
   yourself drawing it. If a field needs a paragraph of instructions, it
   is not a Friday-night field — move it to qualitative notes
   ([Qualitative & Super Scouting](../qualitative-scouting/),
   two tickets from now).

4. **Choose paper, app, or hybrid and name the failure.** Write one
   paragraph: what you will use at the next event, what dies first
   (phones, Wi-Fi, the one laptop with the sheet, the scout who knows
   the app), and the backup. If you want to see an app, skim
   [QRScout](https://github.com/FRC2713/QRScout)
   and the
   [QRScout 2026 thread](https://www.chiefdelphi.com/t/qrscout-2026/510981).
   You are not required to deploy it. You are required to know that TBA
   prefills match lists and does **not** replace your columns.

5. **Draft a staffing plan for a 12-hour Friday.** Assume a typical
   qualification schedule (matches about every 7–10 minutes once the
   field is rolling). Write:

   - how many match scouts per match (six is the honest number)
   - who is *not* match-scouting because they are in the pit or on
     drive crew
   - a pit-scout shift that does not overlap the same three people all
     day
   - where the scout lead sits
   - who aggregates paper into whatever the coach will read Saturday
     morning

   If your team has four scouts total, design for four — including the
   ugly compromise — instead of a fantasy roster of twelve.

6. **Time a teammate on a recorded match; cut what they miss.** Hand
   the paper sheet to a teammate who did not design it. Play
   [Einstein Finals 1](https://www.youtube.com/watch?v=EjF9we707DA)
   (or Quals from a Week 1 event on
   [TBA](https://www.thebluealliance.com/)
   that has video). They scout **one** assigned bumper. You watch them,
   not the field. Cross out every field they skip, guess, or ask you
   about. Update the schema. The sheet that survives Friday is the one
   a tired freshman can finish.

## Acceptance Criteria

- [ ] A scouting schema exists: each field has a type, a decision it
      changes, and a yes/no on real-time recordability.
- [ ] A paper sheet exists (photo or PDF is fine) that fits one side
      and uses the schema.
- [ ] Paper, app, or hybrid is chosen in writing, with the failure mode
      you are accepting and the backup.
- [ ] A 12-hour Friday staffing plan exists, including who is *not*
      scouting.
- [ ] A teammate filled the sheet on a recorded match; at least one
      field was cut or simplified because they missed it.
- [ ] A mentor can explain the schema back to you from the paper alone.

## Resources

- [The Blue Alliance](https://www.thebluealliance.com/)
- [TBA API docs (v3)](https://www.thebluealliance.com/apidocs/v3)
- [Statbotics](https://www.statbotics.io/)
- [QRScout (GitHub)](https://github.com/FRC2713/QRScout)
- [Chief Delphi: What do you expect from a scouting app?](https://www.chiefdelphi.com/t/what-do-you-expect-from-a-scouting-app/506324)
- [Chief Delphi: Scouting Methods](https://www.chiefdelphi.com/t/scouting-methods/511265)
- [Chief Delphi: QRScout 2026](https://www.chiefdelphi.com/t/qrscout-2026/510981)
- [Einstein Final 1 (YouTube)](https://www.youtube.com/watch?v=EjF9we707DA)
- [Robot Priorities](../robot-priorities/)
- [Pit Scouting](../pit-scouting/)
- [Match Scouting](../match-scouting/)

## Notes

- Collecting a column you will not look at is how scouts stop trusting
  the system. Cut until it hurts, then add back one field after the
  first event — not before.
- TBA and Statbotics will reappear in
  [Data Analysis](../data-analysis/)
  as *complements*. They are not a reason to skip match scouting.
- Do not assign the same three people to pits and stands all day. They
  will silently drop one of the two.
- Next:
  [Pit Scouting](../pit-scouting/)
  (order 5), then
  [Match Scouting](../match-scouting/).
  Bring the paper sheet. You will fill it from video before you fill it
  in a venue.
