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


def get_files_format(path: str, file_format: str) -> list:
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


def delete_files_formats(path_name: str, file_format: str):
    """
    Удаление файла по формату
    :param path_name: Имя файла
    :param file_format: Формат файла
    """
    files = get_files_format(path_name, file_format)
    if len(files) == 0:
        print("Нету файлов для удаления!")

    for file in files:
        os.remove(file)
        print(f"Файл: \"{file}\" успешно удалён!")


def delete_files_start(path_name: str, file_start: str):
    """
    Удаление файла по начальной строке
    :param path_name: Имя файла
    :param file_start: Начальная подстрока
    """
    files = []

    for file in os.listdir(path_name):
        if file.startswith(file_start):
            files.append(file)

    if len(files) == 0:
        print("Нету файлов для удаления!")

    for file in files:
        os.remove(file)
        print(f"Файл: \"{file}\" успешно удалён!")


def delete_files_end(path_name: str, file_end: str):
    """
    Удаление файла по концу названия файла
    :param path_name: Имя файла
    :param file_end: Конечная подстрока
    """
    files = []

    for file in os.listdir(path_name):
        if file.rsplit('.', maxsplit=1)[0].endswith(file_end):
            files.append(file)

    if len(files) == 0:
        print("Нету файлов для удаления!")

    for file in files:
        os.remove(file)
        print(f"Файл: \"{file}\" успешно удалён!")


def delete_files_inside(path_name: str, file_inside: str):
    """
    Удаление файла если есть подстрока в название файла
    :param path_name: Имя файла
    :param file_inside: Подстрока внутри слова
    """
    files = []

    for file in os.listdir(path_name):
        if file_inside in file.rsplit('.', maxsplit=1)[0]:
            files.append(file)

    if len(files) == 0:
        print("Нету файлов для удаления!")

    for file in files:
        os.remove(file)
        print(f"Файл: \"{file}\" успешно удалён!")
