#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='12.12.11.137'))
chan = conn.channel()
chan.exchange_declare(exchange='logs', type='finout')

# 创建随机队列
result = chan.queue_declare(exclusive=True)
queue_name = result.method.queue

# 消息队列绑定exchange
chan.queue_bind(exchange='logs', queue=queue_name)

print("[x] Waiting for logs. To exit press CTRL+C.")

def callbak(ch, method, properties, body):
    print("[x] %r" % body)

chan.basic_consume(callbak, queue=queue_name, no_ack=True)

chan.start_consuming()