#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

from greenlet import greenlet


def test1():
    print(11)
    gr2.switch()
    print(33)
    gr2.switch()


def test2():
    print(22)
    gr1.switch()
    print(44)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
