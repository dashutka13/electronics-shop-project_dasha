import pytest
from src.item import Item


def test_calculate_total_price():
    """
    Запускает тестирование
    метода calculate_total_price
    """
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000

    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    """
    Запускает тестирование
    метода apply_discount
    """
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.apply_discount() == 8500

    assert item2.apply_discount() == 17000


