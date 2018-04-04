#Author ZhengZhong,Jiang


# class F1:
#     def bar(self):
#         print("Test")
#         return "OK"
#
#     def show(self):
#         print("F1.show")
#
#
# class F2(F1):
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print("F2.show")
#
#
# obj = F2('alex')
# obj.show()
# obj.bar()


# class c1:
#     def f1(self):
#         print("c1.f1")
#     def f2(self):
#         print("c1.f2")
#     def f4(self):
#         print("c1.f4")
#
# class c2(c1):
#     def f1(self):
#         print("c2.f1")
#
# class c3:
#     def f4(self):
#         print("c3.f1")
#
# class c4(c3):
#     def f1(self):
#         print("c4.f1")
#     def f2(self):
#         print("c4.f2")
#
# class c5(c2, c4):
#     def ff(self):
#         pass
#
# obj = c5()
# obj.f2()
# obj.f4()

class c0:
    def f4(self):
        print("c0.f4")

class c1(c0):
    def f1(self):
        print("c1.f1")

class c2(c1):
    def f1(self):
        print("c2.f1")

class c3(c0):
    def f1(self):
        print("c3.f1")

class c4(c3):
    def f1(self):
        print("c4.f1")

class c5(c2, c4):
    def ff(self):
        pass

obj = c5()
obj.f4()
