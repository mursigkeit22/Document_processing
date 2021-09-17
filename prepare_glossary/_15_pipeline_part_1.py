"""
Для файла _1_separated
- чистим от пустых строк по столбцам А  Б
- дважды по каждому столбцу вытаскиваем комменты в скобках

"""


from openpyxl import load_workbook
from helper_functions import *


workbook = load_workbook(filename="./excel_docs/_1_КТК_first_list_separated.xlsx")
work_sheet = workbook["Лист1"]
delete_raw_with_empty_cell(work_sheet, 1)
delete_raw_with_empty_cell(work_sheet, 2)

move_comments_to_notes_safe(work_sheet, "A", "C")
move_comments_to_notes_safe(work_sheet, "A", "C")
move_comments_to_notes_safe(work_sheet, "B", "D")
move_comments_to_notes_safe(work_sheet, "B", "D")

workbook.save("./ready_excel_docs/done_part_1_separated.xlsx")
