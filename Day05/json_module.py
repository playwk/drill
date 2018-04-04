# Auther: ZhengZhong,Jiang

import json

di = {'k1': 'v1'}

result = json.dumps(di)
print(result,type(result))



st = '{"k1":"v1"}'

result = json.loads(st)
print(result,type(result))



