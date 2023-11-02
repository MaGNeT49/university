def save_file(file: str, words: list):
    if words == 0:
        return 0

    count = len(words)
    new_words = sorted(words)

    with open(file, mode='w', encoding="utf8") as f:
        f.write(f"Всего уникальных слов: {count}\n{'=' * 22}\n")

        for i in new_words:
            f.write(f'{i}\n')
