import xmldiff

from lxml import etree
from xmldiff import main, formatting

# diff = main.diff_files('work_docs/xml/_1/styles.xml', 'work_docs/xml/_2/styles.xml',
# formatter=formatting.XMLFormatter(pretty_print=True)
#                        )
diff = main.diff_files('work_docs/xml/docm_unpack/20210526_IT_Strategy_RUS/customXml/item2.xml', 'work_docs/xml/docx_unpack/20210526_IT_Strategy_RUS/customXml/item2.xml',
                       formatter=formatting.XMLFormatter())


print(diff)