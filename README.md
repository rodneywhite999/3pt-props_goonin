[README.md](https://github.com/user-attachments/files/25471542/README.md)
# NBA 3PT Prop Scanner

A single-file browser tool that scans live NBA 3-point prop lines across sportsbooks and identifies edges using a Poisson-based projection model fed by real player stats from the balldontlie API.

## How It Works

1. Pulls live 3PT prop odds from multiple sportsbooks via The Odds API
2. Fetches real player game logs from balldontlie (season averages + last 10 games)
3. Projects expected 3-pointers made using a modified Poisson model with contextual adjustments:
   - Opponent 3PT defense ranking
   - Home/away splits
   - Pace and game total
   - Spread/blowout risk (minutes reduction)
   - Foul trouble tendency
   - Teammate effects (spacing/usage changes from injuries)
4. Compares model probabilities against book odds to find edges
5. Grades edges as LEAN / VALUE / STRONG based on magnitude

## Setup

You need two free/cheap API keys:

| API | Cost | What it does |
|-----|------|-------------|
| [The Odds API](https://the-odds-api.com) | Free (500 req/mo) | Live prop odds from sportsbooks |
| [balldontlie](https://app.balldontlie.io) | $9.99/mo (ALL-STAR tier) | Real player game logs and stats |

### First Run

1. Open `3pt-scanner-v8.html` in any browser
2. Go to the **⚙ Setup** tab and paste both API keys
3. Go to the **👥 Players** tab and click **📡 Refresh All Stats**
4. Wait ~5 minutes for the initial data pull (103 players)
5. Go to the **📊 Scanner** tab and click **🚀 Scan All 3PT Props**

### Daily Use

1. Click **📡 Refresh All Stats** once per day (~30 seconds on retries)
2. Click **🚀 Scan** whenever you want to check lines

## Important: No Estimated Data

This scanner enforces a strict rule: **stats are either real API data or blank**. There are zero estimates or hardcoded numbers. If you see a player marked with ✗ in the Players tab, their data hasn't been verified yet — run Refresh.

## What the Scan Shows

- **STRONG** — Large edge (5%+), high confidence
- **VALUE** — Moderate edge worth considering
- **LEAN** — Small edge, proceed with caution
- **λ (lambda)** — Model's projected 3PM for the game
- **Edge %** — How far the model's probability diverges from the book's implied probability

## Tech Stack

- Single HTML file, no build tools, no dependencies
- Vanilla JavaScript
- All data stored in browser localStorage
- Works on desktop and mobile

## License

MIT — do whatever you want with it.
