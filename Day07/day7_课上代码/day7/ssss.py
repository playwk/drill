#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from xml.etree import ElementTree as ET

tree = ET.parse('xo.xml')
root = tree.getroot()

for child in root:
    print(child.tag,child.attrib)
    for gradechild in child:
        print(gradechild.tag, gradechild.text)
