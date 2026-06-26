#!/usr/bin/env python3
"""
TryHackMe Stats Card Generator
Credentials loaded from environment variables — never hardcoded.
"""
import json, os, sys, urllib.request, urllib.error
from datetime import datetime

USERNAME  = "edwindominic7878"
USER_HASH = os.environ.get("THM_USER_HASH", "")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; GitHubActions/1.0)",
    "Accept": "application/json",
    "Referer": f"https://tryhackme.com/p/{USERNAME}",
}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code} for {url}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def get_stats():
    stats = {
        "username": USERNAME,
        "rank":     "Unranked",
        "points":   0,
        "rooms":    0,
        "streak":   0,
        "badges":   0,
    }

    if not USER_HASH:
        print("WARNING: THM_USER_HASH not set — rooms count will be 0", file=sys.stderr)

    # 1. Public profile — rank, points, streak
    d = fetch(f"https://tryhackme.com/api/v2/public-profile?username={USERNAME}")
    if d and d.get("success") and d.get("userProfile"):
        p = d["userProfile"]
        stats["points"] = p.get("points", 0)
        ur = p.get("userRank", {})
        stats["rank"]   = ur.get("title", "Unranked") if isinstance(ur, dict) else str(ur)
        sk = p.get("streak", {})
        stats["streak"] = sk.get("currentStreak", 0) if isinstance(sk, dict) else 0

    # 2. Completed rooms count — needs user hash
    if USER_HASH:
        d2 = fetch(
            f"https://tryhackme.com/api/v2/public-profile/completed-rooms"
            f"?user={USER_HASH}&limit=1&page=1"
        )
        if d2 and isinstance(d2, dict):
            stats["rooms"] = d2.get("total", d2.get("count", 0))

    # 3. Badges count — username only, no hash needed
    d3 = fetch(f"https://tryhackme.com/api/v2/users/badges?username={USERNAME}")
    if d3 and isinstance(d3, list):
        stats["badges"] = len(d3)
    elif d3 and isinstance(d3, dict):
        stats["badges"] = len(d3.get("data", d3.get("badges", [])))

    print(f"Stats: {stats}")
    return stats

def make_svg(s, path):
    W, H = 480, 160

    rank_colour = {
        "newbie":       "#6e7681",
        "junior":       "#3fb950",
        "intermediate": "#1f6feb",
        "advanced":     "#d29922",
        "expert":       "#f85149",
        "master":       "#bc8cff",
        "god":          "#ffa657",
    }.get(s["rank"].lower(), "#8b949e")

    rank_label_w = max(len(s["rank"]) * 8 + 20, 60)

    svg = f"""<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hdr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#1f6feb" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#1f6feb" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <rect width="{W}" height="{H}" rx="6" fill="#0d1117" stroke="#21262d" stroke-width="1"/>
  <rect width="{W}" height="3" rx="1" fill="#1f6feb" opacity="0.9"/>
  <rect x="0" y="0" width="155" height="{H}" rx="6" fill="url(#hdr)"/>

  <!-- label -->
  <text x="20" y="26" font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="#1f6feb" font-weight="600" letter-spacing="0.8">TRYHACKME</text>

  <!-- username -->
  <text x="20" y="48" font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
    font-size="15" fill="#e6edf3" font-weight="600">{s["username"]}</text>

  <!-- rank pill -->
  <rect x="18" y="58" width="{rank_label_w}" height="18" rx="9"
    fill="{rank_colour}" opacity="0.15" stroke="{rank_colour}" stroke-width="0.8"/>
  <text x="{18 + rank_label_w // 2}" y="71"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="10" fill="{rank_colour}" text-anchor="middle" font-weight="600"
    >{s["rank"].title()}</text>

  <!-- divider 1 -->
  <line x1="155" y1="14" x2="155" y2="{H - 14}" stroke="#21262d" stroke-width="1"/>

  <!-- Points -->
  <text x="178" y="50" font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="24" fill="#e6edf3" font-weight="700">{s["points"]:,}</text>
  <text x="178" y="66" font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="0.8">POINTS</text>

  <!-- Rooms -->
  <text x="178" y="108" font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="24" fill="#3fb950" font-weight="700">{s["rooms"]}</text>
  <text x="178" y="124" font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="0.8">ROOMS COMPLETED</text>

  <!-- divider 2 -->
  <line x1="318" y1="14" x2="318" y2="{H - 14}" stroke="#21262d" stroke-width="1"/>

  <!-- Streak -->
  <text x="342" y="50" font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="24" fill="#d29922" font-weight="700">{s["streak"]}</text>
  <text x="342" y="66" font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="0.8">DAY STREAK</text>

  <!-- Badges -->
  <text x="342" y="108" font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="24" fill="#bc8cff" font-weight="700">{s["badges"]}</text>
  <text x="342" y="124" font-family="-apple-system,BlinkMacSystemFont,sans-serif"
    font-size="9" fill="#6e7681" letter-spacing="0.8">BADGES EARNED</text>

  <!-- updated timestamp -->
  <text x="{W - 10}" y="{H - 8}"
    font-family="ui-monospace,'SF Mono',Consolas,monospace"
    font-size="8" fill="#30363d" text-anchor="end"
    >Updated {datetime.utcnow().strftime("%Y-%m-%d %H:%M")} UTC</text>

  <!-- bottom pulse -->
  <rect x="0" y="{H - 3}" width="{W}" height="1" fill="#1f6feb" opacity="0">
    <animate attributeName="opacity" values="0;0.5;0" dur="4s" repeatCount="indefinite"/>
  </rect>
</svg>"""

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(svg)
    print(f"Written: {path}")

if __name__ == "__main__":
    if not USER_HASH:
        print("ERROR: THM_USER_HASH environment variable not set.", file=sys.stderr)
        sys.exit(1)
    s = get_stats()
    make_svg(s, "assets/thm-stats.svg")
