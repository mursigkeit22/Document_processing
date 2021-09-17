"""
Для файла _8
- чистим от пустых строк по столбцу А и столбцу Б
- находим аббревиатуры в круглых скобках в конце и в начале предложения - заменяем на палку + аббр
- оставшиеся скобки в конце переносим в нотес

"""

from openpyxl import load_workbook
from helper_functions import *

import re

workbook = load_workbook(filename="./excel_docs/part_2.xlsx")
work_sheet = workbook["Лист1"]
delete_raw_with_empty_cell(work_sheet, 1)
delete_raw_with_empty_cell(work_sheet, 2)

for cell in work_sheet["A"]:
    cell.value = cell.value.strip()
    abbr_begin = find_abbr_in_parentheses_begin(cell.value)
    if abbr_begin:
        cell.value = re.sub(re.escape(abbr_begin), abbr_begin[1:-1] + " | ", cell.value)
    abbr_end = find_abbr_in_parentheses_end(cell.value)
    if abbr_end:
        cell.value = re.sub(re.escape(abbr_end), " | " + abbr_end[1:-1], cell.value)

for cell in work_sheet["B"]:
    cell.value = cell.value.strip()
    abbr_begin = find_abbr_in_parentheses_begin(cell.value)
    if abbr_begin:
        cell.value = re.sub(re.escape(abbr_begin), abbr_begin[1:-1] + " | ", cell.value)
    abbr_end = find_abbr_in_parentheses_end(cell.value)
    if abbr_end:
        cell.value = re.sub(re.escape(abbr_end), " | " + abbr_end[1:-1], cell.value)


move_comments_to_notes(work_sheet, "A", "C", )
move_comments_to_notes(work_sheet, "B", "D", )


workbook.save("./ready_excel_docs/done_part_2.xlsx")
