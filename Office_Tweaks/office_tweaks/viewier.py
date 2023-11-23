from Office_Tweaks.office_tweaks.directory import *
from Office_Tweaks.office_tweaks.converter import *
from Office_Tweaks.office_tweaks.compressor import *


def changing_directory():
    """
    Функция изменения директории
    """
    path = input("Укажите корректный путь к рабочему каталогу: ")

    change_catalog(path)
    print()


def converter_file(file_format: str):
    """
    Функция конвертирует либо из формата PDF в Docx, либо Docx в PDF
    :param file_format: формат файла из которого конвертируется
    """
    files = get_files_format(get_current_catalog(), file_format)

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

    num = input("Введите номер файла для преобразования "
                "(чтобы преобразовать все файлы из данного каталога введите 0): ")

    if num.isdigit():
        if 0 <= int(num) <= len(files):
            num = int(num)
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
    else:
        print("Введено не число!")
    print()


def image_compression():
    """
    Сжатие изображения
    """
    files = get_files_formats(get_current_catalog(), [".jpeg", ".gif", ".png", ".jpg"])
    count = 1

    if len(files) == 0:
        print("0 файлов изображения в данной директории.\n")
        return

    print("Список файлов с расширением (\'.jpeg\', \'.gif\', \'.png\', \'.jpg\') в данном каталоге: \n")

    for file in files:
        print(f"{count}. {file}")
        count += 1

    num = input("Введите номер файла для преобразования "
                "(чтобы преобразовать все файлы из данного каталога введите 0): ")
    quality = input("Введите параметр сжатия (от 0 до 100): ")

    if num.isdigit() and quality.isdigit():
        if 0 <= int(num) <= len(files) and 0 <= int(quality) <= 100:
            num = int(num)
            quality = int(quality)

            if num == 0:
                compression(files, quality)
            else:
                compression(files[num - 1], quality)
        else:
            print("Такого числа нет в списке!")
    else:
        print("Введено не число!")
    print()


def show():
    """
    Отображение меню
    """
    while True:
        print(f"Текущий каталог: {get_current_catalog()}\n\nВыберите действие: \n\n0. Сменить рабочий каталог\n"
              f"1. Преобразовать PDF в Docx\n2. Преобразовать Docx в PDF\n"
              f"3. Произвести сжатие изображения\n4. Удалить группу файлов\n5. Выход\n")
        user_input = input("Ваш выбор: ")
        print()

        if user_input.isdigit():
            match int(user_input):
                case 0:
                    changing_directory()
                case 1:
                    converter_file(".pdf")
                case 2:
                    converter_file(".docx")
                case 3:
                    image_compression()
                case 4:
                    print()
                case 5:
                    break
                case _:
                    print("Введено неправильное значение!")
        else:
            print("Введена не цифра!")


if __name__ == "__main__":
    show()
