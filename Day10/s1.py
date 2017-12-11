# Auther: ZhengZhong,Jiang

li = [x+1 for x in range(10)]
print(li)

li = [x+1 for x in range(10) if x > 6]
print(li)

li = [lambda:x for x in range(10)]

print(li)
ret = li[0]()
ret2 = li[1]()
print(ret)
print(ret2)
