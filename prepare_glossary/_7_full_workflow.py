"""
Работаем с каждым листом отдельно.
Лист Glossary:
 - итерируемся по колонке Б снизу вверх, удаляем строки, где есть пустые ячейки
 - итерируемся по колонке А, отделяем аббревиатуры
 - итерируемся по колонке А, скобочки из конца строки переносим в Notes
 - итерируемся по колонке Б, скобочки в конце переносим в Notes

Лист Abbreviations
 - итерируемся по колонке Д снизу вверх, удаляем строки, где есть пустые ячейки
 - итерируемся по колонке B снизу вверх, удаляем строки, где есть пустые ячейки
 - итерируемся по колонке Б, скобочки из конца строки переносим в Notes
 - итерируемся по колонке Д, скобочки в конце переносим в Notes

Лист Document Types:
- итерируемся по колонке C снизу вверх, удаляем строки, где есть пустые ячейки
- итерируемся по колонке Б, скобочки из конца строки переносим в Notes
 - итерируемся по колонке С, скобочки в конце переносим в Notes

"""

from openpyxl import load_workbook

from helper_functions import *

workbook = load_workbook(filename="./excel_docs/English - Russian Technical Language (Р.B_Chevron)_Prepared.xlsx")

sheet_glossary = workbook["Glossary"]
#- итерируемся по колонке Б снизу вверх, удаляем строки, где есть пустые ячейки
delete_raw_with_empty_cell(sheet_glossary, 2)
# - итерируемся по колонке А, отделяем аббревиатуры типа - (LCCA)
for cell in sheet_glossary["A"]:
    if "(" in cell.value:
        pattern = "- \([A-Z]{2,}\)"
        search_result = re.search(pattern, cell.value)
        if search_result:
            found_sequence = search_result.group(0)
            only_letters = re.search("[A-Z]{2,}", found_sequence).group(0)
            cell.value = re.sub(re.escape(found_sequence), "| " + only_letters, cell.value)

# - итерируемся по колонке А, скобочки из конца строки переносим в Notes
move_comments_to_notes(sheet_glossary, "A", "C", check_english_column)
#- итерируемся по колонке Б, скобочки в конце переносим в Notes
move_comments_to_notes(sheet_glossary, "B", "D", check_russian_column)


sheet_abbreviations = workbook["Abbreviations"]
# - итерируемся по колонке Д снизу вверх, удаляем строки, где есть пустые ячейки
delete_raw_with_empty_cell(sheet_abbreviations, 4)
# - итерируемся по колонке B снизу вверх, удаляем строки, где есть пустые ячейки
delete_raw_with_empty_cell(sheet_abbreviations, 2)
#  - итерируемся по колонке Б, скобочки из конца строки переносим в Notes
move_comments_to_notes(sheet_abbreviations, "B", "E", check_english_column)
#  - итерируемся по колонке Д, скобочки в конце переносим в Notes
move_comments_to_notes(sheet_abbreviations, "D", "F", check_russian_column)


sheet_document_types = workbook["Document Types"]
# - итерируемся по колонке C снизу вверх, удаляем строки, где есть пустые ячейки
delete_raw_with_empty_cell(sheet_document_types, 3)
# - итерируемся по колонке Б, скобочки из конца строки переносим в Notes
move_comments_to_notes(sheet_document_types, "B", "D", check_english_column)
#  - итерируемся по колонке С, скобочки в конце переносим в Notes
move_comments_to_notes(sheet_document_types, "C", "E", check_russian_column)

workbook.save("./ready_excel_docs/done.xlsx")
