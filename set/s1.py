# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/5/25 0025 上午 8:38

import shutil
import requests
import time


def url_test(url):
    response = requests.get(url, timeout=3)
    if response.status_code == '200':
        return True


def get_upstream():
    with open('nginx.conf', "r", ) as f:
        lines = f.readlines()
        upstream_set = {}
        tag = 0
        key = ''
        for line in lines:
            if 'upstream' in line:
                key = line.split()[1]
                upstream_set[key] = []
                tag = 1
            if tag == 1 and line.strip().startswith('server'):
                host = line.split()[1].strip()[:-1]
                upstream_set.get(key).append(host)
            if tag == 1 and '}' in line:
                tag = 0
    return upstream_set


def get_all_host(upstream_set):
    all_hosts = []
    for item in upstream_set.values():
        for host in item:
            all_hosts.append(host)
    return all_hosts


def check_server(all_hosts):
    error_hosts = []
    for host in all_hosts:
        if not url_test(host):
            error_hosts.append(host)
    return error_hosts


def conf_bak():
    now_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    shutil.copy('nginx.conf', 'nginx.conf.%s' % now_time)


def modify_conf(error_hosts):
    with open('nginx.conf.tmp', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() in error_hosts:
                lines.remove(line)
    with open('nginx.conf', 'w') as f:
        for line in lines:
            f.write(line)


