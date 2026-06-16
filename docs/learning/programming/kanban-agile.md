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

## Overview

Kanban is a workflow-management method that helps a team visualize its work,
limit how much is in progress at once, and keep things flowing. We apply it
through GitHub Issues and a project board. This lesson covers the core
terminology and how a healthy board operates.

## Prerequisites

- [GitHub Basics](../github/) — you'll be creating and organizing issues.

## What you'll learn

- The vocabulary of agile/Kanban work cycles.
- What makes a good, actionable issue.
- How tasks flow across a Kanban board.

## Key terminology

- **Ticket / Issue** — a single unit of work, written in our standard issue format
  (see below).
- **Sprint** — a fixed work cycle (often about one week) during which selected
  tickets are worked.
- **Standup** — a short, regular meeting where each person reports the status of
  their in-progress and in-review tickets and raises blockers.
- **Scrum Master** — the person who runs the scrum process: sprint planning,
  standups, and retrospectives. They review completed work and keep the board's
  workload realistic.
- **Sprint Planning** — a meeting at the start of a sprint where tickets are
  selected into the sprint backlog (and lower-priority items are set aside).
- **Retrospective** — a meeting at the end of a sprint to check finished tickets
  against their acceptance criteria and discuss what to improve.

## Writing a good issue

Every ticket should contain:

- **Name** — a few words summarizing the task.
- **Description** — what is being asked, and why it matters to the team.
- **Acceptance Criteria** — the exact, checkable conditions that mean "done."
- **References** — links, docs, or people that help complete the work.
- **Notes** — any extra considerations.
- **Size / Velocity** — a rough effort estimate on a fixed scale (e.g. 1–3, where
  1 is "within a day," 2 is "within a sprint," 3 is "multiple sprints"). This
  helps balance how much work a sprint takes on.
- **Labels & Project** (GitHub) — categorize the ticket and attach it to the board.

## A typical board layout

Tasks flow left to right through columns such as:

- **IceBox** — low-priority items parked for later.
- **Unplanned** — draft tickets not yet selected; reviewed regularly at standup.
- **Selected** — tickets pulled into the current sprint backlog.
- **In Progress** — actively being worked this sprint.
- **In Review** — finished and awaiting review against acceptance criteria.
- **Done** — reviewed and accepted.
- **Archive** — completed work from past sprints.

## Steps & acceptance criteria

- [ ] Be able to define each term above in your own words.
- [ ] Create a new, well-formed issue (in your own learning repository, or on your
      team's board) that includes every component listed in "Writing a good issue."
- [ ] Move a ticket through the board (Selected → In Progress → In Review) for a
      real task and have it reviewed.

## Resources

- [Kanban principles & practices (Wrike guide)](https://www.wrike.com/kanban-guide/kanban-principles-practices/)
- [GitHub Docs: Planning and tracking with Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)

## Notes

- Limiting work-in-progress is the heart of Kanban: it's better to *finish* a few
  tickets than to *start* many.
