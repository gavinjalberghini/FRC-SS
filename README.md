# FRC-SS — FRC Playbook

A static GitHub Pages site (Jekyll) that hosts a **playbook for running an FRC
robotics team**. It's meant to be a living, team-editable home for:

- **Mission & Values** (`/mission/`) — what the team stands for.
- **Org Chart** (`/org-chart/`) — roles, responsibilities, and structure.
- **Team Contract** (`/contract/`) — conduct, commitment, and safety expectations.
- **Season Roadmap** (`/roadmap/`) — a phase-by-phase plan for the year.
- **Learning Hub** (`/learning/`) — role-based resources for every member.

> The current content is a **stub/template**. Replace the placeholder text with
> your team's real details (mission, names, vendors, links, etc.).

## Project structure

All written page content lives in `docs/`; everything at the repo root is site
infrastructure (layout, styling, config, tooling). Pages render at their
`permalink`, not their file path, so the folder layout never changes their URLs.

```text
.
├── docs/                  # All written content (pages)
│   ├── index.html         #   Home page (permalink: /)
│   ├── mission.md         #   Mission & values
│   ├── org-chart.md       #   Org chart
│   ├── contract.md        #   Team contract
│   ├── roadmap.md         #   Season roadmap
│   └── learning/          #   Learning hub + per-role tracks
├── .github/workflows/     # GitHub Actions: build & deploy to Pages
├── _config.yml            # Site settings (title, baseurl, team info)
├── _data/nav.yml          # Header/footer navigation
├── _includes/             # head, header, footer partials
├── _layouts/              # default + page layouts
├── _sass/main.scss        # Site styles (imported by assets/css/style.scss)
├── assets/css/style.scss  # Jekyll entry point (compiled to /assets/css/style.css)
├── Taskfile.yml           # Local lint / build / test tasks (go-task)
├── Gemfile                # Ruby deps (Jekyll + html-proofer)
└── package.json           # Node deps (markdownlint, stylelint, prettier)
```

## Configure for your team

Edit `_config.yml` and update the `team:` block (number, name, region) and the
`title`/`tagline`. Update `baseurl` to match how the site is served (see below).

## Local development & tooling

Day-to-day work is driven by [go-task](https://taskfile.dev). Run `task` with no
arguments to list everything.

### Prerequisites

- **Ruby 3.1+ (via Homebrew)** — builds and serves the Jekyll site.
- **Node.js + npm** — runs the linters/formatter (markdownlint, stylelint, Prettier).
- **go-task** — the task runner (`brew install go-task`).

The macOS system Ruby is too old for Jekyll, so install a current Ruby with
[Homebrew](https://brew.sh) (works on macOS and on WSL2 via Linuxbrew):

```bash
brew install ruby
```

Then make sure that Ruby (not the system one at `/usr/bin/ruby`) is used by
adding this to your shell profile (`~/.zshrc` or `~/.bashrc`). It's written to be
portable across macOS and WSL2:

```bash
# Prefer Homebrew's Ruby over the system Ruby
if command -v brew >/dev/null 2>&1; then
  export PATH="$(brew --prefix ruby)/bin:$PATH"
fi
```

Open a new shell and confirm with `ruby -v` (should be 3.1+).

> **WSL2:** install Homebrew first (<https://brew.sh>), then `brew install ruby`.
> The shell-profile snippet above already resolves the correct path on Linuxbrew.

### One-time setup

```bash
task install   # installs Node tools (npm) + Ruby gems into ./vendor/bundle
```

Gems install into the project's `./vendor/bundle` (git-ignored), so nothing is
installed globally.

### Common tasks

| Command              | What it does                                                |
| -------------------- | ----------------------------------------------------------- |
| `task serve`         | Serve locally with live reload (<http://localhost:4000/FRC-SS/>) |
| `task build`         | Build the site into `_site/`                                |
| `task lint`          | Lint Markdown, SCSS, and formatting                         |
| `task format`        | Auto-fix formatting (Prettier + `stylelint --fix`)          |
| `task test`          | Build, then validate HTML and internal links (no network)   |
| `task test:external` | Also check external links (slower, needs network)           |
| `task check`         | `lint` + `build` + `test` — run this before opening a PR     |
| `task clean`         | Remove `_site/` and caches                                  |

The linters are also exposed as npm scripts (`npm run lint`, `npm run format`)
if you prefer not to install go-task. For a local preview without the project
path, run `bundle exec jekyll serve --baseurl ""` and open <http://localhost:4000/>.

## Deploy with GitHub Pages

The site deploys at `https://gavinjalberghini.github.io/FRC-SS/` via **GitHub
Actions** (`.github/workflows/pages.yml`), which builds with the modern Jekyll
version pinned in the `Gemfile` rather than GitHub's frozen, EOL built-in build.

One-time setup:

1. In **Settings → Pages**, set **Source** to **GitHub Actions**.
2. Push to `main`. The workflow builds and publishes automatically; subsequent
   pushes redeploy.

The workflow sets `baseurl` to `/FRC-SS` automatically (via `configure-pages`),
so you don't need to change `_config.yml` for deployment. If you later use a
custom domain, set `baseurl` to `""` and add a `CNAME` file.

> Because we deploy via Actions (not a branch folder), the `docs/` content folder
> needs no special Pages configuration — the whole repo is built as one Jekyll site.

## Contributing

This is a team document. Propose changes by opening a pull request — every
member is encouraged to keep the playbook accurate and useful. Run `task check`
before pushing so linting and link validation pass.
