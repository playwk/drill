# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/12/7 9:24

import datetime

import xlrd
from xlutils.copy import copy
import configparser

nowtime = datetime.datetime.now().strftime('%Y%m%d')


def copyNewSheet():
    rb = xlrd.open_workbook('mmc_db_check.xls', formatting_info=True)
    wb = copy(rb)
    rs = rb.sheet_by_index(0)
    wb.add_sheet(nowtime)
    ws = wb.get_sheet(-1)
    for row in range(rs.nrows):
        for col in range(rs.ncols):
            ws.write(row, col, rs.cell_value(row, col))
    wb.save('mmc_db_check.xls')


def loadStatus(section, option):
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

def putNewValue(section, option):
    pass

if __name__ == '__main__':
    # copyNewSheet()
    loadStatus('master12.12.12.128', 'DatadirStatu')

