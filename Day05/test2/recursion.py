# Auther: ZhengZhong,Jiang


def func(arg):
    arg += 1
    if arg >= 4:
        return "BBB"
    return func(arg)

result = func(1)

print(result)