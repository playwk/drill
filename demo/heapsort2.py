#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Auther: ZhengZhong,Jiang

def adjust(data, low, high):
    temp = data[low]
    i = low
    j = 2 * i + 1
    while j <= high:
        if j < high and data[j] < data[j+1]:
            j += 1
        if temp < data[j]:
            #data[i], data[j] = data[j], data[i]
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = temp


def heapsort(data):
    n = len(data)
    for i in range(n//2 -1, -1, -1):
        adjust(data, i, n-1)
    for i in range(n-1, -1, -1):
        data[0], data[i] = data[i], data[0]
        adjust(data, 0, i-1)
    print(data)


data = [4,2,7,9,3,1,8,6]
heapsort(data)
