import docx
from docx import *

document = Document('./text/test.docx')
sections = document._element.xpath('//w:sectPr')

WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ODML_URI = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
tag_f = WPML_URI + 'ftr'
tag_id = ODML_URI + 'id'
tag_rPr = WPML_URI + 'rPr'
tag_r = WPML_URI + 'r'
tag_highlight = WPML_URI + 'highlight'
tag_val = WPML_URI + 'val'
tag_t = WPML_URI + 't'
tag_vanish = WPML_URI + 'vanish'


def get_ids_headers_footers(sections):
    id_list = []

    for section in sections:
        print(section.xml)
        print("============================")
        header_ref_with_id = section.xpath('//w:headerReference')
        footer_ref_with_id = section.xpath('//w:footerReference')
        for ref in header_ref_with_id:
            id = ref.get(tag_id)
            id_list.append(id)
        for ref in footer_ref_with_id:
            id = ref.get(tag_id)
            id_list.append(id)
    return id_list


header_footer_ids = get_ids_headers_footers(sections)

for id in header_footer_ids:
    print(document.sections._document_part.rels[id].target_part.element.xml)
    print()





print(document._element.xml)
print("==================================")
print(document.sections._document_part.rels['rId7'].target_part.element.xml) #<docx.opc.rel._Relationship object at 0x0000025AA156D460>
print("==================================")

print(document.sections._document_part.rels['rId9'].target_part.element.xml) #<docx.opc.rel._Relationship object at 0x0000025AA156D460>
print("==================================")
# #
print(document.sections._document_part.rels['rId11'].target_part.element.xml) #<docx.opc.rel._Relationship object at 0x0000025AA156D460>
