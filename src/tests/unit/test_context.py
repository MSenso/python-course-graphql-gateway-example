from context import get_context, register_dataloaders
from dataloaders import CountryLoader, NewsLoader


def test_register_dataloaders():
    """
    Тестирование корректного контента в dataloaders
    """
    dataloaders = register_dataloaders()
    assert isinstance(dataloaders, dict)
    assert len(dataloaders) == 2
    assert list(dataloaders.keys()) == ["countries", "news"]
    assert isinstance(dataloaders["countries"], CountryLoader)
    assert isinstance(dataloaders["news"], NewsLoader)


def test_get_context():
    """
    Тестирование корректности контекста
    """
    context = get_context()
    assert len(context) == 1
    assert context.keys() == {"dataloaders"}
    assert isinstance(context["dataloaders"], dict)
