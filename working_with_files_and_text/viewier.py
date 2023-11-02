from working_with_files_and_text.read_file import *
from working_with_files_and_text.save_file import *


def show():
    words = read_file("data.txt")
    save_file('count.txt', words)


if __name__ == "__main__":
    show()
