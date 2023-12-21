from office_tweaks.main import *


def show():
    """
    Отображение меню
    """
    path = get_current_catalog()

    while True:
        print(f"Текущий каталог: {path}\n\nВыберите действие: \n\n0. Сменить рабочий каталог\n"
              f"1. Преобразовать PDF в Docx\n2. Преобразовать Docx в PDF\n"
              f"3. Произвести сжатие изображения\n4. Удалить группу файлов\n5. Выход\n")
        user_input = input("Ваш выбор: ")
        print()

        match user_input:
            case "0":
                path = input("Укажите корректный путь к рабочему каталогу: ")

                changing_directory(path)
                print()
            case "1":
                converter_file(path, ".pdf")
                print()
            case "2":
                converter_file(path, ".docx")
                print()
            case "3":
                image_compression(path)
                print()
            case "4":
                delete_files(path)
                print()
            case "5":
                break
            case _:
                print("Введено неправильное значение!")


if __name__ == "__main__":
    show()
