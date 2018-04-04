# Auther: ZhengZhong,Jiang

class Foo:

    def __getitem__(self, item):
        print('item')
        print('getitem')
        print(item.start)
        print(item.stop)
        print(item.step)

    def __setitem__(self, key, value):
        print('setitem')
        print(key.start)
        print(key.stop)
        print(key.step)

    def __delitem__(self, key):
        print('delitem')
        print(key.start)
        print(key.stop)
        print(key.step)

    # def __iter__(self):
    #     yield 1
    #     yield 2


# -------------------------
obj = Foo()

# obj['a']
# obj['a'] = 'b'
# del obj['a']

# -------------------------
ret = obj[1:2]
obj[1:3] = [11, 22, 33, 44,]
del obj[1:2]

# for i in obj:
#     print(i)