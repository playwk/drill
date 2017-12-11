# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/5/31 0031 下午 16:08

import re
from xml.dom import minidom


def wash(file):
    with open(file, 'r') as f:
        str = f.read().decode('gb18030')
        xml_str_list = re.split('BytesMessage:|</REQUEST>', str)
        xml_list = []
        for item in xml_str_list:
            if item.startswith('<?xml'):
                item=item.replace("GB18030","UTF-8")
                item += "</REQUEST>"
                xml_list.append(item.encode('utf8'))
    print(xml_list)
    return xml_list


def pretty(xml_list):
    for item in xml_list:
        reparsed = minidom.parseString(item)
        print(reparsed.toprettyxml(indent="\t"))


pretty(wash('result'))

