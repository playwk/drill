# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2018/4/4 16:04

import smtplib
import psutil



def send_cpu():
    cpu_statu = psutil.cpu_percent()


    if cpu_statu > 50:
        msg = "CPU 当前使用率%s%% 产生告警！" % cpu_statu
    else:
        msg = "CPU 当前使用率%s%%" % cpu_statu
    smtp = smtplib.SMTP()
    smtp.connect("smtp.sohu.com", 25)
    smtp.login("pylearn@sohu.com", "key@1234")
    smtp.sendmail('pylearn@sohu.com', 'sun_jzz@163.com', msg)


if __name__ == '__main__':
    send_cpu()


