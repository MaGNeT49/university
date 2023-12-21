import PySimpleGUI as sg
from Office_Tweaks.office_tweaks.main import *


def get_all_files_formats(path: str):
    """
    :param path:
    :return:
    """

    return get_files_formats(path, [".pdf", ".docx", ".png", ".jpg", ".gif"])


def count_format_files(data: list, format_files: str) -> int:
    """

    :param data:
    :param format_files:
    :return:
    """
    count = 0

    for i in data:
        if i.endswith(format_files):
            count += 1

    return count


def update_list_directory():
    window['-LISTBOX-'].Update(get_all_files_formats(get_current_catalog()))


# def delete_window():
#     sg.theme("DarkAmber")
#
#     layout = [
#         [sg.Input()],
#         [sg.Button("Удалить все файлы начинающиеся на определенную подстроку", key="delFilesStartSpecificSubstring")],
#         [sg.Button("Удалить все файлы заканчивающиеся на определенную подстроку", key="delFilesEndSpecificSubstring")],
#         [sg.Button("Удалить все файлы содержащие определенную подстроку", key="delFilesSpecificSubstring")],
#         [sg.Button("Удалить все файлы по расширению", key="delFilesExtension")],
#         [sg.Button("Назад")]
#     ]
#
#     return sg.Window('Окно удаления файлов', layout, finalize=True)


def main_window():
    sg.theme("DarkAmber")

    left_col = [
        [sg.Text(f'Текущая дериктория: {get_current_catalog()}', key="TEXT_DIRECTORY")],
        [sg.Button('Сменить рабочий каталог', key="switchDirectory")],
        [sg.Button('Преобразовать PDF в Docx', key="pdfToDocx", disabled=True)],
        [sg.Button('Преобразовать Docx в PDF', key="docxToPdf", disabled=True)],
        [sg.Button('Произвести сжатие изображения', key="compressor", disabled=True), sg.Slider(range=(30, 100), default_value=65, orientation="h", key="rangeCompressor")],
        [sg.Button('Удалить группу файлов', key="deletes", disabled=True)],
        [sg.Button('Выход')]
    ]

    right_col = [
        [sg.Text("")],
        [sg.Listbox([], size=(20, 10), key='-LISTBOX-', select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED,
                    enable_events=True)],
    ]
    layout = [
        sg.vtop([sg.Column(left_col, element_justification='l'), sg.Col(right_col, element_justification='c')])
    ]

    return sg.Window('Office Tweaks', layout, finalize=True)


window1, window2 = main_window(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event in (sg.WIN_CLOSED, 'Выход'):
        break

    if event == "switchDirectory":
        direct = sg.popup_get_folder('Выберите папку', title='Диалог выбора папки', default_path=get_current_catalog())
        changing_directory(direct)
        window["TEXT_DIRECTORY"].update(f'Текущая дериктория: {get_current_catalog()}')
        update_list_directory()

    data = values.get("-LISTBOX-")

    if data is None:
        continue
    if len(data) == 0:
        window["deletes"].update(disabled=True)
        window["pdfToDocx"].update(disabled=True)
        window["docxToPdf"].update(disabled=True)
        window["compressor"].update(disabled=True)
    else:
        window["deletes"].update(disabled=False)

        if event == "deletes":
            sg.Popup("Удалены файлы: " + ",".join(delete_all_files(data)))
            update_list_directory()

        if count_format_files(data, ".pdf") == len(data):
            window["pdfToDocx"].update(disabled=False)
            if event == "pdfToDocx":
                for i in data:
                    convert_pdf_to_docx(i)

                update_list_directory()
        else:
            window["pdfToDocx"].update(disabled=True)

        if count_format_files(data, ".docx") == len(data):
            window["docxToPdf"].update(disabled=False)
            if event == "docxToPdf":
                for i in data:
                    convert_docx_to_pdf(i)

                update_list_directory()
        else:
            window["docxToPdf"].update(disabled=True)

        if count_format_files(data, ".png") + count_format_files(data, ".jpg") + count_format_files(data, ".gif") == len(data):
            window["compressor"].update(disabled=False)
            if event == "compressor":
                for i in data:
                    compression(i, int(values.get('rangeCompressor')))
        else:
            window["compressor"].update(disabled=True)

window.close()
