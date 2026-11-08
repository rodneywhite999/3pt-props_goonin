# NFL Touchdown Alerts 🏈

Sends you a notification **for every touchdown, by every team, in every NFL game** —
typically 15–30 seconds after it happens (well under the 1-minute target).

It polls ESPN's public scoreboard every 15 s and, for each live game, the game's
scoring-play list. Each new touchdown (passing, rushing, return, defensive — any TD)
is sent once to whichever channels you set up:

| Channel | Cost | Setup effort | Notes |
|---|---|---|---|
| **ntfy** (phone push) | Free | 2 min | **Recommended.** Fastest and simplest. iOS + Android. |
| **Microsoft Teams** | Free | 5 min | Posts a card to a chat/channel via a Workflows webhook. |
| **WhatsApp – CallMeBot** | Free | 3 min | Personal-use bot; can be rate-limited on busy Sundays. |
| **WhatsApp – Twilio** | ~$0.005–0.01/msg | 15 min | Official API. Sandbox needs re-joining every 72 h; a production sender needs Meta approval. |

Example alert:

```
TOUCHDOWN Kansas City Chiefs!
Travis Kelce 12 Yd pass from Patrick Mahomes (Harrison Butker Kick)
Q2 4:31 · BUF 7 – KC 14
```

No API keys are needed for the NFL data. The script is a single Python file with no
dependencies (Python 3.9+).

---

## 1. Set up a channel (pick one or more)

### ntfy — phone push (recommended)
1. Install **ntfy** from the App Store / Google Play.
2. Tap **+**, subscribe to a topic with a long random name, e.g. `td-alerts-8f3k2q9x`
   (anyone who knows the name can read it, so make it unguessable).
3. Set `NTFY_TOPIC=td-alerts-8f3k2q9x`.

### Microsoft Teams
1. In Teams, open the chat or channel → **⋯** → **Workflows** →
   *"Send webhook alerts to a chat"* (or *"...to a channel"*).
2. Finish the wizard and copy the webhook URL.
3. Set `TEAMS_WEBHOOK_URL=<that URL>`.

### WhatsApp via CallMeBot (free)
1. Follow the steps at <https://www.callmebot.com/blog/free-api-whatsapp-messages/>
   (add their number, send the activation message, get your API key).
2. Set `CALLMEBOT_PHONE=+15551234567` and `CALLMEBOT_APIKEY=<key>`.

### WhatsApp via Twilio
1. Create a Twilio account → *Messaging → Try it out → Send a WhatsApp message*,
   and join the sandbox from your phone.
2. Set `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`,
   `TWILIO_WHATSAPP_FROM=+14155238886` (sandbox number), `WHATSAPP_TO=+15551234567`.

---

## 2. Run it (pick one)

It has to run somewhere that stays on during games.

### Option A — GitHub Actions (no computer of your own needed)
The workflow at `.github/workflows/nfl-td-alerts.yml` starts every 30 minutes, exits
in seconds if no game is live or about to start, and otherwise watches until the
games finish.

1. Merge this into the repo's **default branch** (scheduled workflows only run from there).
2. Repo → **Settings → Secrets and variables → Actions** → add secrets for your channel
   (e.g. `NTFY_TOPIC`, or `TEAMS_WEBHOOK_URL`, …). Optionally add a *variable*
   `TEAMS_FILTER` such as `KC,BUF` to limit alerts to some teams.
3. **Actions → NFL TD alerts → Run workflow** with *test* ticked to check you get a notification.

Caveats: Actions minutes are free and unlimited for **public** repos. On a **private**
repo they count toward the 2,000 free min/month, and a single NFL week uses roughly
1,500–2,000 minutes, so a private repo would run out within the first week — make the
repo public (the secrets stay private) or use option B/C. GitHub can start scheduled runs a few minutes late
(the job starts watching 75 min before kickoff to absorb that), and pauses schedules
after 60 days without commits to the repo.

### Option B — Docker (any always-on PC, Raspberry Pi, or cheap VPS)
```bash
cd nfl-td-alerts
cp .env.example .env      # fill in your channel
docker compose up -d --build
docker compose run --rm td-alerts python td_alerts.py --test
```

### Option C — plain Python
```bash
cd nfl-td-alerts
export NTFY_TOPIC=td-alerts-8f3k2q9x
python3 td_alerts.py --test   # check the channel
python3 td_alerts.py          # run forever
```
A systemd unit (`td-alerts.service`) is included for Linux servers.

---

## Options

| Variable / flag | Default | Meaning |
|---|---|---|
| `POLL_SECONDS` | `15` | How often to poll. Keep ≥ 10 s to be polite to ESPN. |
| `TEAMS_FILTER` | *(all)* | Comma-separated team abbreviations to limit alerts. |
| `STATE_FILE` | `td_state.json` | Remembers which TDs were sent so restarts don't re-send. |
| `--alert-existing` | off | When first starting mid-game, also send TDs already scored. |
| `--while-games` | off | Exit once nothing is live or starting soon (used by option A). |
| `--once` / `-v` | | Single poll / verbose logging for debugging. |

## How it works / limits
- Data comes from ESPN's public, unofficial JSON endpoints. They are free and
  widely used but undocumented, so ESPN could change them; the script backs off
  and retries on errors.
- Latency = ESPN posting the play (usually ~10–30 s) + up to 15 s polling + delivery (~1–2 s).
- A touchdown overturned on replay after it's already posted will still have been sent.
- Run `python3 -m unittest discover -s tests` for the tests.
