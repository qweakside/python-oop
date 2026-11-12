"""Тесты для MushroomsCollector.

Запуск: py -m pytest
"""

from mushrooms import MushroomsCollector


def test_each_basket_has_own_list() -> None:
    first = MushroomsCollector()
    second = MushroomsCollector()

    first.add_mushroom("Лисичка")

    assert first.mushrooms == ["Лисичка"]
    assert second.mushrooms == []


def test_poisonous_mushroom_is_not_added(capsys) -> None:
    basket = MushroomsCollector()

    basket.add_mushroom("Мухомор")

    assert basket.mushrooms == []
    assert "Нельзя добавить ядовитый гриб" in capsys.readouterr().out


def test_safe_mushroom_is_added() -> None:
    basket = MushroomsCollector()

    basket.add_mushroom("Подберёзовик")

    assert basket.mushrooms == ["Подберёзовик"]


def test_str_joins_mushrooms_with_comma() -> None:
    basket = MushroomsCollector()
    basket.add_mushroom("Белый гриб")
    basket.add_mushroom("Лисичка")

    assert str(basket) == "Белый гриб, Лисичка"


def test_empty_basket_is_empty_string() -> None:
    assert str(MushroomsCollector()) == ""
