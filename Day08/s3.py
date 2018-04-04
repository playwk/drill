# Auther: ZhengZhong,Jiang

#方法的私有与公有
class Foo:
    @staticmethod
    def __f1():
        print("alex")

    @classmethod
    def __f2(cls):
        print(cls)

    def f3(self):
        Foo.__f1()

    def f4(self):
        Foo.__f2()

obj = Foo()

#从外部调用失败
# Foo.__f1()
# Foo.__f2()

#从内部调用成功
obj.f3()
obj.f4()
