#!/usr/bin/env python3
"""
SOC Log Stream Animation Generator
Reads Edwin's GitHub contribution data (via API) and produces an animated SVG
that looks like a SIEM log feed streaming across the contribution grid.
Each contribution cell = a log event. Animated sweep = threat scan.
"""

import json, os, sys, math, random
from datetime import datetime, timedelta

def fetch_contributions(username, token):
    """Fetch 52 weeks of contribution data from GitHub GraphQL API."""
    import urllib.request
    query = """{ user(login: "%s") { contributionsCollection { contributionCalendar { weeks { contributionDays { contributionCount weekday date } } } } } }""" % username
    payload = json.dumps({"query": query}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=payload,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.loads(r.read())
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return weeks

def count_to_level(c):
    if c == 0: return 0
    if c <= 2: return 1
    if c <= 5: return 2
    if c <= 9: return 3
    return 4

def generate_svg(weeks, output_path, dark=True):
    # Colour scheme: dark bg, blue log cells, red animated scanner
    bg        = "#0d1117" if dark else "#ffffff"
    cell_0    = "#161b22" if dark else "#ebedf0"
    cell_cols = ["#161b22", "#0d2137", "#0d3a6e", "#1158c7", "#1f6feb"] if dark else \
                ["#ebedf0", "#9fc5f8", "#4a90d9", "#1f6feb", "#0d47a1"]
    scan_col  = "#f85149"
    text_col  = "#6e7681" if dark else "#57606a"
    label_col = "#8b949e" if dark else "#57606a"

    CELL = 11   # cell size
    GAP  = 3    # gap
    STEP = CELL + GAP
    LEFT = 38   # left margin for day labels
    TOP  = 32   # top margin for month labels

    cols = len(weeks)
    rows = 7
    W = LEFT + cols * STEP + 20
    H = TOP  + rows * STEP + 40

    # Build cell data
    cells = []
    for wi, week in enumerate(weeks):
        for day in week["contributionDays"]:
            wd = day["weekday"]
            lv = count_to_level(day["contributionCount"])
            x  = LEFT + wi * STEP
            y  = TOP  + wd * STEP
            cells.append((x, y, lv, wi, day["contributionCount"]))

    # Month labels
    month_labels = []
    seen_months = set()
    for wi, week in enumerate(weeks):
        for day in week["contributionDays"]:
            try:
                dt = datetime.strptime(day["date"], "%Y-%m-%d")
                m  = dt.strftime("%b")
                if m not in seen_months and dt.day <= 7:
                    seen_months.add(m)
                    month_labels.append((LEFT + wi * STEP, TOP - 6, m))
            except:
                pass

    # Day labels
    day_labels = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

    # SVG start
    lines = [
        f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">',
        f'  <rect width="{W}" height="{H}" fill="{bg}"/>',
    ]

    # Month labels
    for (lx, ly, lm) in month_labels:
        lines.append(f'  <text x="{lx}" y="{ly}" font-family="ui-monospace,monospace" font-size="9" fill="{label_col}">{lm}</text>')

    # Day labels (Mon / Wed / Fri only)
    for di, dl in enumerate(day_labels):
        if di in (1, 3, 5):
            ly = TOP + di * STEP + CELL - 1
            lines.append(f'  <text x="{LEFT-4}" y="{ly}" font-family="ui-monospace,monospace" font-size="9" fill="{label_col}" text-anchor="end">{dl}</text>')

    # Contribution cells
    for (cx, cy, lv, wi, count) in cells:
        colour = cell_cols[lv]
        lines.append(f'  <rect x="{cx}" y="{cy}" width="{CELL}" height="{CELL}" rx="2" fill="{colour}"/>')

    # Animated scanner — vertical line sweeping left→right
    scan_dur  = "3.5s"
    x_start   = LEFT - 2
    x_end     = LEFT + cols * STEP + 4
    scan_x    = LEFT

    lines.append(f'  <!-- SOC Scan sweep -->')
    # Glow rect wide
    lines.append(f'  <rect x="{scan_x}" y="{TOP-4}" width="3" height="{rows*STEP+8}" rx="1" fill="{scan_col}" opacity="0.18">')
    lines.append(f'    <animate attributeName="x" from="{x_start}" to="{x_end}" dur="{scan_dur}" repeatCount="indefinite"/>')
    lines.append(f'    <animate attributeName="opacity" values="0;0.18;0.18;0" keyTimes="0;0.02;0.98;1" dur="{scan_dur}" repeatCount="indefinite"/>')
    lines.append(f'  </rect>')
    # Thin bright line
    lines.append(f'  <rect x="{scan_x}" y="{TOP-4}" width="1" height="{rows*STEP+8}" fill="{scan_col}" opacity="0.9">')
    lines.append(f'    <animate attributeName="x" from="{x_start}" to="{x_end}" dur="{scan_dur}" repeatCount="indefinite"/>')
    lines.append(f'    <animate attributeName="opacity" values="0;0.9;0.9;0" keyTimes="0;0.02;0.98;1" dur="{scan_dur}" repeatCount="indefinite"/>')
    lines.append(f'  </rect>')

    # Bottom label
    lines.append(f'  <text x="{LEFT}" y="{H-6}" font-family="ui-monospace,monospace" font-size="8" fill="{text_col}">SIEM LOG EVENTS · CONTRIBUTION ACTIVITY</text>')

    lines.append('</svg>')
    svg = "\n".join(lines)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(svg)
    print(f"Written: {output_path} ({len(svg)} bytes, {len(cells)} cells)")

if __name__ == "__main__":
    token    = os.environ.get("GITHUB_TOKEN", "")
    username = os.environ.get("GITHUB_USERNAME", "edwii-78")
    if not token:
        print("ERROR: GITHUB_TOKEN not set", file=sys.stderr)
        sys.exit(1)
    print(f"Fetching contributions for {username}...")
    weeks = fetch_contributions(username, token)
    generate_svg(weeks, "dist/soc-log-stream-dark.svg", dark=True)
    generate_svg(weeks, "dist/soc-log-stream.svg",      dark=False)
    print("Done.")
