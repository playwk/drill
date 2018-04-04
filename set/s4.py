# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/6/8 0008 上午 10:51
import re
from xml.dom import minidom


def wash(file_name):
    with open(file_name, 'r') as f:
        s = f.read().decode('utf8')
        print('-----', s)
        xml_str_list = re.split('BytesMessage:|</REQUEST>', s)
        xml_list = []
        for item in xml_str_list:
            if item.startswith('<?xml'):
                item = item.replace("GB18030", "UTF-8")
                item += "</REQUEST>"
                xml_list.append(item)
    print(xml_list)
    return xml_list


wash('new')


def pretty(xml_list):
    for item in xml_list:
        reparsed = minidom.parseString(item)
        print(reparsed.toprettyxml(indent="\t"))


pretty(wash('new'))

with open('result', 'r') as f:
    str = f.read()
    print(str.decode(encoding='gbk'))
