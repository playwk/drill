#Author ZhengZhong,Jiang

import zipfile

z = zipfile.ZipFile('test.zip', 'a')
z.write('__init__.py')
z.write('s1.py')
z.close()


zi = zipfile.ZipFile('test.zip', 'r')
zi.extractall()

for i in zi.namelist():
    print(i, type(i))
za = zipfile.ZipFile('test.zip', 'r')
zi.extract('s1.py')
