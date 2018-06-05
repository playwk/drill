# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2018/6/5 15:24

import json, requests

filter_name = ["connections", "accepts", "handled", "request", "reading", "writing", "waiting"]


def nginx_status(url):
    data = {}
    all_status = []
    response = requests.get(url, timeout=1)
    result = response.text
    result_list = result.split(' ')
    filter_list = []
    for item in result_list:
        if item.isdigit():
            filter_list.append(str(item))
    for (status, program) in zip(filter_list, filter_name):
        status_dict = {}
        status_dict['{#STATUS}'] = status
        status_dict['{#PROGRM}'] = program
        all_status.append(status_dict)

    data['data'] = all_status
    jsonStr = json.dumps(data, sort_keys=True, indent=4)
    print(jsonStr)


if __name__ == "__main__":
    url = "http://localhost/ngx_status"
    nginx_status(url)