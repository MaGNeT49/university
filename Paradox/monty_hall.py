from random import randint


def monty_hall(numberOfIterations: int = 10000):
    '''
    :param numberOfIterations: Количество итераций
    :return: Вероятность изменения при выборе другой двери
    '''
    countChooseOtherDoor = 0

    for _ in range(0, numberOfIterations):
        userNumDoor = randint(1, 3)
        doorNotEmpty = randint(1, 3)

        if userNumDoor != doorNotEmpty:
            countChooseOtherDoor += 1

    return countChooseOtherDoor * 100 / numberOfIterations


def main():
    print(monty_hall())


if __name__ == "__main__":
    main()
