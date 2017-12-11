#!/bin/bash
#date:2017-11-23 
#author:张守祝
#discribe:mysql status

#disk status
masterip=12.12.12.128
user=sync
password=sync
dir=/var/lib/mysql/
masterper=`df $dir|awk '/mapper/{print $5}'`
echo -e "[master$masterip]"
echo "DatadirStatu=$dir $masterper%"
#master mysql status
#mysql -u$user -p$password -h$masterip -e'status'|awk '/Thread/{print $1,$2}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$masterip -e'status'|awk '/Question/{print $3,$4}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$masterip -e'status'|awk '/Slow queries/{print $5,$6,$7}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$masterip -e'status'|awk '/Opens:/{print $8,$9}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$masterip -e'status'|awk '/Flush tables:/{print $10,$11,$12}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$masterip -e'status'|awk '/Open tables/{print $13,$14,$15}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$masterip -e'status'|awk '/Queries per second avg:/{print $16,$17,$18,$19,$20}'|awk -F':' '{print $1"="$2}'

#mysql status
mysql -u$user -p$password -h$masterip -e'status'|awk '/^Threads:/{print "Status="$0}'

#mysql uptime
mysql -u$user -p$password -h$masterip -e'status'|awk '/Uptime/{print $0}'|awk -F':' '{print $1"="$2}'|awk '{print $1,$2,$3,$4,$5,$6,$7}'

#数据库数据量
#dbs=`mysql -u$user -p$password -h$masterip -e'show databases;'|sed '1d'`
dbs=("zabbix")
for db in $dbs
do
        dbsize=`mysql -u$user -p$password -h$masterip -e"SELECT sum(DATA_LENGTH)+sum(INDEX_LENGTH) FROM information_schema.TABLES where TABLE_SCHEMA='$db'"|sed -n '2p'`
        #echo -n "$db " ;echo "scale=4;$dbsize/1048576"|awk '{print $1/$2}'
        echo -n "$db=" ; echo $dbsize 1048576|awk '{printf "%.4f\n",$1/$2}'
done
#当前连接数

conns=`mysql -u$user -p$password -h $masterip -e'show full processlist'|sed '1d'|wc -l`
echo "CurrentConn=$conns"

#历史最大连接数
mysql -u$user -p$password -h $masterip -e'show status'|awk '/^Max_used_connections/{print $1"="$2}'
###########################################################

#slaveip=192.168.136.137
#user=tom
#password=123
#dir=/var/lib/mysql/
#slaveper=`ssh $slaveip df $dir|awk '/mapper/{print $5}'`
#echo -e  "\033[41;37m [slave$slaveip]\033[0m"
#echo "DataDir=$dir"
#echo "DataSpaceUsed=$slaveper"
##slave mysql status
#mysql -u$user -p$password -h$slaveip -e'status'|awk '/Thread/{print $1,$2}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$slaveip -e'status'|awk '/Question/{print $3,$4}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$slaveip -e'status'|awk '/Slow queries/{print $5,$6,$7}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$slaveip -e'status'|awk '/Opens:/{print $8,$9}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$slaveip -e'status'|awk '/Flush tables:/{print $10,$11,$12}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$slaveip -e'status'|awk '/Open tables/{print $13,$14,$15}'|awk -F':' '{print $1"="$2}'
#mysql -u$user -p$password -h$slaveip -e'status'|awk '/Queries per second avg:/{print $16,$17,$18,$19,$20}'|awk -F':' '{print $1"="$2}'
##mysql uptime
#mysql -u$user -p$password -h$slaveip -e'status'|awk '/Uptime/{print $0}'|awk -F':' '{print $1"="$2}'|awk '{print $1,$2,$3,$4,$5,$6,$7}'
##数据库数据量
#dbs=`mysql -u$user -p$password -h$slaveip -e'show databases;'|sed '1d'`
#for db in $dbs
#do
#        dbsize=`mysql -u$user -p$password -h$slaveip -e"SELECT sum(DATA_LENGTH)+sum(INDEX_LENGTH) FROM information_schema.TABLES where TABLE_SCHEMA='$db'"|sed -n '2p'`
#        #echo  -n "$db " ;echo "scale=4;$dbsize/1048576"|bc
#        echo -n "$db=" ; echo $dbsize 1048576|awk '{printf "%.4f\n", $1/$2}'
#done
#
##当前连接数
#conns=`mysql -u$user -p$password -h $slaveip -e'show full processlist'|sed '1d'|wc -l`
#echo "CurrentConn=$conns"
