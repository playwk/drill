#Author ZhengZhong,Jiang
import pickle
cast=['name','sex','age']
print(cast.count('addr'))
with open('tst.txt', 'r+') as f:
    old=f.read()
    f.seek(0)
    f.write("new line\n" + old)