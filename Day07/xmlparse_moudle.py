# Auther: ZhengZhong,Jiang

from xml.etree import ElementTree as et

# tree = et.parse('xo.xml')
# root = tree.getroot()
# print(root, "\n", root.tag)
#
# for child in root:
#     print(child.tag, child.attrib)
#     for grandchild in child:
#         print(grandchild.tag, grandchild.text)


info = open('xo.xml', 'r').read()

root = et.XML(info)

for node in root.iter('year'):
    print(node.tag, node.attrib, node.text)
    new_year = int(node.text) + 1
    node.text = str(new_year)

    node.set('name', 'alex')
    node.set('age', '18')

    del node.attrib['name']

tree = et.ElementTree(root)
tree.write('xo.xml', encoding='utf-8')



