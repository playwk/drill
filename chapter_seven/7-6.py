# _*_ coding: utf-8 _*_
# @Author ZhengZhong,Jiang
# @DataTime 2017/4/24 0024 下午 15:29

# 使用描述符对实例属性做类型检查


class Attr(object):
    def __init__(self, name, is_type):
        self.name = name
        self.is_type = is_type

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.is_type):
            raise TypeError("expected an %s" % self.is_type)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person(object):
    name = Attr('name', str)
    age = Attr('age', int)
    height = Attr('height', float)


man = Person()
man.name = 'jiang'
print(man.name)
man.age = '18'
print(man.age)
man.height = 1.72
print(man.height)
