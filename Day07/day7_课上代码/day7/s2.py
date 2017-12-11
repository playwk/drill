#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
# 打开文件，读取XML内容
from xml.etree import ElementTree as ET
str_xml = open('xo.xml', 'r').read()

# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root = ET.XML(str_xml)

############ 操作 ############

# 顶层标签
print(root.tag)

# 循环所有的year节点
for node in root.iter('year'):
    # 将year节点中的内容自增一
    new_year = int(node.text) + 1
    node.text = str(new_year)

    # 设置属性
    node.set('name', 'alex')
    node.set('age', '18')
    # 删除属性
    del node.attrib['name']

############ 保存文件 ############
tree = ET.ElementTree(root)
tree.write("newnew.xml", encoding='utf-8')