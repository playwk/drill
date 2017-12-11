#Author ZhengZhong,Jiang

class Foo:

    def __init__(self, name, age, msg):
        self.name = name
        self.age = age
        self.msg = msg
        self.add = 'something'

    def m1(self):
        print(self.name,self.age,self.msg,self.add)

obj1 = Foo('alex', '30', 'python')
obj2 = Foo('eric', '40', 'Java')
obj1.m1()
obj2.m1()
