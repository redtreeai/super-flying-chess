# -*- coding: utf-8 -*-
# @Time    : 19-6-17 下午5:12
# @Author  : Redtree
# @File    : eventer.py
# @Desc : 所有事件的主驱动



import pygame
import sys
from logic import loader
from logic import s_title,s_game
from data import title_page,game_page
from data import player_runtime
import time

# 创建时钟对象 (可以控制游戏循环频率)
clock = pygame.time.Clock()

while 1:

    #监听鼠标是否点击
    is_mouse_down = False
    #键盘

    keys={
        'tab':0,
        '1':0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0
    }

    #监听鼠标点位置
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_down = True
        else:
            is_mouse_down = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.key == pygame.K_TAB:
                keys['tab'] = 1
            else:
                keys['tab'] = 0

            #筛子作弊按键
            if event.key == pygame.K_1:
                keys['1'] = 1
            else:
                keys['1'] = 0
            if event.key == pygame.K_2:
                keys['2'] = 1
            else:
                keys['2'] = 0
            if event.key == pygame.K_3:
                keys['3'] = 1
            else:
                keys['3'] = 0
            if event.key == pygame.K_4:
                keys['4'] = 1
            else:
                keys['4'] = 0
            if event.key == pygame.K_5:
                keys['5'] = 1
            else:
                keys['5'] = 0
            if event.key == pygame.K_6:
                keys['6'] = 1
            else:
                keys['6'] = 0
            if event.key == pygame.K_SPACE:
                pygame.image.save(loader.screen,'show/'+str(int(time.time()))+'.png')

    # # 持续按住的事件处理
    # key_pressed = pygame.key.get_pressed()
    # if key_pressed[pygame.K_TAB]:
    #     keys['tab'] = 1

    if loader.curs_code == title_page.SCODE:
        if player_runtime.MUSIC['title']==False:
            loader.TITLE_SOUND.play(-1)
            player_runtime.MUSIC['title'] = True
        s_title.dojob(x,y,is_mouse_down,keys)
    elif loader.curs_code == game_page.SCODE:
        if player_runtime.MUSIC['title'] == True:
            loader.TITLE_SOUND.stop()
        s_game.dojob(x,y,is_mouse_down,keys)

    player_runtime.INFO['gclock'] = player_runtime.INFO['gclock'] +1
    pygame.display.update()
    # 通过时钟对象指定循环频率
    clock.tick(60)  # 每秒循环60次