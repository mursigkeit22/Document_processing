from docx import *

document = Document('./text/test.docx')
body_elements = document._body._body
for el in body_elements[4:]:

        print(el.xml)
        print("++++++++++++++++++++++++++++++++++++")

print("===============================================================")

p = document.paragraphs[-2]
for run in p.runs:

        if run.font.highlight_color is None:
            run.font.hidden = True


print(body_elements[-3].xml)