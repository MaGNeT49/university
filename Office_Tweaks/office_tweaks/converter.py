from pdf2docx import Converter
from docx2pdf import convert
from directory import get_files_format


def get_files_pdf(path):
    """
    Функция возращает список файлов PDF
    :param path: Путь файла
    :return: Файлы PDF
    """
    return get_files_format(path, ".pdf")


def get_files_docx(path):
    """
    Функция возращает список файлов PDF
    :param path: Путь файла
    :return: Файлы PDF
    """
    return get_files_format(path, ".docx")


def all_convert_pdf_to_docx(files: list):
    """

    :param files:
    :return:
    """
    for pdf_file in files:
        convert_pdf_to_docx(pdf_file)


def convert_pdf_to_docx(pdf_file: str):
    """

    :param pdf_file:
    :return:
    """
    docx_file = str(pdf_file) + ".docx"
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()


def all_convert_docx_to_pdf(files: list):
    """

    :param files:
    :return:
    """
    for pdf_file in files:
        convert_docx_to_pdf(pdf_file)


def convert_docx_to_pdf(docx_file: str):
    """

    :param docx_file:
    :return:
    """
    convert(docx_file, docx_file + ".pdf")
