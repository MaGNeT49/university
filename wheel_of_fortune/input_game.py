def get_words():
    with open("input.txt", mode="r", encoding="utf8") as f:
        words = f.read().splitlines()
    return words


def get_record():
    with open("record.txt", mode="r", encoding="utf8") as f:
        file_record = int(str(f.read()))
    return file_record


def save_record(record: int):
    with open("record.txt", mode="w", encoding="utf8") as file:
        file.write(str(record))
