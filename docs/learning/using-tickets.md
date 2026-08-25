---
layout: page
title: Using the learning tickets
permalink: /learning/using-tickets/
---

The Learning Hub is a **guideline**, not a classroom app. Pages teach and
assign work. They do not log students in, store progress, or collect
homework. A team that wants a board, reviewers, and a record of who finished
what should export these tickets into **their own** GitHub (or other) space.

That is the same idea as the assignment issues in
[ml-bootcamp](https://github.com/gavinjalberghini/ml-bootcamp): the template
carries the tickets; each team (or mentee repo) owns the issues.

## What a ticket is

Every lesson is written as a ticket with the same spine:

1. **Description** — enough teaching that you are actually being taught, not
   handed a topic title.
2. **Tasks** — numbered, procedural work. Read this, watch that, build this,
   demonstrate that.
3. **Acceptance criteria** — observable checks a mentor can sign. A file, a
   written answer, a shop demonstration, a CAD document — not "understand X."
4. **Resources** — official docs, videos, articles, and books the tasks
   already pointed at.

Work stays where the team already works: a student GitHub repo, an Onshape
document, a shop sign-off sheet, a shared drive. This website never becomes
that system of record.

## Export tickets into your GitHub

From a clone of this playbook:

```bash
gh auth login
python3 scripts/create_issues.py --dry-run
python3 scripts/create_issues.py --repo your-org/team-learning
python3 scripts/create_issues.py --track programming --repo your-org/team-learning
```

`--dry-run` prints the issue titles without creating anything. `--track`
exports one curriculum. `--no-labels` skips labels if the target repo does
not have them yet.

To take the tickets as plain markdown (no Jekyll front matter):

```bash
python3 scripts/create_issues.py --dry-run --export-dir dist/tickets
```

That writes `dist/tickets/<track>/*.md`. Commit that folder, hand it to
another importer, or recreate issues later.

Suggested labels on the receiving repo: the track name (`programming`,
`mechanical`, …), the role id (`programmer`, `fabricator`, …), and
`size-1` / `size-2` / `size-3`.

## After export

- Put the issues on a **GitHub Project**. Columns such as Icebox / Selected /
  In Progress / In Review / Done are enough.
- A student claims one ticket, does the work in *their* repo or shop, and
  moves the card to In Review with a link to the evidence.
- A mentor accepts against the ticket's acceptance criteria — not against a
  vibe.
- This playbook is not updated when a student finishes a ticket. Their team's
  board is.

Full authoring and export notes live in the repo at
[`tickets/README.md`](https://github.com/gavinjalberghini/FRC-SS/blob/main/tickets/README.md).
