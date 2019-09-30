# -*- coding: utf-8 -*-
# @Time    : 19-7-w15 上午11:40
# @Author  : Redtree
# @File    : saver.py
# @Desc :  游戏存档操作


import pickle
import time
import pygame
import os


'''
这是存档格式数据  0代表没有存档

SDATA = {
    'slot1':'null',
    'slot2':'null',
    'slot3':'null'
}
'''


#读取存档列表
def read_sd():

    try:
        f = open('save/tsd.pkl', 'rb')
        pd = pickle.load(f)
        f.close()
        res = []

        t1 = pd['slot1']
        t2 = pd['slot2']
        t3 = pd['slot3']

        if t1 == 'null':
            cobj1 = {'img_path': '', 'date': '', 'round': '存档为空'}
        else:
            ct = str(t1).split('a')[0]
            cr = str(t1).split('a')[1]
            date = transtime(int(ct))
            cr = '第' + cr + '回合'
            img_res = pygame.image.load('save/slot1.jpg')
            img_res = pygame.transform.scale(img_res,(300,180))
            cobj1 = {'img_path': 'save/slot1.jpg', 'date': date, 'round': cr,'img_res':img_res}

        if t2 == 'null':
            cobj2 = {'img_path': '', 'date': '', 'round': '存档为空'}
        else:
            ct = str(t2).split('a')[0]
            cr = str(t2).split('a')[1]
            date = transtime(int(ct))
            cr = '第' + cr + '回合'
            img_res = pygame.image.load('save/slot2.jpg')
            img_res = pygame.transform.scale(img_res, (300, 180))
            cobj2 = {'img_path': 'save/slot2.jpg', 'date': date, 'round': cr,'img_res':img_res}

        if t3 == 'null':
            cobj3 = {'img_path': '', 'date': '', 'round': '存档为空'}
        else:
            ct = str(t3).split('a')[0]
            cr = str(t3).split('a')[1]
            date = transtime(int(ct))
            cr = '第' + cr + '回合'
            img_res = pygame.image.load('save/slot1.jpg')
            img_res = pygame.transform.scale(img_res, (300, 180))
            cobj3 = {'img_path': 'save/slot3.jpg', 'date': date, 'round': cr,'img_res':img_res}

        res.append(cobj1)
        res.append(cobj2)
        res.append(cobj3)

        return res
    except Exception as err:
        print(err)
        erres = [{'img_path': '', 'date': '', 'round': '无法存档'},
                 {'img_path': '', 'date': '', 'round': '无法存档'},
                 {'img_path': '', 'date': '', 'round': '无法存档'}]
        return erres


#存档
def save(info,save_path):
    try:
        f = open(save_path, 'wb')
        pickle.dump(info,f)
        f.close()
        return True
    except Exception as err:
        print(err)
        return False


#载入存档
def load(save_path):
    try:
        f = open(save_path,'rb')
        return pickle.load(f)
    except Exception as err:
        print(err)
        return False


#获取当前时间
def get_time():
    return int(time.time())


#时间戳转日期
def transtime(t):
    ta = time.localtime(t)
    ot = time.strftime("%Y-%m-%d %H:%M:%S", ta)
    return ot


#打包前要重置
#重置存档

# SDATA = {
#     'slot1':'null',
#     'slot2':'null',
#     'slot3':'null'
# }
# save(SDATA,'../save/tsd.pkl')