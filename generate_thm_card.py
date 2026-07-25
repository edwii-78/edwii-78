#!/usr/bin/env python3
"""
TryHackMe Stats Card — SOC Edition
Edwin Dominic | edwii-78
Update STATS when your profile changes. Run via GitHub Actions.
"""
from datetime import datetime
import os

# ── UPDATE WHEN STATS CHANGE ──────────────────────────────────────────────────
STATS = {
    "username":   "edwindominic7878",
    "rank":       "Seeker",
    "percentile": "Top 30%",
    "points":     34,
    "rooms":      16,
    "streak":     42,
    "badges":     3,
    "paths":      2,
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

def make_svg() -> str:
    s   = STATS
    rc  = RANK_COLOUR
    W   = 760
    H   = 210
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Column x-positions for stat groups
    C1, C2, C3, C4 = 220, 365, 510, 648

    # Thin horizontal rule y
    MID = 120

    return f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Left panel ambient glow -->
    <linearGradient id="lpanel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{rc}" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="{rc}" stop-opacity="0.00"/>
    </linearGradient>
    <!-- Top accent bar -->
    <linearGradient id="topbar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{rc}"    stop-opacity="0.0"/>
      <stop offset="20%"  stop-color="{rc}"    stop-opacity="1.0"/>
      <stop offset="65%"  stop-color="#1f6feb" stop-opacity="1.0"/>
      <stop offset="100%" stop-color="#1f6feb" stop-opacity="0.0"/>
    </linearGradient>
    <!-- Bottom pulse bar -->
    <linearGradient id="botbar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{rc}"    stop-opacity="0.0"/>
      <stop offset="35%"  stop-color="{rc}"    stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#1f6feb" stop-opacity="0.0"/>
    </linearGradient>
  </defs>

  <!-- Card base -->
  <rect width="{W}" height="{H}" rx="8" fill="#0d1117" stroke="#21262d" stroke-width="0.5"/>

  <!-- Left panel ambient tint -->
  <rect x="0" y="0" width="200" height="{H}" rx="8" fill="url(#lpanel)"/>

  <!-- Top accent line -->
  <rect x="0" y="0" width="{W}" height="2" rx="1" fill="url(#topbar)"/>

  <!-- Left edge accent -->
  <rect x="0" y="12" width="2" height="{H - 24}" rx="1" fill="{rc}" opacity="0.6"/>

  <!-- ── LEFT IDENTITY PANEL ─────────────────────────────────────────── -->

  <!-- Platform label -->
  <text x="18" y="32"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="{rc}" font-weight="700" letter-spacing="2"
    opacity="0.7">TRYHACKME</text>

  <!-- Username -->
  <text x="18" y="56"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,sans-serif"
    font-size="17" fill="#e6edf3" font-weight="600"
    textLength="174" lengthAdjust="spacingAndGlyphs">{s["username"]}</text>

  <!-- Rank pill — no filter, solid colour only -->
  <rect x="16" y="64" width="86" height="18" rx="9"
    fill="{rc}" opacity="0.12" stroke="{rc}" stroke-width="0.6"/>
  <text x="59" y="76"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="{rc}" text-anchor="middle"
    font-weight="700" letter-spacing="0.5">{s["rank"].upper()}</text>

  <!-- Thin rule -->
  <line x1="16" y1="96" x2="188" y2="96" stroke="#21262d" stroke-width="0.5"/>

  <!-- Percentile — the standout number -->
  <text x="16" y="126"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="26" fill="{rc}" font-weight="700">{s["percentile"]}</text>

  <text x="16" y="142"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="1.2">GLOBAL PERCENTILE</text>

  <!-- ── VERTICAL DIVIDERS ──────────────────────────────────────────── -->
  <line x1="200" y1="14" x2="200" y2="{H - 22}" stroke="#21262d" stroke-width="0.5"/>
  <line x1="345" y1="14" x2="345" y2="{H - 22}" stroke="#21262d" stroke-width="0.5"/>
  <line x1="490" y1="14" x2="490" y2="{H - 22}" stroke="#21262d" stroke-width="0.5"/>
  <line x1="635" y1="14" x2="635" y2="{H - 22}" stroke="#21262d" stroke-width="0.5"/>

  <!-- ── HORIZONTAL MID RULE (separates top/bottom stat rows) ──────── -->
  <line x1="200" y1="{MID}" x2="{W - 4}" y2="{MID}" stroke="#21262d" stroke-width="0.5"/>

  <!-- ── STAT: POINTS ──────────────────────────────────────────────── -->
  <text x="{C1}" y="40"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681" letter-spacing="1.5">POINTS</text>
  <text x="{C1}" y="90"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="40" fill="#e6edf3" font-weight="700">{s["points"]:,}</text>

  <!-- ── STAT: ROOMS COMPLETED ─────────────────────────────────────── -->
  <text x="{C2}" y="40"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681" letter-spacing="1.5">ROOMS</text>
  <text x="{C2}" y="90"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="40" fill="#3fb950" font-weight="700">{s["rooms"]}</text>

  <!-- ── STAT: DAY STREAK ──────────────────────────────────────────── -->
  <text x="{C3}" y="40"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681" letter-spacing="1.5">DAY STREAK</text>
  <text x="{C3}" y="90"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="40" fill="#d29922" font-weight="700">{s["streak"]}</text>

  <!-- ── STAT: BADGES ──────────────────────────────────────────────── -->
  <text x="{C4}" y="40"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681" letter-spacing="1.5">BADGES</text>
  <text x="{C4}" y="90"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="40" fill="#bc8cff" font-weight="700">{s["badges"]}</text>

  <!-- ── BOTTOM ROW — secondary stats ─────────────────────────────── -->

  <!-- Completed label -->
  <text x="{C2}" y="{MID + 20}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681" letter-spacing="1">COMPLETED</text>
  <text x="{C2}" y="{MID + 42}"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
    font-size="12" fill="#8b949e">{s["rooms"]} rooms · {s["badges"]} badges</text>

  <!-- Streak context -->
  <text x="{C3}" y="{MID + 20}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681" letter-spacing="1">BEST STREAK</text>
  <text x="{C3}" y="{MID + 42}"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
    font-size="12" fill="#8b949e">{s["streak"]} days active</text>

  <!-- Paths -->
  <text x="{C4}" y="{MID + 20}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681" letter-spacing="1">ACTIVE PATHS</text>
  <text x="{C4}" y="{MID + 42}"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
    font-size="12" fill="#8b949e">SOC L1 · AI Security</text>

  <!-- Left panel bottom — cert callout -->
  <text x="16" y="{MID + 20}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#6e7681" letter-spacing="1">CLEARANCE</text>
  <text x="16" y="{MID + 40}"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
    font-size="11" fill="{rc}">CEH v13 · CSCU</text>

  <!-- ── FOOTER ─────────────────────────────────────────────────────── -->
  <line x1="0" y1="{H - 22}" x2="{W}" y2="{H - 22}" stroke="#21262d" stroke-width="0.5"/>

  <!-- Status dot -->
  <circle cx="14" cy="{H - 11}" r="3.5" fill="#3fb950">
    <animate attributeName="opacity" values="1;0.15;1" dur="2.4s" repeatCount="indefinite"/>
  </circle>
  <text x="23" y="{H - 7}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#3fb950" letter-spacing="0.5">ACTIVE</text>

  <!-- Profile URL -->
  <text x="90" y="{H - 7}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#30363d">tryhackme.com/p/{s["username"]}</text>

  <!-- Timestamp -->
  <text x="{W - 8}" y="{H - 7}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#30363d" text-anchor="end">Updated {now}</text>

  <!-- Bottom animated pulse -->
  <rect x="0" y="{H - 2}" width="{W}" height="2" rx="1" fill="url(#botbar)" opacity="0">
    <animate attributeName="opacity" values="0;0.7;0" dur="3.5s" repeatCount="indefinite"/>
  </rect>
</svg>"""


if __name__ == "__main__":
    svg  = make_svg()
    os.makedirs("assets", exist_ok=True)
    path = "assets/thm-stats.svg"
    with open(path, "w") as f:
        f.write(svg)
    print(f"Written {path}  ({len(svg):,} bytes)")
    print(f"Stats: {STATS}")
