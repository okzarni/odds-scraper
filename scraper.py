import json
from datetime import datetime

data = [
    {
        "match": "Arsenal vs Chelsea",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "bookmakers": [
            {"name": "Bet365", "home": 1.80, "draw": 3.50, "away": 4.20},
            {"name": "1xBet", "home": 1.85, "draw": 3.40, "away": 4.10}
        ]
    }
]

with open("odds.json", "w") as f:
    json.dump(data, f, indent=4)

print("Test odds written successfully.")
