import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup


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
    try:
        sel = Selector(html_content)
        next_page = sel.css('.next::attr(href)').get()
        return next_page
    except AttributeError:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content)

    return {
        "url": soup.find("link", {"rel": "canonical"})["href"].strip(),
        "title": soup.find("h1", {"class": "entry-title"}).text.strip(),
        "timestamp": soup.find("li", {"class": "meta-date"}).text,
        "writer": soup.find("span", {"class": "author"}).a.text,
        "reading_time": int(
            soup.find("li", {"class": "meta-reading-time"}).text.split()[0]
        ),
        "summary": soup.find(
            "div", {"class": "entry-content"}
        ).p.text.strip(),
        "category": soup.find("span", {"class": "label"}).text,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
