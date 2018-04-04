# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/17 14:25
import sys
import requests

filter_name = ["active", "accepts", "handled", "requests", "reading", "writing", "waiting"]


def process_list():
    url = "http://localhost/ngx_status"
    response = requests.get(url, timeout=1)
    result = response.text
    result_list = result.split()
    filter_list = filter(lambda x: x.isdigit(), result_list)
    return filter_list


def result_dict(arg, filter_list):
    status_dict = {x: y for (x, y) in zip(filter_name, filter_list)}
    key = arg[0]
    print(status_dict[key])


if __name__ == "__main__":
    result_dict(sys.argv[1:], process_list())



