"""
Для файла _8
- чистим от пустых строк по столбцам А  Б C
- находим аббревиатуры в круглых скобках в конце и в начале предложения по столбцам А  Б C - заменяем на палку + аббр
- оставшиеся скобки в конце переносим в нотес по столбцам А  Б C - получаем текст оттуда и конкатенируем

"""

from openpyxl import load_workbook
from helper_functions import *

import re

workbook = load_workbook(filename="./excel_docs/part_7.xlsx")
work_sheet = workbook["Лист1"]
delete_raw_with_empty_cell(work_sheet, 1)
delete_raw_with_empty_cell(work_sheet, 2)
delete_raw_with_empty_cell(work_sheet, 3)


change_cell_abbr_parentheses(work_sheet, "A")
change_cell_abbr_parentheses(work_sheet, "B")
change_cell_abbr_parentheses(work_sheet, "C")


move_comments_to_notes_safe(work_sheet, "A", "D")
move_comments_to_notes_safe(work_sheet, "B", "D")
move_comments_to_notes_safe(work_sheet, "C", "E")

workbook.save("./ready_excel_docs/done_part_7.xlsx")
