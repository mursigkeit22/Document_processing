from docx import *
import docx

document = Document('./text/full.docx')

elements = document._element.xpath('//w:r')
"""
//	Selects nodes in the document from the current node 
that match the selection no matter where they are
"""
WPML_URI = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
tag_rPr = WPML_URI + 'rPr'
tag_highlight = WPML_URI + 'highlight'
tag_val = WPML_URI + 'val'
tag_t = WPML_URI + 't'
tag_vanish = WPML_URI + 'vanish'
for element in elements:
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

document.save('./text/result_xml.docx')
