# -*- coding: utf-8 -*-
# @Time    : 19-7-10 下午5:18
# @Author  : Redtree
# @File    : name_creator.py
# @Desc : 名字创造器


import random

def get_name():
    name_list1 = ['绝望的','邪恶的','可爱的','高大的','爱哭的','胆小的','帅气的','很皮的','坏的很的','美丽的']
    name_list2 = ['冬瓜','红薯','番茄','田亮','山姆','莎莉','波波','皮蛋','蓝牛','妞妞','臭姐','和夫']
    return random.choice(name_list1)+random.choice(name_list2)