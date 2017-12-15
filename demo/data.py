# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/12/7 9:24


# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import datetime

import xlrd, xlwt
from xlutils.copy import copy
import configparser
import pymysql

nowtime = datetime.datetime.now().strftime('%Y%m%d')

# col_width = 256 * 20


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


def load_status(section, option):
    config = configparser.ConfigParser()
    config.read('mysqlstatus')
    res = config.options(section)
    print(res)
    try:
        value = config.get(section, option)
        print(value)
        return value
    except ValueError:
        print('获取%s状态值失败！' % option)


def put_new_value():
    rb = xlrd.open_workbook('mmc_db_check.xls', formatting_info=True)
    wb = copy(rb)
    ws = wb.get_sheet(-1)
    ws.write(1, 1, load_status('master', 'DatadirStatu'), style)
    ws.write(2, 1, load_status('master', 'Status'), style)
    ws.write(3, 1, load_status('master', 'Uptime'), style)
    ws.write(5, 1, load_status('master', 'CurrentConn'), style)
    ws.write(6, 1, load_status('master', 'Max_used_connections'),
            style)
    ws.write(7, 1, load_status('master', 'LogAlarm'), style)

    ws.write(1, 2, load_status('slave', 'DatadirStatu'), style)
    ws.write(2, 2, load_status('slave', 'Status'), style)
    ws.write(3, 2, load_status('slave', 'Uptime'), style)
    ws.write(5, 2, load_status('slave', 'CurrentConn'), style)
    ws.write(6, 2, load_status('slave', 'Max_used_connections'),
            style)
    ws.write(7, 2, load_status('slave', 'SyncStatus'), style)
    wb.save('mmc_db_check.xls')

def test():
    conn = pymysql.connect(host='12.12.12.129', port=3306,
                           user='root', password='key@1234'
                           )
    cur = conn.cursor()
    cur.execute("show status like 'Max_used_connections';")
    max_used_conn = cur.fetchall()[0][1]
    print(max_used_conn)

if __name__ == '__main__':
    # copy_new_sheet()
    # put_new_value()
    test()

