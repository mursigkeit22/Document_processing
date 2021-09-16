from openpyxl import load_workbook
import re

workbook = load_workbook(filename="./excel_docs/English - Russian Technical Language (Р.B_Chevron)_Prepared.xlsx")
for sheet in workbook.worksheets:
    print(sheet)

