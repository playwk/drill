#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

import pika
import sys

conn = pika.BlockingConnection(pika.ConnectionParameters(host='12.12.11.137'))
chan = conn.channel()
chan.exchange_declare(exchange='logs', type='fanout')

# message = ' '.join(sys.argv[1:]) or 'info: Hello World!'
message = 'hello! '
chan.basic_publish(exchange='logs', routing_key='', body=message)
print("[x] Send %r" % message)
conn.close()
