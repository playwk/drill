#coding=utf-8
import httplib2  

h = httplib2.Http(".cache") 

#下载沪深300成份股
resp, content = h.request("http://115.29.204.48/webdata/000300cons.xls", "GET")
with open("000300cons.xls","wb") as code:
	code.write(content)

#下载沪深300成份股权重
resp, content = h.request("http://115.29.204.48/webdata/000300closeweight.xls", "GET")
with open("000300closeweight.xls","wb") as code:
	code.write(content)

#下载中证500成份股
resp, content = h.request("http://115.29.204.48/webdata/000905cons.xls", "GET")
with open("000905cons.xls","wb") as code:
	code.write(content)

#下载中证500成份股权重
resp, content = h.request("http://115.29.204.48/webdata/000905closeweight.xls", "GET")
with open("000905closeweight.xls","wb") as code:
	code.write(content)

#下载上证50成份股
resp, content = h.request("http://115.29.204.48/webdata/000016cons.xls", "GET")
with open("000016cons.xls","wb") as code:
	code.write(content)

headers = {'Connection': 'keep-alive'} 
resp, content = h.request("http://www.swsindex.com/downloadfiles.aspx?swindexcode=SwClass&type=530&columnid=8892",
    "GET", headers=headers)

headers['Cookie'] = resp['set-cookie']
headers['Upgrade-Insecure-Requests'] = '1'
headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
headers['Accept-Encoding'] = 'gzip, deflate'
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
headers['Referer'] = 'http://www.swsindex.com/downloadfiles.aspx?swindexcode=SwClass&type=530&columnid=8892'

resp, content = h.request("http://www.swsindex.com/downloadfiles.aspx?swindexcode=SwClass&type=530&columnid=8892",
    "GET", headers = headers) 

with open("SwClass.xls", "wb") as code:
	code.write(content)