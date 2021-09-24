import docx
from docx import *

document = Document('./text/full.docx')
sections = document._element.xpath('//w:sectPr')

WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
ODML_URI = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
tag_f = WPML_URI + 'ftr'
tag_id = ODML_URI + 'id'
tag_rPr = WPML_URI + 'rPr'
tag_r = WPML_URI + 'r'
tag_highlight = WPML_URI + 'highlight'
tag_t = WPML_URI + 't'
tag_vanish = WPML_URI + 'vanish'


def get_ids_headers_footers(sections):
    """ по идее, там 3 headers и 3 footers (четный, нечетный и для первого листа).
     Боковые колонтитулы спрятаны в headers (не знаю, всегда или нет).
     Из каждого колонтитула забираем его id, по которому ниже сможем вытащить xml с ним"""
    id_list = []

    for section in sections:
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
    """ вытаскиваем xml с колонтитулами по его id"""

    work = document.sections._document_part.rels[id].target_part.element

    temp = work.xpath('//w:r')
    for element in temp:
        try:
            rprs = element.findall(tag_rPr)
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

document.save('./text/result_footers.docx')
