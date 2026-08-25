---
layout: strategy-lesson
title: Data Analysis
subtitle: Rank teams from your data and public sources (TBA, Statbotics) without drowning in spreadsheets.
permalink: /learning/strategy-scouting/data-analysis/
role: veteran
order: 8
size: 3
time: "2–3 hrs"
---

## Description

Analysis is how scouting becomes a ranking. The failure mode is a
40-column sheet nobody trusts. This ticket is a small set of views —
**your data first**, then public models, then the places they disagree —
that a lead can explain in a meeting.

You have match sheets, a data dictionary, pit cards, and qualitative
notes from the last four tickets. Those are the dataset. TBA and
Statbotics are extra eyes. They are not the pick list.

**The Blue Alliance**
([thebluealliance.com](https://www.thebluealliance.com/))
is official results, match video, rankings, and OPR-style aggregates.
**Statbotics**
([statbotics.io](https://www.statbotics.io/))
is EPA — Expected Points Added — a model that tries to strip schedule
luck and put a team's contribution in point units. Read
[The EPA model](https://www.statbotics.io/blog/epa)
far enough to know EPA is a prediction, not a photograph of a jammed
intake. Use public models to *challenge* your list: "EPA loves this
team; we have them unscouted" is a to-do. "EPA loves this team; first
pick" is outsourcing.

Averages hide boom-bust robots. Look at **consistency** (do they do it
every match) as well as the mean. Mark every team with a tiny sample.
At a 24-team event, everyone has a tiny sample. When *n* is 2,
qualitative and pit cards carry more weight. Say so out loud.

This website does not store analysis workbooks. Build the cards in a
sheet or doc your team owns. The next ticket,
[Building a Pick List](../pick-lists/),
is where you defend a ranking with a paragraph. This ticket is the
cards you will point at.

## Prerequisites

- [Match Scouting](../match-scouting/)
  (sheets plus dictionary).
- [Qualitative & Super Scouting](../qualitative-scouting/)
  (match-cited notes).
- Pit cards from
  [Pit Scouting](../pit-scouting/)
  if you have them.

## What you'll learn

- How to summarize a team in a few numbers you could defend on a
  whiteboard.
- How to use TBA and Statbotics without handing them the captain's
  microphone.
- How to handle small samples and schedule luck without pretending
  certainty.

## Tasks

1. **Build team cards from *your* data.** Pick a recorded event you can
   pretend you scouted. The intended set for this track:

   - Your Einstein Finals 1 sheets and qualitative notes for the six
     teams on
     [2026cmptx_f1m1](https://www.thebluealliance.com/match/2026cmptx_f1m1).
   - Enough extra matches from
     [Einstein 2026](https://www.thebluealliance.com/event/2026cmptx)
     or from those teams' earlier events on TBA that each card has a
     stated *n* (matches you actually watched or sheeted). If *n* is 1,
     write *n* = 1 in a large font. Do not invent rows.

   Each card, one screen or one index card:

   - team number, *n*
   - auto success rate or auto points (your definition)
   - teleop scoring rate (cycles or bursts — pick one, stay consistent
     with the dictionary)
   - endgame success rate
   - disable / no-show / card flags
   - one qualitative sentence with a match key
   - pit claim vs. field, if you have a pit card

   Consistency: did they do the thing every match, or once for a reel?

2. **Pull the public numbers on the same teams.** For each of the six
   (or for eight teams if you expanded the set):

   - TBA: find the team page and an event they played (not only
     Einstein). Note rank, record, and any OPR/component stats TBA
     shows for that event.
   - Statbotics: search the team and year, e.g. start from
     [statbotics.io](https://www.statbotics.io/)
     and open the 2026 profile. Note total EPA and any auto / teleop /
     endgame split.

   Write them *next to* your card, not on top of it. If you want the
   API later, it lives at
   [Statbotics REST](https://www.statbotics.io/api/rest)
   and
   [TBA API v3](https://www.thebluealliance.com/apidocs/v3).
   You do not need an API for this ticket.

3. **Explain two disagreements.** Compare a ranking of your top 8 (or
   the six Einstein teams plus two more you looked up) to Statbotics
   EPA order and to TBA OPR or rank. Write a paragraph each for **two**
   teams where the orders disagree. Allowed reasons: you saw a disabled
   match they ate; EPA is still warming up after week 1; your *n* is 1
   and theirs is 12; they sandbagged quals; your cycle definition
   ignores defense. Forbidden reason: "I just like them."

4. **Mark uncertainty.** On every card with fewer than four scouted
   matches, write **LOW n** where a captain will see it. On a 24-team
   event this will be most of the field after Friday. The pick meeting
   is allowed to lean on pit cards and qualitative here. They are not
   allowed to pretend *n* = 2 is a season.

5. **Produce a one-screen coach view.** Collapse the cards into
   something a coach can read in 30 seconds before a match: team
   numbers, two numbers that matter for *your* role (from
   [Robot Priorities](../robot-priorities/)),
   flags, and a single word of qualitative. If it does not fit on a
   phone screenshot, it is not a coach view. This is not the pick
   list yet — it is the dashboard the pick list will be argued from.

6. **Write the complementarity rule in your own words.** Four
   sentences, no jargon pile-up:

   - What your sheets know that EPA cannot.
   - What EPA/TBA know that six tired scouts cannot (the other 50
     matches, schedule strength).
   - What you will do when they disagree (watch another match — do
     not average the disagreement away).
   - What you will never do (paste Statbotics into the first-pick
     slot and go to lunch).

## Acceptance Criteria

- [ ] Team cards exist for at least six teams with *n*, auto, teleop
      rate, endgame rate, flags, and one cited qualitative sentence.
- [ ] TBA and Statbotics numbers sit next to those cards for the same
      teams.
- [ ] Two disagreements with public models are explained in a
      paragraph each, with evidence (a match key or a sample-size
      note).
- [ ] Every team with fewer than four scouted matches is marked
      **LOW n**.
- [ ] A one-screen coach view exists.
- [ ] The four-sentence complementarity rule is written in your words
      and a mentor can ask you to say it without the page.

## Resources

- [The Blue Alliance](https://www.thebluealliance.com/)
- [TBA API v3](https://www.thebluealliance.com/apidocs/v3)
- [TBA: Einstein 2026](https://www.thebluealliance.com/event/2026cmptx)
- [TBA: 2026 Einstein Finals 1](https://www.thebluealliance.com/match/2026cmptx_f1m1)
- [Statbotics](https://www.statbotics.io/)
- [Statbotics: the EPA model](https://www.statbotics.io/blog/epa)
- [Statbotics REST API](https://www.statbotics.io/api/rest)
- [Chief Delphi: FRC Pick List Maker](https://www.chiefdelphi.com/t/frc-pick-list-maker/517475)
  — example of combining CSVs with EPA; do not skip your own cards.
- [Building a Pick List](../pick-lists/)
- [Match Scouting](../match-scouting/)
- [Qualitative & Super Scouting](../qualitative-scouting/)

## Notes

- A team that played three sandbag qualification matches is not their
  Sunday self. Playoff video is a different distribution. Label it.
- Do not overfit. A 40-column model on 24 teams is a story about your
  model, not about the field.
- Public data updates during the event. Your sheets update when a
  scout turns them in. Those are different clocks.
- Next:
  [Building a Pick List](../pick-lists/).
  Bring the cards and the coach view. You will produce a ranked list
  with a paragraph of justification a captain can read under time
  pressure.
