import requests
import os
from datetime import date
from .models import Contact
from django.conf import settings


def get_news():
    url = f"https://newsapi.org/v2/top-headlines?category=business&apiKey={os.getenv('NEWS_API_KEY')}"
    response = requests.get(url)
    return response.json().get("articles", [])


def upcoming_birthdays(user, days=7):
    today = date.today()
    result = []

    for c in Contact.objects.filter(user=user, birthday__isnull=False):
        bday = c.birthday.replace(year=today.year)

        if bday < today:
            bday = bday.replace(year=today.year + 1)

        if 0 <= (bday - today).days <= days:
            result.append(c)

    return result



def get_gaming_news():
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=gaming"
        f"&apiKey={settings.NEWS_API_KEY}"
    )

    response = requests.get(url)

    print(response.json())

    data = response.json()

    return data.get("articles", [])