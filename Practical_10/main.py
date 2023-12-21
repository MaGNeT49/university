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
    is_pdf_docx = True if len(get_files_pdf(get_current_catalog())) == 0 else False

    left_col = [
        [sg.Text(f'Текущая дериктория: {get_current_catalog()}', key="TEXT")],
        [sg.Button('Сменить рабочий каталог', key="0")],
        [sg.Button('Преобразовать PDF в Docx', key="1", disabled=is_pdf_docx)],
        [sg.Button('Преобразовать Docx в PDF', key="2")],
        [sg.Button('Произвести сжатие изображения', key="3")],
        [sg.Button('Удалить группу файлов', key="4")],
        [sg.Button('Выход')]
    ]

    right_col = [
        [sg.Text("")],
        [sg.Listbox([], size=(20, 10), key='-LISTBOX-', select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED, enable_events=True)],
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

    if event == "0":
        file_list = get_files_format(get_current_catalog(), "pdf")
        direct = sg.popup_get_folder('Выберите папку', title='Диалог выбора папки', default_path=get_current_catalog())
        changing_directory(direct)
        window["TEXT"].update(f'Текущая дериктория: {get_current_catalog()}')
        window['-LISTBOX-'].Update(os.listdir(get_current_catalog()))

    if window == window1 and event == '1':
        window2 = pdf_to_docx_window()
        window1.hide()

    if window == window2 and event == 'Назад':
        window2.close()  # Закрытие второго окна
        window2 = None  # Сброс ссылки на второе окно
        window1.un_hide()

window.close()
