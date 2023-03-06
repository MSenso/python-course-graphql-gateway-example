from services.places import PlacesService

from tests.unit.utils import get_places_from_file, assert_place


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
