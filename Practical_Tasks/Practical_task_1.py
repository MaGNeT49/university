from random import randint


def MontiHallProblem():
    countChooseYourDoor = 0
    countChooseOtherDoor = 0
    userNumDoor = 0
    doorNotEmpty = 0
    numberOfAttempts = 1000

    for _ in range(0, numberOfAttempts):
        userNumDoor = randint(1, 3)
        doorNotEmpty = randint(1, 3)

        if userNumDoor == doorNotEmpty:
            countChooseYourDoor += 1
        else:
            countChooseOtherDoor += 1

    return countChooseYourDoor * 100 / numberOfAttempts, countChooseOtherDoor * 100 / numberOfAttempts


def main():
    print(MontiHallProblem())


if __name__ == "__main__":
    main()
