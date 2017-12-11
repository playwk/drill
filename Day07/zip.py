# Auther: ZhengZhong,Jiang

import zipfile

#压缩功能
# z = zipfile.ZipFile('demo.zip', 'w')
# z.write('xo.xml')
# z.write('xxoo.xml')
# # z.close()
#
# # z = zipfile.ZipFile('demo.zip', 'w')
# z.write('configparser.info')
# z.close()

#解压功能
z = zipfile.ZipFile('demo.zip', 'r')
# for i in z.namelist():
#     print(i,type(i))

z.extract('xo.xml')
z.extractall()
z.close()

