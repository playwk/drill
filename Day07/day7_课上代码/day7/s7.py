#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import zipfile

# 压缩
# z = zipfile.ZipFile('laxi.zip', 'a')
# z.write('newnew.xml')
# z.write('xo.xml')
# z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
# z.extractall()

# for item in z.namelist():
#     print(item,type(item))
z.extract("new.xml")

z.close()