# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/12/12 19:54

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

import os
import datetime
from subprocess import Popen, PIPE

import psutil
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


class Check:
    def __init__(self, role):
        self.role = role
        config = configparser.ConfigParser()
        config.read('check.conf')
        #res = config.options(self.role)

        try:
            self.host = config.get(self.role, 'host')
            self.port = config.get(self.role, 'port')
            self.user = config.get(self.role, 'user')
            self.password = config.get(self.role, 'password')
            self.data_vol = config.get(self.role, 'data_vol')
            self.check_dbs = config.get(self.role, 'check_dbs')
            self.errlog_path = config.get(self.role, 'errlog_path')

            if self.role == 'master':
                self.bak_vol = config.get(self.role, 'bak_vol')
        except ValueError:
            print('获取状态值失败!')

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

    def data_vol_used(self):
        data_vol_used = psutil.disk_usage(self.data_vol).percent
        return data_vol_used

    def status(self):
        res = Popen("mysql -h%s -P%s -u%s -p%s -e'status'" % (self.host,
            str(self.port), self.user, self.password), shell=True, stdout=PIPE)
        return res.stdout.readlines()
        #return res.stdout.readlines()[-3].rstrip("\n")

    def uptime(self):
        #res = Popen("grep '^Uptime'", shell=True, stdin=self.status(), stdout=PIPE)
        #return res.stdout
        res = self.status()[-5].strip("\n")
        return res.split(':')[1].strip("\t")

    def basestatus(self):
        #res = Popen("grep '^Threads'", shell=True, stdin=self.status(), stdout=PIPE)
        #print(res.stdout)
        res = self.status()
        return res[-3].strip("\n")

    def data_size(self):
        res = Popen("mysql -h%s -P%s -u%s -p%s -e'SELECT concat(truncate((sum(DATA_LENGTH)+sum(INDEX_LENGTH))/1024/1024, 2), 'MB') as data_size FROM information_schema.TABLES where TABLE_SCHEMA=%s'"
                  % (self.host, self.port,
                     self.user, self.password,
                     self.check_dbs), shell=True, stdout=PIPE)
        dbsize = Popen("sed -n '2p'", shell=True, stdin=res.stdout, stdout=PIPE)
        return dbsize

    def conn(self):
        try:
            conn = pymysql.connect(self.host, self.port,
                                   self.user, self.password
                                   )
            cur = conn.cursor()
            cur.execute("show processlist;")
            current_conn = len(cur.fetchall())
            cur.execute("show status like 'Max_used_connections';")
            max_used_conn = cur.fetchall()[0][1]
            cur.close()
            conn.close()
            return current_conn, max_used_conn
        except pymysql.Error as e:
            print("pymysql Error!", e)
            return False

    def log_alarm(self):
        log_filter = Popen("grep %s %s".format(nowtime, self.errlog_path), shell=True,
                          stdout=PIPE)
        log_alarm = Popen("grep -iw '\[error\]'", shell=True, stdin=log_filter.stdout, stdout=PIPE)
        if not log_alarm:
            return u'无告警'
        else:
            return u'有告警'

    def bak_vol(self):
        os.path.exists("%s/%s" % (self.bak_vol, 'name'))
        bak_vol_used = psutil.disk_usage(self.bak_vol).percent
        return bak_vol_used

    def mycat_status(self):
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if p.name() == 'wrpper-linux-x86-64':
                return u'正常'
            else:
                return u'不正常'

    # def get_value(self):
    #     check_res = {}
    #     mysql_status = Popen("mysql -u%s -p%s -e'status'".format(self.user, self.password),
    #                          shell=True, stdout=PIPE)
    #     uptime = Popen("grep '^Uptime'", shell=True, stdin=mysql_status.stdout, stdout=PIPE)
    #     basestatus = Popen("grep '^Threads'", shell=True, stdin=mysql_status.stdout, stdout=PIPE)
    #
    #     conn_status = Popen("mysql -h% -P%s -u%s -p%s -e'show status like '%conn%''" % (self.host, self.port, self.user, self.password),
    #                          shell=True, stdout=PIPE)
    #     current_conn = Popen("awk '/Threads_connected/{print $2}'", shell=True, stdin=conn_status.stdout, stdout=PIPE)
    #     max_used_conn = Popen("awk '/Max_used_connections/{print $2}'", shell=True, stdin=conn_status.stdout, stdout=PIPE)
    #
    #     log_filter = Popen("grep %s %s".format(nowtime, check_category['errlog_path']), shell=True,
    #                       stdout=PIPE)
    #     log_alarm = Popen("grep -iw '\[error\]'", shell=True, stdin=log_filter.stdout, stdout=PIPE)
    #     if not log_alarm:
    #         log_alarm = u'无告警'
    #     else:
    #         log_alarm = u'有告警'
    #
    #     check_res['data_vol_used'] = data_vol_used
    #     check_res['uptime'] = uptime
    #     check_res['basestatus'] = basestatus
    #     check_res['current_conn'] = current_conn
    #     check_res['max_used_conn'] = max_used_conn
    #     check_res['log_alarm'] = log_alarm
    #     check_res['dbsize'] = dbsize
    #
    #     if self.role == "slave":
    #         check_res['sync_status'] = self.syncstatus()
    #     elif self.role == "master":
    #         check_res['db_bak'] =
    #     return check_res

    def copy_new_sheet(self):
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

    def put_new_value(self):
        rb = xlrd.open_workbook('mmc_db_check.xls', formatting_info=True)
        wb = copy(rb)
        ws = wb.get_sheet(-1)
        if self.role == 'master':
            ws.write(1, 1, self.data_vol, style)
            ws.write(2, 1, self.basestatus(), style)
            ws.write(3, 1, self.uptime(), style)
            ws.write(4, 1, self.data_size(), style)
            ws.write(5, 1, self.conn()[0], style)
            ws.write(6, 1, self.conn()[1], style)
            ws.write(8, 1, self.log_alarm(), style)
            ws.write(9, 1, self.bak_vol, style)
            ws.write(10, 1, self.mycat_status(), style)
        elif self.role == 'slave':
            ws.write(1, 2, self.data_vol, style)
            ws.write(2, 2, self.basestatus(), style)
            ws.write(3, 2, self.uptime(), style)
            ws.write(4, 2, self.data_size(), style)
            ws.write(5, 2, self.conn()[0], style)
            ws.write(6, 2, self.conn()[1], style)
            ws.write(7, 2, self.syncstatus(), style)
            ws.write(8, 2, self.log_alarm(), style)

        wb.save('mmc_db_check.xls')

if __name__ == '__main__':
    master_check = Check('master')
    print(master_check.uptime())
    print(master_check.basestatus())
    master_check.copy_new_sheet()
    master_check.put_new_value()
    slave_check = Check('slave')
    slave_check.put_new_value()
