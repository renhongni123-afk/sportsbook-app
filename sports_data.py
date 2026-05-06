import random
from datetime import datetime, timedelta


def generate_events():
    """Generate a rich set of sports events with realistic odds."""
    now = datetime.now()

    events = [
        # ── Football / Soccer ─────────────────────────────────
        {
            "id": "f1", "sport": "⚽ Football", "league": "Premier League",
            "home": "Manchester City", "away": "Arsenal",
            "time": (now + timedelta(hours=2)).strftime("%H:%M"),
            "date": "Today",
            "status": "upcoming",
            "odds": {"home": 1.85, "draw": 3.60, "away": 4.20},
        },
        {
            "id": "f2", "sport": "⚽ Football", "league": "Premier League",
            "home": "Liverpool", "away": "Chelsea",
            "time": (now + timedelta(hours=5)).strftime("%H:%M"),
            "date": "Today",
            "status": "upcoming",
            "odds": {"home": 2.10, "draw": 3.40, "away": 3.30},
        },
        {
            "id": "f3", "sport": "⚽ Football", "league": "La Liga",
            "home": "Real Madrid", "away": "Barcelona",
            "time": "21:00", "date": "Today",
            "status": "live",
            "score": {"home": 1, "away": 1},
            "minute": 67,
            "odds": {"home": 2.40, "draw": 3.10, "away": 2.90},
        },
        {
            "id": "f4", "sport": "⚽ Football", "league": "Bundesliga",
            "home": "Bayern Munich", "away": "Borussia Dortmund",
            "time": "18:30", "date": "Tomorrow",
            "status": "upcoming",
            "odds": {"home": 1.65, "draw": 4.00, "away": 5.00},
        },
        {
            "id": "f5", "sport": "⚽ Football", "league": "Serie A",
            "home": "Inter Milan", "away": "AC Milan",
            "time": "20:45", "date": "Tomorrow",
            "status": "upcoming",
            "odds": {"home": 2.20, "draw": 3.30, "away": 3.10},
        },
        {
            "id": "f6", "sport": "⚽ Football", "league": "中超联赛",
            "home": "上海海港", "away": "北京国安",
            "time": "19:35", "date": "Today",
            "status": "live",
            "score": {"home": 2, "away": 0},
            "minute": 54,
            "odds": {"home": 1.25, "draw": 5.50, "away": 9.00},
        },
        {
            "id": "f7", "sport": "⚽ Football", "league": "J-League",
            "home": "Vissel Kobe", "away": "Yokohama F. Marinos",
            "time": "14:00", "date": "Tomorrow",
            "status": "upcoming",
            "odds": {"home": 2.50, "draw": 3.20, "away": 2.80},
        },

        # ── Basketball ────────────────────────────────────────
        {
            "id": "b1", "sport": "🏀 Basketball", "league": "NBA",
            "home": "LA Lakers", "away": "Golden State Warriors",
            "time": (now + timedelta(hours=3)).strftime("%H:%M"),
            "date": "Today",
            "status": "live",
            "score": {"home": 87, "away": 92},
            "minute": "Q3 4:22",
            "odds": {"home": 2.05, "away": 1.78},
        },
        {
            "id": "b2", "sport": "🏀 Basketball", "league": "NBA",
            "home": "Boston Celtics", "away": "Miami Heat",
            "time": "02:30", "date": "Tomorrow",
            "status": "upcoming",
            "odds": {"home": 1.72, "away": 2.15},
        },
        {
            "id": "b3", "sport": "🏀 Basketball", "league": "NBA",
            "home": "Denver Nuggets", "away": "Phoenix Suns",
            "time": "04:00", "date": "Tomorrow",
            "status": "upcoming",
            "odds": {"home": 1.90, "away": 1.95},
        },
        {
            "id": "b4", "sport": "🏀 Basketball", "league": "CBA",
            "home": "广东东莞", "away": "辽宁本钢",
            "time": "19:30", "date": "Today",
            "status": "live",
            "score": {"home": 68, "away": 71},
            "minute": "Q3 8:15",
            "odds": {"home": 2.20, "away": 1.70},
        },

        # ── Tennis ────────────────────────────────────────────
        {
            "id": "t1", "sport": "🎾 Tennis", "league": "ATP Masters",
            "home": "Novak Djokovic", "away": "Carlos Alcaraz",
            "time": (now + timedelta(hours=1)).strftime("%H:%M"),
            "date": "Today",
            "status": "upcoming",
            "odds": {"home": 1.95, "away": 1.88},
        },
        {
            "id": "t2", "sport": "🎾 Tennis", "league": "WTA Tour",
            "home": "Iga Swiatek", "away": "Aryna Sabalenka",
            "time": "15:00", "date": "Today",
            "status": "live",
            "score": {"home": "6-4, 3", "away": "2, 5"},
            "minute": "Set 2",
            "odds": {"home": 1.60, "away": 2.35},
        },
        {
            "id": "t3", "sport": "🎾 Tennis", "league": "ATP Masters",
            "home": "Jannik Sinner", "away": "Daniil Medvedev",
            "time": "17:00", "date": "Today",
            "status": "upcoming",
            "odds": {"home": 1.55, "away": 2.45},
        },

        # ── American Football ─────────────────────────────────
        {
            "id": "a1", "sport": "🏈 NFL", "league": "NFL",
            "home": "Kansas City Chiefs", "away": "San Francisco 49ers",
            "time": "01:20", "date": "Tomorrow",
            "status": "upcoming",
            "odds": {"home": 1.80, "draw": None, "away": 2.05},
        },

        # ── Horse Racing ──────────────────────────────────────
        {
            "id": "h1", "sport": "🏇 Horse Racing", "league": "HKJC — Happy Valley",
            "home": "Race 5 — 快活谷", "away": "",
            "time": (now + timedelta(minutes=30)).strftime("%H:%M"),
            "date": "Today",
            "status": "upcoming",
            "odds": {"Win": 3.20, "Place": 1.40, "Each Way": 2.10},
        },
        {
            "id": "h2", "sport": "🏇 Horse Racing", "league": "HKJC — Sha Tin",
            "home": "Race 8 — 沙田", "away": "",
            "time": (now + timedelta(hours=1, minutes=45)).strftime("%H:%M"),
            "date": "Today",
            "status": "upcoming",
            "odds": {"Win": 5.50, "Place": 2.10, "Each Way": 3.60},
        },

        # ── Esports ───────────────────────────────────────────
        {
            "id": "e1", "sport": "🎮 Esports", "league": "League of Legends — LPL",
            "home": "JDG", "away": "T1",
            "time": "20:00", "date": "Today",
            "status": "upcoming",
            "odds": {"home": 1.75, "away": 2.10},
        },
        {
            "id": "e2", "sport": "🎮 Esports", "league": "CS2 Major",
            "home": "FaZe Clan", "away": "Natus Vincere",
            "time": "22:00", "date": "Today",
            "status": "live",
            "score": {"home": 12, "away": 10},
            "minute": "Map 2",
            "odds": {"home": 1.55, "away": 2.40},
        },
    ]
    return events


def fluctuate_odds(events):
    """Simulate real-time odds movement (small random shifts)."""
    for ev in events:
        if ev["status"] == "live":
            for key in ev["odds"]:
                if ev["odds"][key] is not None:
                    shift = random.uniform(-0.15, 0.15)
                    ev["odds"][key] = round(max(1.01, ev["odds"][key] + shift), 2)
    return events


SPORTS = [
    "All",
    "⚽ Football",
    "🏀 Basketball",
    "🎾 Tennis",
    "🏈 NFL",
    "🏇 Horse Racing",
    "🎮 Esports",
]
