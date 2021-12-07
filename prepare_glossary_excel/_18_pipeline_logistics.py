# итерируемся по колонке А, проверяем текст слева направо.
# Доходим до первой точки с запятой. Вырезаем текст вместо с точкой с запятой
# и вставляем его в колонку В [1:]
# То же самое делаем с колонками D и E

from openpyxl import load_workbook

from helper_functions import *

workbook = load_workbook(filename="./excel_docs/logistics.xlsx")

sheet_glossary = workbook["Logistics"]
delete_raw_with_empty_cell(sheet_glossary, 1)
delete_raw_with_empty_cell(sheet_glossary, 4)


def move(column_from, column_to):
    for cell in sheet_glossary[column_from]:
        index = cell.value.rfind(";")
        if index > -1:
            print(cell, cell.value, index)
            text_to_move = cell.value[index:]
            print(text_to_move)
            new_value = cell.value[:index]
            cell.value = new_value
            print(new_value)
            sheet_glossary[f"{column_to}{cell.row}"] = text_to_move[1:].strip()


move("A", "B")
move("D", "E")


workbook.save("./ready_excel_docs/logistics_done.xlsx")
