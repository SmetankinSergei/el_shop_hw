import pytest

from src import DAO
from src.my_exceptions import InstantiateCSVError


def test_check_row():
    row = {'name': 'pencil', 'price': '100', 'quantity': '1'}
    broken_row = {'name': 'pencil', 'price': '100', 'quantity': None}
    assert DAO.check_row(row)
    with pytest.raises(InstantiateCSVError):
        DAO.check_row(broken_row)
