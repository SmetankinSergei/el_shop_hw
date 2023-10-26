from src import languages
from src.item import Item


class Keyboard(Item):
    def __init__(self, name, price, amount):
        super().__init__(name, price, amount)
        self.__language = languages.Language.EN

    @property
    def language(self):
        """Геттер для языка"""
        return self.__language

    def change_lang(self):
        """Смена языка"""
        if self.__language == languages.Language.EN:
            self.__language = languages.Language.RU
        else:
            self.__language = languages.Language.EN
