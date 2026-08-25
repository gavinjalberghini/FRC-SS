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

## Description

Being a lead programmer is less about writing the most lines and
more about making the *whole team's* code good enough to ship
on Thursday. The job has two halves that look like they compete:
**code review** (slow down, make it right, teach) and **build-
season leadership** (make a cut, integrate on the real robot,
protect driver practice). Doing only one of them is how you get
either a beautiful repo that never drives or a robot that only
you can deploy.

This is the last programming ticket. You have researched other
teams in [Researching Robot Code](../researching-robot-code/)
and you have (or can run) vision from
[Vision & PhotonVision](../vision-photonvision/). Everything
before that — Git, Java, Tuner X, Kanban, coordinates, autos —
is the material you are now responsible for *in other people*.
The easy mistakes: reviews that say "looks good" on a 800-line
PR; reviews that nitpick import order while a subsystem is
unsafe; a board with twelve In Progress cards; merging to
`main` on the field because "we need it for this match" with
no reviewer.

This ticket is ongoing on purpose. You will run real reviews,
write down how *this* team branches and ships, and lead through
at least one integration or practice block. Evidence lives in
GitHub (PR comments you wrote) and in
`frc-learning/leadership/`. This website does not promote you
to lead. Mentors and the team do, against the checkboxes
below.

## Prerequisites

- Programmer and veteran tickets completed, plus real
  experience contributing to the team's robot repo — not only
  `frc-learning`.
- [Kanban & Agile Practices](../kanban-agile/) — you already
  know what a well-formed issue looks like. Leads enforce it.
- [Researching Robot Code](../researching-robot-code/) so
  architecture opinions are cited, not aesthetic.
- Permission to review and merge (or to recommend merge) on
  the team repo.

## What you'll learn

- How to give and receive review that is specific, kind, and
  about the change — using a shared comment language.
- How to own branch workflow, integration, and a realistic
  board through a season.
- How to coordinate software with build, electrical, strategy,
  and drive team so "the code is done" means the robot does
  the thing.

## Running good code reviews

