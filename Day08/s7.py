# Auther: ZhengZhong,Jiang


class Foo:
    instance = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instanse(cls):
        if cls.instance:
            return cls.instance
        else:
            obj = cls('alex')
            cls.instance = obj
            return obj


f1 = Foo.get_instanse()
print(f1)