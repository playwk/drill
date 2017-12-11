#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
class SQLHelper:

    def __init__(self, a1, a2, a3):
        print('自动执行init')
        self.hhost = a1
        self.uuserane = a2
        self.pwd = a3
        self.create('sss')
    def fetch(self, sql):
        # 连接数据
        print(self.hhost)
        print(self.uuserane)
        print(self.pwd)
        print(sql)
    def create(self, sql):
        pass
    def remove(self, nid):
        pass
    def modify(self, name):
        pass

# obj1 = SQLHelper('c1.salt.com', 'alex', 123)
# obj2 = SQLHelper('c2.salt.com', 'alex1', 12333)
# obj1.create()


# obj.remove()
# obj.modify()


# class Person:
#
#     def __init__(self, name, age, money):
#         self.name = name
#         self.age =age
#         self.money = money
#
#     def shopping(self):
#         self.money = self.money - 2
#
# long = Person('龙', 18, -1)
# hu = Person('虎', 18, 2)
# bao = Person('豹', 73, 10)
#
# bao.shopping()
# hu.shopping()


class c1:

    def __init__(self,name,obj):
        self.name = name
        self.obj = obj

class c2:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name)
        return 123

class c3:
    def __init__(self, a1):
        self.money = 123
        self.aaa = a1


c2_obj = c2('aa', 11)
# c2_obj是c2类型
# - name = "aa"
# - age = 11
c1_obj = c1("alex", c2_obj)
# c1_obj 是c1 类型
# - name = "alex"
# - obj = c2_obj
c3_obj = c3(c1_obj)
# 使用c3_obj执行show方法
ret = c3_obj.aaa.obj.show()
print(ret)









