# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2018/4/4 16:17

import smtplib
import psutil



def send_status():
    mem_data = psutil.virtual_memory()
    mem_statu = mem_data.percent

    if mem_statu > 50:
        mem_msg = "MEM 当前使用率%s%% 产生告警！" % mem_statu
    else:
        mem_msg = "MEM 当前使用率%s%%" % mem_statu
    smtp = smtplib.SMTP()
    smtp.connect("smtp.sohu.com", 25)
    smtp.login("pylearn@sohu.com", "key@1234")
    smtp.sendmail('pylearn@sohu.com', 'sun_jzz@163.com', mem_msg)


if __name__ == '__main__':
    send_status()