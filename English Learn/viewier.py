from main import *


def show():
    words = get_words()
    words = normalized_words(words)
    words = sorted_words(words)
    translate_words(words)


if __name__ == "__main__":
    show()
