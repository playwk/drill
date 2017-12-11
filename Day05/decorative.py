# Auther: ZhengZhong,Jiang

def outer1(func):
    def inner(args):
        print("中国")
        result = func(args)
        return result

    return inner


def outer2(func):
    def inner(args):
        print("北京")
        result = func(args)
        return result
    return inner

@outer1
@outer2
def print_info(args):
    print(args)
    return "OK"

print_info('alex')