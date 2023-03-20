import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake  use-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    sel = Selector(text=html_content)
    cards = []
    for article in sel.css('.cs-overlay-link'):
        link = article.css('a::attr(href)').get()
        if link:
            cards.append(link)
    return cards


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
