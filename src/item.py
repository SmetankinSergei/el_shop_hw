from src import DAO
from src.constants import NOT_A_NUMBER_MESSAGE


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, amount):
        self.__name = name
        self.price = price
        self.amount = amount
        Item.all.append(self)

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.amount})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.amount + other.amount

    @property
    def name(self):
        """Геттер для названия"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Сеттер для названия"""
        new_name = new_name if len(new_name) <= 10 else new_name[:10]
        self.__name = new_name

    def calculate_total_price(self):
        """Вычисление цены всех товаров"""
        return self.price * self.amount

    def apply_discount(self):
        """Применяет установленную скидку для конкретного товара."""
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализация экземпляров через файл"""
        items_data = DAO.get_all_data()
        if items_data:
            for row in items_data:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(string):
        """Получение числа из строки"""
        try:
            result = float(string)
            return int(result)
        except ValueError:
            print(NOT_A_NUMBER_MESSAGE)
