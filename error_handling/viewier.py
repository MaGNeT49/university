from error_handling.file_processing import *


def show():
    file = input("Введите имя файла: ")

    print(processing(file))


if __name__ == "__main__":
    show()
