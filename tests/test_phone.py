from src.phone import Phone


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_sim_amount():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.sim_amount == 2
