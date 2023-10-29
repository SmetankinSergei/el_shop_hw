from enum import Enum


class CheckState(Enum):
    NORMAL = 0
    BROKEN_FILE = 1
    FILE_NOT_EXIST = 2
