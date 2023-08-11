import csv


class InstantiateCSVError(Exception):
    """Класс исключения в случае повреждения файла."""
    def __init__(self, *args, **kwargs):
        self.message = 'InstantiateCSVError: Файл item.csv поврежден'


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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Нельзя сложить Phone или Item с экземплярами не Phone или Item классов')
        return self.quantity + other.quantity

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

        try:
            with open(items, 'r', encoding="windows-1251") as file:
                items_csv = csv.DictReader(file)
                for row in items_csv:
                    Item(row['name'], int(float(row['price'])), int(float(row['quantity'])))

        except FileNotFoundError:
            print("Отсутствует файл item.csv")

        except InstantiateCSVError as e:
            print(e.message)

    @staticmethod
    def string_to_number(string):
        """
        статический метод, возвращающий число из числа-строки
        """
        return int(float(string))
