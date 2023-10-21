from random import randint


def main():
    words = []

    with open("input.txt", mode="r", encoding="utf8") as f:
        words = f.read().splitlines()

    file_record = 0

    with open("record.txt", mode="r", encoding="utf8") as f:
        file_record = int(str(f.read()))

    record = 0
    word = words[randint(0, len(words) - 1)]
    health = 3
    word_hide = []

    for i in range(0, len(word)):
        word_hide.append("\u25A0")

    isplay = True

    while isplay:
        if "".join(word_hide) != word and health > 0:
            word_hide_str = " ".join(word_hide)
            print(f"{word_hide_str} | \u2665x{health}")
            letter = input("Назовите букву или слово целиком: ")

        if letter == word or "".join(word_hide) == word:
            record += 1
            print(" ".join(word.upper()))
            print("Вы выиграли! Приз в студию!")
            print(f"Рекорд: {max(record, file_record)}")

            if input("Вы хотите продолжить (да/нет)? ") == "да":
                health = 3
                word = words[randint(0, len(words) - 1)]

                word_hide.clear()
                for i in range(0, len(word)):
                    word_hide.append("\u25A0")
            else:
                break
        elif letter in word_hide:
            print("Такая буква уже есть.")
        elif letter in word:
            for i in range(0, len(word)):
                if word[i] == letter:
                    word_hide[i] = letter.upper()
        elif health == 0:
            print(f"Рекорд: {max(record, file_record)}")
            if input("Вы хотите продолжить? (да/нет)") == "да":
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

    with open("record.txt", mode="w", encoding="utf8") as file:
        file.write(str(max(record, file_record)))


if __name__ == "__main__":
    main()
