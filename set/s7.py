# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/17 15:59
from itertools import *

# for i in ifilterfalse(lambda x: x > 5, [2, 3, 5, 6, 7]):
#     print(i)


for m in dropwhile(lambda x: x < 5, [1, 3, 6, 7, 1]):
    print(m)

# for m, n in product('abc', [1, 2]):
#     print m, n