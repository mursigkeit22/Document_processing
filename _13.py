from lxml import etree


# tree = ET.parse('work_docs/xml/docm_unpack/20210526_IT_Strategy_RUS/customXml/item2.xml',)
doc = etree.parse('work_docs/xml/docm_unpack/20210526_IT_Strategy_RUS/customXml/item2.xml',)
# root = tree.getroot()
print(doc)
