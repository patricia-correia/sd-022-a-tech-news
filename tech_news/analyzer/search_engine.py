from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "$i"}})
    return [(news["title"], news["url"]) for news in search]


# Requisito 8
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        time = search_news({"timestamp": date})
        return [(news["title"], news["url"]) for news in time]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    search = search_news({"category": {"$regex": category, "$options": "$i"}})
    return [(news["title"], news["url"]) for news in search]
