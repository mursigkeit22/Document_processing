import docx
from docx import *

document = Document('./text/test.docx')
elements = document._element.xpath('//w:sectPr')

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


def get_ids_headers_footers(elements):
    id_list = []

    for el in elements:
        header_ref_with_id = el.xpath('//w:headerReference')
        footer_ref_with_id = el.xpath('//w:footerReference')
        for ref in header_ref_with_id:
            id = ref.get(tag_id)
            id_list.append(id)
        for ref in footer_ref_with_id:
            id = ref.get(tag_id)
            id_list.append(id)
    return id_list


# header_footer_ids = get_ids_headers_footers(elements)

# for id in header_footer_ids[1:2]:
#     print(document.sections._document_part.rels[id].target_part.element.xml)
#     print()

work = document.sections._document_part.rels['rId7'].target_part.element
# temp = work.xpath('//w:r')
# temp = work.findall(tag_r)
# print(temp)


temp = work.xpath('//w:r') # work.xpath('//w:r')
for element in temp:
    try:
        rprs = element.findall(tag_rPr)
        print("rprs", rprs)
        if len(rprs) == 0:
            tag_text = element.find(tag_t)
            rpr = docx.oxml.shared.OxmlElement('w:rPr')
            rpr.append(docx.oxml.shared.OxmlElement('w:vanish'))
            tag_text.addprevious(rpr)

        for rPr in rprs:
            high = rPr.findall(tag_highlight)
            if len(high) == 0:
                rPr.append(docx.oxml.shared.OxmlElement('w:vanish'))
    except AttributeError:  # when there is no text
        pass

# document.save('./text/result_footers.docx')
# print(temp)



# tag_rPr = WPML_URI + 'rPr'
# tag_highlight = WPML_URI + 'highlight'
# tag_val = WPML_URI + 'val'
# tag_t = WPML_URI + 't'

# for element in elements:
# #     print(element.find(tag_f))
#     for el in element:
#         # print(el.find(tag_f))
#         # el.xpath('//w:ftr')
#         try:
#             print(el.xml)
#         except:
#             for x in el:
#                print(x)

# print(document._element.xml)
# print("==================================")
# print(document.sections._document_part.rels['rId7'].target_part.element.xml) #<docx.opc.rel._Relationship object at 0x0000025AA156D460>
# print("==================================")

# print(document.sections._document_part.rels['rId9'].target_part.element.xml) #<docx.opc.rel._Relationship object at 0x0000025AA156D460>
# print("==================================")
# # #
# print(document.sections._document_part.rels['rId11'].target_part.element.xml) #<docx.opc.rel._Relationship object at 0x0000025AA156D460>
