from practical_7.main import *


def show():

    print("Чтобы выйти введите \"0\".")

    while True:
        input_user = input("Введите название книге: ")
        if input_user == '0':
            break
        data = get_books(input_user)
        print(data)
        print(get_totals(data))


if __name__ == "__main__":
    show()
