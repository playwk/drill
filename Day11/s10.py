#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

import multiprocessing
from multiprocessing import Process
from multiprocessing import queues


def foo(arg, args):
    args.put(arg)
    print('say hi', arg, args.qsize())

if __name__ == '__main__':
    li = queues.Queue(20, ctx=multiprocessing)
    for i in range(10):
        p = Process(target=foo, args=(i, li, ))
        p.start()
