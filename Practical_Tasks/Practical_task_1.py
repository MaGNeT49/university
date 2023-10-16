from random import randint


def MontiHallProblem(numberOfAttempts: int = 100):
    '''
    :param numberOfAttempts: Количество попыток обработки парадокса Монти Холла
    :return: Вероятность изменения при выборе другой двери
    '''
    countChooseOtherDoor = 0

    for _ in range(0, numberOfAttempts):
        userNumDoor = randint(1, 3)
        doorNotEmpty = randint(1, 3)

        if userNumDoor != doorNotEmpty:
            countChooseOtherDoor += 1

    return countChooseOtherDoor * 100 / numberOfAttempts


def main():
    print(MontiHallProblem())


if __name__ == "__main__":
    main()

