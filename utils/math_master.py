# -*- coding: utf-8 -*-
# @Time    : 19-7-4 下午2:14
# @Author  : Redtree
# @File    : math_master.py
# @Desc : 数学运行函数集


#求两点的距离
def check_distance(pos1,pos2):
    x_distance =abs(pos1[0]-pos2[0])
    y_distance =abs(pos1[1]-pos2[1])
    distance = int((x_distance*x_distance+y_distance*y_distance)**0.05)
    return distance