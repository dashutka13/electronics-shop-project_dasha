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

    item2.pay_rate = 0.75

    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 8500

    assert item2.price == 15000



