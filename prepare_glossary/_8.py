from openpyxl import load_workbook



workbook = load_workbook(filename="./excel_docs/test.xlsx")
sheet_glossary = workbook["Лист1"]


def move_all_end_comments_to_notes(sheet, column_letter_from, column_letter_to, ):
    for cell in sheet[column_letter_from]:

        if cell.value.strip().endswith(")") and "(" in cell.value:
            # Достаем текст в скобках, записываем его во временную переменную,
            text_in_paretheses_with_paretheses = cell.value[cell.value.rfind("("):cell.value.rfind(")")+1]
            print("text_in_paretheses:", text_in_paretheses_with_paretheses)
            # вырезаем его из ячейки,
            cleaned_text = cell.value.replace(text_in_paretheses_with_paretheses, "")
            print("cleaned_text:", cleaned_text)
            # сохраняем ячейку,
            cell.value = cleaned_text

            #сохраняем в переменную текст из ячейки Notes
            old_text = sheet[f"{column_letter_to}{cell.row}"].value
            if old_text is None:
                old_text = ""
            # print("old_text.value", old_text.value)
            # записываем вырезанный текст в ячейку Notes
            sheet[f"{column_letter_to}{cell.row}"] = text_in_paretheses_with_paretheses + " " + old_text
move_all_end_comments_to_notes(sheet_glossary, "D", "F", )

workbook.save("./ready_excel_docs/test_done.xlsx")