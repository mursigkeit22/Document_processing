import re


def delete_raw_with_empty_cell(work_sheet, column_num):  # TODO: check if it works with first raw!
    """ Column numbers are 1, 2, 3 ... Not 0, 1, 2, 3!!!"""
    for rowNum in range(work_sheet.max_row, 0, -1):
        # print(work_sheet.cell(row=rowNum, column=2))
        if work_sheet.cell(row=rowNum, column=column_num).value is None:
            # print("hop")
            work_sheet.delete_rows(rowNum)


def check_english_column(value):
    if "/" in value or "=" in value or "[" in value or "]" in value:
        return False
    return True


def check_russian_column(value):
    if "/" in value or "=" in value or "[" in value or "]" in value:
        # print("FOUND", value)
        return False
    # проверяем наличие аббревиатур в скобках
    if re.search("\([А-Я]{2,}\)", value):
        # print("FOUND2", value)
        return False
    # проверяем наличие английского текста
    if re.search("[a-zA-Z]", value):
        # print("FOUND3", value)
        return False
    return True


def move_comments_to_notes_with_check(sheet, column_letter_from, column_letter_to, check_function):
    for cell in sheet[column_letter_from]:
        if check_function(cell.value):
            if cell.value.strip().endswith(")") and "(" in cell.value:
                # Достаем текст в скобках, записываем его во временную переменную,
                text_in_paretheses = cell.value[cell.value.rfind("(") + 1:cell.value.rfind(")")]
                # вырезаем его из ячейки,
                cleaned_text = cell.value.replace("(" + text_in_paretheses + ")", "")
                # print("cleaned_text:", cleaned_text)
                # сохраняем ячейку,
                cell.value = cleaned_text
                # записываем вырезанный текст в новую ячейку
                sheet[f"{column_letter_to}{cell.row}"] = text_in_paretheses


def move_comments_to_notes(sheet, column_letter_from, column_letter_to):
    for cell in sheet[column_letter_from]:
        try:
            if cell.value.strip().endswith(")") and "(" in cell.value:
                # Достаем текст в скобках, записываем его во временную переменную,
                text_in_paretheses = cell.value[cell.value.rfind("(") + 1:cell.value.rfind(")")]
                # вырезаем его из ячейки,
                cleaned_text = cell.value.replace("(" + text_in_paretheses + ")", "")
                # print("cleaned_text:", cleaned_text)
                # сохраняем ячейку,
                cell.value = cleaned_text
                # записываем вырезанный текст в новую ячейку
                sheet[f"{column_letter_to}{cell.row}"] = text_in_paretheses
        except:
            print(cell, cell.value)


def move_comments_to_notes_safe(sheet, column_letter_from, column_letter_to, ):
    for cell in sheet[column_letter_from]:

        if cell.value.strip().endswith(")") and "(" in cell.value:
            # Достаем текст в скобках, записываем его во временную переменную,
            text_in_paretheses_with_paretheses = cell.value[cell.value.rfind("("):cell.value.rfind(")") + 1]
            # вырезаем его из ячейки,
            cleaned_text = cell.value.replace(text_in_paretheses_with_paretheses, "")
            # сохраняем ячейку,
            cell.value = cleaned_text
            # сохраняем в переменную текст из ячейки Notes
            old_text = sheet[f"{column_letter_to}{cell.row}"].value
            if old_text is None:
                old_text = ""
            # записываем вырезанный текст в ячейку Notes
            sheet[f"{column_letter_to}{cell.row}"] = text_in_paretheses_with_paretheses + " " + old_text


def find_abbr_in_parentheses_begin(value):
    pattern_ru_and_eng_begin = r"^\([A-ZА-Я]{2,}\)"
    search_result_begin = re.search(pattern_ru_and_eng_begin, value)
    if search_result_begin:
        return search_result_begin.group(0)


def find_abbr_in_parentheses_end(value):
    pattern_ru_and_eng_end = r"\([A-ZА-Я]{2,}\)$"
    search_result_end = re.search(pattern_ru_and_eng_end, value)
    if search_result_end:
        return search_result_end.group(0)
