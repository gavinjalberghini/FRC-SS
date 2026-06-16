---
layout: lesson
title: Code Review & Build-Season Leadership
subtitle: Run reviews, own the codebase lifecycle, and lead the team through build season.
permalink: /learning/programming/code-review-leadership/
role: lead
order: 17
size: 2
time: "Ongoing"
---

## Overview

Being a lead programmer is less about writing the most code and more about making
the *whole team's* code good and getting it shipped. This lesson covers the two
core leadership responsibilities: running effective code reviews and steering the
software effort through a build season.

## Prerequisites

- All Programmer and Veteran lessons, plus real experience contributing to and
  reviewing robot code.

## What you'll learn

- How to give and receive useful code review.
- How to own the codebase across a season.
- How to coordinate the software team with the rest of the robot.

## Running good code reviews

- [ ] Review **pull requests** promptly so teammates aren't blocked.
- [ ] Check for correctness, readability, and consistency with team conventions —
      not just "does it work."
- [ ] Leave specific, kind, actionable comments; explain the "why," and prefer
      questions over commands.
- [ ] Require that code builds and (where possible) is tested before merging.
- [ ] Make sure changes are documented (README/JavaDoc/comments as appropriate).

## Owning the codebase

- [ ] Maintain a clean branch and PR workflow that everyone follows.
- [ ] Lead architecture decisions: subsystem structure, where commands live,
      naming and constants conventions.
- [ ] Keep an eye on integration — make sure independently-developed features come
      together on the real robot.
- [ ] Track work on the team board and keep the sprint workload realistic.

## Leading through build season

- [ ] Coordinate with build, electrical, and strategy so software targets the
      right capabilities.
- [ ] Plan for testing time and driver practice — reliable code beats clever code.
- [ ] Hold pre-competition reviews and sign off on software before events.
- [ ] Mentor newer programmers and make sure everyone has the tools and docs they
      need.

## Resources

- [Google's Code Review Developer Guide](https://google.github.io/eng-practices/review/)
- [Conventional Comments](https://conventionalcomments.org/) — a format for clear review feedback.
- [WPILib documentation](https://docs.wpilib.org/) — the shared source of truth for the team.

## Notes

- The best leaders make themselves replaceable: document decisions and grow the
  next set of leads so the team stays strong year over year.
- This area is still being built out — add team-specific review checklists and
  build-season playbooks here as the team develops them.
