#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='12.12.11.140'))

channel = conn.channel()

channel.queue_declare(queue='m')

channel.basic_publish(exchange='', routing_key='m', body='Hello World!')

print("[x] Send 'Hello World!'")

conn.close()
