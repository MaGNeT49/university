from Office_Tweaks.office_tweaks.directory import *
from Office_Tweaks.office_tweaks.converter import *
from Office_Tweaks.office_tweaks.compressor import *


def changing_directory(path: str):
    """
    Функция для меню, которая изменяет директорию
    :param path: Путь директории
    """
    change_catalog(path)


def converter_file(path: str, file_format: str):
    """
    Функция конвертирует либо из формата PDF в Docx, либо Docx в PDF
    :param path: Путь к файлу
    :param file_format: формат файла из которого конвертируется
    """
    files = get_files_format(path, file_format)

    count = 1
    if len(files) == 0:
        if file_format == ".pdf":
            print("0 файлов PDF в данной директории.")
        elif file_format == ".docx":
            print("0 файлов Docx в данной директории.")
        print()
        return

    print(f"Список файлов с расширением {file_format} в данном каталоге:\n")

    for file in files:
        print(f"{count}. {file}")
        count += 1
    try:
        num = int(input("Введите номер файла для преобразования "
                        "(чтобы преобразовать все файлы "
                        "из данного каталога введите 0): "))

        if 0 <= num <= len(files):
            if num == 0:
                if file_format == ".pdf":
                    all_convert_pdf_to_docx(files)
                elif file_format == ".docx":
                    all_convert_docx_to_pdf(files)
            else:
                if file_format == ".pdf":
                    convert_pdf_to_docx(files[num - 1])
                elif file_format == ".docx":
                    convert_docx_to_pdf(files[num - 1])
        else:
            print("Такого числа нет в списке!")
    except ValueError:
        print("Введено не число!")
    print()


def image_compression(path: str):
    """
    Функция в меню, которая делает сжатие изображения
    :param path: Путь к файлам
    """
    files = get_files_formats(path, [".jpeg", ".gif", ".png", ".jpg"])
    count = 1

    if len(files) == 0:
        print("0 файлов изображения в данной директории.\n")
        return

    print("Список файлов с расширением (\'.jpeg\', \'.gif\', \'.png\', \'.jpg\') в данном каталоге: \n")

    for file in files:
        print(f"{count}. {file}")
        count += 1

    try:
        num = int(input("Введите номер файла для преобразования "
                        "(чтобы преобразовать все файлы "
                        "из данного каталога введите 0): "))

        if 0 <= num <= len(files):
            quality = int(input("Введите параметр сжатия (от 0 до 100): "))
            if 0 <= quality <= 100:
                if num == 0:
                    for file in files:
                        compression(file, quality)
                else:
                    compression(files[num - 1], quality)
            else:
                print("Число не входит в диапозон от 0 до 100!")
        else:
            print("Такого числа нет в списке!")
    except ValueError:
        print("Введено не число!")
    print()


def delete_files(path: str):
    """
    Функция в меню, которая даёт на выбор 4 действия для удаления файла(ов)
    :param path: Путь к файлам
    """
    print("Выберите действие:\n\n1. Удалить все файлы начинающиеся на определенную подстроку"
          "\n2. Удалить все файлы заканчивающиеся на определенную подстроку"
          "\n3. Удалить все файлы содержащие определенную подстроку"
          "\n4. Удалить все файлы по расширению")
    num = input("Введите номер действия: ")

    match num:
        case "1":
            delete_files_start(path, input("Введите подстроку: "))
        case "2":
            delete_files_end(path, input("Введите подстроку: "))
        case "3":
            delete_files_inside(path, input("Введите подстроку: "))
        case "4":
            delete_files_formats(path, input("Введите подстроку: "))
            print(path)
        case _:
            print("Нет такого действия!")
