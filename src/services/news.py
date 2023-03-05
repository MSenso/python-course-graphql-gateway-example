import json
import logging
import os
from models.news import NewsModel

logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)


class NewsService:
    """
    Сервис для работы с данными о новостях.
    """

    @staticmethod
    def create_news(news: dict):
        return NewsModel(
            id=news.get("id"),
            title=news.get("title"),
            author=news.get("author"),
            description=news.get("description"),
            content=news.get("content"),
            source=news.get("source").get("name"),
            url=news.get("url"),
            published_at=news.get("publishedAt"),
        )

    def get_news(self) -> dict[str, list[NewsModel]]:
        """
        Получение списка новостей.
        :return:
        """
        base_directory = "fixtures/news/"
        json_news = [file for file in os.listdir(base_directory) if file.endswith('.json')]
        result = {}
        for file in json_news:
            alpha2code = file.split(".")[0]
            file_path = base_directory + file
            with open(file_path, encoding="utf-8") as json_file:
                if data := json.load(json_file):
                    result[alpha2code] = [
                        self.create_news(news)
                        for news in data.get("articles", [])
                    ]
        return result
