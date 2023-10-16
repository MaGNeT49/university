from random import randint


def monty_hall(numberOfIterations: int = 100):
    '''
    :param numberOfIterations: Количество итерций
    :return: Вероятность изменения при выборе другой двери
    '''
    countChooseOtherDoor = 0

    for _ in range(0, numberOfIterations):
        userNumDoor = randint(1, 3)
        doorNotEmpty = randint(1, 3)

        if userNumDoor != doorNotEmpty:
            countChooseOtherDoor += 1

    return countChooseOtherDoor * 100 / numberOfIterations


def birthday(numberOfIterations: int = 100, numberOfPeopleInGroup: int = 23):
    '''
    :param numberOfIterations: Количество итерций
    :param numberOfPeopleInGroup: Количество людей в группе
    :return: вероятность совпадений дня рождения хотя бы у двух людей
    '''
    countOfMatches = 0

    for _ in range(0, numberOfIterations):
        groups = []
        for i in range(0, numberOfPeopleInGroup):
            groups.append(randint(1, 366))

        counts = {}
        for person in groups:
            if person in counts:
                countOfMatches += 1
                break
            else:
                counts[person] = 1

    return countOfMatches * 100 / numberOfIterations


def main():
    print(monty_hall())
    print(birthday())


if __name__ == "__main__":
    main()
