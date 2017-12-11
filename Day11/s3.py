# Auther: ZhengZhong,Jiang
# -*- coding:utf-8 -*-

import threading
import queue
import time

q = queue.Queue(5)


def f1(args):
    q.put('%s - 包子' % str(args))


for i in range(30):
    c = threading.Thread(target=f1, args=(i, ))
    c.start()


def f2(args):
    while True:
        print(args, q.get())
        time.sleep(2)
        if q.qsize() == 0:
            break

for i in range(3):
    s = threading.Thread(target=f2, args=(i, ))
    s.start()

