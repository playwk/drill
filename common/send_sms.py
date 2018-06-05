# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2018/6/5 15:13

import sys
import time
import json, requests

reload(sys)
sys.setdefaultencoding("utf-8")

apikey = "7489766dd0ef09d3adc9f080232a847e"


def send_sms(apikey, text, mobile):
    sms_host = "sms.yunpian.com"
    # 端口号
    port = 443
    # 版本号
    version = "v2"
    # 智能匹配模板短信接口的URI
    sms_send_uri = "/" + version + "/sms/batch_send.json"
    params = {'apikey': apikey, 'text': text, 'mobile': mobile}
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    url = "https://%s:%s%s" % (sms_host, port, sms_send_uri)
    response = requests.post(url, timeout=30, params=params, headers=headers)
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    with open('/tmp/send_sms.log', 'a+') as f:
        f.write("%s %s\n" % (current_time, response.text))


def main(arg):
    mobile = arg[0]
    text = arg[1]
    send_sms(apikey, text, mobile)


if __name__ == "__main__":
    main(sys.argv[1:])