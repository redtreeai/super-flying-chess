# -*- coding: utf-8 -*-
# @Time    : 19-7-5 下午4:46
# @Author  : Redtree
# @File    : timer.py
# @Desc :

import time
from data import player_runtime


#获取毫秒级时间戳
def get_mtime():
    t = time.time()
    return int(round(t * 1000))


#获取秒级别时间戳
def get_stime():
    return int(time.time())


#获取游戏世界时间
def get_clock():
    return player_runtime.INFO['gclock']

