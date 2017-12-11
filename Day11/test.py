#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang


import memcache


mc = memcache.Client(['12.12.11.137:11211'], debug=True, )
mc.set('num', 500)
print(mc.get('num'))



