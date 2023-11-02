def processing(file: str):
    f = open(file, mode='r', encoding='utf8')
    count_num = int(f.readline())

    numbers = []
    for i in range(0, count_num):
        numbers.append(int(f.readline()))

    return numbers
