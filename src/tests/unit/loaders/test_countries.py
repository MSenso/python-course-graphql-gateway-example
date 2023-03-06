import pytest

from dataloaders import CountryLoader

from tests.unit.utils import get_country_from_file, assert_country, get_countries_from_file


@pytest.fixture
def loader():
    return CountryLoader()


def test_load_one_country(loader):
    actual = loader.load("IE").get()
    expected = get_country_from_file()
    assert_country(actual, expected)


def test_load_many_countries(loader):
    actual_countries = loader.load_many(["IE", "RU", "RS", "US"]).get()
    expected_countries = get_countries_from_file()
    assert len(actual_countries) == len(expected_countries)
    for i, (actual, expected) in enumerate(zip(actual_countries, expected_countries)):
        assert_country(actual, expected)
