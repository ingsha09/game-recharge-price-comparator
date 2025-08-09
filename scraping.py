import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_mobile_legends_codashop():
    url = "https://www.codashop.com/api/product/MOBILE_LEGENDS"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.codashop.com/en-us/mobile-legends",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest"
    }
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code != 200:
            print(f"Codashop returned status {res.status_code}")
            return []
        data = res.json()
        results = []
        for item in data.get("data", {}).get("items", []):
            amount = item.get("name", "")
            price = item.get("price", {}).get("amount", 0)
            results.append({
                "game": "Mobile Legends",
                "currency_type": "Diamonds",
                "amount": amount,
                "price": price,
                "vendor": "Codashop"
            })
        return results
    except Exception as e:
        print(f"Error scraping Codashop ML: {e}")
        return []

def scrape_free_fire_seagm():
    """
    Fetch Free Fire diamonds from SEAGM API.
    """
    url = "https://www.seagm.com/api/v2/product/detail?game_id=10&product_id=ff-diamonds"
    # Note: SEAGM doesn't provide a public free API, so instead we scrape their HTML and parse JSON inside it.
    # This is a workaround based on their current frontend. It can break anytime.

    url_html = "https://www.seagm.com/en-us/free-fire-diamonds-my-top-up"
    try:
        r = requests.get(url_html, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return []
        # SEAGM loads product info via JS. We'll try to parse the embedded JSON:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text, "html.parser")
        script = soup.find("script", text=lambda t: t and "window.__INITIAL_STATE__" in t)
        if not script:
            return []
        import json, re
        m = re.search(r"window\.__INITIAL_STATE__\s*=\s*({.*?});", script.string, re.DOTALL)
        if not m:
            return []
        state_json = json.loads(m.group(1))
        # Traverse the state JSON to get product list
        items = []
        products = state_json.get("product", {}).get("productList", [])
        for p in products:
            name = p.get("name", "")
            price = p.get("price", {}).get("price", 0)
            items.append({
                "game": "Free Fire",
                "currency_type": "Diamonds",
                "amount": name,
                "price": price,
                "vendor": "SEAGM"
            })
        return items
    except Exception as e:
        print(f"Error scraping SEAGM Free Fire: {e}")
        return []

def scrape_pubg_uc_seagm():
    """
    Fetch PUBG UC from SEAGM by scraping their HTML + embedded JSON.
    """
    url_html = "https://www.seagm.com/en-us/pubg-mobile-uc-top-up-global"
    try:
        r = requests.get(url_html, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return []
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text, "html.parser")
        script = soup.find("script", text=lambda t: t and "window.__INITIAL_STATE__" in t)
        if not script:
            return []
        import json, re
        m = re.search(r"window\.__INITIAL_STATE__\s*=\s*({.*?});", script.string, re.DOTALL)
        if not m:
            return []
        state_json = json.loads(m.group(1))
        items = []
        products = state_json.get("product", {}).get("productList", [])
        for p in products:
            name = p.get("name", "")
            price = p.get("price", {}).get("price", 0)
            items.append({
                "game": "PUBG Mobile",
                "currency_type": "UC",
                "amount": name,
                "price": price,
                "vendor": "SEAGM"
            })
        return items
    except Exception as e:
        print(f"Error scraping SEAGM PUBG: {e}")
        return []
