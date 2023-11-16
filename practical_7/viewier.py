from practical_7.main import *


def show():
    f = open("books.csv", "r", encoding="utf-8")
    reader_ = csv.reader(f, delimiter='|')
    book_ = get_books("python")
    print(book_)
    print(get_totals(book_))
    print(get_totals(list(reader_)))
    f.close()


if __name__ == "__main__":
    show()
#