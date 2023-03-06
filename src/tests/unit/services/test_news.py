import json
from datetime import datetime

from services.news import NewsService


def get_news_from_file():
    names = ["ie", "rs", "ru"]
    news = {}
    for name in names:
        with open("fixtures/news/" + name + ".json", encoding="utf-8") as file:
            news[name] = json.load(file)["articles"]
    return news


def test_read_news():
    """
    Тестирование получения новостей
    """
    news = NewsService().get_news()
    assert len(news) == 3
    assert news.keys() == {"ru", "ie", "rs"}
    file_news = get_news_from_file()
    for name in news.keys():
        expected_news = file_news[name]
        actual_news = news[name]
        assert len(actual_news) == len(expected_news)
        for i, (actual, expected) in enumerate(zip(actual_news, expected_news)):
            assert actual.author == expected["author"]
            assert actual.source == expected["source"]["name"]
            assert actual.title == expected["title"]
            assert actual.description is None
            assert actual.url == expected["url"]
            assert datetime.strftime(actual.published_at, "%Y-%m-%dT%H:%M:%SZ") == expected["publishedAt"]
            assert actual.content == expected["content"]
