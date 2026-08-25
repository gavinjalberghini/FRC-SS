---
layout: lesson
title: GitHub Basics
subtitle: Set up your GitHub account, profile, and security so you can collaborate.
permalink: /learning/programming/github/
role: programmer
order: 1
size: 1
time: "30–60 min"
---

## Description

Git and GitHub are related but not the same thing. **Git** is the version-control
software that lives on your computer and records snapshots of a project.
**GitHub** is a website that hosts Git repositories and adds the collaboration
layer an FRC software team actually uses: pull requests, issues, review comments,
and project boards.

This first ticket exists so that every later programming ticket has a place to
land. You will do the learning work in **your own** repositories — a profile
README now, a personal `frc-learning` repo in the next ticket — not by pushing
unreviewed code onto the team's robot repo. Mentors review that work the same
way they review robot code: as a pull request against written acceptance
criteria.

You will find supplementary videos and docs at the bottom of this ticket. Issues
and project boards are covered in depth in
[Kanban & Agile Practices](../kanban-agile/); you only need to know they exist
for now.

This site does not track whether you finished. If your team exported these
tickets into its own GitHub, close this issue there once a mentor accepts the
criteria below.

## Prerequisites

- A school or personal email address you can receive mail at.
- A web browser. You do not need Git installed yet — that is the next ticket.

## What you'll learn

- How GitHub relates to Git, and why FRC teams use both.
- How to create a GitHub account, put a face on it, and lock it down with
  two-factor authentication.
- How a **profile README** introduces you to teammates who have never met you.

## Tasks

1. **Understand the two tools.** Watch
   [Git vs GitHub — what's the difference?](https://www.youtube.com/watch?v=w3jLJU7DT5E)
   (about 6 minutes) and skim GitHub's
   [Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)
   guide through the "Create a repository" section. You are not creating a
   project repo yet. Write two sentences in a scratch note (keep it — you will
   paste it into your profile README): *Git is …* and *GitHub is …*.

2. **Create the account.** If you do not already have a GitHub account, create
   one at [github.com/signup](https://github.com/signup). Use an email you will
   still have after graduation if you can; school addresses sometimes vanish.
   Pick a username you are willing to put on a college application and a
   resume — `xXrobotgodXx` is funny for a week. If your team has a GitHub
   Organization, ask a mentor to invite you after this ticket, not before. You
   will still do learning work in repositories you own.

3. **Put a face on the account.** Add a profile photo
   ([GitHub: personal profile settings](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile#changing-your-profile-picture)).
   Mentors review dozens of PRs. A real photo (or a consistent avatar) is how
   they tell you apart from the next new programmer. A blank identicon is a
   valid account and an unhelpful teammate.

4. **Turn on two-factor authentication.** Follow
   [Configuring two-factor authentication](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication).
   Use an authenticator app (Authy, 1Password, Google Authenticator) rather than
   SMS if you can. Save the recovery codes somewhere that is not a screenshot
   in your camera roll. GitHub will eventually require 2FA on any account that
   contributes to an organization; do it now so a forgotten phone does not lock
   you out of build season.

5. **Publish a profile README.** A profile README is a repository whose name is
   **exactly** your username. GitHub renders its `README.md` on your profile
   page. Follow
   [Managing your profile README](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)
   and write a short page that includes:

   - your name and the name you want teammates to use
   - your graduation year
   - the two sentences from Task 1
   - one thing you already know (any language, CAD, shop skill, or "nothing
     yet, here to learn")
   - one thing you want out of this curriculum

   Use [this Markdown cheatsheet](https://www.markdownguide.org/cheat-sheet/)
   if the syntax is new. Keep it under about 30 lines. You are introducing
   yourself, not writing a portfolio.

6. **Hand it to a mentor.** Send your profile URL
   (`https://github.com/<your-username>`) to the programming mentor or lead.
   If your team exported these tickets, paste that URL on this issue and move
   it to In Review.

## Acceptance Criteria

- [ ] You can explain, in two sentences of your own words, the difference
      between Git and GitHub.
- [ ] A GitHub account exists with a non-default profile picture.
- [ ] Two-factor authentication is enabled. A mentor does not need to see
      recovery codes; they need you to say it is on and that you stored the
      codes off your phone's camera roll.
- [ ] A profile README is published at a repo named exactly your username and
      includes name, graduation year, the Git vs GitHub sentences, one current
      skill, and one learning goal.
- [ ] A mentor has the profile URL.

## Resources

- [Git vs GitHub (YouTube, ~6 min)](https://www.youtube.com/watch?v=w3jLJU7DT5E)
- [GitHub Docs: Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)
- [GitHub Docs: Personalizing your profile](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile)
- [GitHub Docs: Managing your profile README](https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)
- [GitHub Docs: Configuring 2FA](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)
- [Markdown Guide — cheat sheet](https://www.markdownguide.org/cheat-sheet/)
- [GitHub Docs: About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) — preview of the next collaboration tool
- [GitHub Docs: About Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects) — where exported tickets live on a team board

## Notes

- Resolving merge conflicts is not required here, but learn the *idea* early:
  two people edited the same lines, Git will not guess, a human picks. It
  comes up constantly once a repo is shared.
- Do not put a password, personal phone number, or home address in the
  profile README.
- The next ticket ([Git Fundamentals](../git/)) is where you install Git,
  clone a repo you own, and open your first pull request.
