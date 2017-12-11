# Auther: ZhengZhong,Jiang

# def fun():
#     print("---A")
#     yield 1
#     print("---B")
#     yield 2
#     print("---C")
#     yield 3
#
#
# ret = fun()
#
# for i in ret:
#     print(i)

# def myrange(arg):
#     start = 0
#     while True:
#         if start > arg:
#             return
#         yield start
#         start += 1
#
# ret = myrange(100)
#
# for i in ret:
#     print(i)


def func(arg):
    arg += 1
    if arg >= 4:
        return "end"
    return func(arg)

result = func(1)

print(result)

