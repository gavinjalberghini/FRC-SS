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

## Overview

Git is the version-control system that lets a whole team work on the same code
without overwriting each other. In this lesson you'll practice the everyday Git
workflow on **your own repository**: creating it, making a branch, committing
changes, pushing, and opening a pull request (PR) for review. You'll reuse this
same repository for the other learning modules (like Java Fundamentals).

## Prerequisites

- [GitHub Basics](../github/) completed (account set up).
- Git installed on your computer.

## What you'll learn

- How to authenticate with GitHub over SSH.
- The clone → branch → commit → push → pull request cycle.
- How to get your work reviewed and merged.

## Steps & acceptance criteria

- [ ] Install Git and set your identity so commits are attributed to you:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"   # the email on your GitHub account
```

- [ ] Set up an **SSH key** and add it to your GitHub account.
- [ ] Create your **own** repository on GitHub for your learning work (for
      example, `frc-learning`), then clone it to your computer:

```bash
git clone git@github.com:your-username/frc-learning.git
```

- [ ] Create a new branch named after yourself or your task:

```bash
git checkout -b firstname-intro
```

- [ ] Add a small change (for example, a short README that introduces you), then
      stage and commit it:

```bash
git add .
git commit -m "Add intro for Firstname"
```

- [ ] Push your branch to GitHub:

```bash
git push -u origin firstname-intro
```

- [ ] Open a **pull request** from your pushed branch and ask a mentor to review it.

## Resources

- [Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [GitHub Docs: Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitHub Docs: About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)
- [Pro Git book (free)](https://git-scm.com/book/en/v2)

## Notes

- After you push a new branch, the console prints a link you can use to open the
  pull request directly.
- GitHub no longer accepts your account password on the command line — use an SSH
  key (above) or a personal access token.
