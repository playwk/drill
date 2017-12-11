#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Auther: ZhengZhong,Jiang

import contextlib
import socket


@contextlib.contextmanager
def fu(host, port):
    sk = socket.socket()
    sk.bind((host, port))
    sk.listen(5)
    try:
        yield sk
    finally:
        sk.close()

with fu('127.0.0.1', 8888) as f:
    print(f)
