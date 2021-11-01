from contextlib import redirect_stdout

from pywinauto import Application

app = Application(backend="uia").start(r"C:\Program Files (x86)\Notepad++\notepad++.exe")
app.window().draw_outline()
app.window().menu_select("File -> Open")
with open("notepad_identifiers/temp.txt", "w", encoding="utf8") as f:
    with redirect_stdout(f):
        app.Dialog.print_control_identifiers()
