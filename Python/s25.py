#!/usr/bin/env python
# -*- coding :utf-8 -*-
# @Author    :ZhengZhong,Jiang
# @TIME      :2018/4/7 16:44

import re
import requests
from urllib import parse


def get_data():
    context = "#code#=8888"
    url_context = parse.quote(context)
    print(url_context)
    str = "1[3458]\\d{9}"
    with open('demo.txt', 'r') as f:
        s = re.findall(str, f.read())
        if s:
            for num in s:
                send_msg(num, url_context)


def send_msg(mobile, context):
    url = "http://v.juhe.cn/sms/send"
    r = requests.get(url=url, params="mobile=%s&tpl_id=70455&tpl_value=%s&key=04e07c4d35f3a904e10334c2eb6b9aa5"
                                     %(mobile, context))
    print(r.json())



if __name__ == '__main__':
    get_data()