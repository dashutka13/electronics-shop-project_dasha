from src.item import Item
from src.phone import Phone


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


def test_name_setter():
    """
    Запускает тестирование
    сеттера метода name
    """
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'

    assert item.name == 'Смартфон'

    item.name = 'СуперСмартфон'

    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv():
    """
    Запускает тестирование
    класс-метода instantiate_from_csv
    """
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    """
    Запускает тестирование
    статического метода string_to_number
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    """
    Запускает тестирование
    магического метода __repr__
    """
    item1 = Item("Телевизор", 110000, 5)
    assert repr(item1) == "Item('Телевизор', 110000, 5)"


def test_str():
    """
        Запускает тестирование
        магического метода __str__
        """
    item1 = Item("Кондиционер", 160000, 15)
    assert str(item1) == 'Кондиционер'


def test_item():
    phone1 = Phone("iPhone 100", 195_000_000, 12, 7)

    assert str(phone1) == 'iPhone 100'
    assert repr(phone1) == "Phone('iPhone 100', 195000000, 12, 7)"
    assert phone1.number_of_sim == 7

    item1 = Item("Плеер", 5000, 5)

    assert item1 + phone1 == 17
    assert phone1 + phone1 == 24
