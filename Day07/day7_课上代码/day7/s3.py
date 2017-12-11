#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from xml.etree import ElementTree as ET

tree = ET.parse('xo.xml')
root = tree.getroot()

ele = ET.Element('Alex', {'k1': 'v1'})
ele.text = "我是内容"
root.append(ele)

tree.write("new.xml", encoding="utf-8")

# 列表
# root_list = [
#     []
# ]
#
# list ==> class 类名
# 类名() > 创建了一个对象
# ele = list()
# e = dict()
# el = Element()
# root_list.append(ele)

