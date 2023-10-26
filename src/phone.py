from src.item import Item


class Phone(Item):
    def __init__(self, name, price, amount, sim_amount):
        super().__init__(name, price, amount)
        if sim_amount == 0:
            sim_amount = 1
        self.__sim_amount = sim_amount

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.amount}, {self.sim_amount})"

    @property
    def sim_amount(self):
        """Количество сим карт"""
        return self.__sim_amount
