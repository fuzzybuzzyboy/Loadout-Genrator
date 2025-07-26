import os
import json
import requests
from bs4 import BeautifulSoup
import time
from functools import wraps

def verifydata(filepath="data.json"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if os.path.exists(filepath):
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # Basic check: if data is empty or missing key, scrape
                if not data or "Starting Brawler" not in data:
                    data = func(*args, **kwargs)
            else:
                data = func(*args, **kwargs)
            return data
        return wrapper
    return decorator

@verifydata()
def scrape_brawlers():
    base_url = "https://brawlstars.fandom.com"
    categories = [
        "Rare_Brawlers", "Super_Rare_Brawlers", "Epic_Brawlers",
        "Mythic_Brawlers", "Legendary_Brawlers", "Ultra_Legendary_Brawlers"
    ]
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    os.makedirs("images", exist_ok=True)

    manual = {
        "Epic": {
            "Bonnie": {
                "Gadgets": ["Sugar Rush", "Crash Test"],
                "Starpowers": ["Black Powder", "Wisdom Tooth"]
            },
            "Mandy": {
                "Gadgets": ["Caramalize", "Cookie Crumbs"],
                "Starpowers": ["In My Sights", "Hard Candy"]
            }
        },
        "Mythic": {
            "Willow": {
                "Gadgets": ["Spellbound", "Dive"],
                "Starpowers": ["Love Is Blind", "Obsession"]
            }
        }
    }

    def extract_items(soup, title):
        items, h2 = [], next((h for h in soup.find_all("h2") if h.get_text(strip=True).lower() == title.lower()), None)
        s = h2.find_next_sibling() if h2 else None
        while s and s.name != "h2":
            if s.name == "h3":
                name = s.get_text(strip=True)
                if name: items.append(name)
                while s and s.name not in ["h3", "h2"]:
                    s = s.find_next_sibling()
            else:
                s = s.find_next_sibling()
        return items

    def download_portrait(soup, name):
        imgs = soup.select('img[data-image-name$="Portrait.png"]')
        url = next((img.get("data-src") or img.get("src") for img in reversed(imgs) if (img.get("data-src") or img.get("src")).startswith("http")), None)
        if url:
            r = session.get(url)
            with open(f"images/{name}.png", "wb") as f:
                f.write(r.content)

    final_data = {"Starting Brawler": {}}

    try:
        res = session.get(f"{base_url}/wiki/Shelly")
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")
        if "Shelly" not in final_data["Starting Brawler"]:
            download_portrait(soup, "Shelly")
            final_data["Starting Brawler"]["Shelly"] = {
                "Gadgets": extract_items(soup, "Gadgets"),
                "Starpowers": extract_items(soup, "Star Powers")
            }
    except:
        pass
    time.sleep(1)

    all_brawlers = {}
    for cat in categories:
        try:
            res = session.get(f"{base_url}/wiki/Category:{cat}")
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")
            catname = cat.replace("_", " ").replace("Brawlers", "").strip()
            all_brawlers[catname] = {a.get_text(strip=True): base_url + a.get("href") for a in soup.select("a.category-page__member-link")}
        except:
            pass
        time.sleep(1)

    for rarity, brawlers in all_brawlers.items():
        final_data.setdefault(rarity, {})
        for name, url in brawlers.items():
            if name in manual.get(rarity, {}) or name in final_data.get(rarity, {}):
                continue
            try:
                res = session.get(url)
                res.raise_for_status()
                soup = BeautifulSoup(res.text, "html.parser")
                download_portrait(soup, name)
                gadgets = extract_items(soup, "Gadgets")
                starpowers = extract_items(soup, "Star Powers")
                final_data[rarity][name] = {"Gadgets": gadgets, "Starpowers": starpowers}
            except:
                pass
            time.sleep(0.5)

    for rarity, brawlers in manual.items():
        final_data.setdefault(rarity, {}).update(brawlers)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
    return final_data


# Usage example:
if __name__ == "__main__":
    data = scrape_brawlers()
    print("Brawler data loaded or scraped successfully.")
