import requests
from bs4 import BeautifulSoup
from random import choice

HEADERS_LIST = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16 Safari/605.1.15"}
]

def scrape_mobile_legends():
    url = "https://example.com/mobile-legends-recharge"
    r = requests.get(url, headers=choice(HEADERS_LIST))
    soup = BeautifulSoup(r.text, "lxml")
    
    # Example scraping logic — adapt based on site HTML
    items = []
    for product in soup.select(".product"):
        name = product.select_one(".title").text.strip()
        price = product.select_one(".price").text.strip()
        items.append({"item": name, "price": price, "source": "Example Store"})
    return items

def scrape_free_fire():
    url = "https://example.com/free-fire-recharge"
    r = requests.get(url, headers=choice(HEADERS_LIST))
    soup = BeautifulSoup(r.text, "lxml")

    items = []
    for product in soup.select(".product"):
        name = product.select_one(".title").text.strip()
        price = product.select_one(".price").text.strip()
        items.append({"item": name, "price": price, "source": "Example Store"})
    return items

def scrape_pubg():
    url = "https://example.com/pubg-uc-recharge"
    r = requests.get(url, headers=choice(HEADERS_LIST))
    soup = BeautifulSoup(r.text, "lxml")

    items = []
    for product in soup.select(".product"):
        name = product.select_one(".title").text.strip()
        price = product.select_one(".price").text.strip()
        items.append({"item": name, "price": price, "source": "Example Store"})
    return items
