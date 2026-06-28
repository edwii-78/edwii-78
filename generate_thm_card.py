#!/usr/bin/env python3
"""
TryHackMe Stats Card Generator
Stats are set here and updated manually — THM API blocks GitHub Actions IPs
and requires 100+ points before exposing rank data publicly.
Update STATS dict whenever your THM profile changes.
"""
from datetime import datetime
import os

# ── UPDATE THESE WHEN YOUR STATS CHANGE ──────────────────────────────────────
STATS = {
    "username":   "edwindominic7878",
    "rank":       "Seeker",
    "percentile": "Top 9%",
    "points":     34,
    "rooms":      13,
    "streak":     24,
    "badges":     2,
}
# ─────────────────────────────────────────────────────────────────────────────

RANK_COLOUR = {
    "seeker":       "#a371f7",
    "newbie":       "#6e7681",
    "junior":       "#3fb950",
    "intermediate": "#1f6feb",
    "advanced":     "#d29922",
    "expert":       "#f85149",
    "master":       "#bc8cff",
    "god":          "#ffa657",
}.get(STATS["rank"].lower(), "#a371f7")

def make_svg():
    s  = STATS
    rc = RANK_COLOUR
    W, H = 580, 200
    now  = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    return f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="leftfade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{rc}" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="{rc}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="topbar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{rc}" stop-opacity="0"/>
      <stop offset="30%" stop-color="{rc}" stop-opacity="1"/>
      <stop offset="70%" stop-color="#1f6feb" stop-opacity="1"/>
      <stop offset="100%" stop-color="#1f6feb" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- card base -->
  <rect width="{W}" height="{H}" rx="8" fill="#0d1117" stroke="#21262d" stroke-width="1"/>

  <!-- left accent tint -->
  <rect x="0" y="0" width="185" height="{H}" rx="8" fill="url(#leftfade)"/>

  <!-- top accent line -->
  <rect x="0" y="0" width="{W}" height="2" rx="1" fill="url(#topbar)"/>

  <!-- left border accent -->
  <rect x="0" y="0" width="2" height="{H}" rx="1" fill="{rc}" opacity="0.6"/>

  <!-- ── LEFT PANEL ─────────────────────────────────────── -->

  <!-- THM wordmark -->
  <text x="22" y="34"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="{rc}" font-weight="700" letter-spacing="2"
    opacity="0.9">TRYHACKME</text>

  <!-- username -->
  <text x="22" y="60"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,sans-serif"
    font-size="17" fill="#e6edf3" font-weight="600">{s["username"]}</text>

  <!-- rank pill -->
  <rect x="20" y="70" width="88" height="20" rx="10"
    fill="{rc}" opacity="0.12" stroke="{rc}" stroke-width="0.8"/>
  <text x="64" y="84"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="{rc}" text-anchor="middle" font-weight="700"
    >{s["rank"].upper()}</text>

  <!-- percentile -->
  <text x="22" y="115"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="20" fill="{rc}" font-weight="700">{s["percentile"]}</text>

  <text x="22" y="132"
    font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="1">GLOBAL RANKING</text>

  <!-- ── DIVIDER ─────────────────────────────────────────── -->
  <line x1="185" y1="18" x2="185" y2="{H-18}"
    stroke="#21262d" stroke-width="1"/>

  <!-- ── STATS GRID ─────────────────────────────────────── -->

  <!-- POINTS -->
  <text x="212" y="56"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="#6e7681" letter-spacing="1">POINTS</text>
  <text x="212" y="90"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="32" fill="#e6edf3" font-weight="700">{s["points"]:,}</text>

  <!-- ROOMS COMPLETED -->
  <text x="212" y="128"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="#6e7681" letter-spacing="1">ROOMS COMPLETED</text>
  <text x="212" y="162"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="32" fill="#3fb950" font-weight="700">{s["rooms"]}</text>

  <!-- divider 2 -->
  <line x1="395" y1="18" x2="395" y2="{H-18}"
    stroke="#21262d" stroke-width="1"/>

  <!-- DAY STREAK -->
  <text x="420" y="56"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="#6e7681" letter-spacing="1">DAY STREAK</text>
  <text x="420" y="90"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="32" fill="#d29922" font-weight="700">{s["streak"]}</text>

  <!-- BADGES EARNED -->
  <text x="420" y="128"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="#6e7681" letter-spacing="1">BADGES EARNED</text>
  <text x="420" y="162"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="32" fill="#bc8cff" font-weight="700">{s["badges"]}</text>

  <!-- ── FOOTER ──────────────────────────────────────────── -->
  <line x1="0" y1="{H-22}" x2="{W}" y2="{H-22}"
    stroke="#21262d" stroke-width="1"/>

  <circle cx="14" cy="{H-11}" r="4" fill="#3fb950">
    <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="24" y="{H-7}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681">LIVE STATS</text>

  <text x="{W-10}" y="{H-7}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#30363d" text-anchor="end">Updated {now}</text>

  <!-- bottom pulse line -->
  <rect x="0" y="{H-2}" width="{W}" height="1" rx="1" fill="#1f6feb" opacity="0">
    <animate attributeName="opacity" values="0;0.4;0" dur="3s" repeatCount="indefinite"/>
  </rect>
</svg>"""

if __name__ == "__main__":
    svg = make_svg()
    os.makedirs("assets", exist_ok=True)
    with open("assets/thm-stats.svg", "w") as f:
        f.write(svg)
    print(f"Written assets/thm-stats.svg ({len(svg)} bytes)")
    print(f"Stats: {STATS}")
