from src.item import Item
from src.mixin import Mixinlang


class Keyboard(Item, Mixinlang):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)




