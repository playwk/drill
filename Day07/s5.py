#Author ZhengZhong,Jiang

class c1:
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj

class c2:
    def __init__(self,name):
        self.name = name

    def m(self):
        print(self.name)
        return "OK"


class c3:
    def __init__(self, name):
        self.name = name

c2_obj = c2('alex')
c1_obj = c1('eric', c2_obj)
c3_obj = c3(c1_obj)

ret = c3_obj.name.obj.m()
print(ret)
