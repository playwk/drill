# _*_ coding: utf-8 _*_
# @Author ZhengZhong,Jiang
# @DataTime 2017/4/20 0020 下午 16:58

import xlrd, xlwt

book = xlrd.open_workbook(filename='demo.xlsx')

book.sheets()

sheet = book.sheet_by_index(0)

print(sheet.nrows)

print(sheet.ncols)

print(sheet.cell(0, 0))

cell = sheet.cell(0, 0)

print(cell.ctype)

print(sheet.row(1))

print(sheet.row_values(1))

print(sheet.row_values(1, 1))

wbook = xlwt.Workbook()

wsheet = wbook.add_sheet('sheet1')





