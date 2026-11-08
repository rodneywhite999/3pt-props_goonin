import sys, tempfile, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import td_alerts as t  # noqa: E402


def board(state="in"):
    return {"events": [{
        "id": "401", "date": "2026-11-08T18:00Z",
        "competitions": [{
            "status": {"type": {"state": state}},
            "competitors": [
                {"homeAway": "home", "team": {"abbreviation": "KC"}},
                {"homeAway": "away", "team": {"abbreviation": "BUF"}},
            ],
        }],
    }]}


def play(pid, kind="TD", team="KC", away=0, home=7):
    return {
        "id": pid,
        "type": {"text": "Passing Touchdown" if kind == "TD" else "Field Goal Good", "abbreviation": kind},
        "scoringType": {"name": "touchdown" if kind == "TD" else "field-goal", "abbreviation": kind},
        "text": "Travis Kelce 12 Yd pass from Patrick Mahomes (Harrison Butker Kick)",
        "period": {"number": 2}, "clock": {"displayValue": "4:31"},
        "team": {"abbreviation": team, "displayName": "Kansas City Chiefs"},
        "awayScore": away, "homeScore": home,
    }


class Recorder(t.Notifier):
    name = "rec"
    def __init__(self): self.sent = []
    def send(self, title, body): self.sent.append((title, body))


class FakeFeed:
    def __init__(self): self.state, self.plays = "in", []
    def __call__(self, url, params=None):
        return board(self.state) if url == t.SCOREBOARD_URL else {"scoringPlays": self.plays}


class WatcherTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.cfg = t.Config()
        self.cfg.state_file = Path(self.tmp.name) / "s.json"
        self.cfg.team_filter = frozenset()
        self.feed, self.rec = FakeFeed(), Recorder()
        self.addCleanup(self.tmp.cleanup)
        real_post = t.http_post
        self.addCleanup(lambda: setattr(t, "http_post", real_post))

    def watcher(self):
        return t.Watcher(self.cfg, [self.rec], fetch=self.feed)

    def test_existing_tds_skipped_new_ones_alerted_once(self):
        self.feed.plays = [play("1")]
        w = self.watcher(); w.poll()
        self.assertEqual(self.rec.sent, [])              # scored before we were watching
        self.feed.plays.append(play("2", away=7, home=14))
        self.feed.plays.append(play("3", kind="FG", home=17))
        w.poll(); w.poll()
        self.assertEqual(len(self.rec.sent), 1)          # one TD, FG ignored, no dupes
        title, body = self.rec.sent[0]
        self.assertIn("Kansas City Chiefs", title)
        self.assertIn("Q2 4:31 · BUF 7 – KC 14", body)

    def test_state_survives_restart(self):
        self.feed.plays = []
        self.watcher().poll()
        self.feed.plays = [play("9")]
        w2 = self.watcher(); w2.poll()                   # new process, game already primed
        self.assertEqual(len(self.rec.sent), 1)
        self.watcher().poll()
        self.assertEqual(len(self.rec.sent), 1)

    def test_final_poll_catches_walkoff_td(self):
        w = self.watcher(); w.poll()
        self.feed.state, self.feed.plays = "post", [play("ot", home=30)]
        w.poll()
        self.assertEqual(len(self.rec.sent), 1)
        self.feed.plays.append(play("x"))
        w.poll()                                         # game no longer tracked
        self.assertEqual(len(self.rec.sent), 1)

    def test_team_filter(self):
        self.cfg.team_filter = frozenset({"BUF"})
        w = self.watcher(); w.poll()
        self.feed.plays = [play("1", team="KC")]
        w.poll()
        self.assertEqual(self.rec.sent, [])

    def test_quarter_labels(self):
        self.assertEqual([t.quarter_label(i) for i in (1, 4, 5, 6)], ["Q1", "Q4", "OT", "2OT"])

    def test_ntfy_title_header_is_latin1(self):
        seen = {}
        t.http_post = lambda url, data, headers, timeout=10: seen.update(headers) or 200
        t.NtfyNotifier("topic", "https://ntfy.sh").send("🏈 TOUCHDOWN Chiefs!", "x")
        seen["Title"].encode("latin-1")
        self.assertEqual(seen["Title"], "TOUCHDOWN Chiefs!")


if __name__ == "__main__":
    unittest.main()
