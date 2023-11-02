from os import path


def read_file(file: str):
    if not path.exists(file):
        print("Файл не существует")
        return 0

    lst = []
    with open(file, mode="r", encoding="utf8") as f:
        for i in f.read().split():
            lst.append(''.join(filter(str.isalnum, i.lower())))

    if '' in lst:
        lst.remove('')

    return list(set(lst))
