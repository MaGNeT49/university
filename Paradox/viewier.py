from Paradox.monty_hall import *
from Paradox.birthday import *


def show():
    input_monty_hall = input("Введите количество итераций monty hall: ")
    input_birthday_group = input("Введите количество человек в группе: ")
    input_birthday_iteration = input("Введите количество итераций в дне рождения: ")

    if input_monty_hall.isdigit():
        print(f"Monty Hall: {monty_hall(int(input_monty_hall))} %")
    else:
        print(f"Monty Hall: {monty_hall()} %")

    if input_birthday_iteration.isdigit():
        print(f"Birthday: {birthday(numberOfIterations=int(input_birthday_iteration))} %")
    elif input_birthday_group.isdigit():
        print(f"Birthday: {birthday(int(input_birthday_group))} %")
    elif input_birthday_iteration.isdigit() and input_birthday_group.isdigit():
        print(f"Birthday: {birthday(int(input_birthday_group), int(input_birthday_iteration))} %")
    else:
        print(f"Birthday: {birthday()} %")


if __name__ == "__main__":
    show()
