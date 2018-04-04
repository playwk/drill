#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Auther: ZhengZhong,Jiang

import contextlib

@contextlib.contextmanager
def work_state(state_list, worker_thread):
    state_list.append(worker_thread)
    try:
        yield
    finally:
        state_list.remove(worker_thread)

free_list = []

current_thread = 'alex'

with work_state(free_list, current_thread):
    print('123')
