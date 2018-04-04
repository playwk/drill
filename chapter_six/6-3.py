# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/4/27 0027 下午 15:03

from xml.etree.ElementTree import Element, ElementTree, tostring

f = open('demo.xml', 'r')

et = parse(f)

root = et.getroot()

print(root)

print(root.tag)

print(root.attrib)

print(root.text)

print(root.text.strip())

for child in root:
    print(child.get('category'))


print(root.find('book'))

print(root.findall('book'))

generator_obj = root.iterfind('book')

for i in generator_obj:
    print(i.get('category'))


# find(), findall(), iterfind() 只能找当前节点直接的子元素

# iter() 查找当前节点所有子元素

# findall(匹配模式)

# book/*

for x in root.findall('book/*'): # 匹配book下所有子元素
    print(x)

for x in root.findall('.//year'): # 无论year在哪个节点
    print(x)

# root.findall('.//year/..') # 后面的..描述父元素

# root.findall('title[@lang]') # title 包含lang属性的元素

# root.findall('title[@lang=en]') # title 包含lang属性等于en的元素
# root.findall('title[@lang=en]') # title 包含lang属性等于en的元素

# root.findall('title[1]') 找到的第一个子元素

# root.findall('title[2]') 找到的第二个子元素

# root.findall('title[last()]') 找到的最后子元素

# root.findall('title[last()-1]') 找到的最后倒数第二个元素

e = Element('Data')

e.set('name', 'abc')

tostring(e)

e.text = '123'

tostring(e)

print(tostring(e))

e2 = Element('Row')

e.append(e2)

e3 = Element('Open')

e3.text = '8.80'

e2.append(e3)

print(tostring(e))


et = ElementTree(e)

print('---', e2.tail)

et.write('test.xml')


