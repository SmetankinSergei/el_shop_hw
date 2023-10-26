from src.item import Item
from src.phone import Phone


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25


def test_name():
    item = Item("Смартфон", 10000, 20)
    assert item.name == "Смартфон"
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) > 0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    