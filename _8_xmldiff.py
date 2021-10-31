import xmldiff

from lxml import etree
from xmldiff import main, formatting

diff = main.diff_files('work_docs/xml/docm_unpack/20210526_IT_Strategy_RUS/customXml/item2.xml', 'work_docs/xml/docx_unpack/20210526_IT_Strategy_RUS/customXml/item2.xml',
                       formatter=formatting.XMLFormatter())