#!/usr/bin/env python3
"""Create GitHub issues from the playbook's learning tickets.

This site does not track student work. A team copies the tickets into *their*
GitHub repository (Issues + a Project board) and mentors students there.

Usage (from the repo root, after `gh auth login`):

    python3 scripts/create_issues.py --dry-run
    python3 scripts/create_issues.py --repo owner/team-learning
    python3 scripts/create_issues.py --track programming --repo owner/team-learning
    python3 scripts/create_issues.py --export-dir dist/tickets
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

TRACKS = {
    "programming": "Programming",
    "mechanical": "Mechanical",
    "electrical": "Electrical",
    "cad": "CAD",
    "printing": "3D Printing",
    "business-outreach": "Business",
    "strategy-scouting": "Strategy",
    "drive-team": "Drive Team",
    "leadership": "Leadership",
}


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, parts[2].lstrip("\n")


def discover_tickets(root: pathlib.Path, track: str | None) -> list[pathlib.Path]:
    learning = root / "docs" / "learning"
    files: list[pathlib.Path] = []
    tracks = [track] if track else sorted(TRACKS)
    for name in tracks:
        if name not in TRACKS:
            raise SystemExit(f"unknown track {name!r}; choose from: {', '.join(TRACKS)}")
        files.extend(sorted((learning / name).glob("*.md")))
    return files


def issue_title(track: str, meta: dict[str, str]) -> str:
    label = TRACKS[track]
    order = meta.get("order", "")
    title = meta.get("title") or "Untitled ticket"
    if order.isdigit():
        return f"[{label} {int(order):02d}] {title}"
    return f"[{label}] {title}"


def issue_body(track: str, meta: dict[str, str], body: str, page_url: str | None) -> str:
    role = meta.get("role", "")
    size = meta.get("size", "")
    time = meta.get("time", "")
    header_bits = [f"**Track:** {TRACKS[track]}"]
    if role:
        header_bits.append(f"**Role:** {role}")
    if size:
        header_bits.append(f"**Effort:** {size}/3")
    if time:
        header_bits.append(f"**Time:** {time}")
    header = " · ".join(header_bits)
    if page_url:
        header += f"\n\nPlaybook page: {page_url}"
    if not body.endswith("\n"):
        body += "\n"
    return f"{header}\n\n{body}"


def page_url(track: str, path: pathlib.Path) -> str:
    return f"https://gavinjalberghini.github.io/FRC-SS/learning/{track}/{path.stem}/"


def write_export(export_dir: pathlib.Path, track: str, path: pathlib.Path, title: str, body: str) -> None:
    dest_dir = export_dir / track
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{path.name}"
    dest.write_text(f"# {title}\n\n{body}", encoding="utf-8")


def create_issue(repo: str | None, title: str, body: str, labels: list[str]) -> None:
    cmd = ["gh", "issue", "create", "--title", title, "--body", body]
    for label in labels:
        cmd.extend(["--label", label])
    if repo:
        cmd.extend(["--repo", repo])
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        raise SystemExit(result.returncode)
    print(result.stdout.strip())


def main() -> None:
    parser = argparse.ArgumentParser(description="Export learning tickets as GitHub issues")
    parser.add_argument("--repo", help="owner/name (defaults to the current gh repo)")
    parser.add_argument("--track", choices=sorted(TRACKS), help="export one track only")
    parser.add_argument("--dry-run", action="store_true", help="print titles without creating issues")
    parser.add_argument(
        "--export-dir",
        type=pathlib.Path,
        help="also write portable markdown copies (no Jekyll front matter)",
    )
    parser.add_argument(
        "--no-labels",
        action="store_true",
        help="do not attach track/role/size labels (use if the target repo has no labels yet)",
    )
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parents[1]
    files = discover_tickets(root, args.track)
    if not files:
        raise SystemExit("no ticket files found")

    if args.export_dir:
        args.export_dir.mkdir(parents=True, exist_ok=True)

    for path in files:
        track = path.parent.name
        meta, body = parse_front_matter(path.read_text(encoding="utf-8"))
        title = issue_title(track, meta)
        full_body = issue_body(track, meta, body, page_url(track, path))
        labels = [] if args.no_labels else [track, meta.get("role", ""), f"size-{meta.get('size', '1')}"]
        labels = [label for label in labels if label]
        print(f"{track}/{path.name}: {title}")
        if args.export_dir:
            write_export(args.export_dir, track, path, title, full_body)
        if args.dry_run:
            continue
        create_issue(args.repo, title, full_body, labels)


if __name__ == "__main__":
    main()
