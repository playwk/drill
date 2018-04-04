#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2017/3/16 0016 下午 15:33
# @Author   : ZhengZhong,Jiang

data = [5, 4, 7, 8, 2, 3, 1, 9]


def bubble_sort(data):
    for i in range(len(data) - 1):
        flag = True
        for j in range(len(data) - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                flag = False
        if flag:
            return data
    return data


def choice_sort(data):
    for i in range(len(data) - 1):
        min_loc = i
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                min_loc = j
    return data


def insert_sort(data):
    for i in range(len(data)):
        tmp = data[i]
        j = i - 1
        while j >= 0 and data[j] > tmp:
            data[j+1] = data[j]
            j -= 1
        data[i] = tmp
    return data


def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)
    return data


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


def adjust_heap(data,i,size):
    lchild = 2 * i + 1
    rchild = 2 * i + 1
    max_loc = i
    if i < size/2:
        if lchild < size and data[lchild] > data[max_loc]:
            max_loc = lchild
        if rchild < size and data[rchild] > data[max_loc]:
            max_loc = rchild
        if max_loc != i:
            data[max_loc], data[i] = data[i], data[max_loc]
        adjust_heap(data, max_loc, size)


def build_heap(data, size):
    for i in range(0, size)[::-1]:
        adjust_heap(data, i, size)


def heap_sort(data):
    size = len(data)
    build_heap(data, size)
    for i in range(0, size)[::-1]:
        data[0], data[i] = data[i], data[0]
        adjust_heap(data, i, size)


print(bubble_sort(data))
print(choice_sort(data))
print(insert_sort(data))
print(quick_sort(data, 0, 7))

