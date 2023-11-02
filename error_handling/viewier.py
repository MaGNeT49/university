from error_handling.file_processing import *


def show():
    print("Введите \"выход\" чтобы завершить программу.")
    while True:
        file = input("Введите имя файла: ")

        if file == "выход":
            break

        print(processing(file))


if __name__ == "__main__":
    show()
