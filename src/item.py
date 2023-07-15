import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_str):
        """
        Метод проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае, обрезать строку (оставить первые 10 символов).
        """
        if len(name_str) > 10:
            self.__name = name_str[:10]
        else:
            self.__name = name_str

    @classmethod
    def instantiate_from_csv(cls, items="../src/items.csv"):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all = []

        with open(items, 'r', encoding="windows-1251") as file:
            items_csv = csv.DictReader(file)
            for row in items_csv:
                Item(row['name'], int(float(row['price'])), int(float(row['quantity'])))

    @staticmethod
    def string_to_number(string):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(string))



