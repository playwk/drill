#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

import redis

class redisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='12.12.11.140')

    def public(self, msg, chan):
        self.__conn.publish(chan, msg)
        return True

    def subscribe(self, chan):
        pub = self.__conn.pubsub()
        pub.subscribe(chan)
        pub.parse_response()
        return pub
