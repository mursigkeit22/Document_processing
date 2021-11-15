import lxml.etree

tree = lxml.etree.parse('./text/Ira.DOC.sdlxliff')
pretty = lxml.etree.tostring(tree, encoding="unicode", pretty_print=True)
with open('tis_manager/text/done/Ira.DOC_pretty.sdlxliff', "w", encoding="utf8", ) as f:
    print(pretty, file=f)
