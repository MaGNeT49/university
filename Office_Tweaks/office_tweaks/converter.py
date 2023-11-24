from pdf2docx import Converter
from docx2pdf import convert
from Office_Tweaks.office_tweaks.directory import get_files_format


def get_files_pdf(path: str) -> list:
    """
    Функция возращает список файлов PDF
    :param path: Путь файла
    :return: Файлы PDF
    """
    return get_files_format(path, ".pdf")


def get_files_docx(path: str) -> list:
    """
    Функция возращает список файлов PDF
    :param path: Путь файла
    :return: Файлы PDF
    """
    return get_files_format(path, ".docx")


def all_convert_pdf_to_docx(files: list):
    """
    Конвертация всех PDF файлов в Docx
    :param files: Список файлов
    """
    for pdf_file in files:
        convert_pdf_to_docx(pdf_file)


def convert_pdf_to_docx(pdf_file: str):
    """
    Конвертация PDF файла в Docx
    :param pdf_file: PDF файл
    """
    docx_file = str(pdf_file) + ".docx"
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()


def all_convert_docx_to_pdf(files: list):
    """
    Конвертация всех Docx файлов в PDF
    :param files: Список файлов
    """
    for pdf_file in files:
        convert_docx_to_pdf(pdf_file)


def convert_docx_to_pdf(docx_file: str):
    """
    Конвертация Docx файла в PDF
    :param docx_file: Docx файл
    """
    convert(docx_file, docx_file + ".pdf")
