---
layout: lesson
title: Git Fundamentals
subtitle: Clone, branch, commit, push, and open pull requests from the command line.
permalink: /learning/programming/git/
role: programmer
order: 2
size: 2
time: "1–2 hrs"
---

## Description

Git is the version-control system that lets a whole team edit the same project
without silently overwriting each other. The everyday motion is always the
same: **clone** a repository, **branch** so your work is isolated, **commit**
snapshots of what changed, **push** those snapshots to GitHub, and open a
**pull request** so another human can review before the work lands on the
default branch.

This ticket is a lab, not a lecture. You will practice that loop on a
repository **you own**, named something like `frc-learning`. Every later
programming ticket that asks you to write code or notes (Java exercises,
research write-ups, robot experiments) goes in this repo. Mentors review it
the same way they review robot code: branch, PR, acceptance criteria.

You already have a GitHub account from [GitHub Basics](../github/). You do not
need access to the team's robot repository to finish this ticket. In fact,
you should not practice `git push --force` anywhere near it.

## Prerequisites

- [GitHub Basics](../github/) completed (account, 2FA, profile README).
- A computer you can install software on. Windows users should install
  [Git for Windows](https://gitforwindows.org/) (includes Git Bash) or
  [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install). macOS and
  Linux can use Terminal.

## What you'll learn

- How to install Git and set the name and email that will appear on your
  commits.
- How to authenticate to GitHub from the command line (SSH is preferred;
  a personal access token works).
- The clone → branch → commit → push → pull request cycle, by doing it
  once for real.

## Tasks

1. **Install Git and set your identity.** Follow
   [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
   for your OS. Then, in a terminal:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

   Use the same email as your GitHub account so GitHub links the commits to
   you. Confirm with `git config --global --list` and `git --version`. If
   command-line Git is new, watch
   [Git clone, commit, and push](https://www.youtube.com/watch?v=5HLst694D_Y)
   once through before Task 4 — then come back and type the commands
   yourself. Do not paste from a chatbot and call it practice.

2. **Authenticate to GitHub.** Pick one method and finish it:

   - **SSH (recommended):**
     [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
     Generate a key, add it to the ssh-agent, and paste the public key into
     GitHub → Settings → SSH and GPG keys. Test with
     `ssh -T git@github.com`.
   - **HTTPS + personal access token:**
     [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).
     GitHub no longer accepts your account password on the command line.
     A token is a password. Store it in a password manager, not in a
     screenshot and not in the repo.

3. **Create the learning repository.** On GitHub, create a new **public or
   private** repository named `frc-learning` (or similar). Do not
   initialize it with a README if you want to practice the first commit
   yourself; initializing with a README is also fine. Clone it:

   ```bash
   git clone git@github.com:your-username/frc-learning.git
   cd frc-learning
   ```

   If you used HTTPS, the URL starts with `https://github.com/...`.

4. **Branch, then change one file.** Watch
   [Git branching](https://www.youtube.com/watch?v=JTE2Fn_sCZs) if the word
   "branch" is still fuzzy. Then:

   ```bash
   git checkout -b firstname-intro
   ```

   Create `README.md` in the repo root (or edit the one GitHub made) so it
   contains:

   - your name
   - your graduation year
   - a one-paragraph "what I want to learn on the programming team"
   - a link to your profile README from the previous ticket

   This file is the seed of a repo you will keep using. Later tickets will
   add folders such as `java/` and `research/`.

5. **Stage, commit, and push.**

   ```bash
   git status
   git add README.md
   git commit -m "Add intro for Firstname"
   git push -u origin firstname-intro
   ```

   `git status` before `git add` is a habit, not a nicety — it is how you
   notice you were about to commit a secret or a zip of last year's robot
   code. After a first push of a new branch, Git prints a URL that opens
   the pull request form. Use it.

6. **Open a pull request.** Follow
   [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
   and, if you want a walkthrough,
   [this PR tutorial](https://www.youtube.com/watch?v=rgbCcBNZcdQ).
   The PR should:

   - target the repository's default branch (`main` or `master`)
   - have a title that says what changed, not "first pr"
   - mention this ticket by name in the body
   - ask a mentor to review it

   Merge happens **after** review, not before. On your personal
   `frc-learning` repo you can merge it yourself once a mentor has looked
   — the point is the review, not the permission model.

7. **Read one short chapter.** Skim
   [Pro Git, Chapter 2: Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
   through "Recording Changes to the Repository." You do not need to
   memorize every flag. You need `status`, `add`, `commit`, `log`, and
   `diff` to feel boring.

## Acceptance Criteria

- [ ] `git --version` prints a version, and `user.name` / `user.email` are
      set to your real name and GitHub email.
- [ ] You can authenticate to GitHub from the terminal (`ssh -T git@github.com`
      succeeds, or `git push` over HTTPS works with a token).
- [ ] A repository you own exists and is cloned on your computer.
- [ ] A branch that is not the default branch contains a `README.md` with
      your name, graduation year, a learning goal, and a link to your
      profile.
- [ ] That branch was pushed, and a pull request is open (or was merged
      after a mentor looked at it).
- [ ] You can, without looking at this page, list the commands for clone,
      branch, add, commit, and push in the right order.

## Resources

- [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Pro Git book (free)](https://git-scm.com/book/en/v2)
- [GitHub Docs: Connecting with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitHub Docs: Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- [GitHub Docs: About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- [HubSpot: Git and GitHub for beginners](https://product.hubspot.com/blog/git-and-github-tutorial-for-beginners)
- [Git clone, commit, and push (YouTube)](https://www.youtube.com/watch?v=5HLst694D_Y)
- [Git branching (YouTube)](https://www.youtube.com/watch?v=JTE2Fn_sCZs)
- [Git pull request tutorial (YouTube)](https://www.youtube.com/watch?v=rgbCcBNZcdQ)
- [Git for Windows](https://gitforwindows.org/)
- [WSL2 install](https://learn.microsoft.com/en-us/windows/wsl/install)

## Notes

- After you push a new branch, the console prints a link you can use to
  open the pull request directly. Use that link. Do not hunt through the
  GitHub UI the first time if you do not have to.
- GitHub in the command line no longer accepts passwords. Use an SSH key
  or a personal access token.
- Never `git add .` blindly in a folder that contains robot logs, vendor
  binaries, or `.env` files. `git status` first.
- The next ticket, [Java Fundamentals](../java-fundamentals/), is a
  multi-week course. Put each exercise in this `frc-learning` repo on its
  own branch and open a PR when a unit's exercises pass.
