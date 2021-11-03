import glob
import os
from time import sleep

from pywinauto import Application, ElementNotFoundError, MatchError
from pywinauto.application import ProcessNotFoundError

"""
Перед запуском скрипта:
- раскладку переключить на англ
- язык интерфейса нотпада переключить на англ
- переименовать путь к файлу, чтобы там не было пробелов, скобок и т.п.
- узнать, как обращаться к кнопкам можно через app.Dialog.print_control_identifiers()
- и всё равно через раз нихера не будет работать
"""


def get_file_list(folder):
    file_list = []
    for filename in glob.iglob(folder + '**/**', recursive=True):
        if os.path.isfile(filename):
            file_list.append(filename)
    return file_list


first = get_file_list(r"C:\mein\some_things\тексты\NewMicrosoftWordDocument")
second = get_file_list(r"C:\mein\some_things\тексты\NewMicrosoftWordDocument2")

try:
    old_app = Application(backend="uia").connect(path=r"C:\Program Files (x86)\Notepad++\notepad++.exe")
    print(old_app.windows())
    sleep(1)
    try:
        old_app.window().Dialog.type_keys("%{F4}")
    except MatchError as e:
        print(e)

    old_app.window().menu_select("File -> Exit")
    old_app.window().DontSave.click()
except (ProcessNotFoundError, ElementNotFoundError) as e:
    print(e)
sleep(1)
app = Application(backend="uia").start(r"C:\Program Files (x86)\Notepad++\notepad++.exe")
sleep(1)
app.window().draw_outline()
app.window().menu_select("File -> Close all")
for el in first:
    app.window().menu_select("File -> Open")

    app.Dialog['Имя файла:Edit'].type_keys(el).type_keys("{ENTER}")

