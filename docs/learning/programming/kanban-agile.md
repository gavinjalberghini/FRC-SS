---
layout: lesson
title: Kanban & Agile Practices
subtitle: Plan and track the team's work with sprints, standups, and well-formed issues.
permalink: /learning/programming/kanban-agile/
role: veteran
order: 6
size: 1
time: "~45 min"
---

## Description

A programming team that can write Java and blink a Talon still fails the
season if nobody knows what is in progress, what is blocked, and what
"done" means. Kanban is a way to **see** the work, **limit** how much is
started at once, and keep tickets moving to done. FRC teams apply it with
GitHub Issues and a Project board — the same tools you met in passing in
[GitHub Basics](../github/).

This is the first veteran ticket. Programmer-track work (Git, Java,
hardware, Tuner X) was mostly *your* skills. Veteran work is *shared*
work: subsystems, driver controls, autos. Shared work without a board
becomes Slack archaeology and a Thursday panic. The easy mistakes are
starting five tickets, writing issues that say "fix drive," and treating
In Review as a junk drawer.

You will learn the vocabulary, write one issue the way this curriculum
writes tickets, and move a real card across a board. The issue you write
can live in your `frc-learning` repo or on the team's project — this
website does not track it. Mentors accept against the acceptance criteria
below, the same way they will accept robot PRs.

The next ticket, [Reading Driver Input](../driver-input/), is the first
WPILib veteran lab. Finish this one first so the lab has a ticket to sit
on.

## Prerequisites

- [GitHub Basics](../github/) — you have an account and know what an
  issue is.
- [Git Fundamentals](../git/) — you can open a pull request. A board
  without PRs is a to-do list.
- Access to either your `frc-learning` repo's Issues tab or the team's
  GitHub Project. Ask a mentor which board veterans use.

## What you'll learn

- The words a standup actually uses: ticket, sprint, WIP, blocker,
  acceptance criteria.
- What belongs in a well-formed issue — and what "fix it" is missing.
- How a card should move from Selected to Done, and why In Review is a
  real column.

## Key terminology

- **Ticket / Issue** — a single unit of work, written with a name,
  description, acceptance criteria, and references. These learning pages
  *are* tickets. Robot work should look like them.
- **Sprint** — a fixed work cycle (often about one week in build season)
  during which a small set of tickets is selected. Work that does not
  fit is not "also started." It waits.
- **Standup** — a short, regular meeting. Each person says what moved,
  what is in review, and what is blocked. It is not a design review.
- **Scrum Master** (or whoever runs the board) — the person who runs
  planning, standups, and retrospectives, and who pushes back when the
  sprint is overweight.
- **Sprint Planning** — the meeting that pulls tickets into Selected
  and leaves the rest in Unplanned or Icebox.
- **Retrospective** — the meeting at the end of a sprint that checks
  finished tickets against their acceptance criteria and names one
  process change.
- **WIP (work in progress)** — how many tickets are actually being
  worked. Limiting WIP is the whole point. Three finished tickets beat
  ten half-started ones.

