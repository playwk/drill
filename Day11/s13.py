#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

from multiprocessing import Pool
import time


def foo(i):
    time.sleep(1)
    print(i)


if __name__ == '__main__':
    pool = Pool(5)
    for i in range(30):
        # pool.apply(func=foo, args=(i, ))
        pool.apply_async(func=foo, args=(i, ))
    pool.close()
    pool.join()

