#!/usr/bin/env python3
"""
TryHackMe Stats Card Generator - Fixed endpoints
Stats hardcoded as fallback, API attempted first.
"""
import json, os, sys, urllib.request, urllib.error
from datetime import datetime

USERNAME  = "edwindominic7878"
USER_HASH = os.environ.get("THM_USER_HASH", "")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": f"https://tryhackme.com/p/{USERNAME}",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read()
            print(f"  OK {url} -> {raw[:120]}")
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code} {url}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  ERR {url}: {e}", file=sys.stderr)
        return None

def get_stats():
    # Fallback = what we can read from your profile screenshot
    stats = {
        "username": USERNAME,
        "rank":     "Seeker",
        "percentile": "Top 35%",
        "points":   34,
        "rooms":    13,
        "streak":   22,
        "badges":   2,
    }

    # Try endpoint 1 — v2 public-profile
    d = fetch(f"https://tryhackme.com/api/v2/public-profile?username={USERNAME}")
    if d:
        p = d.get("userProfile") or d.get("data") or d
        if isinstance(p, dict):
            stats["points"]  = p.get("points", stats["points"])
            stats["streak"]  = p.get("currentStreak", p.get("streak", stats["streak"]))
            ur = p.get("userRank") or p.get("rank", {})
            if isinstance(ur, dict):
                stats["rank"] = ur.get("title", stats["rank"])
            elif isinstance(ur, str):
                stats["rank"] = ur

    # Try endpoint 2 — v1 public profile (older, more reliable)
    d2 = fetch(f"https://tryhackme.com/api/user/{USERNAME}")
    if d2:
        stats["points"]     = d2.get("points",         stats["points"])
        stats["rooms"]      = d2.get("completedRooms", stats["rooms"])
        stats["streak"]     = d2.get("streak",         stats["streak"])

    # Try endpoint 3 — badges list
    d3 = fetch(f"https://tryhackme.com/api/v2/users/badges?username={USERNAME}")
    if d3:
        if isinstance(d3, list):
            stats["badges"] = len(d3)
        elif isinstance(d3, dict):
            bl = d3.get("data") or d3.get("badges") or []
            stats["badges"] = len(bl)

    print(f"Final stats: {stats}")
    return stats

def make_svg(s, path):
    W, H = 480, 160

    rank_colour = {
        "seeker":       "#a371f7",
        "newbie":       "#6e7681",
        "junior":       "#3fb950",
        "intermediate": "#1f6feb",
        "advanced":     "#d29922",
        "expert":       "#f85149",
        "master":       "#bc8cff",
        "god":          "#ffa657",
    }.get(s["rank"].lower(), "#a371f7")

    rank_text = f"{s['rank'].title()}"
    pct_text  = s.get("percentile", "")
    left_line2 = pct_text if pct_text else rank_text

    svg = f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="lgrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1f6feb" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#1f6feb" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- card -->
  <rect width="{W}" height="{H}" rx="6" fill="#0d1117" stroke="#21262d" stroke-width="1"/>
  <!-- top accent -->
  <rect width="{W}" height="2" rx="1" fill="#1f6feb" opacity="0.9"/>
  <!-- left tint -->
  <rect x="0" y="0" width="155" height="{H}" rx="6" fill="url(#lgrad)"/>

  <!-- THM label -->
  <text x="20" y="26"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="#1f6feb" font-weight="600" letter-spacing="1">TRYHACKME</text>

  <!-- username -->
  <text x="20" y="47"
    font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
    font-size="15" fill="#e6edf3" font-weight="600">{s["username"]}</text>

  <!-- rank pill -->
  <rect x="18" y="56" width="80" height="17" rx="8"
    fill="{rank_colour}" opacity="0.15" stroke="{rank_colour}" stroke-width="0.8"/>
  <text x="58" y="68"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="9" fill="{rank_colour}" text-anchor="middle" font-weight="600">{rank_text}</text>

  <!-- percentile -->
  <text x="20" y="92"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="11" fill="{rank_colour}" font-weight="600">{left_line2}</text>

  <!-- divider 1 -->
  <line x1="155" y1="14" x2="155" y2="{H-14}" stroke="#21262d" stroke-width="1"/>

  <!-- POINTS -->
  <text x="178" y="48"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="26" fill="#e6edf3" font-weight="700">{s["points"]:,}</text>
  <text x="178" y="63"
    font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="0.8">POINTS</text>

  <!-- ROOMS -->
  <text x="178" y="108"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="26" fill="#3fb950" font-weight="700">{s["rooms"]}</text>
  <text x="178" y="123"
    font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="0.8">ROOMS COMPLETED</text>

  <!-- divider 2 -->
  <line x1="318" y1="14" x2="318" y2="{H-14}" stroke="#21262d" stroke-width="1"/>

  <!-- STREAK -->
  <text x="342" y="48"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="26" fill="#d29922" font-weight="700">{s["streak"]}</text>
  <text x="342" y="63"
    font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="0.8">DAY STREAK</text>

  <!-- BADGES -->
  <text x="342" y="108"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="26" fill="#bc8cff" font-weight="700">{s["badges"]}</text>
  <text x="342" y="123"
    font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="0.8">BADGES EARNED</text>

  <!-- timestamp -->
  <text x="{W-10}" y="{H-7}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#30363d" text-anchor="end"
    >Updated {datetime.utcnow().strftime("%Y-%m-%d %H:%M")} UTC</text>

  <!-- bottom pulse -->
  <rect x="0" y="{H-2}" width="{W}" height="1" fill="#1f6feb" opacity="0">
    <animate attributeName="opacity" values="0;0.5;0" dur="4s" repeatCount="indefinite"/>
  </rect>
</svg>"""

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(svg)
    print(f"Written: {path}")

if __name__ == "__main__":
    s = get_stats()
    make_svg(s, "assets/thm-stats.svg")
