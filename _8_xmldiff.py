import xmldiff

from lxml import etree
from xmldiff import main, formatting

diff = main.diff_files('work_docs/xml/_1/styles.xml', 'work_docs/xml/_2/styles.xml',


formatter=formatting.XMLFormatter(pretty_print=True)
                       )
print(diff)