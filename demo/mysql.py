# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/12/12 19:54

import time
from subprocess import Popen, PIPE

import pymysql
import configparser


nowtime = time.strftime('%Y-%m', time.localtime(time.time()))

class DatabaseConn:
    def __init__(self, host, port=3306, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connection(self):
        def wrapper(func):
            conn = None
            try:
                conn = pymysql.connect(self.host, self.port,
                                       self.user, self.password
                                       )
            except pymysql.Error as e:
                print("%s连接失败!".format(self.host))
            conn.close()
            return conn
        return wrapper



class BaseStatus:
    def __init__(self, role):
        self.role = role

    def load(self):
        config = configparser.ConfigParser()
        config.read('check.conf')
        res = config.options(self.role)
        print(res)
        config_category= {}
        try:
            host = config.get(self.role, 'host')
            port = config.get(self.role, 'port')
            user = config.get(self.role, 'user')
            password = config.get(self.role, 'password')
            data_vol = config.get(self.role, 'data_vol')
            check_dbs = config.get(self.role, 'check_dbs')
            errlog_path = config.get(self.role, 'errlog_path')

            config_category['host'] = host
            config_category['port'] = port
            config_category['user'] = user
            config_category['password'] = password
            config_category['check_dbs'] = check_dbs
            config_category['data_vol'] = data_vol
            config_category['errlog_path'] = errlog_path

            if self.role == 'master':
                bak_dir = config.get(self.role, 'bak_dir')
                config_category['bak_dir'] = bak_dir
        except ValueError:
            print('获取状态值失败!')
        return config_category

    def syncstatus(self):
        status = False
        load_statu = self.load()
        if load_statu:
            try:
                conn = pymysql.connect(load_statu['host'], load_statu['port'],
                                       load_statu['user'], load_statu['password']
                                       )
                cur = conn.cursor()
                cur.execute('show slave status')
                for n in cur.fetchall():
                    if n[10] == n[11] == 'Yes':
                        status = True
                cur.close()
                conn.close()
            except pymysql.Error as e:
                print("pymysql Error!", e)
        return status

    def get_value(self):
        check_res = {}
        check_category = self.load()
        if check_category:
            data_vol_used = Popen("du -sh %s" % check_category['data_vol'], stdout=PIPE)
            mysql_status = Popen("mysql -u%s -p%s -e'status'".format(check_category['user'], check_category['password']),
                                 shell=True, stdout=PIPE)
            uptime = Popen("grep '^Uptime'", shell=True, stdin=mysql_status.stdout, stdout=PIPE)
            basestatus = Popen("grep '^Threads'", shell=True, stdin=mysql_status.stdout, stdout=PIPE)

            conn_status = Popen("mysql -u%s -p%s -e'show status like '%conn%''".format(check_category['user'], check_category['password']),
                                 shell=True, stdout=PIPE)
            current_conn = Popen("awk '/Threads_connected/{print $2}'", shell=True, stdin=conn_status.stdout, stdout=PIPE)
            max_used_conn = Popen("awk '/Max_used_connections/{print $2}'", shell=True, stdin=conn_status.stdout, stdout=PIPE)
            dbsize = Popen("mysql -h%s -u%s -p%s -e'SELECT sum(DATA_LENGTH)+sum(INDEX_LENGTH) FROM information_schema.TABLES where TABLE_SCHEMA=%s'"
                           % (),)

            log_filter = Popen("grep %s %s".format(nowtime, check_category['errlog_path']), shell=True,
                              stdout=PIPE)
            log_alarm = Popen("grep -iw '\[error\]'", shell=True, stdin=log_filter.stdout, stdout=PIPE)
            if not log_alarm:
                log_alarm = u'无告警'
            else:
                log_alarm = u'有告警'

            check_res['data_vol_used'] = data_vol_used
            check_res['uptime'] = uptime
            check_res['basestatus'] = basestatus
            check_res['current_conn'] = current_conn
            check_res['max_used_conn'] = max_used_conn
            check_res['log_alarm'] = log_alarm

            if self.role == "slave":
                check_res['sync_status'] = self.syncstatus()
        return check_res


