# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/6/12 0012 下午 17:26

#coding=utf-8
import requests


#下载沪深300成份股
resp = requests.get("http://115.29.204.48/webdata/000300cons.xls")
with open("000300cons.xls","wb") as code:
	code.write(resp.content)

#下载沪深300成份股权重
resp = requests.get("http://115.29.204.48/webdata/000300closeweight.xls")
with open("000300closeweight.xls","wb") as code:
	code.write(resp.content)

#下载中证500成份股
resp = requests.get("http://115.29.204.48/webdata/000905cons.xls")
with open("000905cons.xls","wb") as code:
	code.write(resp.content)

#下载中证500成份股权重
resp = requests.get("http://115.29.204.48/webdata/000905closeweight.xls")
with open("000905closeweight.xls","wb") as code:
	code.write(resp.content)

#下载上证50成份股
resp = requests.get("http://115.29.204.48/webdata/000016cons.xls")
with open("000016cons.xls","wb") as code:
	code.write(resp.content)

headers = {'Connection': 'keep-alive'}
resp = requests.get("http://www.swsindex.com/downloadfiles.aspx?swindexcode=SwClass&type=530&columnid=8892",
    cookies=headers)

headers['Cookie'] = resp.headers['Set-Cookie']
headers['Upgrade-Insecure-Requests'] = '1'
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
headers['Accept-Encoding'] = 'gzip, deflate'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
headers['Referer'] = 'http://www.swsindex.com/downloadfiles.aspx?swindexcode=SwClass&type=530&columnid=8892'

resp = requests.get("http://www.swsindex.com/downloadfiles.aspx?swindexcode=SwClass&type=530&columnid=8892",
    headers=headers)

with open("SwClass.xls", "wb") as code:
	code.write(resp.content)