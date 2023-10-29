import csv

from src import check_state
from src.constants import ITEMS_CVS_PATH, ITEMS_CVS_BROKEN_PATH_TEST
from src.my_exceptions import InstantiateCSVError

state = check_state.CheckState.NORMAL


def get_all_data():
    """Получение всех данных из файла"""
    paths = {'NORMAL': ITEMS_CVS_PATH, 'BROKEN_FILE': ITEMS_CVS_BROKEN_PATH_TEST, 'FILE_NOT_EXIST': ' '}
    try:
        with open(paths[state.name], encoding='UTF-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader if check_row(row)]
    except FileNotFoundError:
        print("Отсутствует файл items.csv")


def check_row(row):
    """Проверяет наличие значений у всех ключей (конкретной модели повреждений не задано, я решил, что
    для примера подойдёт отсутствие значения)"""
    for value in row.values():
        if not value:
            raise InstantiateCSVError('Файл items.csv поврежден')
    return True
