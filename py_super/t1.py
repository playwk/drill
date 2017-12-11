# _*_ coding: utf-8 _*_
# @Author ZhengZhong,Jiang
# @DataTime 2017/4/24 0024 上午 10:14


class A(object):
    def __init__(self):
        print "enter A"
        print "leave A"


class B(object):
    def __init__(self):
        print "enter B"
        print "leave B"


class C(A):
    def __init__(self):
        print "enter C"
        super(C, self).__init__()
        print "leave C"


class D(A):
    def __init__(self):
        print "enter D"
        super(D, self).__init__()
        print "leave D"


class E(B, C):
    def __init__(self):
        print "enter E"
        B.__init__(self)
        C.__init__(self)
        print "leave E"


class F(E, D):
    def __init__(self):
        print "enter F"
        E.__init__(self)
        D.__init__(self)
        print "leave F"


f = F()


class IntTuple(tuple):

    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)


    def __init__(self ,iterable):
        super(IntTuple, self).__init__(iterable)


t = IntTuple(['abc', -1, 9, 0, -3, 6, 'b'])

print t

# __dict__ 动态绑定对象属性

# __slots__ 提前声明

# 让对象支持是上下文管理  with语句
#    __enter__ 开始时执行
#    __exit__ 结束后执行

# 比较运算符方法重载
# __lt__, __le__, __gt__, __ge__, __eq__, __ne__
# 标准库下的functools下的类装饰器total_ordering简化
