#！/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang
import threading


def condition():
    inp = input('>>> ')
    if inp == 'True':
        ret = True
    else:
        ret = False
    return ret


def func(args, c):
    print(args)
    c.acquire()
    c.wait_for(condition)
    print(args+100)
    c.release()


con = threading.Condition()

for i in range(10):
    t = threading.Thread(target=func, args=(i, con, ))
    t.start()

