import lxml.etree
tree = lxml.etree.parse('./text/hand_italic.xml')
pretty = lxml.etree.tostring(tree, encoding="unicode", pretty_print=True)
print(pretty)