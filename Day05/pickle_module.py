# Auther: ZhengZhong,Jiang

import pickle

li = [11, 22, 33]

result = pickle.dumps(li)
print(result)


result2 = pickle.loads(result)
print(result2)


pickle.dump(li, open('info2.db', 'wb'))

result3 = pickle.load(open('info2.db', 'rb'))

print(result3)