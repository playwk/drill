#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

from multiprocessing import Process
from multiprocessing import Array


def foo(i, arg):
    arg[i] = i + 100
    for items in arg:
        print(items)
    print('--------------------')

if __name__ == '__main__':
    li = Array('i', 10)
    for i in range(10):
        p = Process(target=foo, args=(i, li, ))
        p.start()