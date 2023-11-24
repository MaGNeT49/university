import pymorphy3
from translate import Translator


def get_words() -> list:
    """
    :return: Возвращает список слов
    """
    data = []

    with open("data.txt", "r", encoding="utf8") as file:
        for i in file.readlines():
            row = i.replace('\n', '').replace(',', '').replace(')', '').replace('?', '')
            for j in row.split():
                data.append(j.lower())

    return data


def normalized_words(words: list) -> list:
    """
    :param words: Список слов
    :return: Возвращает нормализванные слова
    """
    morph = pymorphy3.MorphAnalyzer()
    words = [morph.parse(i)[0].normal_form for i in words]

    return words


def sorted_words(words: list):
    """
    Сортировка слов по убыванию
    :param words: Список слов
    :return: Список слов по убыванию
    """
    dictionary = {}

    for i in words:
        if i not in dictionary:
            dictionary[i] = 1
        elif i in dictionary:
            dictionary[i] += 1

    list_d = list(sorted(dictionary.items()))
    list_d.sort(reverse=True, key=lambda i: i[1])

    return list_d


def translate_words(words: list):
    """
    Перевод список слов
    :param words: Список слов
    """
    translator = Translator(from_lang="ru", to_lang="en")

    with open("translation.txt", "w", encoding="utf8") as file:
        file.write("Исходное слово|Перевод|Количество упоминаний\n")
        for i in range(len(words)):
            translation = translator.translate(words[i][0])
            file.write(f"{words[i][0]}|{translation}|{words[i][1]}\n")
            print(f"Переведено слов: {i + 1}")
