import json
from datetime import datetime

from services.places import PlacesService


def get_places_from_file():
    with open("fixtures/places.json", encoding="utf-8") as file:
        places = json.load(file)["data"]
    return places


def assert_place(actual, expected):
    assert actual.id == expected["id"]
    assert actual.city == expected["city"]
    assert actual.country == expected["country"]
    assert actual.latitude == expected["latitude"]
    assert actual.longitude == expected["longitude"]
    assert actual.locality == expected["locality"]
    assert actual.description == expected["description"]
    assert datetime.strftime(actual.created_at, "%Y-%m-%dT%H:%M:%S.%f") == expected["created_at"]


def test_read_places():
    """
    Тестирование получения всех мест
    """
    places = PlacesService().get_places()
    file_places = get_places_from_file()
    assert len(places) == len(file_places)
    for i, (actual, expected) in enumerate(zip(places, file_places)):
        assert_place(actual, expected)


def test_read_place():
    """
    Тестирование получения одного места
    """
    actual = PlacesService().get_place(1)
    expected = get_places_from_file()[0]
    assert_place(actual, expected)
