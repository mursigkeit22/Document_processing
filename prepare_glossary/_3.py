# обработка русской колонки. 1. проверяем на наличие косых линий
from openpyxl import load_workbook
import re

workbook = load_workbook(filename="./documents_excel/rus_test_python.xlsx")
sheet_to_focus = 'Лист1'

# TODO: проверить на наличие косых черт и знаков равно и с ними ничего не делать!
workbook.active = 0
work_sheet = workbook.active


def check(value):
    if "/" in value or "=" in value or "[" in value or "]" in value:
        # print("FOUND", value)
        return False
    if re.search("\([А-Я]{2,}\)", value):
        # print("FOUND2", value)
        return False
    if re.search("[a-zA-Z]", value):
        # print("FOUND3", value)
        return False
    return True


for cell in work_sheet["B"]:
    # print(cell.row)
    if check(cell.value):
        if cell.value.endswith(")") and "(" in cell.value:
            # Достаем текст в скобках,
            text_in_paretheses = cell.value[cell.value.rfind("(") + 1:cell.value.rfind(")")]
            # записываем его во временную переменную,
            # вырезаем его из ячейки,
            cleaned_text = cell.value.replace("(" + text_in_paretheses + ")", "")
            print("cleaned_text:", cleaned_text)
            # сохраняем ячейку,
            cell.value = cleaned_text
            # записываем вырезанный текст в новую ячейку

            work_sheet[f"D{cell.row}"] = text_in_paretheses
workbook.save("./new_docs/_Rustest_python.xlsx")
