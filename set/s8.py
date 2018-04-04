# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/10 0010 上午 8:42

data = [5, 7, 6, 8, 9, 2, 3, 1]


def choice_sort(data):
    for i in range(len(data) - 1):
        min = i #初始化最小的元素下标
        for j in range(i + 1, len(data)):
            if data[min] > data[j]:
                min = j #找到最小元素的下标
        data[i], data[min] = data[min], data[i] #交换
    return data


print(choice_sort(data))