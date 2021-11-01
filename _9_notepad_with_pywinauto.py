from contextlib import redirect_stdout
from time import sleep

from pywinauto import Application, ElementNotFoundError, MatchError
from pywinauto.application import ProcessNotFoundError

"""
Перед запуском скрипта:
- раскладку переключить на англ
- язык интерфейса нотпада переключить на англ
- переименовать путь к файлу, чтобы там не было пробелов, скобок и т.п.
- узнать, как обращаться к кнопкам app.Dialog.print_control_identifiers()
"""
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
app.window().menu_select("File -> Open")

app.Dialog['Имя файла:Edit'].type_keys("C:\mein\some_things\тексты\\NewMicrosoftWordDocument2\word\styles.xml").type_keys("{ENTER}")
# app.Dialog['ОткрытьButton4'].click()
    # .type_keys(
    # "{ENTER}")
