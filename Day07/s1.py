#Author ZhengZhong,Jiang

from xml.etree import ElementTree as ET

tree = ET.parse('applicationContext-dubbo-provide.xml')

root = tree.getroot()

print(root)

for child in root:
    print(child.tag, child.attrib)
    for gradechild in child:
        print(gradechild.tag, gradechild.text)