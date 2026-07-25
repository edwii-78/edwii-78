#!/usr/bin/env python3
"""
SOC Log Stream Animation Generator
Edwin Dominic | edwii-78
Reads contribution data via GitHub GraphQL API.
Each cell = a log event. Red scan line = SIEM detection sweep.
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime


# ── CONFIG ────────────────────────────────────────────────────────────────────
USERNAME = os.environ.get("GITHUB_USERNAME", "edwii-78")
TOKEN    = os.environ.get("GITHUB_TOKEN", "")

PALETTE_DARK = {
    "bg":       "#0d1117",
    "empty":    "#161b22",
    "levels":   ["#161b22", "#0d2137", "#0d3a6e", "#1158c7", "#1f6feb"],
    "scan":     "#f85149",
    "label":    "#8b949e",
    "caption":  "#6e7681",
    "border":   "#21262d",
}

PALETTE_LIGHT = {
    "bg":       "#ffffff",
    "empty":    "#ebedf0",
    "levels":   ["#ebedf0", "#9fc5f8", "#4a90d9", "#1f6feb", "#0d47a1"],
    "scan":     "#cf222e",
    "label":    "#57606a",
    "caption":  "#6e7681",
    "border":   "#d0d7de",
}

# Grid geometry
CELL = 11
GAP  = 3
STEP = CELL + GAP
LEFT = 32      # left margin for day labels
TOP  = 28      # top margin for month labels
# ─────────────────────────────────────────────────────────────────────────────


def fetch_contributions(username: str, token: str) -> list:
    query = (
        '{ user(login: "%s") { contributionsCollection {'
        ' contributionCalendar { weeks { contributionDays {'
        ' contributionCount weekday date } } } } } }' % username
    )
    payload = json.dumps({"query": query}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
    return (
        data["data"]["user"]
            ["contributionsCollection"]
            ["contributionCalendar"]
            ["weeks"]
    )


def count_to_level(c: int) -> int:
    if c == 0:  return 0
    if c <= 2:  return 1
    if c <= 5:  return 2
    if c <= 9:  return 3
    return 4


def month_labels(weeks: list) -> list:
    """Return (x, label) pairs — deduplicated by (month, year) so
    Jan 2025 and Jan 2026 both appear correctly."""
    seen   = set()
    labels = []
    for wi, week in enumerate(weeks):
        for day in week["contributionDays"]:
            try:
                dt = datetime.strptime(day["date"], "%Y-%m-%d")
            except ValueError:
                continue
            key = (dt.year, dt.month)
            if key not in seen and dt.day <= 7:
                seen.add(key)
                x = LEFT + wi * STEP
                labels.append((x, dt.strftime("%b")))
    return labels


def generate_svg(weeks: list, dark: bool = True) -> str:
    p    = PALETTE_DARK if dark else PALETTE_LIGHT
    cols = len(weeks)
    W    = LEFT + cols * STEP + 16
    H    = TOP  + 7 * STEP + 32

    x_start = LEFT - 1
    x_end   = LEFT + cols * STEP + 2

    lines = [
        f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}"'
        f' xmlns="http://www.w3.org/2000/svg">',
        f'  <rect width="{W}" height="{H}" fill="{p["bg"]}"/>',
    ]

    # ── Month labels ──────────────────────────────────────────────────────────
    for (mx, mlabel) in month_labels(weeks):
        lines.append(
            f'  <text x="{mx}" y="{TOP - 6}"'
            f' font-family="ui-monospace,\'SF Mono\',Consolas,monospace"'
            f' font-size="9" fill="{p["label"]}">{mlabel}</text>'
        )

    # ── Day labels (Mon / Wed / Fri) ──────────────────────────────────────────
    for di, dl in enumerate(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]):
        if di in (1, 3, 5):
            ly = TOP + di * STEP + CELL - 1
            lines.append(
                f'  <text x="{LEFT - 5}" y="{ly}"'
                f' font-family="ui-monospace,\'SF Mono\',Consolas,monospace"'
                f' font-size="9" fill="{p["label"]}" text-anchor="end">{dl}</text>'
            )

    # ── Contribution cells ────────────────────────────────────────────────────
    for week in weeks:
        for day in week["contributionDays"]:
            lv  = count_to_level(day["contributionCount"])
            col = p["levels"][lv]
            wd  = day["weekday"]
            # calc week index from first week
            wi  = weeks.index(week)
            cx  = LEFT + wi * STEP
            cy  = TOP  + wd * STEP
            lines.append(
                f'  <rect x="{cx}" y="{cy}" width="{CELL}" height="{CELL}"'
                f' rx="2" fill="{col}"/>'
            )

    # ── Scan line — single 1px element, no glow rect ─────────────────────────
    scan_y  = TOP - 3
    scan_h  = 7 * STEP + 6
    scan_dur = "3.5s"

    lines.append("  <!-- SOC SIEM detection sweep -->")
    lines.append(
        f'  <rect x="{x_start}" y="{scan_y}" width="1" height="{scan_h}"'
        f' fill="{p["scan"]}" opacity="0">'
    )
    lines.append(
        f'    <animate attributeName="x"'
        f' from="{x_start}" to="{x_end}" dur="{scan_dur}" repeatCount="indefinite"/>'
    )
    lines.append(
        f'    <animate attributeName="opacity"'
        f' values="0;0.9;0.9;0" keyTimes="0;0.02;0.98;1"'
        f' dur="{scan_dur}" repeatCount="indefinite"/>'
    )
    lines.append("  </rect>")

    lines.append("</svg>")
    return "\n".join(lines)


def write(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"Written: {path}  ({len(content):,} bytes)")


if __name__ == "__main__":
    if not TOKEN:
        print("ERROR: GITHUB_TOKEN not set", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching contributions for {USERNAME}...")
    weeks = fetch_contributions(USERNAME, TOKEN)
    print(f"  {len(weeks)} weeks fetched")

    write("dist/soc-log-stream-dark.svg",  generate_svg(weeks, dark=True))
    write("dist/soc-log-stream.svg",       generate_svg(weeks, dark=False))
    print("Done.")
