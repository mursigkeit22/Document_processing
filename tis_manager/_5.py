from docx import *

document = Document('./text/test.docx')
body_elements = document._body._body
# for el in body_elements[5]:
#     print(el.xml)
#     print("++++++++++++++++++++++++++++++++++++")
#
# print("===============================================================")
#
print(body_elements[-3].xml)

element = body_elements[-3]
children = list(element)
print(children)


