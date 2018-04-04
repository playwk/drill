import random
import time
import sys
import copy


def call_time(func):
    def wrapper(*args,  **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print('%s running time: %s secs.' % (func.__name__,  t2 - t1))
        return res
    return wrapper


@call_time
def bubble_sort(data):
    for i in range(len(data) - 1 ):

        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
    return data


@call_time
def bubble_sort_v(data):
    for i in range(len(data) - 1):
        flag = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag = True
        if not flag:
            return data
    return data


@call_time
def choice_sort(data):
    for i in range(len(data) - 1):
        min_loc = i
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                min_loc = j
        data[i], data[min_loc] = data[min_loc], data[i]
    return data


@call_time
def insert_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        j = i - 1
        while j >= 0 and data[j] > tmp:
            data[j+1] = data[j]
            j -= 1
        print(j)
        data[j+1] = tmp
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


@call_time
def quick_sort_x(data):
    return quick_sort(data, 0, len(data)-1)




sys.setrecursionlimit(100000)
data = list(range(1000))
data2 = [5, 4, 7, 8, 2, 3, 1, 9]
# random.shuffle(data)
data.reverse()
insert_sort(data2)
print(data2)
quick_sort_x(data)

