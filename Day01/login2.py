#!/usr/bin/env python3
# Author: Zhangxunan
import sys
import getpass
#计数器
counter = 1
#user.txt格式
#用户名  密码   是否锁定(0:正常,1:锁定)
#rose  123456     1
#读取用户名密码，并将用户存到字典里。
#users = {'jack':['123456','0'],'rose':['123456','1']}
users = {}
f = open('user.txt','r')
for user in f.readlines():
    users[user.strip().split()[0]] = user.strip().split()[1:]
f.close()

#用户被锁定之后，重新把字典写入文件
def write_file(users):
    str = ''
    for user in users:
        str += user + ' ' + ' '.join(users[user]) + '\n'
    f = open('user.txt', 'w')
    f.write(str.strip())
    f.close()

while True:
    username = input('username:').strip()
    password = getpass.getpass('password:')
    #用户名存在，用户没有锁定，并且密码正确
    if username in users.keys() and users[username][1] == '0' and password == users[username][0]:
        print('登录成功，欢迎!')
        sys.exit(0)
    #用户名存在，用户没有锁定，但是密码错误，如果密码输入错误三次则锁定用户。
    elif username in users.keys() and users[username][1] == '0' and password != users[username][0]:
        counter += 1
        if counter > 3:
            users[username][1] = '1'
            write_file(users)
            print('密码错误输入三次,',username,'锁定')
            continue
        print('密码错误，请重新输入!')
    #用户名存在，但是已经被锁定，直接退出
    elif username in users.keys() and users[username][1] == '1':
        print(username,'用户已经被锁定，即将退出!')
        sys.exit(1)
    #用户名不存在，重新输入
    else:
        print(username,'用户不存在!')