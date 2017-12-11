# Auther: ZhengZhong,Jiang

import tarfile

#压缩功能
# t = tarfile.TarFile('demo.tar', 'w')
# t.add('xo.xml')
# t.add('xxoo.xml')
# t.close()
#
# t = tarfile.TarFile('demo.tar', 'a')
# t.add('configparser.info')
# t.close()

t = tarfile.TarFile('demo.tar', 'r')
for i in t.getmembers():
    print(i, type(i))

obj = t.getmember('xo.xml')
t.extract(obj)
t.close()