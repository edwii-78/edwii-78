#!/usr/bin/env python3
"""
TryHackMe Stats Card — SOC Themed
Update STATS dict manually when your profile changes.
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
    W, H = 740, 230
    now  = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # stat column x positions
    C1, C2, C3 = 230, 420, 590

    return f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="leftpanel" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{rc}" stop-opacity="0.13"/>
      <stop offset="100%" stop-color="{rc}" stop-opacity="0.02"/>
    </linearGradient>
    <linearGradient id="topbar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{rc}"     stop-opacity="0.9"/>
      <stop offset="50%"  stop-color="#1f6feb"  stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{rc}"     stop-opacity="0.3"/>
    </linearGradient>
    <linearGradient id="botbar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="{rc}"    stop-opacity="0"/>
      <stop offset="40%"  stop-color="{rc}"    stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#1f6feb" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <!-- ── BASE ── -->
  <rect width="{W}" height="{H}" rx="10" fill="#0d1117" stroke="#21262d" stroke-width="1"/>

  <!-- left panel tint -->
  <rect x="0" y="0" width="205" height="{H}" rx="10" fill="url(#leftpanel)"/>

  <!-- top accent bar -->
  <rect x="0" y="0" width="{W}" height="3" rx="1" fill="url(#topbar)"/>

  <!-- left edge accent -->
  <rect x="0" y="0" width="3" height="{H}" rx="1" fill="{rc}" opacity="0.7"/>

  <!-- ── LEFT PANEL ── -->

  <!-- THM label -->
  <text x="24" y="36"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="{rc}" font-weight="700" letter-spacing="2.5"
    opacity="0.85">TRYHACKME</text>

  <!-- username -->
  <text x="24" y="65"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,sans-serif"
    font-size="19" fill="#e6edf3" font-weight="600">{s["username"]}</text>

  <!-- rank pill -->
  <rect x="22" y="76" width="100" height="22" rx="11"
    fill="{rc}" opacity="0.12" stroke="{rc}" stroke-width="0.8"/>
  <text x="72" y="91"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="{rc}" text-anchor="middle" font-weight="700"
    filter="url(#glow)">{s["rank"].upper()}</text>

  <!-- separator -->
  <line x1="24" y1="114" x2="182" y2="114" stroke="#21262d" stroke-width="1"/>

  <!-- percentile big number -->
  <text x="24" y="148"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="28" fill="{rc}" font-weight="700"
    filter="url(#glow)">{s["percentile"]}</text>

  <text x="24" y="166"
    font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="1.5">GLOBAL PERCENTILE</text>

  <!-- ── VERTICAL DIVIDERS ── -->
  <line x1="205" y1="16" x2="205" y2="{H-16}" stroke="#21262d" stroke-width="1"/>
  <line x1="420" y1="16" x2="420" y2="{H-16}" stroke="#21262d" stroke-width="1"/>
  <line x1="590" y1="16" x2="590" y2="{H-16}" stroke="#21262d" stroke-width="1"/>

  <!-- ── STAT: POINTS ── -->
  <text x="{C1}" y="50"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="#6e7681" letter-spacing="1.5">POINTS</text>
  <text x="{C1}" y="105"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="46" fill="#e6edf3" font-weight="700">{s["points"]:,}</text>
  <!-- small bar indicator -->
  <rect x="{C1}" y="118" width="80" height="2" rx="1" fill="#21262d"/>
  <rect x="{C1}" y="118" width="{min(80, int(s['points']/2))}" height="2" rx="1" fill="#e6edf3" opacity="0.4"/>

  <!-- ── STAT: ROOMS ── -->
  <text x="{C2}" y="50"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="#6e7681" letter-spacing="1.5">ROOMS COMPLETED</text>
  <text x="{C2}" y="105"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="46" fill="#3fb950" font-weight="700">{s["rooms"]}</text>
  <rect x="{C2}" y="118" width="80" height="2" rx="1" fill="#21262d"/>
  <rect x="{C2}" y="118" width="{min(80, s['rooms']*6)}" height="2" rx="1" fill="#3fb950" opacity="0.5"/>

  <!-- ── STAT: STREAK ── -->
  <text x="{C3}" y="50"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="#6e7681" letter-spacing="1.5">DAY STREAK</text>
  <text x="{C3}" y="105"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="46" fill="#d29922" font-weight="700">{s["streak"]}</text>
  <rect x="{C3}" y="118" width="80" height="2" rx="1" fill="#21262d"/>
  <rect x="{C3}" y="118" width="{min(80, s['streak']*3)}" height="2" rx="1" fill="#d29922" opacity="0.5"/>

  <!-- ── STAT: BADGES (bottom row) ── -->
  <text x="{C1}" y="152"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="#6e7681" letter-spacing="1.5">BADGES EARNED</text>
  <text x="{C1}" y="186"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="36" fill="#bc8cff" font-weight="700">{s["badges"]}</text>

  <!-- paths completed label -->
  <text x="{C2}" y="152"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="#6e7681" letter-spacing="1.5">ACTIVE PATHS</text>
  <text x="{C2}" y="186"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="36" fill="#1f6feb" font-weight="700">2</text>

  <!-- account type -->
  <text x="{C3}" y="152"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="#6e7681" letter-spacing="1.5">ACCOUNT TYPE</text>
  <text x="{C3}" y="186"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="18" fill="#8b949e" font-weight="600">FREE</text>

  <!-- ── FOOTER ── -->
  <rect x="0" y="{H-26}" width="{W}" height="1" fill="#21262d"/>

  <!-- blinking online dot -->
  <circle cx="18" cy="{H-12}" r="4" fill="#3fb950">
    <animate attributeName="opacity" values="1;0.15;1" dur="2.2s" repeatCount="indefinite"/>
  </circle>
  <text x="28" y="{H-8}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#3fb950" letter-spacing="0.5">PROFILE ACTIVE</text>

  <!-- THM link hint -->
  <text x="190" y="{H-8}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#30363d">tryhackme.com/p/{s["username"]}</text>

  <!-- timestamp right -->
  <text x="{W-10}" y="{H-8}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#30363d" text-anchor="end">Updated {now}</text>

  <!-- bottom animated pulse -->
  <rect x="0" y="{H-2}" width="{W}" height="2" rx="1" fill="url(#botbar)" opacity="0">
    <animate attributeName="opacity" values="0;0.8;0" dur="3.5s" repeatCount="indefinite"/>
  </rect>
</svg>"""

if __name__ == "__main__":
    svg = make_svg()
    os.makedirs("assets", exist_ok=True)
    path = "assets/thm-stats.svg"
    with open(path, "w") as f:
        f.write(svg)
    print(f"Written {path}  ({len(svg):,} bytes)")
    print(f"Stats used: {STATS}")
