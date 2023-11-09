from datetime import datetime

file = open("schedule.txt", mode="r", encoding="utf8")

lst = [x.replace('\n', '') for x in file.readlines()]
lst_raise = []

for i in lst:
    new_lst = i.split()
    if 'Рейс' == new_lst[0] and new_lst[1].isdigit() and \
        (("прибыл" == new_lst[2] and "из" == new_lst[3]) or \
        ("отправился" == new_lst[2]  and "в" == new_lst[3])) and \
        new_lst[4].istitle() and new_lst[5] == 'в' and datetime.strptime(new_lst[6], "%H:%M:%S"):
        lst_raise.append(f'[{new_lst[6]}] - Поезд № {new_lst[1]} {new_lst[3]} {new_lst[4]}')
print(lst_raise)

file.close()

file = open("raise.txt", mode="w", encoding="utf8")

for i in lst_raise:
    file.write(f'{i}\n')
#