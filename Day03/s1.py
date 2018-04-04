# Author ZhengZhong,Jiang


# def print_out(name_info,age_info):
#     print('name: {0} | age: {1}'.format(name_info,age_info))
#
# print('result'.center(25,'-'))
# print_out('alex','18')


# def print_out(name_info,age_info=18):
#     print('name: {name} | age: {name}'.format(name=name_info, age=age_info))
#
# print('result'.center(25,'-'))
# print_out('alex')
#
#
# def print_out(name_info,age_info):
#     print('name: {name} | age: {age}'.format(age=age_info,name=name_info))
#
# print('result'.center(25,'-'))
# print_out(age_info=18,name_info='alex')

# def print_out(*args):
#     print('name: {0} | age: {1}'.format(args[0], args[1]))
#
# print('result'.center(25,'-'))
# print_out(*['alex',18,])

# def print_out(**kwargs):
#     print('name: {name} | age: {age}'.format(age=kwargs['age'], name=kwargs['name']))
#
# print('result'.center(25,'-'))
# print_out(**{'name':'alex','age':18,})

# def print_out(*args,**kwargs):
#     print('name: {name} | age: {age}'.format(age=kwargs['age'], name=args[0]))
#
# print('result'.center(25,'-'))
# print_out(*['alex'],**{'age':18,})


# def plus(x):
#     return lambda y:x+y
#
# result = plus(2)
# print(result(3))

# f = open('user.info','r+')
# print(f.read())
# print(f.tell())
# f.seek(6)
# print(f.read())
# print(f.tell())
# f.close()


# f = open('user.info','r+')
# f.write('wang aaa')
# f.flush()
# print(f.readline())


f = open("db", 'a',encoding="utf-8")
f.write("xyz")
f.flush()
input('abc')