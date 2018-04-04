# Auther: ZhengZhong,Jiang
# -*- coding:utf-8 -*-

import threading
import time
NUM = 10


def func(arg, lock):
    global NUM
    lock.acquire()
    NUM -= 1
    time.sleep(3)
    lock.release()
    print(arg, NUM)

l = threading.BoundedSemaphore(5)

for i in range(10):
    t = threading.Thread(target=func, args=(i, l, ))
    t.start()
