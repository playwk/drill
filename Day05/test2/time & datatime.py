# Auther: ZhengZhong,Jiang

import time
import datetime

print(time.time())

print(time.ctime())

print(time.ctime(time.time()-86400))

print(time.gmtime(time.time()-86400))

print(time.mktime(time.gmtime(time.time()-86400)))

print(time.localtime(time.time()))

print(time.strftime("%Y-%m-%d %H:%M:%S"))
