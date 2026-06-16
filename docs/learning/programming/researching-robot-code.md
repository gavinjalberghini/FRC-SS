---
layout: lesson
title: Researching Robot Code
subtitle: Study other teams' open-source code to improve our own architecture.
permalink: /learning/programming/researching-robot-code/
role: lead
order: 15
size: 2
time: "1–2 hrs"
---

## Overview

Many FRC teams open-source their robot code. Reading it is one of the best ways to
level up: you see real patterns, conventions, and trade-offs that you can borrow.
This lesson is about reading code critically and bringing the best ideas back to
our codebase.

## Prerequisites

- [Code a Robot](../code-a-robot/) — you'll get the most out of this once you've
  written robot code yourself.

## What you'll learn

- How to find high-quality open-source FRC code.
- A checklist of questions to ask while reading a codebase.
- How to turn what you find into proposals for our team.

## Questions to ask while reading a codebase

- Does the code use a **state machine**, or the standard command-based flow?
- Are they using a swerve template (e.g. YAGSL, a vendor template, or custom)?
- What **naming conventions** do they use? Are constants gathered in one file?
- How do they break the robot into **subsystems**?
- Where do most **commands** live — a commands folder, `RobotContainer`, or inside
  subsystems?
- How do they write commands that need **more than one subsystem**?
- How large is `RobotContainer`, and what goes in it?
- What do they use for **autonomous** — PathPlanner, Choreo, or both?
- What naming convention do they use for autonomous paths?
- Do they split routes into multiple connected paths, or one big path each?

## Steps & acceptance criteria

- [ ] Find a team whose robot impressed you and locate their public code.
- [ ] Read through it and answer the questions above, citing specific files where
      possible.
- [ ] Write up your findings (as a document or issue) and share it with mentors so
      it can inform our codebase next season.

## Where to find good code

- [The Blue Alliance](https://www.thebluealliance.com/) — find strong teams, then
  look for links to their code repositories.
- [Chief Delphi](https://www.chiefdelphi.com/) — many teams publish their code and
  technical write-ups here (search for "open alliance" build threads).

## Notes

- The goal is to improve *our* code, so favor patterns you can realistically adopt
  over clever tricks that would be hard to maintain.
