# Learning tickets

This playbook's learning modules are **tickets**: a description of what to
learn, explicit tasks, checkable acceptance criteria, and curated outside
resources. They are written so a mentor can assign one and a student can finish
it without guessing what "done" means.

The website is a **guideline**, not a gradebook. It does not sign students in,
store progress, or collect homework. A team that wants to track work should
export these tickets into **their own** GitHub (or other) environment.

## Ticket anatomy

Every lesson page in `docs/learning/<track>/*.md` is a ticket. The body uses
the same sections as the tickets in
[ml-bootcamp](https://github.com/gavinjalberghini/ml-bootcamp):

| Section | What it is for |
| --- | --- |
| **Description** | Teach the idea. Why it matters on an FRC team, what is easy to get wrong, and how this ticket connects to the one before and after it. |
| **Prerequisites** | What must already be true. Link earlier tickets. |
| **What you'll learn** | A short list of outcomes, in student language. |
| **Tasks** | Numbered, procedural work. Watch, read, try, write, demonstrate. Offload depth to a specific video, article, or official doc when that source is better than rewriting it. |
| **Acceptance Criteria** | Achievable, observable checks a mentor can sign off. Prefer a named artifact, a demonstration, or a written answer over "understand X." |
| **Resources** | The outside material the tasks already pointed at, collected in one place. |
| **Notes** | Gotchas, scope limits, and what *not* to do. |

Front matter (`title`, `role`, `order`, `size`, `time`, `permalink`) is for the
website. The export script strips it and builds a GitHub issue title like
`[Programming 01] GitHub Basics`.

## Export into a team's GitHub

1. Create (or pick) the repository where the team will track learning — a
   dedicated `team-learning` repo is typical. This playbook repo should stay
   a guideline.
2. Optionally create labels that match the export: track names
   (`programming`, `mechanical`, …), role ids (`programmer`, `fabricator`, …),
   and `size-1` / `size-2` / `size-3`.
3. From a clone of this playbook:

   ```bash
   gh auth login
   python3 scripts/create_issues.py --dry-run
   python3 scripts/create_issues.py --repo your-org/team-learning
   python3 scripts/create_issues.py --track programming --repo your-org/team-learning
   ```

   Add `--no-labels` if the target repo does not have those labels yet.

4. Put the created issues on a GitHub Project. Students move a card
   Selected → In Progress → In Review → Done. Mentors accept against the
   ticket's acceptance criteria.

To get portable markdown (no Jekyll front matter) without creating issues:

```bash
python3 scripts/create_issues.py --dry-run --export-dir dist/tickets
```

That writes one file per ticket under `dist/tickets/<track>/`. A team can
commit that folder, feed it to another tool, or import it later.

## What this repo will not do

- Host student repositories, Onshape homework, or shop sign-off sheets.
- Provide a login, progress bar, or quiz engine.
- Close tickets for you. Acceptance happens on the team's board, in the shop,
  or in a mentoring conversation.

## Authoring a new ticket

Add a lesson markdown file under `docs/learning/<track>/`, add a matching
entry in the track's `_data/*_curriculum.yml`, and keep the sections above.
Write as if you are teaching in person: explain the idea, then give a task
that proves it, then name the evidence. Point at FIRST, WPILib, vendor docs,
FRCDesign, and well-chosen videos instead of inventing a textbook from
scratch.
