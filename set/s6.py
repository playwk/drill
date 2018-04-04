# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/6/12 0012 下午 17:26
#
# from HTMLParser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#   def handle_starttag(self, tag, attrs):
#     print "a start tag:",tag,self.getpos()
#
# parser=MyHTMLParser()
# parser.feed()

import BeautifulSoup
import pymysql

def get_tables(htmldoc):
    soup = BeautifulSoup.BeautifulSoup(open(htmldoc))
    t_head = soup.findAll('tr')[0]
    t_body = soup.findAll('tr')[1:]
    print(t_head)
    # print(t_body)


print get_tables('demo.htm')

conn = pymysql.connect(host='12.12.12.134', port=3306, user='demo',
                       passwd='key@1234', db='demo', charset="utf8")

cur = conn.cursor()

aaa = "create table t(id int,name varchar(10)) engine=innodb charset utf8"
cur.execute("create table %s()")