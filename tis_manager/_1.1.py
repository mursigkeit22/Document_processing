from docx import *

document = Document('./text/test.docx')


body_elements = document._body._body
print(len(body_elements))
print("++++++++++++++++++")

for el in body_elements:
        print(el.xml)

print("==============================================================")
print(body_elements.xml)



