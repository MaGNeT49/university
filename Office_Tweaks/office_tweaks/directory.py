import os


def get_current_catalog():
    """
    :return: текущий каталог
    """
    return os.getcwd()


def change_catalog(path: str):
    """
    Функция меняет каталог
    :param path: Путь директории
    """
    if is_valid_path(path):
        os.chdir(path)


def is_valid_path(path: str) -> bool:
    """
    Проверка на вернуй путь к директории
    :param path: Путь к директории
    :return: True - если путь правильный, False - если путь неправильный
    """
    check = True
    if not os.path.exists(path):
        print(f"Пути \"{path}\" не существует!")
        return False
    if not os.path.isdir(path):
        print(f"Путь \"{path}\" не является директорией!")
        return False
    else:
        return True
