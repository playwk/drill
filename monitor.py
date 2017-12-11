# -*- coding: utf-8 -*-
# @author ZhengZhong,Jiang
# @time 2017/12/4 16:42

import subprocess
import pymysql

def mysql_cmd():
    dbConn = pymysql.connect(
        host='12.12.12.128',
        port=3306,
        user='sync',
        password='sync',
    )

    cursor = dbConn.cursor()

    sql = 'show status where variable_name in ("Aborted_clients", "Bytes_received", "Compression")'

    cursor.execute(sql)
    result = cursor.fetchall()
    # for line in result:
    print(result)


def shell_cmd():
    stauts = subprocess.Popen("mysql -h 12.12.12.128 -usync -psync -e'status'", shell=True,
                              stdout=subprocess.PIPE)
    result = stauts.communicate()
    for line in result:
        print(line)

shell_cmd()

