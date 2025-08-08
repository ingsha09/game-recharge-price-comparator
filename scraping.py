import requests
from bs4 import BeautifulSoup
from random import choice
import re

HEADERS_LIST = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
]

def parse_price(text):
    match = re.search(r'[\d,.]+', text.replace(',', ''))
    return float(match.group()) if match else None

def scrape_mobile_legends_codashop():
    url = "https://www.codashop.com/en-us/mobile-legends"
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
    url = "https://www.seagm.com/en-us/free-fire-diamonds-my-top-up"
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
    url = "https://www.seagm.com/en-us/pubg-mobile-uc-top-up-global"
    res = requests.get(url, headers=choice(HEADERS_LIST), timeout=15)
    soup = BeautifulSoup(res.text, "html.parser")
    results = []
    for item in soup.select("div[itemprop='offers']"):
        name = item.select_one("div.title") or item.select_one(".product-title")
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
