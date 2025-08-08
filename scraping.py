import requests
from bs4 import BeautifulSoup
from random import choice
import re

HEADERS_LIST = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/118 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/16 Safari/605.1.15"}
]

def parse_price(text):
    # Strip non-numeric characters, support decimals
    match = re.search(r'[\d,.]+', text.replace(',', ''))
    return float(match.group()) if match else None

def scrape_mobile_legends_codashop():
    """
    Scrape Mobile Legends Diamonds from Codashop.
    """
    url = "https://www.codashop.com/en-us/mobile-legends"  # Official Codashop ML page 0
    res = requests.get(url, headers=choice(HEADERS_LIST), timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")
    results = []
    for item in soup.select(".denomination__item"):
        denom = item.select_one(".denomination__label")
        price = item.select_one(".denomination__price")
        if denom and price:
            results.append({
                "game": "Mobile Legends",
                "currency_type": "Diamonds",
                "amount": denom.get_text(strip=True),
                "price": parse_price(price.get_text(strip=True)),
                "vendor": "Codashop"
            })
    return results

def scrape_free_fire_seagm():
    """
    Scrape Free Fire Diamonds from SEAGM.
    """
    url = "https://www.seagm.com/en-us/free-fire-diamonds-my-top-up"  # SEAGM FF Diamonds page (MY/SG/PH/KH) 1
    res = requests.get(url, headers=choice(HEADERS_LIST), timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")
    results = []
    for item in soup.select("div[itemprop='offers']"):
        name = item.select_one("div.title") or item.select_one(".product-title") 
        price = item.select_one("div.price") or item.select_one(".product-price")
        if name and price:
            results.append({
                "game": "Free Fire",
                "currency_type": "Diamonds",
                "amount": name.get_text(strip=True),
                "price": parse_price(price.get_text(strip=True)),
                "vendor": "SEAGM"
            })
    return results

def scrape_pubg_uc_seagm():
    """
    Scrape PUBG UC packages from SEAGM.
    """
    url = "https://www.seagm.com/en-us/pubg-mobile-uc-top-up-global"  # SEAGM PUBG UC page 2
    res = requests.get(url, headers=choice(HEADERS_LIST), timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")
    results = []
    for item in soup.select("div[itemprop='offers']"):
        name = item.select_one("div.title") or item.select_one("div.product-title")
        price = item.select_one("div.price") or item.select_one(".product-price")
        if name and price:
            results.append({
                "game": "PUBG Mobile",
                "currency_type": "UC",
                "amount": name.get_text(strip=True),
                "price": parse_price(price.get_text(strip=True)),
                "vendor": "SEAGM"
            })
    return results

def scrape_mobile_legends_lapakgaming():
    """
    Scrape Mobile Legends Diamonds from LapakGaming.
    """
    url = "https://www.lapakgaming.com/en-ph/mobile-legends"  # ML Diamonds on LapakGaming 3
    res = requests.get(url, headers=choice(HEADERS_LIST), timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")
    results = []
    for item in soup.select(".product-item") or soup.select("div.product-list .product"):
        name = item.select_one(".product-title") or item.select_one(".title")
        price = item.select_one(".product-price") or item.select_one(".price")
        if name and price:
            results.append({
                "game": "Mobile Legends",
                "currency_type": "Diamonds",
                "amount": name.get_text(strip=True),
                "price": parse_price(price.get_text(strip=True)),
                "vendor": "LapakGaming"
            })
    return results

if __name__ == "__main__":
    print("Codashop ML:", scrape_mobile_legends_codashop())
    print("SEAGM FF:", scrape_free_fire_seagm())
    print("SEAGM PUBG:", scrape_pubg_uc_seagm())
    print("LapakGaming ML:", scrape_mobile_legends_lapakgaming())
