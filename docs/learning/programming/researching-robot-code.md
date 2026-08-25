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

## Description

Many FRC teams publish their robot code. Reading it is one of the
fastest ways to level up after you have written some of your own:
you see real subsystem boundaries, real auto structure, and real
trade-offs — including ones that would be a bad fit for *this*
team. This ticket is not "star a GitHub repo." It is critical
reading with a written recommendation.

This is the first lead ticket. The veteran track ended at
[Autonomous Paths](../autonomous/) and
[Code a Robot](../code-a-robot/). You now know what a command-
based swerve project feels like from the inside. That is the
prerequisite for reading someone else's without drowning. The
next ticket, [Vision & PhotonVision](../vision-photonvision/), is
a specific technical hole this research often surfaces. The last
ticket, [Code Review & Build-Season Leadership](../code-review-leadership/),
is how you turn research into a season, not a bookmarks folder.

The easy mistakes: copying a 254-style state machine into a
five-person team that still struggles with `RobotContainer`;
treating YAGSL versus vendor swerve as a moral issue; writing
"they use PathPlanner" without saying *how* they split paths;
opening a 40,000-line monorepo on Sunday night and calling it
research.

You will pick one team's public code, answer a fixed list of
questions with file citations, and propose at most two changes
this team could actually adopt. The write-up lives in
`frc-learning/research/`. This website does not grade it. A
mentor (and, ideally, the rest of programming) should read it
like a design review.

## Prerequisites

- [Code a Robot](../code-a-robot/) — you have generated or
  substantially worked a drivetrain. If you only read Java
  tutorials, this ticket will be tourism.
- [Autonomous Paths](../autonomous/) so "path versus auto" and
  PathPlanner versus Choreo are not new words.
- Comfort cloning a public repo and navigating it in VS Code
  without deploying it to *your* robot.

## What you'll learn

- Where to find high-quality open FRC code, and how to tell a
  showcase repo from a midseason dump.
- A checklist of architecture questions to ask every codebase
  once, so you compare teams fairly.
- How to turn notes into a proposal with a cost, not a vibe.

## Questions to ask while reading a codebase

Answer these. Cite a path (`src/main/java/frc/robot/RobotContainer.java`)
and a short quote or description — not "somewhere in commands."

- Do they use a **state machine**, the standard command-based
  flow, or both (for example, a state machine inside one
  subsystem)?
- What **swerve** stack is it — YAGSL, a vendor template (CTRE
  generator, REV), AdvantageKit swerve, or custom kinematics?
- What **naming conventions** do they use? Are constants in one
  file, per-subsystem files, or generated?
- How is the robot broken into **subsystems**? What is
  surprisingly *not* a subsystem?
- Where do **commands** live — a `commands/` folder,
  `RobotContainer`, factory methods on the subsystem, or a
  mix?
- How do they write commands that need **more than one
  subsystem**?
- How large is `RobotContainer`, and what still goes in it?
- What do they use for **autonomous** — PathPlanner, Choreo,
  both, or something older?
- What naming convention do they use for autos and paths?
- Do they split a routine into **multiple connected paths**
  or one large path per auto?

If the repo has logging (AdvantageKit, SignalLogger, etc.), add
one extra question: what do they log that this team does not,
and would that logging fit our laptops and our drivers?

## Where to find good code

- [The Blue Alliance](https://www.thebluealliance.com/) — find
  a team whose robot you respected, then hunt their "code" or
  "GitHub" links on the team page or a Chief Delphi thread.
- [Chief Delphi](https://www.chiefdelphi.com/) — search Open
  Alliance build threads; many teams post weekly code dumps
  with context, which is more useful than a bare repo.
- Known public orgs (examples, not a ranking):
  [Team 254](https://github.com/Team254),
  [Mechanical Advantage 6328](https://github.com/Mechanical-Advantage),
  [Citrus Circuits 1678](https://github.com/frc1678),
  [CTRE Phoenix 6 examples](https://github.com/CrossTheRoadElec/Phoenix6-Examples)
  (examples, not a team robot — still useful for vendor
  patterns).

Pick a repo from the **same season language** you use (Java
command-based). A 2018 LabVIEW repo will not teach this
ticket.

## Tasks

1. **Pick a team on purpose.** On TBA, identify a team whose
   robot (drive, auto, or mechanism) impressed you. Find their
   public robot code for a recent season. If there is no public
   code, pick another team — do not review a screenshot of a
   reveal video. Write the team number, year, repo URL, and
   *why this robot* in `research/README.md`.

2. **Clone and walk.** Clone the repo. Do not deploy it. Open
   it in VS Code. Skim `README`, `build.gradle` / vendordeps,
   and the package tree. In `research/walkthrough.md`, spend
   half a page on first impressions: build system, vendor
   deps, how scary `RobotContainer` is.

3. **Answer the checklist.** In
   `research/architecture.md`, answer every bullet under
   "Questions to ask" with a file citation. "Could not find"
   is allowed **once**, with what you searched. "They probably
   use PathPlanner" without a file is not allowed.

4. **Propose two adoptions, maximum.** In
   `research/proposals.md`, write **one or two** changes this
   team could make next season (or this season, if early).
   Each proposal needs: the current pain, what the other team
   does (cite files), what we would copy, what we would
   *not* copy, and a size (1–3) like
   [Kanban](../kanban-agile/). Favor something a mid-size
   student team can maintain. A clever trick that only the
   author understands is a reject.

5. **Share it like a lead.** Open a pull request on
   `frc-learning` with the `research/` folder. Paste the PR
   (or a PDF export) to programming mentors and, if you have
   one, the lead channel. If the team exported this ticket,
   attach the PR to the issue. Offer to walk the architecture
   doc in a 15-minute standup.

6. **Optional stretch.** If vision is how that team scores,
   note how they structured PhotonVision / Limelight code.
   You will need that instinct in
   [Vision & PhotonVision](../vision-photonvision/).

## Acceptance Criteria

- [ ] `research/README.md` names team, year, repo URL, and why
      you picked them.
- [ ] `research/walkthrough.md` is a first-impressions page
      with vendordeps / package tree notes.
- [ ] `research/architecture.md` answers every checklist
      question with a file path (or one documented miss).
- [ ] `research/proposals.md` has at most two proposals, each
      with pain, citation, adopt / do-not-adopt, and a size.
- [ ] A pull request is open or was merged, and a mentor
      (or the programming group) has seen the write-up.
- [ ] You can, in conversation, explain the other team's
      auto structure without opening the repo.

## Resources

- [The Blue Alliance](https://www.thebluealliance.com/)
- [Chief Delphi](https://www.chiefdelphi.com/)
- [WPILib: Structuring a command-based project](https://docs.wpilib.org/en/stable/docs/software/commandbased/structuring-command-based-project.html)
- [PathPlanner documentation](https://pathplanner.dev/home.html)
- [Team 254 on GitHub](https://github.com/Team254)
- [Mechanical Advantage on GitHub](https://github.com/Mechanical-Advantage)
- [FRC 1678 on GitHub](https://github.com/frc1678)
- [Phoenix 6 examples](https://github.com/CrossTheRoadElec/Phoenix6-Examples)

## Notes

- The goal is to improve *our* code. A pattern you cannot
  staff or explain in a code review is not a gift.
- License and courtesy: public code is still someone's work.
  Do not paste large files into our robot repo. Reimplement
  the *idea*, and mention the source in the proposal.
- Next: [Vision & PhotonVision](../vision-photonvision/). If
  your research team localized off tags, bring those file
  names with you.
