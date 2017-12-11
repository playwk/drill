#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

import s03

obj = s03.redisHelper()
data = obj.subscribe('fm103.7')
print(data.parse_response())
