#Author ZhengZhong,Jiang

import tarfile

t = tarfile.TarFile('test.tar', 'w')
t.add('s1.py', arcname='ss1.py')
t.add('s2.py', arcname='ss2.py')
t.close()

t = tarfile.TarFile('test.tar', 'r')
for i in t:
    print(i)
t.extractall()
obj = t.getmember('ss2.py')
t.extract(obj)
t.close()
