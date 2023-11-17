import re


def main():
    file = open(r"D:\GitHub\university_python\practical_6\schedule.txt", mode="r", encoding="utf8")
    lst = file.read().splitlines()
    lst_raise = []
    pattern = r"^Рейс\s\d+\s(отправился\sв|прибыл\sиз)\s\w+\sв\s(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"

    for i in lst:
        row = i.split()
        match = re.search(pattern, i)

        if match:
            lst_raise.append(f'[{row[6]}] - Поезд № {row[1]} {row[3]} {row[4]}')

    file.close()

    file = open("raise.txt", mode="w", encoding="utf8")

    for i in lst_raise:
        file.write(f'{i}\n')


if __name__ == "__main__":
    main()
