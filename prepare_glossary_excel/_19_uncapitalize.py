from openpyxl import load_workbook
workbook = load_workbook(filename="./excel_docs/logistics_with_separator.xlsx")

sheet_glossary = workbook["Logistics"]


def decapitalize(column):
    for cell in sheet_glossary[column]:
        if cell.value[0].isupper() and cell.value[1:].islower():
            cell.value = cell.value.lower()


decapitalize("A")
decapitalize("D")

workbook.save("./ready_excel_docs/logistics_with_separator_done.xlsx")