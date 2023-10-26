from src.keyboard import Keyboard


def test_language():
    kb = Keyboard('Dark Project KD87A', 9600, 2)
    assert str(kb.language) == 'EN'


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 2)
    kb.change_lang()
    assert str(kb.language) == 'RU'
