#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters(host='12.12.11.140'))
channel = conn.channel()

channel.queue_declare(queue='m')


def callbak(ch, method, properties, body):
    print('[x] receivd %r' % body)

channel.basic_consume(callbak, queue='m', no_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
