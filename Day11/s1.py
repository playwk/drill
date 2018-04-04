# Auther: ZhengZhong,Jiang
# -*- coding:utf-8 -*-

import threading
import time 


def f1(args):
    print(args)
    time.sleep(2)

# obj = threading.Thread(target=f1, args=(123, ))
# obj.start()


class Mythread(threading.Thread):
    def __init__(self, func, args):
        self.func = func
        self.args = args

obj = Mythread(f1, 1)
obj.func(obj.args)
