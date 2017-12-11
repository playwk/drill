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

nowtime = datetime.datetime.now().strftime('%Y%m%d')

col_width = 256 * 20


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
                ws.col(c).width = len(str(rs.cell_value(r,c))) * 128
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
    ws.write(1, 1, load_status('master12.12.12.128', 'DatadirStatu'), style)
    ws.write(2, 1, load_status('master12.12.12.128', 'Status'), style)
    ws.write(3, 1, load_status('master12.12.12.128', 'Uptime'), style)
    ws.write(5, 1, load_status('master12.12.12.128', 'CurrentConn'), style)
    ws.write(6, 1, load_status('master12.12.12.128', 'Max_used_connections'),
            style)
    #ws.write(2, 1, load_status('master12.12.12.128', 'DatadirStatu'))
    #ws.write(4, 1, load_status('master12.12.12.128', 'Status'))
    #ws.write(6, 1, load_status('master12.12.12.128', 'Uptime'))
    #ws.write(18, 1, load_status('master12.12.12.128', 'CurrentConn'))
    #ws.write(20, 1, load_status('master12.12.12.128', 'Max_used_connections'))
    wb.save('mmc_db_check.xls')

if __name__ == '__main__':
    copy_new_sheet()
    put_new_value()

