# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/7/3 0003 上午 8:43
import sys, getopt
import requests
import json


class Zabbix():
    def __init__(self):
        self.url = "http://zabbix.cmbc.com.cn/api_jsonrpc.php"
        self.header = {"Content-Type": "application/json"}

    def login(self):
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "user.login",
                "params": {
                    "user": "Admin",
                    "password": "key@1234"
                },
                "id": 1
            })

        try:
            response = requests.post(self.url, data=data, headers=self.header)
        except requests.RequestException as e:
            result = e
        else:
            result = json.loads(response.text)['result']
        return result

    def get_host_list(self):
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "host.get",
                "params": {
                    # "output": "extend",
                    # "filter": {"host": ["Zabbix server", ]}
                    "output": ["hostid", "name", "available"],
                    "filter": {"host": ""}
                },
                "auth": self.login(),
                "id": 1
            }
        )
        try:
            response = requests.post(self.url, data=data, headers=self.header)
        except requests.RequestException as e:
            print(e)
        else:
            result = json.loads(response.text)['result']
            for index, item in enumerate(result):
                print(index, item['hostid'], item['available'], item['name'])

    def get_host_items(self, host_id):
        data = json.dumps(
            {
                "jsonrpc": "2.0",
                "method": "item.get",
                "params": {
                    # "output": "extend",
                    "output": ["itemid", "name", "templateid"],
                    "hostids": host_id,
                    # "search": { "key_": "" },
                    "sortfield": "name"
                },
                "auth": self.login(),
                "id": 1
            }
        )
        try:
            response = requests.post(self.url, data=data, headers=self.header)
        except requests.RequestException as e:
            print(e)
        else:
            result = json.loads(response.text)['result']
            # print(result)
            for index, item in enumerate(result):
                print(index, item)


def main(obj, argv):
    try:
        opts, args = getopt.getopt(argv, "hai:")
    except:
        print('zabbix_api.py\t-a 显示所有主机')
        print('\t\t-i 查看指定主机的所有监控项')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('zabbix_api.py\t-a 显示所有主机')
            print('\t\t-i 查看指定主机的所有监控项')
            sys.exit()
        elif opt == '-a':
            obj.get_host_list()
        elif opt == "-i":
            host_id = arg
            obj.get_host_items(host_id)


if __name__ == '__main__':
    obj = Zabbix()
    main(obj, sys.argv[1:])