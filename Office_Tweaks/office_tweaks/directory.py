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


def get_files_format(path: str, file_format: str):
    """
    Получение файлов по формату в директории
    :param path: директория поиска файлов
    :param file_format: файловый формат
    :return: список файлов
    """
    files = []

    for file in os.listdir(path):
        if file.endswith(file_format):
            files.append(file)

    return files


def get_files_formats(path: str, file_formats: list):
    """
        Получение файлов по несколько форматов в директории
        :param path: директория поиска файлов
        :param file_formats: файловые форматы
        :return: список файлов
        """
    files = []
    for i in file_formats:
        for file in get_files_format(path, i):
            files.append(file)

    return files
