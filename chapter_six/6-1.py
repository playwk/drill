# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/10/19 15:48

import csv
from urllib import urlretrieve

urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', filename='pingan.csv')