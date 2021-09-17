from openpyxl import load_workbook
import re

"""
сначала проверяем на пустые строки
"""

workbook = load_workbook(filename="./excel_docs/test_alpha.xlsx")
work_sheet = workbook["Лист1"]

# if all(x.isalpha() or x.isspace() for x in original): re.findall(r'\d+|[^A-Za-z]+|[A-Za-z\s]+', s)
for cell in work_sheet["A"]:
    # print(cell.value)
    found = re.search("[A-Za-z]", cell.value)
    if found:
        first_index = found.span()[0]
        print( cell.value[first_index:])
