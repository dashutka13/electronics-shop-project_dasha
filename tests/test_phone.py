import pytest

from src.item import Item
from src.phone import Phone


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    assert str(phone1) == 'iPhone 14'


def test_repr():
    phone1 = Phone("iPhone 18", 170_000, 12, 9)

    assert repr(phone1) == "Phone('iPhone 18', 170000, 12, 9)"


def test_number_of_sim():
    phone1 = Phone("iPhone 18", 170_000, 12, 9)

    assert phone1.number_of_sim == 9


def test_add():
    phone1 = Phone("iPhone 18", 170_000, 12, 9)
    item1 = Item("Смартфон", 10000, 20)

    assert item1 + phone1 == 32

    assert phone1 + phone1 == 24
