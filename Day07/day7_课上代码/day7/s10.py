#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

class F1: # 父类，基类
    def show(self):
        print('show')

    def foo(self):
        print(self.name)

class F2(F1): # 子类，派生类
    def __init__(self, name):
        self.name = name

    def bar(self):
        print('bar')
    def show(self):
        print('F2.show')

obj = F2('alex')
# obj.show()
obj.foo()


# obj = F2()
# obj.bar()
# obj.show()
# obj = F1()
# obj.bar()




#
# class S1:
#
#     def F1(self):
#         self.F2()
#
#     def F2(self):
#         pass
#
# class S2(S1):
#
#     def F3(self):
#         self.F1()
#
#     def F2(self):
#         pass
#
# obj = S2()
# obj.F3()
# obj = S1()
# obj.F1()


class C_2:
    def f2(self):
        print('C-2')

class C_1(C_2):
    def f2(self):
        print('C-1')

class C0(C_2):
    def f1(self):
        print('C0')

class C1(C0):

    def f1(self):
        print('C1')

class C2(C_1):
    def f2(self):
        print('C2')

class C3(C1,C2):
    def f3(self):
        pass

obj = C3()
obj.f2()




# import socketserver
#
# obj = socketserver.ThreadingTCPServer()
#
# obj.serve_forever()






