#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from xml.etree import ElementTree as ET


# 创建根节点
root = ET.Element("famliy")


# 创建节点大儿子
son1 = ET.Element('son', {'name': '儿1'})
# 创建小儿子
son2 = ET.Element('son', {"name": '儿2'})

# 在大儿子中创建两个孙子
grandson1 = ET.Element('grandson', {'name': '儿11'})
grandson2 = ET.Element('grandson', {'name': '儿12'})
son1.append(grandson1)
son1.append(grandson2)


# 把儿子添加到根节点中
root.append(son1)
root.append(son1)

tree = ET.ElementTree(root)
tree.write('oooo.xml',encoding='utf-8', xml_declaration=True, short_empty_elements=False)