# Auther: ZhengZhong,Jiang


import json,requests


response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
response.encoding = 'utf-8'

# print(response.text, type(response.text))

dic = json.loads(response.text)

# print(dic, type(dic))


json.dump(dic,open('info.db', 'w'))
info = json.load(open('info.db', 'r'))
print(info)