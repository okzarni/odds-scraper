import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.oddsportal.com/matches/soccer/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

matches = []

for row in soup.select(".table-main tbody tr"):
    try:
        match = row.select_one(".name").text.strip()
        odds = [o.text for o in row.select(".odds-nowrp")]
        
        matches.append({
            "match": match,
            "odds": odds
        })
    except:
        continue

with open("odds.json", "w") as f:
    json.dump(matches, f, indent=2)

print("Odds data saved.")