Read Google's
[Code Review Developer Guide](https://google.github.io/eng-practices/review/)
(the reviewer pages, not only the intro) and
[Conventional Comments](https://conventionalcomments.org/).
You do not need to adopt every label. You do need a way to
mark *nit* versus *blocker* so a freshman can tell which
comments stall the merge.

Practices that hold up in FRC:

- Review **promptly**. A PR that sits three days teaches
  people to bypass review.
- Check correctness, readability, and team conventions — not
  only "it drove once in the shop."
- Leave specific, kind, actionable comments. Explain the
  *why*. Prefer questions ("what happens if this Optional is
  empty on the field?") over commands ("fix this").
- Require that the change **builds** and, where possible, was
  run on a robot or in sim. "Works on my machine" is not a
  test.
- Require documentation when behavior changed: README, JavaDoc,
  or a comment next to a non-obvious invert. The
  [Java documentation unit](../java-fundamentals/) still
  applies on a robot.
- Do not merge your own large change without a second pair of
  eyes unless the team has an explicit emergency rule *and*
  you write down what you did after the match.

GitHub's
[About pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)
is the button-level how-to.

## Owning the codebase

- Maintain a branch and PR workflow people can recite:
  branch from `main`, small PRs, CI or at least compile,
  review, then merge. Write it in
  `leadership/workflow.md` if it is not already in the robot
  README.
- Lead architecture: subsystem cuts, where commands live,
  naming, constants, logging. Use the research ticket's
  proposals; do not redesign every Sunday.
- Watch integration. Features developed on separate
  branches still have to run **together** on the robot
  before you call the sprint done.
- Keep the Kanban board honest. Limit WIP. A lead who
  starts every ticket is a bottleneck, not a hero.

## Leading through build season

- Coordinate with build, electrical, and strategy so
  software targets the robot you will actually have, not
  the CAD from week 2.
- Protect testing time and driver practice. Reliable code
  beats a clever auto that has never seen carpet.
- Hold a pre-competition software sign-off: what is on
  `main`, what is disabled, what the backup auto is, who
  has the deploy laptop.
- Mentor newer programmers. If only you can image a Pi or
  read a stack trace, you failed
  [Debugging](../debugging/) as a teacher.
- Make yourself replaceable. Document decisions. The note
  in the original lesson still stands: the best leads grow
  the next leads.

## Tasks

1. **Read the review guides.** Read Google's
   [reviewer guide](https://google.github.io/eng-practices/review/reviewer/)
   and
   [The Standard of Code Review](https://google.github.io/eng-practices/review/reviewer/standard.html),
   plus
   [Conventional Comments](https://conventionalcomments.org/).
   In `leadership/review-standards.md`, write this team's
   rules in one page: what blocks a merge, what is a nit,
   how fast a first response should be, when sim is enough
   versus hardware.

2. **Review two real pull requests.** On the team robot
   repo (or, if the season is quiet, on two substantial
   `frc-learning` PRs from newer students), leave a review
   that uses at least one blocking comment or a clear
   "approved because …" with something you actually
   checked (build, a test, a convention). Link both
   reviews in `leadership/reviews.md`. Screenshot is
   optional; the GitHub review URL is the artifact.

3. **Receive a review without melting.** Open or point to
   a PR *you* authored that received comments. In the same
   file, write how you responded (changed the code, asked
   a question, or explained why you did not change it).
   Leads who never get reviewed rot.

4. **Write the season workflow.** In
   `leadership/workflow.md`, document: branch names, how
   tickets move on the board, who may merge, what happens
   on Thursday of an event, and where deploy credentials
   / radio programming live (not the passwords — the
   *people* and the doc link). Get a mentor to ack it.

5. **Run one integration or practice block.** Own a
   session where independently-written features meet the
   robot: a drivetrain + intake night, an auto practice,
   or a vision bring-up. Write a short after-action in
   `leadership/integration.md`: what you planned, what
   actually worked, what you cut, what the board looks
   like after. Use Test mode and traces from
   [Debugging](../debugging/) instead of "try teleop
   again."

6. **Pre-event sign-off template.** Add
   `leadership/pre-event-checklist.md` with checkboxes
   you would actually walk: image/firmware versions,
   auto list, disabled features, backup driver
   laptop, vision IPs from
   [Vision](../vision-photonvision/), alliance-color
   behavior from
   [Alliance Color](../alliance-color/). You do not
   need an event this week; you need a checklist a
   future you will use.

7. **Hand the folder to mentors.** Open a pull request
   on `frc-learning` with `leadership/`. If the team
   exported this ticket, keep it open until a mentor
   agrees you have *done* reviews and integration, not
   only written about them. This ticket is ongoing;
   "Done" means the first loop is real.

## Acceptance Criteria

- [ ] `leadership/review-standards.md` states merge
      blockers, nits, response time, and sim-versus-
      hardware rules.
- [ ] Two pull request reviews you wrote are linked.
      At least one contains a specific comment (not
      only "LGTM").
- [ ] You documented a review *you received* and how
      you responded.
- [ ] `leadership/workflow.md` describes branch/PR/
      merge and event emergency rules. A mentor
      acknowledged it.
- [ ] `leadership/integration.md` is an after-action
      from a real integration or practice block you
      led.
- [ ] `leadership/pre-event-checklist.md` exists and
      mentions firmware, autos, vision IPs, and
      alliance behavior.
- [ ] A mentor is willing to say you review promptly
      and you do not merge unreviewed emergencies
      without writing them down.

## Resources

- [Google: Code Review Developer Guide](https://google.github.io/eng-practices/review/)
- [Google: How to do a code review](https://google.github.io/eng-practices/review/reviewer/)
- [Google: The Standard of Code Review](https://google.github.io/eng-practices/review/reviewer/standard.html)
- [Conventional Comments](https://conventionalcomments.org/)
- [GitHub: About pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)
- [GitHub: Commenting on a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request)
- [WPILib documentation](https://docs.wpilib.org/en/stable/) — shared
  source of truth when a review argument is actually a
  docs argument
- [Kanban & Agile Practices](../kanban-agile/) — the board
  you are now responsible for

## Notes

- The best leaders make themselves replaceable: document
  decisions and grow the next leads so the team survives
  graduation.
- Kind is not the same as vague. "This invert is
  undocumented and will cost a match" is kind to the
  drive team.
- If you are drowning, the answer is to cut scope and
  shrink PRs — not to skip review. That is the same WIP
  limit you already learned.
- There is no next programming ticket. Your next job is
  to assign these tickets to someone else and mean it.
