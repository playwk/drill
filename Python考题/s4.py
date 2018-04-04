# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2018/4/4 16:27

import smtplib
import psutil


def send_pids():
    pid_data = psutil.pids()
    pid_num = len(pid_data)

    if pid_num > 200:
        pid_msg = "MEM 当前使用率%s%% 产生告警！" % pid_num
    else:
        pid_msg = "MEM 当前使用率%s%%" % pid_num
    smtp = smtplib.SMTP()
    smtp.connect("smtp.sohu.com", 25)
    smtp.login("pylearn@sohu.com", "key@1234")
    smtp.sendmail('pylearn@sohu.com', 'sun_jzz@163.com', pid_msg)


if __name__ == '__main__':
    send_pids()