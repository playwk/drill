#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang
import time
from multiprocessing import Process
from multiprocessing import Manager


def foo(arg1, arg2):
    arg2[arg1] = arg1 + 100
    print(arg2.values())

if __name__ == '__main__':
    obj = Manager()
    li = obj.dict()
    for i in range(10):
        t = Process(target=foo, args=(i, li))
        t.start()
        t.join()
    # time.sleep(0.1)
