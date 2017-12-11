# Auther: ZhengZhong,Jiang

class C1:
    def f1(self):
        print('c1.f1')

class C2(C1):
    def f2(self):
        # super 关键字， 主动执行父类方法
        super(C2, self).f1()
        print('c2.f2')

obj = C2()
obj.f2()



