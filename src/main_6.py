from src import DAO, check_state
from src.item import Item

if __name__ == '__main__':
    """Для того, чтобы вручную не менять пути для проверки и не делать несколько вызовов, я написал Enum 
    для состояния проверки, и перед каждой проверкой меняю его на нужный. FileNotFoundError ловится и обрабатывается 
    в блоке except. Тк исключение обрабатывается, то ошибки, как тут написано в закомментированной строке, не будет, 
    будет только сообщение. Оно будет в самом верху, белым цветом, тк это штатное поведение, и уже после него начнётся 
    стэктрейс исключения"""
    DAO.state = check_state.CheckState.FILE_NOT_EXIST
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    DAO.state = check_state.CheckState.BROKEN_FILE
    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
