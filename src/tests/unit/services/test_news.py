from services.news import NewsService

from tests.unit.utils import get_countries_news_from_file, assert_news


def test_read_news():
    """
    Тестирование получения новостей
    """
    news = NewsService().get_news()
    assert len(news) == 3
    assert news.keys() == {"ru", "ie", "rs"}
    file_news = get_countries_news_from_file()
    for name in news.keys():
        expected_news = file_news[name]
        actual_news = news[name]
        assert len(actual_news) == len(expected_news)
        for i, (actual, expected) in enumerate(zip(actual_news, expected_news)):
            assert_news(actual, expected)
