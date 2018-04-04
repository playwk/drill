# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/4/27 0027 下午 15:35

import csv
from xml.etree.ElementTree import Element, ElementTree, tostring
from xml.dom import minidom


def csvToxml(fname):
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)

        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):  #使用zip方法 同时迭代两个可迭代对象
                e = Element(tag)
                e.text = text
                eRow.append(e)
    return ElementTree(root)


# def pretty(e, level=0):
#     if len(e) > 0:
#         e.text = '\n' + '\t' * (level + 1)
#         for child in e:
#             pretty(child, level + 1)
#         child.tail = child.tail[:-1]
#         print(child.)
#     e.tail = '\n' + '\t' * level

def pretty(e):
    e = tostring(e, 'utf-8')
    reparsed = minidom.parseString(e)
    return reparsed.toprettyxml(indent="\t")



et = csvToxml('table.csv')

# et.write('table.xml')

with open('table.xml', 'w') as w:
    w.write(pretty(et))


