from django.shortcuts import render
from .services import get_gaming_news


def news_list(request):
    news = get_gaming_news()

    return render(request, "news/list.html", {
        "news": news
    })