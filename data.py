import random
from datetime import datetime, timedelta

def generate_events():
    now = datetime.now()

    events = [
        # Football / Soccer
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
        # Basketball
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
        # Tennis
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
        # American Football
        {
            "id": "a1", "sport": "🏈 NFL", "league": "NFL",
            "home": "Kansas City Chiefs", "away": "San Francisco 49ers",
            "time": "01:20", "date": "Tomorrow",
            "status": "upcoming",
            "odds": {"home": 1.80, "draw": None, "away": 2.05},
        },
        # Horse Racing
        {
            "id": "h1", "sport": "🏇 Horse Racing", "league": "HKJC",
            "home": "Race 5 — Happy Valley", "away": "",
            "time": (now + timedelta(minutes=30)).strftime("%H:%M"),
            "date": "Today",
            "status": "upcoming",
            "odds": {"Win": 3.20, "Place": 1.40, "Each Way": 2.10},
        },
    ]
    return events


SPORTS = ["All", "⚽ Football", "🏀 Basketball", "🎾 Tennis", "🏈 NFL", "🏇 Horse Racing"]
