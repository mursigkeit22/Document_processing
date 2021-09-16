from openpyxl import load_workbook
import re

workbook = load_workbook(filename="./documents_excel/Glossary_sheet_full.xlsx")

workbook.active = 0
work_sheet = workbook.active

# Abbreviations like - (LCCA)
for cell in work_sheet["A"]:
    try:
        if "(" in cell.value:

            pattern = "- \([A-Z]{2,}\)"
            search_result = re.search(pattern, cell.value)
            if search_result:
                found_sequence = search_result.group(0)
                only_letters = re.search("[A-Z]{2,}", found_sequence).group(0)
                cell.value = re.sub(re.escape(found_sequence), "| " + only_letters, cell.value)
    except:
        print(cell, cell.row, cell.value)
        exit()


def check_A(value):
    if "/" in value or "=" in value or "[" in value or "]" in value:
        # print("FOUND", value)
        return False
    return True


for cell in work_sheet["A"]:
    try:
        if check_A(cell.value):
            if cell.value.endswith(")") and "(" in cell.value:
                # print("cell.value:", cell.value)
                # Достаем текст в скобках,
                text_in_paretheses = cell.value[cell.value.rfind("(") + 1:cell.value.rfind(")")]
                # записываем его во временную переменную,
                # вырезаем его из ячейки,
                cleaned_text = cell.value.replace("(" + text_in_paretheses + ")", "")
                # print("cleaned_text:", cleaned_text)
                # сохраняем ячейку,
                cell.value = cleaned_text
                # записываем вырезанный текст в новую ячейку

                work_sheet[f"C{cell.row}"] = text_in_paretheses
    except:
        print(cell, cell.row, cell.value)
        exit()


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
    try:
        # print(cell.row)
        if check(cell.value):
            if cell.value.strip().endswith(")") and "(" in cell.value:
                # Достаем текст в скобках,
                text_in_paretheses = cell.value[cell.value.rfind("(") + 1:cell.value.rfind(")")]
                # записываем его во временную переменную,
                # вырезаем его из ячейки,
                cleaned_text = cell.value.replace("(" + text_in_paretheses + ")", "")
                # print("cleaned_text:", cleaned_text)
                # сохраняем ячейку,
                cell.value = cleaned_text
                # записываем вырезанный текст в новую ячейку

                work_sheet[f"D{cell.row}"] = text_in_paretheses
    except TypeError:
        pass
    except Exception as ex:
        print(ex)
        print(cell, cell.row, cell.value)
        exit()

workbook.save("./new_docs/done.xlsx")
