# Auther: ZhengZhong,Jiang
# -*- coding:utf-8 -*-

import threading


def func(arg, c):
    print(arg)
    c.acquire()
    c.wait()
    print(arg+100)
    c.release()


con = threading.Condition()

for i in range(10):
    t = threading.Thread(target=func, args=(i, con, ))
    t.start()

while True:
    inp = input('>>> ')
    if inp == 'q':
        break
    con.acquire()
    con.notify(int(inp))
    con.release()
