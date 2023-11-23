from Office_Tweaks.office_tweaks.directory import *
from Office_Tweaks.office_tweaks.converter import *


def show():
    while True:
        print(f"Текущий каталог: {get_current_catalog()}\n\nВыберите действие: \n\n0. Сменить рабочий каталог\n"
              f"1. Преобразовать PDF в Docx\n2. Преобразовать Docx в PDF\n"
              f"3. Произвести сжатие изображения\n4. Удалить группу файлов\n5. Выход\n")
        user_input = input("Ваш выбор: ")
        match user_input:
            case '0':
                path = input("Укажите корректный путь к рабочему каталогу: ")

                change_catalog(path)
                print()
            case '1':
                count = show_files_pdf(get_current_catalog())
                num = input("Введите номер файла для преобразования "
                            "(чтобы преобразовать все файлы из данного каталога введите 0): ")
                if num.isdigit():
                    num = int(num)

                else:
                    print("Введено не число!")
                print()
            case '2':
                print()
            case '3':
                print()
            case '4':
                print()
            case '5':
                break
            case '_':
                print()


if __name__ == "__main__":
    show()
