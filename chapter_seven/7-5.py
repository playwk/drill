# _*_ coding: utf-8 _*_
# @Author ZhengZhong,Jiang
# @DataTime 2017/4/24 0024 下午 15:12

# 类比较操作


from functools import total_ordering
from abc import abstractmethod
from math import pi


@total_ordering
class Shape():
    @abstractmethod
    def area(self):     #定义抽象方法
        pass

    def __lt__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not instance of Shape')
        return self.area() < obj.area()

    def __eq__(self, obj):
        if not isinstance(obj, Shape):
            raise TypeError('obj is not instance of Shape')
        return self.area() == obj.area()


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        s = self.w * self.h
        return s


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        s = pi * self.r ** 2
        return s

s1 = Rectangle(3, 4)
s2 = Circle(2)

print(s1 <= 12 )