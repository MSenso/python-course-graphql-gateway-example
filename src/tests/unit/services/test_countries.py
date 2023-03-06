from services.countries import CountriesService

from tests.unit.utils import get_countries_from_file, assert_country


def test_read_countries():
    """
    Тестирование получения стран
    """
    countries = CountriesService().get_countries()
    file_countries = get_countries_from_file()
    assert len(countries) == len(file_countries)
    for i, (actual, expected) in enumerate(zip(countries, file_countries)):
        assert_country(actual, expected)
