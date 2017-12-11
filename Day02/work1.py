#Author ZhengZhong,Jiang

import os,json,prettytable,datetime

if os.path.exists('user.db') == False:
    print('初始化系统用户... ...')
    data = {'admin':['123456','1','1','0']}
    json.dump(data,open('user.db', 'a'))
    print('初始化系统用户完成！')
    print('Username: admin\nPassword: 123456')


if os.path.exists('history.db') == False:
    print('初始化用户数据... ...')
    data = {'admin':['小米电视','1','2016-05-20 18:00:00']}
    json.dump(data,open('history.db', 'a'))
    print('初始化用户数据完成！')

if os.path.exists('shop_car.db') == False:
    data = {'admin':{'Mac Pro':['1','8999','1970-01-01 00:00:01']}}
    json.dump(data,open('shop_car.db', 'a'))

if os.path.exists('product.db') == False:
    data = {'家电':{'小米电视':['100','3999'],'Mac':['10','8999']}}
    json.dump(data,open('product.db', 'a'))


msg = '''
-------------------------
          1.登录
          2.注册
          3.退出
-------------------------
按1选择登录，按2选择注册，按其他任意键选择退出
'''

msg_user = '''
-------------------------
          1.开始购物
		  2.查看订单
		  3.账户充值
		  4.账户信息
按q退出登录
-------------------------
按1选择登录，按2选择注册，按其他任意键选择退出
'''



msg_admin = '''
-------------------------
          1.用户管理
          2.商品管理
		  3.账户信息
按q退出登录
-------------------------
按1选择登录，按2选择注册，按其他任意键选择退出
'''

def user(username):
    print(msg_user)
    choose = input('请输入您的选择：')
    if choose == '1':
        items_temp = {}
        product_info = json.load(open('product.db','r'))
        for items in enumerate(list(product_info.keys())):
            print(items[0],items[1])
            items_temp[items[0]] = items[1]
        print(items_temp)
        while True:
            choose_type = input('请选择商品类别：')
            if items_temp[int(choose_type)] == None:
                print('选择的商品类别不存在')
                continue
            else:
                product_temp = {}
                product_dict = product_info[items_temp[int(choose_type)]]
                print(product_dict)
                filed = ['商品编号','商品名称','剩余数量','商品价格']
                print_out = prettytable.PrettyTable(filed)
                print_out.align['商品编号'] = '1'
                print_out.padding_width = 1
                for product in enumerate(product_dict):
                    product_temp[product[0]] = product[1]
                    print_out.add_row([product[0],product[1],\
                                       product_dict[product[1]][0],product_dict[product[1]][1]])
                print(print_out)
                while True:
                    choose_product = input('请选择商品：')
                    if product_temp[int(choose_product)] == None:
                        print('选择的商品不存在!')
                        continue
                    else:
                        product_num = input('请输入购买数量：')
                        if int(product_num) > int(product_dict[product[1]][0]):
                            print('存货不足！请减少购买数量或更改购买商品！')
                            continue
                        else:
                            data = json.load(open('shop_car.db','r'))
                            data[username] = {product_temp[int(choose_product)]:[product_num,str(int(product_num)*int(product_dict[product[1]][1])),\
                                                                                 datetime.datetime.now().strftime('%b-%d-%y %H:%M:%S')]}
                            json.dump(data,open('shop_car.db','w'))

#

flag = True
while flag:
    print(msg)
    choose = input('请输入您的选择：')
    if choose == '2':
        try:
            while flag:
                userdata = json.load(open('user.db','r'))
                user_list = list(userdata.keys())
                user_name = input('请输入注册用户名：')
                if user_list.count(user_name) >0:
                    print('该用户名已被占用,请使用其他用户名注册！')
                    continue
                else:
                    break
        except IOError as err:
            print('File error: %s' % str(err))
            exit()
        user_pass = input('请输入注册密码：')
        print('\033[31;1m注意：如果是管理员用户，请输入1，其他输入都将默认为普通用户\033[0m')
        admin = input('是否管理员：')
        if admin == '1':
            user_type = 1
        else:
            user_type = 0
            data = json.load(open('user.db','r'))
            data[user_name] = [user_pass, user_type, '1', '0']
            json.dump(data,open('user.db','a'))
    elif choose == '1':
        count = 0
        lock_temp = []
        user_temp = {}
        user_info = json.load(open('user.db', 'r'))
        user_temp = list(user_info.keys())
        while flag:
            username = input('用户名：')
            password = input('密码：')
            user_msg = username in user_temp
            if user_msg == True:
                if user_info[username][2] == '0':
                    print('用户已被锁定！请联系管理员解锁！返回上级菜单按b,继续按c，其他任意键退出！')
                    choose = input('请输入选择：')
                    if choose == 'b':
                        break
                    elif choose == 'c':
                        continue
                    else:
                        exit()
                else:
                    if password == user_info[username][0]:
                        if user_info[username][1] == '1':
                            print('管理员')
                            exit()
                        else:
                            print('用户')
                            user(username)
                            exit()
                    else:
                        print('密码错误！')
                        lock_temp.append(username)
            else:
                    print('该用户不存在！返回上级菜单按b,继续按c，其他任意键退出！')
                    choose = input('请输入选择：')
                    if choose == 'b':
                        break
                    elif choose == 'c':
                        continue
                    else:
                        exit()
            if lock_temp.count(username) >2:
                print('密码重试次数太多，用户被锁定！')
                userupdate = json.load(open('user.db','r'))
                user_info[username][2] = '1'
                json.dump(user_info,open('user.db','w'))
                exit()
            continue
        continue