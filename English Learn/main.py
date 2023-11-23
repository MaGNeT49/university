import pymorphy3
from translate import Translator

data = []
with open("data.txt", "r", encoding="utf8") as file:
    for i in file.readlines():
        row = i.replace('\n', '').replace(',', '').replace(')', '').replace('?', '')
        for j in row.split():
            data.append(j.lower())

morph = pymorphy3.MorphAnalyzer()
data = [morph.parse(i)[0].normal_form for i in data]
dictionary = {}

for i in data:
    if i not in dictionary:
        dictionary[i] = 1
    elif i in dictionary:
        dictionary[i] += 1

list_d = list(sorted(dictionary.items()))
list_d.sort(reverse=True, key=lambda i: i[1])

translator = Translator(from_lang="ru", to_lang="en")

with open("translation.txt", "w", encoding="utf8") as file:
    for i in range(len(list_d)):
        translation = translator.translate(list_d[i][0])
        file.write(f"{list_d[i][0]}|{translation}|{list_d[i][1]}\n")
        print(f"Переведено {i + 1} слов")