Read Atlassian's
[What is Kanban?](https://www.atlassian.com/agile/kanban)
for the general method (visualize, limit WIP, manage flow). Then come
back; the team's board is GitHub, not Jira.

## Writing a good issue

Every ticket should contain:

- **Name** — a few words that say the task, not the vibe. "Invert
  intake belt" beats "intake stuff."
- **Description** — what is being asked, and why it matters to the
  robot or the team this week.
- **Acceptance Criteria** — checkable conditions that mean done. A
  mentor or reviewer should be able to sign them without a meeting.
- **References** — docs, a CAD screenshot, a person, a related PR.
- **Notes** — safety, "robot on blocks," "do not merge on Thursday."
- **Size** — a rough effort on a fixed scale (1 = within a day, 2 =
  within a sprint, 3 = multiple sprints). Size is for planning, not
  for ego.
- **Labels & Project** — so the card appears on the board the team
  actually looks at.

If a ticket has no acceptance criteria, it is a chat message wearing
an issue number.

## A typical board layout

Tasks flow left to right:

- **IceBox** — low-priority items parked for later.
- **Unplanned** — drafts not yet selected; glance at them in standup.
- **Selected** — the sprint backlog. If it is here, someone may start
  it.
- **In Progress** — actively being worked. Limit this column on
  purpose.
- **In Review** — finished, waiting for a human against the criteria.
  A PR link belongs here.
- **Done** — reviewed and accepted.
- **Archive** — last sprint's Done, so the board stays readable.

Cards do not skip In Review because "it worked on my laptop."

## Tasks

1. **Read the method, then the tool.** Read
   [What is Kanban?](https://www.atlassian.com/agile/kanban)
   through the sections on visualizing work and WIP limits. Skim
   [Kanban principles (Wrike)](https://www.wrike.com/kanban-guide/kanban-principles-practices/)
   if you want a second phrasing. Then read GitHub's
   [About Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
   and
   [Quickstart for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects)
   far enough that you can create an issue and put it on a board.

2. **Write the vocabulary down.** In `frc-learning`, create
   `process/kanban.md`. Define, in two sentences each and in your own
   words: ticket, sprint, standup, WIP, acceptance criteria, In Review.
   Do not paste this page.

3. **Write one well-formed issue.** Create a **real** GitHub issue (in
   `frc-learning` or on the team board — ask which). It must include
   every component listed under "Writing a good issue." Pick work you
   will actually do this week: a Java exercise leftover, a hardware
   note fix, or the next ticket's lab setup. Size it 1 or 2. Paste the
   issue URL into `process/kanban.md`.

4. **Move the card.** Put that issue on a Project board (create a
   simple one on `frc-learning` if the team has not invited you yet:
   Selected, In Progress, In Review, Done). Move it Selected → In
   Progress when you start, In Review when the work exists, and leave
   it there until a mentor or teammate checks the criteria. Screenshot
   the board at In Review into `process/kanban.md` or the folder next
   to it.

5. **Sit in one standup.** Attend the programming standup (or a
   mentor 1:1 that substitutes). In `process/kanban.md`, write the
   three things *you* said or would have said: last progress, next
   step, blocker (or "no blocker"). If the team has no standup yet,
   write the three sentences anyway and ask a mentor when one starts.

6. **Commit the notes.** Branch, commit `process/kanban.md`, open a
   pull request. If the team exported these tickets, paste the issue
   URL and the PR URL on this learning issue and move it to In Review.

## Acceptance Criteria

- [ ] `process/kanban.md` defines ticket, sprint, standup, WIP,
      acceptance criteria, and In Review in your own words.
- [ ] A GitHub issue you created includes name, description,
      acceptance criteria, references, notes, and a size.
- [ ] That issue was placed on a Project board and moved through
      Selected → In Progress → In Review. A screenshot or board URL
      is in the notes.
- [ ] A mentor or teammate reviewed the issue against *its*
      acceptance criteria (not against this ticket's).
- [ ] You have standup notes (three sentences) in
      `process/kanban.md`.
- [ ] A pull request for the notes is open or was merged after
      review.

## Resources

- [Atlassian: What is Kanban?](https://www.atlassian.com/agile/kanban)
- [Kanban principles & practices (Wrike)](https://www.wrike.com/kanban-guide/kanban-principles-practices/)
- [GitHub Docs: About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)
- [GitHub Docs: About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
- [GitHub Docs: Quickstart for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects)
- [GitHub Docs: Creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue)

## Notes

- Limiting work-in-progress is the heart of Kanban. If In Progress has
  more cards than people, stop starting and start finishing.
- An issue without acceptance criteria will be "done" forever and
  finished never. Write the checkboxes first, then the description.
- Learning tickets exported by
  `scripts/create_issues.py` are already in this format. Use them as
  examples when you write robot tickets.
- Next: [Reading Driver Input](../driver-input/). Put *that* lab on
  the board as a ticket before you open VS Code, if the team works
  that way.
