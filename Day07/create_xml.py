# Auther: ZhengZhong,Jiang

from xml.etree import ElementTree as et
from xml.dom import minidom

root = et.Element('data', {'name': 'alex'})

son1 = et.Element('son1', {'name': 'son1'})
son2 = et.Element('son2', {'name': 'son2'})

grandson1 = et.Element('grandson1', {'name': 'grandson1'})
grandson2 = et.Element('grandson2', {'name': 'grandson2'})

son1.append(grandson1)
son2.append(grandson2)

root.append(son1)
root.append(son2)

tree = et.ElementTree(root)
def prettify(elem):
    rough_string = et.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")
str = prettify(root)

f = open('xxoo.xml', 'w', encoding='utf-8')
f.write(str)
f.close()