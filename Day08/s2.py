# Auther: ZhengZhong,Jiang

#字段的私有与公有

class Foo:
    __cc = 123

    def __init__(self, name):
        self.__name = name

    def f1(self):
        print(Foo.__cc)

    def f2(self):
        print(self.__name)



obj = Foo('alex')

# 从内部调用失败
# print(Foo.__cc)
# print(obj.__name)

# 从外部调用成功
obj.f1()
obj.f2()