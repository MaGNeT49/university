import PySimpleGUI as sg
from Office_Tweaks.office_tweaks.main import *


def pdf_to_docx_window():
    sg.theme('DarkAmber')
    data = get_files_format(get_current_catalog(), "pdf")

    layout1 = [
        [sg.Listbox(values=[row for row in data], size=(30, 6), key='-LISTBOX-')],
        [sg.Button('Назад')]
    ]

    return sg.Window('Окно 1', layout1, finalize=True)


def main_window():
    layout = [
        [sg.Text(f'Текущая дериктория: {get_current_catalog()}', key="TEXT")],
        [sg.Button('Сменить рабочий каталог', key="0")],
        [sg.Button('Преобразовать PDF в Docx', key="1")],
        [sg.Button('Преобразовать Docx в PDF', key="2")],
        [sg.Button('Произвести сжатие изображения', key="3")],
        [sg.Button('Удалить группу файлов', key="4")],
        [sg.Button('Выход')]
    ]

    return sg.Window('Office Tweaks', layout, finalize=True)


window1, window2 = main_window(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == window1 and event in (sg.WIN_CLOSED, 'Выход'):
        break

    if event == "0":
        direct = sg.popup_get_folder('Выберите папку', title='Диалог выбора папки', default_path=get_current_catalog())
        changing_directory(direct)
        window["TEXT"].update(f'Текущая дериктория: {get_current_catalog()}')

    if window == window1 and event == '1':
        window2 = pdf_to_docx_window()
        window1.hide()

    if window == window2 and event == 'Назад':
        window2.close()  # Закрытие второго окна
        window2 = None  # Сброс ссылки на второе окно
        window1.un_hide()

window.close()
