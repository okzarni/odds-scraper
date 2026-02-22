import json
from datetime import datetime
from playwright.sync_api import sync_playwright

URL = "https://www.oddsportal.com/soccer/"

def scrape():
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL, timeout=60000)

        page.wait_for_timeout(5000)

        matches = page.query_selector_all("table tbody tr")

        for row in matches[:5]:
            cols = row.query_selector_all("td")
            if len(cols) > 3:
                match_name = cols[1].inner_text()
                home = cols[-3].inner_text()
                draw = cols[-2].inner_text()
                away = cols[-1].inner_text()

                data.append({
                    "match": match_name,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "bookmakers": [
                        {
                            "name": "OddsPortal Avg",
                            "home": home,
                            "draw": draw,
                            "away": away
                        }
                    ]
                })

        browser.close()

    with open("odds.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    scrape()
