import csv


def get_books(word: str):
    file = open("books.csv", mode="r", encoding="utf-8")
    reader = csv.reader(file, delimiter='|')
    answer = []

    for row in reader:
        if word.lower() in row[1].lower():
            answer.append(row)

    file.close()

    return answer


def get_totals(data: list, add=100):
    answer = []
    for row in data:
        if not(str(row[3]).isdigit() or str(row[3]).isdigit()):
            continue
        if (int(row[3]) * float(row[4])) < 500:
            answer.append((row[0], int(row[3]) * float(row[4]) + add))
        else:
            answer.append((row[0], int(row[3]) * float(row[4])))

    return answer


if __name__ == "__main__":
    file = open("books.csv", "r", encoding="utf-8")
    reader = csv.reader(file, delimiter='|')
    book = get_books("python")
    print(book)
    print(get_totals(book))
    print(get_totals(list(reader)))
    file.close()
