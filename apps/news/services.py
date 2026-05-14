import requests
from django.conf import settings


def get_gaming_news():

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=gaming OR videogames OR steam"
        f"&language=en"
        f"&sortBy=publishedAt"
        f"&pageSize=10"
        f"&apiKey={settings.NEWS_API_KEY}"
    )

    response = requests.get(url)

    print(response.json())

    data = response.json()

    return data.get("articles", [])