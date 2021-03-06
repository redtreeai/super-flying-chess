# -*- coding: utf-8 -*-
# @Time    : 19-8-26 下午5:03
# @Author  : Redtree
# @File    : routes.py
# @Desc :

DATA = {
    #'位于基地的路线'
    'base':[
        #基地
        ((0, 0), (0, 2)),
        ((0, 1), (0, 2)),
        ((1, 0), (0, 2)),
        ((1, 1), (0, 2)),
        ((11, 0), (10, 0)),
        ((12, 0), (10, 0)),
        ((11, 1), (10, 0)),
        ((12, 1), (10, 0)),
        ((0, 11), (2, 12)),
        ((1, 11), (2, 12)),
        ((0, 12), (2, 12)),
        ((1, 12), (2, 12)),
        ((11, 11), (12, 10)),
        ((12, 11), (12, 10)),
        ((11, 12), (12, 10)),
        ((12, 12), (12, 10))
    ],
    # 普通地图块
    'common':[
              #普通路线
              ((0, 3), (1, 3)),
              ((1, 3), (2, 3)),
              ((2, 3), (3, 3)),
              ((3, 3), (3, 2)),
              ((3, 2), (3, 1)),
              ((3, 1), (3, 0)),
              ((3, 0), (4, 0)),
              ((4, 0), (5, 0)),
              ((5, 0), (6, 0)),
              ((6, 0), (7, 0)),
              ((7, 0), (8, 0)),
              ((8, 0), (9, 0)),
              ((9, 0), (9, 1)),
              ((9, 1), (9, 2)),
              ((9, 2), (9, 3)),
              ((9, 3), (10, 3)),
              ((10, 3), (11, 3)),
              ((11, 3), (12, 3)),
              ((12, 3), (12, 4)),
              ((12, 4), (12, 5)),
              ((12, 5), (12, 6)),
              ((12, 6), (12, 7)),
              ((12, 7), (12, 8)),
              ((12, 8), (12, 9)),
              ((12, 9), (11, 9)),
              ((11, 9), (10, 9)),
              ((10, 9), (9, 9)),
              ((9, 9), (9, 10)),
              ((9, 10), (9, 11)),
              ((9, 11), (9, 12)),
              ((9, 12), (8, 12)),
              ((8, 12), (7, 12)),
              ((7, 12), (6, 12)),
              ((6, 12), (5, 12)),
              ((5, 12), (4, 12)),
              ((4, 12), (3, 12)),
              ((3, 12), (3, 11)),
              ((3, 11), (3, 10)),
              ((3, 10), (3, 9)),
              ((3, 9), (2, 9)),
              ((2, 9), (1, 9)),
              ((1, 9), (0, 9)),
              ((0, 9), (0, 8)),
              ((0, 8), (0, 7)),
              ((0, 7), (0, 6)),
              ((0, 6), (0, 5)),
              ((0, 5), (0, 4)),
              ((0, 4), (0, 3)),
               # 出战点   倒退的时候优先结算非出战点
              ((0, 2), (0, 3)),
              ((10, 0), (9, 0)),
              ((2, 12), (3, 12)),
              ((12, 10), (12, 9))
              ],
    #跳跃地图块
    'jumps_common':[
        #飞机
        ((3, 3), (9, 3)),
        ((9, 3), (9, 9)),
        ((9, 9), (3, 9)),
        ((3, 9), (3, 3)),
    ],

    # 颜色跳跃
    # 红
    'jumps_red':[
        ((0, 3), (3, 1)),
        ((3, 1), (7, 0)),
        ((7, 0), (9, 1)),
        ((9, 1), (12, 3)),
        ((12, 3), (12, 8)),
        ((12, 8), (10, 9)),
        ((10, 9), (8, 12)),
        ((8, 12), (2, 9)),
        ((2, 9), (0, 7)),
    ],
    'jumps_green': [
        # 绿
        ((12, 9), (9, 11)),
        ((9, 11), (5, 12)),
        ((5, 12), (3, 11)),
        ((3, 11), (0, 9)),
        ((0, 9), (0, 4)),
        ((0, 4), (2, 3)),
        ((2, 3), (4, 0)),
        ((4, 0), (10, 3)),
        ((10, 3), (12, 5)),

    ],
    'jumps_blue': [
        #蓝
        ((3, 12), (1, 9)),
        ((1, 9), (0, 5)),
        ((0, 5), (1, 3)),
        ((1, 3), (3, 0)),
        ((3, 0), (8, 0)),
        ((8, 0), (9, 2)),
        ((9, 2), (12, 4)),
        ((12, 4), (9, 10)),
        ((9, 10), (7, 12)),],
    #
    'jumps_yellow': [
        ((9, 0), (11, 3)),
        ((11, 3), (12, 7)),
        ((12, 7), (11, 9)),
        ((11, 9), (9, 12)),
        ((9, 12), (4, 12)),
        ((4, 12), (3, 10)),
        ((3, 10), (0, 8)),
        ((0, 8), (3, 2)),
        ((3, 2), (5, 0)),
    ],

    #提前锁定的线路
    'special_red':[
        (0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6)
    ],
    'special_yellow': [
        (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)
    ],
    'special_blue': [
        (6, 12), (6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6)
    ],
    'special_green': [
        (12, 6), (11, 6), (10, 6), (9, 6), (8, 6), (7, 6), (6, 6)
    ]


}