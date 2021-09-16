from openpyxl import load_workbook
import re

workbook = load_workbook(filename="./documents_excel/test_python.xlsx")
sheet_to_focus = 'Лист1'

#TODO: проверить на наличие косых черт и знаков равно и с ними ничего не делать!
workbook.active = 0
work_sheet = workbook.active

def check(value):
    if "/" in value or "=" in value or "[" in value or "]" in value:
        # print("FOUND", value)
        return False
    return True


for cell in work_sheet["A"]:
    if check(cell.value):
        if cell.value.endswith(")") and "(" in cell.value:
            # print("cell.value:", cell.value)
            # Достаем текст в скобках,
            text_in_paretheses = cell.value[cell.value.rfind("(") + 1:cell.value.rfind(")")]
            # записываем его во временную переменную,
            # вырезаем его из ячейки,
            cleaned_text = cell.value.replace("("+text_in_paretheses+")", "")
            print("cleaned_text:", cleaned_text)
            # сохраняем ячейку,
            cell.value = cleaned_text
            # записываем вырезанный текст в новую ячейку

            work_sheet[f"C{cell.row}"] = text_in_paretheses
workbook.save("./new_docs/test_python.xlsx")