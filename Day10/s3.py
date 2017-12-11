# Auther: ZhengZhong,Jiang

import threading
import time


def f1(args):
    time.sleep(1)
    print(args)


def f2(args):
    time.sleep(3)
    print(args)

print('alex')

t = threading.Thread(target=f2, args=('Wu', ))   # target指定函数名，args传进的参数
t.setDaemon(True)   # true，表示主线程不等此子线程
t.start()   # 不代表当前线程会被立即执行
t.join(2)   # 表示主线程到此，等待 ... 直到子线程执行完毕 参数n表示主线程在此最多等待n秒

f1('eric')
