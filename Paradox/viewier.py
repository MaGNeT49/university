from Paradox.monty_hall import *
from Paradox.birthday import *


def show():
    print(monty_hall(10000), "%")
    print(birthday(1000), "%")


if __name__ == "__main__":
    show()
