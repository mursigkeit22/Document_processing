from time import sleep

from pywinauto import Application, MatchError, ElementNotFoundError
from pywinauto.application import ProcessNotFoundError


app = Application(backend="uia").start(r"C:\Program Files (x86)\Notepad++\notepad++.exe")
app.window().draw_outline()

app.window().menu_select("File -> Open")
app.Dialog['Имя файла:Edit'].type_keys("C:\mein\some_things\тексты\\NewMicrosoftWordDocument2\word\styles.xml").type_keys("{ENTER}")

app.window().menu_select("File -> Open")
app.Dialog['Имя файла:Edit'].type_keys("C:\mein\some_things\тексты\\NewMicrosoftWordDocument2\word\\settings.xml").type_keys("{ENTER}")
sub = app.window().child_window(title_re="settings.xml", )
sub.right_click_input()
app.Menu["Move to New Instance"].click_input()

sleep(1)

second_window = app[r'C:\\mein\\some_things\\тексты\\NewMicrosoftWordDocument2\\word\\settings.xml - Notepad++']
second_window.set_focus()
print(second_window)
second_window.menu_select("File -> Open")

