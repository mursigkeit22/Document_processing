from openpyxl import load_workbook
import re

workbook = load_workbook(filename="./documents_excel/test_python.xlsx")
sheet_to_focus = 'Лист1'


workbook.active = 0
work_sheet = workbook.active

# Abbreviations like - (LCCA)
for cell in work_sheet["A"]:
    if "(" in cell.value:

        pattern = "- \([A-Z]{2,}\)"
        search_result = re.search(pattern, cell.value)
        if search_result:
            found_sequence = search_result.group(0)
            only_letters = re.search("[A-Z]{2,}", found_sequence).group(0)
            cell.value = re.sub(re.escape(found_sequence), "| " + only_letters, cell.value)

# comments in parentheses at the end of the sell

workbook.save("./new_docs/test_python.xlsx")
