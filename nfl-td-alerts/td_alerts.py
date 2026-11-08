#!/usr/bin/env python3
"""
NFL Touchdown Alerts
====================
Watches every NFL game (ESPN's public scoreboard feed) and sends a notification
for every touchdown, by any team, within seconds of ESPN posting it.

Notification channels (enable any combination via environment variables):
  * ntfy        - free push notifications to the ntfy phone app (recommended)
  * Teams       - Microsoft Teams channel/chat via a Workflows webhook
  * WhatsApp    - via Twilio (official API) or CallMeBot (free, personal use)

Standard library only - no pip install needed. Python 3.9+.

Usage:
  python td_alerts.py                # run forever
  python td_alerts.py --test         # send a test notification and exit
  python td_alerts.py --once         # single poll (debugging)
  python td_alerts.py --while-games  # run while games are live/upcoming, then exit
                                     # (used by the GitHub Actions deployment)
"""
from __future__ import annotations

import argparse
import base64
import json
import logging
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

SCOREBOARD_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
SUMMARY_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/summary"
USER_AGENT = "nfl-td-alerts/1.0"

log = logging.getLogger("td_alerts")


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #
def env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


@dataclass
class Config:
    poll_seconds: float = float(env("POLL_SECONDS", "15"))
    state_file: Path = Path(env("STATE_FILE", "td_state.json"))
    # Only alert for these team abbreviations (e.g. "KC,BUF"). Empty = every team.
    team_filter: frozenset = frozenset(
        t.strip().upper() for t in env("TEAMS_FILTER").split(",") if t.strip()
    )
    # --while-games: keep running if a game kicks off within this many minutes
    pregame_minutes: int = int(env("PREGAME_MINUTES", "75"))
    # --while-games: hard stop (GitHub Actions jobs are capped at 6h)
    max_runtime_minutes: int = int(env("MAX_RUNTIME_MINUTES", "345"))


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def http_get_json(url: str, params: dict | None = None, timeout: float = 10) -> dict:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def http_post(url: str, data: bytes, headers: dict, timeout: float = 10) -> int:
    req = urllib.request.Request(url, data=data, headers={"User-Agent": USER_AGENT, **headers}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status


# --------------------------------------------------------------------------- #
# Touchdown model
# --------------------------------------------------------------------------- #
@dataclass
class Touchdown:
    play_id: str
    game_id: str
    team: str           # scoring team abbreviation
    team_name: str
    description: str
    quarter: str
    clock: str
    away: str
    home: str
    away_score: int
    home_score: int

    @property
    def title(self) -> str:
        return f"🏈 TOUCHDOWN {self.team_name or self.team}!"

    @property
    def body(self) -> str:
        return (
            f"{self.description}\n"
            f"{self.quarter} {self.clock} · {self.away} {self.away_score} – {self.home} {self.home_score}"
        ).strip()


def quarter_label(period: int) -> str:
    if period <= 4:
        return f"Q{period}"
    return "OT" if period == 5 else f"{period - 4}OT"


def is_touchdown(play: dict) -> bool:
    for key in ("scoringType", "type"):
        info = play.get(key) or {}
        if str(info.get("abbreviation", "")).upper() == "TD":
            return True
        if "touchdown" in str(info.get("name", "")).lower() or "touchdown" in str(info.get("text", "")).lower():
            return True
    return False


def parse_touchdowns(game_id: str, summary: dict, away: str, home: str) -> list[Touchdown]:
    tds = []
    for play in summary.get("scoringPlays") or []:
        if not is_touchdown(play):
            continue
        team = play.get("team") or {}
        tds.append(
            Touchdown(
                play_id=str(play.get("id")),
                game_id=game_id,
                team=str(team.get("abbreviation", "")).upper(),
                team_name=team.get("displayName") or team.get("name") or "",
                description=play.get("text", "") or (play.get("type") or {}).get("text", "Touchdown"),
                quarter=quarter_label(int((play.get("period") or {}).get("number", 0) or 0)),
                clock=(play.get("clock") or {}).get("displayValue", ""),
                away=away,
                home=home,
                away_score=int(play.get("awayScore", 0) or 0),
                home_score=int(play.get("homeScore", 0) or 0),
            )
        )
    return tds


@dataclass
class Game:
    id: str
    state: str          # "pre" | "in" | "post"
    away: str
    home: str
    start: datetime | None


def parse_scoreboard(board: dict) -> list[Game]:
    games = []
    for ev in board.get("events") or []:
        comp = (ev.get("competitions") or [{}])[0]
        state = ((comp.get("status") or ev.get("status") or {}).get("type") or {}).get("state", "")
        teams = {c.get("homeAway"): (c.get("team") or {}).get("abbreviation", "?") for c in comp.get("competitors") or []}
        start = None
        if ev.get("date"):
            try:
                start = datetime.fromisoformat(ev["date"].replace("Z", "+00:00"))
            except ValueError:
                pass
        games.append(Game(str(ev.get("id")), state, teams.get("away", "?"), teams.get("home", "?"), start))
    return games


# --------------------------------------------------------------------------- #
# Notifiers
# --------------------------------------------------------------------------- #
class Notifier:
    name = "base"

    def send(self, title: str, body: str) -> None:  # pragma: no cover
        raise NotImplementedError


class NtfyNotifier(Notifier):
    name = "ntfy"

    def __init__(self, topic: str, server: str, token: str = ""):
        self.url = f"{server.rstrip('/')}/{topic}"
        self.token = token

    def send(self, title: str, body: str) -> None:
        # HTTP headers must be latin-1, so drop the emoji from the title (the
        # "football" tag makes ntfy show a 🏈 anyway).
        safe_title = title.encode("latin-1", "ignore").decode("latin-1").strip() or "Touchdown"
        headers = {"Title": safe_title, "Priority": "high", "Tags": "football"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        http_post(self.url, body.encode("utf-8"), headers)


class TeamsNotifier(Notifier):
    """Teams 'Workflows' webhook (Power Automate 'When a Teams webhook request is received')."""
    name = "teams"

    def __init__(self, url: str):
        self.url = url

    def send(self, title: str, body: str) -> None:
        card = {
            "type": "message",
            "attachments": [{
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.4",
                    "body": [
                        {"type": "TextBlock", "text": title, "weight": "Bolder", "size": "Large", "wrap": True},
                        *[{"type": "TextBlock", "text": line, "wrap": True} for line in body.split("\n")],
                    ],
                },
            }],
        }
        http_post(self.url, json.dumps(card).encode("utf-8"), {"Content-Type": "application/json"})


class TwilioWhatsAppNotifier(Notifier):
    name = "whatsapp-twilio"

    def __init__(self, sid: str, token: str, from_: str, to: str):
        self.url = f"https://api.twilio.com/2010-04-01/Accounts/{sid}/Messages.json"
        self.auth = base64.b64encode(f"{sid}:{token}".encode()).decode()
        self.from_ = from_ if from_.startswith("whatsapp:") else f"whatsapp:{from_}"
        self.to = to if to.startswith("whatsapp:") else f"whatsapp:{to}"

    def send(self, title: str, body: str) -> None:
        data = urllib.parse.urlencode({"From": self.from_, "To": self.to, "Body": f"*{title}*\n{body}"}).encode()
        http_post(self.url, data, {"Authorization": f"Basic {self.auth}",
                                   "Content-Type": "application/x-www-form-urlencoded"})


class CallMeBotWhatsAppNotifier(Notifier):
    name = "whatsapp-callmebot"

    def __init__(self, phone: str, apikey: str):
        self.phone, self.apikey = phone, apikey

    def send(self, title: str, body: str) -> None:
        q = urllib.parse.urlencode({"phone": self.phone, "text": f"*{title}*\n{body}", "apikey": self.apikey})
        req = urllib.request.Request(f"https://api.callmebot.com/whatsapp.php?{q}", headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15):
            pass


def build_notifiers() -> list[Notifier]:
    out: list[Notifier] = []
    if env("NTFY_TOPIC"):
        out.append(NtfyNotifier(env("NTFY_TOPIC"), env("NTFY_SERVER", "https://ntfy.sh"), env("NTFY_TOKEN")))
    if env("TEAMS_WEBHOOK_URL"):
        out.append(TeamsNotifier(env("TEAMS_WEBHOOK_URL")))
    if env("TWILIO_ACCOUNT_SID") and env("TWILIO_AUTH_TOKEN") and env("TWILIO_WHATSAPP_FROM") and env("WHATSAPP_TO"):
        out.append(TwilioWhatsAppNotifier(env("TWILIO_ACCOUNT_SID"), env("TWILIO_AUTH_TOKEN"),
                                          env("TWILIO_WHATSAPP_FROM"), env("WHATSAPP_TO")))
    if env("CALLMEBOT_PHONE") and env("CALLMEBOT_APIKEY"):
        out.append(CallMeBotWhatsAppNotifier(env("CALLMEBOT_PHONE"), env("CALLMEBOT_APIKEY")))
    return out


def notify_all(notifiers: list[Notifier], title: str, body: str) -> None:
    for n in notifiers:
        for attempt in range(3):
            try:
                n.send(title, body)
                log.info("sent via %s", n.name)
                break
            except Exception as e:  # noqa: BLE001
                log.warning("%s send failed (attempt %d): %s", n.name, attempt + 1, e)
                time.sleep(1 + attempt)


# --------------------------------------------------------------------------- #
# Watcher
# --------------------------------------------------------------------------- #
class Watcher:
    def __init__(self, cfg: Config, notifiers: list[Notifier], fetch=http_get_json):
        self.cfg = cfg
        self.notifiers = notifiers
        self.fetch = fetch
        self.seen: set[str] = set()
        self.primed_games: set[str] = set()   # games whose existing TDs we've recorded
        self.tracking: set[str] = set()       # games seen live this run (re-check once at final)
        self.alert_existing = False           # alert TDs scored before we first saw the game
        self._load()

    # -- state ------------------------------------------------------------- #
    def _load(self) -> None:
        try:
            data = json.loads(self.cfg.state_file.read_text())
            self.seen = set(data.get("seen", []))
            self.primed_games = set(data.get("primed_games", []))
        except FileNotFoundError:
            pass
        except Exception as e:  # noqa: BLE001
            log.warning("could not read state file: %s", e)

    def _save(self) -> None:
        tmp = self.cfg.state_file.with_suffix(".tmp")
        # keep the file small: only the most recent ~5000 entries
        tmp.write_text(json.dumps({"seen": sorted(self.seen)[-5000:],
                                   "primed_games": sorted(self.primed_games)[-1000:]}))
        tmp.replace(self.cfg.state_file)

    # -- polling ----------------------------------------------------------- #
    def poll(self) -> list[Game]:
        board = self.fetch(SCOREBOARD_URL, {"_": int(time.time())})
        games = parse_scoreboard(board)
        changed = False
        for g in games:
            if g.state == "in":
                self.tracking.add(g.id)
            elif g.id not in self.tracking:
                continue
            try:
                summary = self.fetch(SUMMARY_URL, {"event": g.id, "_": int(time.time())})
            except Exception as e:  # noqa: BLE001
                log.warning("summary fetch failed for %s: %s", g.id, e)
                continue
            tds = parse_touchdowns(g.id, summary, g.away, g.home)
            first_look = g.id not in self.primed_games and not self.alert_existing
            for td in tds:
                if td.play_id in self.seen:
                    continue
                self.seen.add(td.play_id)
                changed = True
                if first_look:
                    continue  # TD happened before we started watching this game; don't spam
                if self.cfg.team_filter and td.team not in self.cfg.team_filter:
                    continue
                log.info("TD: %s | %s", td.title, td.body.replace("\n", " | "))
                notify_all(self.notifiers, td.title, td.body)
            if g.id not in self.primed_games:
                self.primed_games.add(g.id)
                changed = True
            if g.state == "post":
                self.tracking.discard(g.id)
        if changed:
            self._save()
        return games

    def games_active_or_soon(self, games: list[Game]) -> bool:
        now = datetime.now(timezone.utc)
        for g in games:
            if g.state == "in" or g.id in self.tracking:
                return True
            if g.state == "pre" and g.start and (g.start - now).total_seconds() <= self.cfg.pregame_minutes * 60:
                return True
        return False

    def run(self, while_games: bool = False) -> None:
        started = time.monotonic()
        backoff = self.cfg.poll_seconds
        while True:
            t0 = time.monotonic()
            try:
                games = self.poll()
                backoff = self.cfg.poll_seconds
                live = sum(1 for g in games if g.state == "in")
                log.debug("polled: %d games, %d live", len(games), live)
                if while_games and not self.games_active_or_soon(games):
                    log.info("no live or upcoming games - exiting")
                    return
            except Exception as e:  # noqa: BLE001
                log.warning("poll failed: %s", e)
                backoff = min(backoff * 2, 60)
            if while_games and time.monotonic() - started > self.cfg.max_runtime_minutes * 60:
                log.info("max runtime reached - exiting")
                return
            time.sleep(max(1.0, backoff - (time.monotonic() - t0)))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="NFL touchdown alerts")
    p.add_argument("--test", action="store_true", help="send a test notification and exit")
    p.add_argument("--once", action="store_true", help="poll once and exit")
    p.add_argument("--while-games", action="store_true", help="exit when no games are live or about to start")
    p.add_argument("--alert-existing", action="store_true",
                   help="on first sight of a game, also alert TDs already scored (default: skip them)")
    p.add_argument("-v", "--verbose", action="store_true")
    a = p.parse_args(argv)

    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO,
                        format="%(asctime)s %(levelname)s %(message)s")
    notifiers = build_notifiers()
    if not notifiers:
        log.error("No notification channel configured. Set NTFY_TOPIC, TEAMS_WEBHOOK_URL, "
                  "Twilio WhatsApp vars, or CALLMEBOT_PHONE/CALLMEBOT_APIKEY. See README.")
        return 2
    log.info("channels: %s", ", ".join(n.name for n in notifiers))

    if a.test:
        notify_all(notifiers, "🏈 TOUCHDOWN Test Team!",
                   "This is a test from nfl-td-alerts. If you see this, alerts are working.\nQ1 0:00 · AWY 0 – HME 7")
        return 0

    w = Watcher(Config(), notifiers)
    w.alert_existing = a.alert_existing
    if a.once:
        games = w.poll()
        log.info("%d games on the board, %d live", len(games), sum(g.state == "in" for g in games))
        return 0
    w.run(while_games=a.while_games)
    return 0


if __name__ == "__main__":
    sys.exit(main())
