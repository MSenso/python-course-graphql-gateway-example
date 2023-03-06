import pytest

from dataloaders import NewsLoader

from tests.unit.utils import get_country_news_from_file, get_countries_news_from_file, assert_news


@pytest.fixture
def loader():
    return NewsLoader()


def test_load_one_article(loader):
    actual_news = loader.load("RU").get()
    expected_news = get_country_news_from_file()
    assert len(actual_news) == len(expected_news)
    for i, (actual, expected) in enumerate(zip(actual_news, expected_news)):
        assert_news(actual, expected)


def test_load_many_news(loader):
    actual_news = loader.load_many(["IE", "RS", "RU"]).get()
    expected_news = get_countries_news_from_file()
    assert len(actual_news) == len(expected_news.keys())
    for i, (actual, expected) in enumerate(zip(actual_news, list(expected_news.values()))):
        for j, (actual_item, expected_item) in enumerate(zip(actual, expected)):
            assert_news(actual_item, expected_item)
