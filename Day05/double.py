# Auther: ZhengZhong,Jiang

status = {}

def check_login(func):
    def inner(*args,**kwargs):
        if status.get("is_login") != None:
            result = func(*args,**kwargs)
            return result
        else:
            print("请登录")
    return inner

def check_admin(func):
    def inner(*args,**kwargs):
        if status.get("is_admin") != None:
            result = func(*args,**kwargs)
            return  result
        else:
            print("权限不足")
    return inner


@check_login
@check_admin
def index():
    print("管理员")
    return "A"


def home():
    print("普通用户 ")
    return "B"


def login():
    username = input("用户名：").strip()
    if username == 'admin' or username == 'alex':
        status["is_login"] = "True"
        if username == 'admin':
            status['is_admin'] = 'True'
        print("登录成功")


def main():
    while True:
        print("1.登录；2.查看；3.管理")
        choose = input("请选择：")
        if choose == '1':
            login()
        elif choose == '2':
            home()
        elif choose == '3':
            index()

main()