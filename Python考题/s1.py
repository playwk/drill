# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2018/4/4 15:15

import socket, platform
import smtplib



def send_info():
    hostname = socket.gethostname()
    system_version = platform.system()

    smtp = smtplib.SMTP()
    smtp.connect("smtp.sohu.com", 25)
    smtp.login("pylearn@sohu.com", "key@1234")
    smtp.sendmail('pylearn@sohu.com', 'sun_jzz@163.com', "主机名称：%s 系统类型：%s" % (hostname, system_version))


if __name__ == '__main__':
    send_info()