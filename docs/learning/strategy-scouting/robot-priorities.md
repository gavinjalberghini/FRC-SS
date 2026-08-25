---
layout: strategy-lesson
title: Robot Priorities
subtitle: Turn game analysis into a must / should / won't list the design and build teams can execute.
permalink: /learning/strategy-scouting/robot-priorities/
role: scout
order: 3
size: 2
time: "1–2 hrs"
---

## Description

A robot that "does everything" does nothing well in week 6. **Priorities**
are how strategy becomes a build plan: must, should, and won't. This ticket
is how to write that list so CAD and mechanical can say no to good ideas —
and so the shop does not relitigate the same climb every Tuesday.

You already have a scoring table and a cycle table from
[Reading the Game](../reading-the-game/)
and
[Scoring, Cycles & Penalties](../scoring-and-cycles/).
Those are inputs. The output is a short list a fabricator can schedule.
If a cycle cannot be timed or cannot be built by your team in the weeks
you have, it does not belong in **Must**.

**Must** means: if this is missing, the robot cannot play the strategy.
Keep the list short. A drivetrain, one scoring path, and a legal bumper
set are typical musts. A third mechanism is not a must until the first
two are reliable. **Should** is high value after the musts work.
**Won't** is good ideas you are not building this year. Writing them
down is the point. An unwritten won't is an argument that returns every
meeting.

Pick an **alliance role**, not a feature list. Primary scorer,
complementary scorer, defender, endgame specialist — and what you need a
partner to do because you will not. A feature list without a role
produces a robot that is busy and lonely.

When people disagree, use the
[Decision-Making Guide]({{ '/decision-making/' | relative_url }}).
Prototypes and cycle math beat opinions. Phase 3 of the
[Season Roadmap]({{ '/roadmap/' | relative_url }})
is when you prove a must with a cardboard and a stopwatch, not a slide
deck. Revisit the list after the first real test, not after every Slack
message.

This site does not store your priority list. Put it where CAD can find
it. The next ticket,
[Designing a Scouting System](../scouting-system-design/),
asks which of these priorities you will measure on other people's robots.
You cannot scout a role you never named.

## Prerequisites

- [Scoring, Cycles & Penalties](../scoring-and-cycles/)
  completed (cycle table with points per second).
- The
  [Decision-Making Guide]({{ '/decision-making/' | relative_url }})
  — know that contested calls get closed, then supported.

## What you'll learn

- How to write a must / should / won't list that is short enough to
  build.
- How to pick an alliance role, and name the partner capability you are
  refusing to own.
- How to change the list when a prototype fails, without reopening every
  closed won't.

## Tasks

1. **Re-read your cycle ranking out loud.** From the last ticket, list
   the cycles in pps order. Circle the ones *your team* can realistically
   prototype in January (tools, people, last year's drivetrain). Cross
   out a cycle that is high pps on Einstein and low pps for a week-6
   robot you can actually ship. That crossed-out row is a candidate for
   **Won't** or for "we need a partner."

2. **Draft must / should / won't, max four musts.** Write three columns:

   - **Must** — no more than four. Each must maps to a cycle or to
     "legal and movable" (drivetrain, bumpers, a scoring path). If you
     have five musts, you have zero.
   - **Should** — the next pps items, only if the musts are already
     reliable.
   - **Won't** — at least three items, including one *popular* idea
     (the climb everyone saw in the animation, the third game piece,
     the full under-the-bumper intake). Give each won't a reason that
     cites cycle math, a rule, or a schedule constraint — not "we don't
     like it."

   If you need a picture of how other teams do this conversation, skim
   [3128's Kickoff recap](https://www.chiefdelphi.com/t/kickoff-day-1-recap/510906)
   or an Open Alliance kickoff post such as
   [1710's 2026 thread](https://www.chiefdelphi.com/t/frc-team-1710-2026-build-thread-open-alliance/507939).
   Copy the *discipline*, not their robot.

3. **State the alliance role in one sentence.** Fill in:

   > This robot is a \_\_\_\_ (primary scorer / complementary scorer /
   > defender / endgame specialist). We will not \_\_\_\_, so we need a
   > partner who can \_\_\_\_.

   A role that requires two "and also" clauses is two robots. Cut it.

4. **Walk the list with a CAD or mechanical lead.** Sit down (or
   message) someone who will have to *build* the musts. For each must,
   they write a feasibility note: "kit chassis + existing shooter,"
   "needs a custom elevator we have never shipped," "illegal under R-…."
   Record those notes on the same page. If they kill a must, demote it
   *now* and promote a should — do not leave a fantasy must on the list
   "for motivation."

5. **Close one disagreement on paper.** Pick the most popular won't, or
   invent the argument your team will actually have ("we have to climb,
   the animation showed climbing"). Write a five-line decision:

   - option A vs option B
   - the cycle-math or rule evidence
   - who decides (see the
     [Decision-Making Guide]({{ '/decision-making/' | relative_url }}))
   - the call
   - the date you will revisit (after the first real test — not
     Thursday's group chat)

   If your team already closed this, write the closed call and the
   evidence. Relitigating a won't in the shop is how week 6 robots grow
   a fourth mechanism.

6. **Publish a one-page priority sheet.** Same length as the game brief.
   Title, role sentence, three columns, feasibility notes, the closed
   decision, and a pointer back to the cycle table. Give it to the same
   person who received the Kickoff brief. If the two pages disagree, fix
   one of them.

## Acceptance Criteria

- [ ] A robot-priority list exists with no more than four musts, a
      should column, and at least three won'ts.
- [ ] One popular idea is in won't with a reason that cites cycle math,
      a rule number, or schedule — not taste.
- [ ] The alliance role is one sentence and names a partner capability
      you will not own.
- [ ] A CAD or mechanical lead (or a mentor standing in) has written
      feasibility notes on the musts.
- [ ] One disagreement is written as a closed decision with a revisit
      date.
- [ ] The one-page sheet does not contradict the cycle table from the
      previous ticket.

## Resources

- [Season Roadmap]({{ '/roadmap/' | relative_url }})
  — Kickoff & Strategy, then Design & Prototyping.
- [Decision-Making Guide]({{ '/decision-making/' | relative_url }})
- [Leadership: Decision-Making]({{ '/learning/leadership/decision-making/' | relative_url }})
- [CAD: Design Methodology]({{ '/learning/cad/design-methodology/' | relative_url }})
- [Chief Delphi: Kickoff Day 1 Recap](https://www.chiefdelphi.com/t/kickoff-day-1-recap/510906)
- [Chief Delphi: 1710 2026 Open Alliance thread](https://www.chiefdelphi.com/t/frc-team-1710-2026-build-thread-open-alliance/507939)
- [2026 Game Manual (PDF)](https://firstfrc.blob.core.windows.net/frc2026/Manual/2026GameManual.pdf)
- [Scoring, Cycles & Penalties](../scoring-and-cycles/)
- [Designing a Scouting System](../scouting-system-design/)

## Notes

- "We'll add it if we have time" is how won'ts become half-built
  shoulds. If it is not scheduled, it is a won't.
- Mentors drive overall strategy and priority on this team; student
  leads facilitate across tasks. Read the decision guide before you
  schedule a vote about bumpers.
- A won't is not an insult to the person who suggested it. It is a
  schedule. Thank them and write the reason down.
- Next:
  [Designing a Scouting System](../scouting-system-design/).
  You will turn these priorities into columns a tired scout can fill on
  a Friday night.
