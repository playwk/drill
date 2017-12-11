# Auther: ZhengZhong,Jiang
# -*- coding:utf-8 -*-

import threading
import time

NUM = 10


def func():
    global NUM
    l.acquire()
    NUM -= 1
    l.release()
    time.sleep(1)
    print(NUM)

l = threading.RLock()

for i in range(10):
    t = threading.Thread(target=func(), args=(l, ))
    t.start()
