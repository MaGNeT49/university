def processing(file: str):
    try:
        f = open(file, mode='r', encoding='utf8')

        count_num = int(f.readline())

        numbers = []
        for i in range(0, count_num):
            numbers.append(int(f.readline()))

        f.close()

    except FileNotFoundError:
        return "Файл не найден"
    except OSError:
        return "Ошибка операционной системы"
    except:
        return "Произошла непредвиденная ошибка!"
    else:
        return numbers
