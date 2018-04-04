# Auther: ZhengZhong,Jiang

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        print(self.name)
        print(self.age)

    def __str__(self):
        return '%s - %d' % (self.name, self.age)

# -------------------
obj = Foo('alex', 20)
Foo('eric', 30)()
obj()

print(obj)
ret = str(obj)
print(ret)


# -------------------
#打印对象中封装的数据
ret = obj.__dict__
print(ret)