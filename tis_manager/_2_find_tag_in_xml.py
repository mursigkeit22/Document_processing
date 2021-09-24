"""
https://stackoverflow.com/questions/55885498/attribute-error-with-docx-document-no-attribute-xpath
"""
from docx import *

document = Document('./text/full.docx')

elements = document._element.xpath('//w:r')
WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
tag_rPr = WPML_URI + 'rPr'
tag_highlight = WPML_URI + 'highlight'
tag_val = WPML_URI + 'val'
tag_t = WPML_URI + 't'
for element in elements[:100]:
    for rPr in element.findall(tag_rPr):
        high = rPr.findall(tag_highlight)
        for hi in high:
            if hi.attrib[tag_val] == 'yellow':
                try:
                    print(element.find(tag_t).text)

                except Exception as ex:
                    print("EXCEPTION:", ex)
