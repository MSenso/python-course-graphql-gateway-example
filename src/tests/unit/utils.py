import json
from datetime import datetime


def get_country_from_file():
    with open("fixtures/countries.json", encoding="utf-8") as file:
        return json.load(file)[0]


def get_countries_from_file():
    with open("fixtures/countries.json", encoding="utf-8") as file:
        countries = json.load(file)
    return countries


def get_countries_news_from_file():
    names = ["ie", "rs", "ru"]
    news = {}
    for name in names:
        with open("fixtures/news/" + name + ".json", encoding="utf-8") as file:
            news[name] = json.load(file)["articles"]
    return news


def get_country_news_from_file():
    with open("fixtures/news/ru.json", encoding="utf-8") as file:
        return json.load(file)["articles"]


def get_places_from_file():
    with open("fixtures/places.json", encoding="utf-8") as file:
        places = json.load(file)["data"]
    return places


def assert_news(actual, expected):
    assert actual.author == expected['author']
    assert actual.source == expected['source']['name']
    assert actual.title == expected['title']
    assert actual.description == expected['description']
    assert actual.url == expected['url']
    assert datetime.strftime(actual.published_at, "%Y-%m-%dT%H:%M:%SZ") == expected["publishedAt"]
    assert actual.content == expected['content']


def assert_country(actual, expected):
    assert actual.name == expected['name']
    assert actual.alpha2code == expected['alpha2code']
    assert actual.alpha3code == expected['alpha3code']
    assert actual.capital == expected['capital']
    assert actual.region == expected['region']
    assert actual.subregion == expected['subregion']
    assert actual.population == expected['population']
    assert actual.latitude == expected['latitude']
    assert actual.longitude == expected['longitude']
    assert actual.demonym == expected['demonym']
    assert actual.area == expected['area']
    assert actual.numeric_code == expected['numeric_code']
    assert actual.flag == expected['flag']
    assert actual.currencies == expected['currencies']
    assert actual.languages == expected['languages']


def assert_place(actual, expected):
    assert actual.id == expected["id"]
    assert actual.city == expected["city"]
    assert actual.country == expected["country"]
    assert actual.latitude == expected["latitude"]
    assert actual.longitude == expected["longitude"]
    assert actual.locality == expected["locality"]
    assert actual.description == expected["description"]
    assert datetime.strftime(actual.created_at, "%Y-%m-%dT%H:%M:%S.%f") == expected["created_at"]
