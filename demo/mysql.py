# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/12/12 19:54

import datetime
from subprocess import Popen, PIPE

import pymysql
import configparser
import xlrd, xlwt
from xlutils.copy import copy


#nowtime = time.strftime('%Y-%m', time.localtime(time.time()))
nowtime = datetime.datetime.now().strftime('%Y%m%d')


font = xlwt.Font()
font.name = 'Verdana'
font.size = 11
style = xlwt.XFStyle()
style.font = font
alignment = xlwt.Alignment()
alignment.wrap = 1
alignment.horz = xlwt.Alignment.HORZ_LEFT
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

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
        config = configparser.ConfigParser()
        config.read('check.conf')
        res = config.options(self.role)
        print(res)
        config_category= {}
        try:
            self.host = config.get(self.role, 'host')
            self.port = config.get(self.role, 'port')
            self.user = config.get(self.role, 'user')
            self.password = config.get(self.role, 'password')
            self.data_vol = config.get(self.role, 'data_vol')
            self.check_dbs = config.get(self.role, 'check_dbs')
            self.errlog_path = config.get(self.role, 'errlog_path')

            #config_category['host'] = host
            #config_category['port'] = port
            #config_category['user'] = user
            #config_category['password'] = password
            #config_category['check_dbs'] = check_dbs
            #config_category['data_vol'] = data_vol
            #config_category['errlog_path'] = errlog_path

            if self.role == 'master':
                self.bak_dir = config.get(self.role, 'bak_dir')
                #config_category['bak_dir'] = bak_dir
            elif self.role == 'slave':
                
        except ValueError:
            print('获取状态值失败!')
        #return config_category

    def syncstatus(self):
        status = False
        try:
            conn = pymysql.connect(self.host, self.port,
                                   self.user, self.password
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

    def dbbak_dir(self):

        dbbak_used = Popen("df %s" % self)

    def get_value(self):
        check_res = {}
        data_vol_used = Popen("du -sh %s" % self.data_vol, stdout=PIPE)
        mysql_status = Popen("mysql -u%s -p%s -e'status'".format(self.user, self.password),
                             shell=True, stdout=PIPE)
        uptime = Popen("grep '^Uptime'", shell=True, stdin=mysql_status.stdout, stdout=PIPE)
        basestatus = Popen("grep '^Threads'", shell=True, stdin=mysql_status.stdout, stdout=PIPE)

        conn_status = Popen("mysql -h% -P%s -u%s -p%s -e'show status like '%conn%''" % (self.host, self.port, self.user, self.password),
                             shell=True, stdout=PIPE)
        current_conn = Popen("awk '/Threads_connected/{print $2}'", shell=True, stdin=conn_status.stdout, stdout=PIPE)
        max_used_conn = Popen("awk '/Max_used_connections/{print $2}'", shell=True, stdin=conn_status.stdout, stdout=PIPE)
        p = Popen("mysql -h%s -P%s -u%s -p%s -e'SELECT concat(truncate((sum(DATA_LENGTH)+sum(INDEX_LENGTH))/1024/1024, 2), 'MB') "
                         "as data_size FROM information_schema.TABLES where TABLE_SCHEMA=%s'"
                       % (self.host, self.port,
                          self.user, self.password,
                          self.check_dbs), shell=True, stdout=PIPE)
        dbsize = Popen("sed -n '2p'", shell=True, stdin=p.stdout, stdout=PIPE)

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
        check_res['dbsize'] = dbsize

        if self.role == "slave":
            check_res['sync_status'] = self.syncstatus()
        elif self.role == "master":
            check_res['db_bak'] =
        return check_res


def copy_new_sheet():
    rb = xlrd.open_workbook('mmc_db_check.xls', formatting_info=True)
    wb = copy(rb)
    rs = rb.sheet_by_index(0)
    wb.add_sheet(nowtime)
    ws = wb.get_sheet(-1)
    for r in range(rs.nrows):
        for c in range(rs.ncols):
            cwidth = ws.col(c).width
            if len(str(rs.cell_value(r, c))) * 128 > cwidth:
                ws.col(c).width = len(str(rs.cell_value(r, c))) * 128
            ws.write(r, c, rs.cell_value(r, c), style)
    wb.save('mmc_db_check.xls')


def put_new_value(load_status):
    rb = xlrd.open_workbook('mmc_db_check.xls', formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(-1)
    ws.write(1, 1, load_status('data_vol_used'), style)
    ws.write(2, 1, load_status('basestatus'), style)
    ws.write(3, 1, load_status('uptime'), style)
    ws.write(4, 1, load_status('dbsize'), style)
    ws.write(5, 1, load_status('current_conn'), style)
    ws.write(6, 1, load_status('max_used_conn'),
             style)
    ws.write(8, 1, load_status('log_alarm'), style)
    ws.write(9, 1, load_status('log_alarm'), style)
    ws.write(10, 1, load_status('log_alarm'), style)

    ws.write(1, 2, load_status('data_vol_used'), style)
    ws.write(2, 2, load_status('basestatus'), style)
    ws.write(3, 2, load_status('uptime'), style)
    ws.write(4, 2, load_status('dbsize'), style)
    ws.write(5, 2, load_status('current_conn'), style)
    ws.write(6, 2, load_status('max_used_conn'),
             style)
    ws.write(7, 2, load_status('sync_status'), style)
    ws.write(8, 2, load_status('log_alarm'), style)

    wb.save('mmc_db_check.xls')

if __name__ == '__main__':
    copy_new_sheet()
    # put_new_value()

