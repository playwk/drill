# Auther: ZhengZhong,Jiang
# -*- coding:utf-8 -*-

import threading


def func(arg, e):
    pass
    print(arg)
    e.wait()
    print(arg+100)

event = threading.Event()

for i in range(10):
    t = threading.Thread(target=func, args=(i, event, ))
    t.start()

event.clear()

inp = input('>>> ')

if inp == '1':
    event.set()
