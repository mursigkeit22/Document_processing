"""
- чистим от пустых строк по столбцу А
- находим первую англ букву
- если не находим англ букву, или индекс первой англ буквы равен 0 - пропускаем
- переносим в столбец Б
- итерируемся по столбцу Б и удаляем пустые строки

"""

from openpyxl import load_workbook
from helper_functions import *

import re


workbook = load_workbook(filename="./excel_docs/КТК_first_list_separate.xlsx")
work_sheet = workbook["Лист1"]
delete_raw_with_empty_cell(work_sheet, 1)

for cell in work_sheet["A"]:
    try:

        found = re.search("[A-Za-z]", cell.value)
        if found:
            first_index = found.span()[0]
            if first_index != 0:
                english_text = cell.value[first_index:]
                cleaned_text = cell.value.replace(english_text, "")
                # сохраняем ячейку
                cell.value = cleaned_text
                # записываем вырезанный текст в новую ячейку
                work_sheet[f"B{cell.row}"] = english_text
    except TypeError:
        print(cell)

delete_raw_with_empty_cell(work_sheet, 2)
workbook.save("./ready_excel_docs/done_КТК_first_list_separate.xlsx")