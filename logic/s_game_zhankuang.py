# -*- coding: utf-8 -*-
# @Time    : 19-8-26 上午10:59
# @Author  : Redtree
# @File    : s_game_zhankuang.py
# @Desc :  游戏中位于战况


import pygame
from logic import loader
from data import player_runtime
from data import title_page
from data import color_rgb


def dojob(x,y,is_mouse_down,keys):
    # 绘制基础底板
    loader.screen.blit(loader.ZKS, (0, 0))
    loader.screen.blit(loader.BAIKE_BACK, (960, 0))

    #绘制英雄实时数据
    rsx = 0
    rsy = 0


    # 绘制所有英雄
    for zz in player_runtime.INFO['zdata']:
        for z in zz:
            img = loader.RMS[z['code']][0]
            ci = pygame.transform.scale(img, (120, 170))
            loader.screen.blit(ci, (rsx * 120, rsy * 340))

            #绘制其他信息
            chp = str(z['hp'])
            cat = str(z['attack'])
            defend = str(z['defend'])
            tag = '基地'
            if z['in_war']==True:
                tag = '战场'
            if z['gowin']==True:
                tag = '核心'

            #爱心
            hp_icon = pygame.transform.scale(loader.HEART, (45, 40))
            loader.screen.blit(hp_icon, (rsx * 120+20, rsy * 340+190))
            #血量
            chp_text = loader.GAME_TEXT_FONT.render(chp, True, color_rgb.WHITE,
                                              None)
            loader.screen.blit(chp_text, (rsx * 120+60, rsy * 340+200))

            # 攻击力
            atk_icon = pygame.transform.scale(loader.ATTACK, (45, 40))
            loader.screen.blit(atk_icon, (rsx * 120 + 20, rsy * 340 + 240))
            atk_text = loader.GAME_TEXT_FONT.render(cat, True, color_rgb.WHITE,
                                                    None)
            loader.screen.blit(atk_text, (rsx * 120 + 60, rsy * 340 + 240))

            # 防御力
            defend_icon = pygame.transform.scale(loader.DEFEND, (45, 40))
            loader.screen.blit(defend_icon, (rsx * 120 + 20, rsy * 340 + 280))
            defend_text = loader.GAME_TEXT_FONT.render(defend, True, color_rgb.WHITE,
                                                    None)
            loader.screen.blit(defend_text, (rsx * 120 + 60, rsy * 340 + 280))

            #基地/出战/抵达核心

            tag_text = loader.GAME_TEXT_FONT.render(tag, True, color_rgb.RED,
                                                    None)
            loader.screen.blit(tag_text, (rsx * 120, rsy * 340))

            rsx = rsx + 1
            if rsx > 7:
                rsx = 0
                rsy = rsy + 1


    # 绘制退出按钮
    if x >= 960 and x < 1040 and y >= 320 and y < 360:
        loader.screen.blit(loader.BAIKE_BACK_BUT2, (960, 320))
        if is_mouse_down == True:
            if player_runtime.INFO['gameover']==False:
                player_runtime.INFO['inzhankuang'] = False
            else:
                loader.curs_code = title_page.SCODE
    else:
        loader.screen.blit(loader.BAIKE_BACK_BUT1, (960, 320))

    #判断是否按tab
    if keys['tab']==1:
        if player_runtime.INFO['gameover'] == False:
            player_runtime.INFO['inzhankuang'] = False
        else:
            loader.curs_code = title_page.SCODE


