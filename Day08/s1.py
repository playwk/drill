# Auther: ZhengZhong,Jiang


class Foo():
    # aa = 123
    #
    # def xx(self):
    #     bb = '456'
    #     print(bb)
    #
    # @staticmethod
    # def yy(args):
    #     print(args)
    #
    # @classmethod
    # def zz(cls):
    #     print(cls)

    @property
    def rr(self):
        print("@property")
        # return "@property"

    @rr.setter
    def rr(self, name):
        print("rr.setter")

    @rr.deleter
    def rr(self):
        print("rr.deleter")

    def f1(self):
        return 'a'

    def f2(self, args):
        print(args)

    def f3(self):
        print('c')

    foo = property(f1, f2, f3)

# -----------
# print(Foo.aa)
#
# # -------------
# obj = Foo()
# obj.xx()
#
# # -------------
# Foo.yy(789)
#
# # -------------
# Foo.zz()

# -------------
q = Foo()
q.rr
# res = q.rr
# print(res)
q.rr = 'alex'
del q.rr


p = Foo()
res = p.foo
print(res)
p.foo = 'alex'
del p.foo
