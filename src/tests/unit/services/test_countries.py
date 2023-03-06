import json

from services.countries import CountriesService


def get_countries_from_file():
    with open("fixtures/countries.json", encoding="utf-8") as file:
        countries = json.load(file)
    return countries


def test_read_countries():
    """
    Тестирование получения стран
    """
    countries = CountriesService().get_countries()
    file_countries = get_countries_from_file()
    assert len(countries) == len(file_countries)
    for i, (actual, expected) in enumerate(zip(countries, file_countries)):
        assert actual.name == expected["name"]
        assert actual.alpha2code == expected["alpha2code"]
        assert actual.alpha3code == expected["alpha3code"]
        assert actual.capital == expected["capital"]
        assert actual.region == expected["region"]
        assert actual.subregion == expected["subregion"]
        assert actual.population == expected["population"]
        assert actual.latitude == expected["latitude"]
        assert actual.longitude == expected["longitude"]
        assert actual.demonym == expected["demonym"]
        assert actual.area == expected["area"]
        assert actual.numeric_code == expected["numeric_code"]
        assert actual.flag == expected["flag"]
        assert actual.currencies == expected["currencies"]
        assert actual.languages == expected["languages"]
