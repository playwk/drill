#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import tarfile

# 压缩
# tar = tarfile.open('your.tar','w')
# tar.add('s1.py', arcname='ssss.py')
# tar.add('s2.py', arcname='cmdb.py')
# tar.close()

# 解压
tar = tarfile.open('your.tar', 'r')
# tar.extractall()  # 可设置解压地址

# for item in tar.getmembers():
#     print(item,type(item))
obj = tar.getmember("ssss.py")
tar.extract(obj)

tar.close()