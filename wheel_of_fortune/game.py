from random import randint
from input_game import get_words, get_record, save_record


def main():
    words = get_words()
    file_record = get_record()
    record = 0
    word = words[randint(0, len(words) - 1)]
    word_hide = []

    for i in range(0, len(word)):
        word_hide.append("\u25A0")

    playing = True

    while True:
        level = input("Введите уровень сложности:\n1 - Лёгкий.\n2 - Средний.\n3 - Сложный.\n")
        if level == '1':
            default_health = 7
            break
        elif level == '2':
            default_health = 5
            break
        elif level == '3':
            default_health = 3
            break
        else:
            print("Вы ввели неправильное значение!")

    health = default_health
    letter = ""

    while playing:
        if "".join(word_hide) != word.upper() and health > 0:
            word_hide_str = " ".join(word_hide)
            print(f"{word_hide_str} | \u2665x{health}")
            letter = input("Назовите букву или слово целиком: ")

        if letter.upper() == word.upper() or "".join(word_hide) == word.upper():
            record += 1
            words.remove(word)
            print(" ".join(word.upper()))
            print("Вы выиграли! Приз в студию!")
            print(f"Рекорд: {max(record, file_record)}")

            if len(words) == 0:
                print("Все слова угаданы.")
                break

            elif input("Вы хотите продолжить (да/нет)? ") == "да":
                health = default_health

                word = words[randint(0, len(words) - 1)]

                word_hide.clear()
                for i in range(0, len(word)):
                    word_hide.append("\u25A0")
            else:
                break
        elif letter.upper() in word_hide:
            print("Такая буква уже есть.")
        elif letter in word:
            for i in range(0, len(word)):
                if word[i] == letter:
                    word_hide[i] = letter.upper()
        elif health == 0:
            if input("Хотите восстановить жизни? (да/нет)\n") == "да":
                print(f"Рекорд: {max(record, file_record)}")
                health = default_health
            elif input("Вы хотите продолжить? (да/нет)") == "да":
                health = 3
                word = words[randint(0, len(words) - 1)]

                word_hide.clear()
                for i in range(0, len(word)):
                    word_hide.append("\u25A0")
            else:
                break
        else:
            health -= 1
            print("Неправильно. Вы теряете жизнь")

    save_record(max(record, file_record))


if __name__ == "__main__":
    main()
