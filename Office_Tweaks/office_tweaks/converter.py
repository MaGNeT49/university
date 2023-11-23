from pdf2docx import parse
import os


def show_files_pdf(path):
    """
    Функция выводит список файлов PDF
    :param path: Путь файла
    :return: Количество файлов PDF
    """
    count = 0
    print("Список файлов с расширением .pdf в данном каталоге:\n")
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            print(f"{count + 1}. {file}")
            count += 1

    return count

