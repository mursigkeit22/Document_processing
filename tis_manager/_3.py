from docx import *

document = Document('./text/full.docx')

# <w:highlight w:val="yellow"/>

words = document._element.xpath('//w:r')
WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
tag_rPr = WPML_URI + 'rPr'
tag_highlight = WPML_URI + 'highlight'
tag_val = WPML_URI + 'val'
tag_t = WPML_URI + 't'
for word in words[:100]:
    print(word)
    for rPr in word.findall(tag_rPr):
        high = rPr.findall(tag_highlight)
        if len(high) == 0:
            try:
                print(word.find(tag_t).text)

            except Exception as ex:
                print("EXCEPTION:", ex)
