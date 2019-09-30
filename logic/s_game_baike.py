# -*- coding: utf-8 -*-
# @Time    : 19-8-26 上午10:59
# @Author  : Redtree
# @File    : s_game_baike.py
# @Desc :  游戏中位于百科页面


from logic import loader
from data import player_runtime
from data.heros import hrs
import pygame
from data import color_rgb


def dojob(x,y,is_mouse_down):
    # 绘制基础底板
    loader.screen.blit(loader.BAIKE_SHOW, (480, 0))
    loader.screen.blit(loader.BAIKE_SELECT, (0, 0))
    loader.screen.blit(loader.BAIKE_BACK, (960, 0))

    rsx = 0
    rsy = 0
    # 绘制所有英雄
    for img in loader.RMS:
        ci = pygame.transform.scale(img[0], (120, 170))
        loader.screen.blit(ci, (rsx * 120, rsy * 170))
        rsx = rsx + 1
        if rsx > 3:
            rsx = 0
            rsy = rsy + 1

    # 绘制英雄选择位置 hero_index
    hidx = -1
    hidy = -1
    if x >= 0 and x < 120:
        hidx = 0
    elif x >= 120 and x < 240:
        hidx = 1
    elif x >= 240 and x < 360:
        hidx = 2
    elif x >= 360 and x < 480:
        hidx = 3

    if y >= 0 and y < 170:
        hidy = 0
    elif y >= 170 and y < 340:
        hidy = 1
    elif y >= 340 and y < 510:
        hidy = 2
    elif y >= 510 and y < 680:
        hidy = 3

    if hidx in [0, 1, 2, 3] and hidy in [0, 1, 2, 3]:
        sf = pygame.transform.scale(loader.SELECT_FIRE, (160, 240))
        loader.screen.blit(sf, (hidx * 120 - 20, hidy * 170 - 30))

        # 获取当前英雄位置
        hid = hidy * 4 + hidx
        # 读取当前英雄数据
        cr_data = hrs.DATA[hid]
        # 名称
        cr_name = cr_data['name']
        # 攻击
        cr_attack = cr_data['attack']
        # 防御
        cr_defend = cr_data['defend']
        # 初始血量
        cr_hp = cr_data['hp']
        # 绝招
        cr_skill = cr_data['skill']
        # 介绍
        cr_desc = cr_data['desc']
        # 接续数据到面板
        # 名称
        hrname = loader.BAIKE_FONT.render(cr_name, True, color_rgb.BLACK,
                                          None)
        loader.screen.blit(hrname, (640, 20))
        # 简介
        hrdesc = loader.BAIKE_FONT.render('"' + cr_desc + '"', True, color_rgb.BLACK,
                                          None)
        loader.screen.blit(hrdesc, (500, 50))
        # 攻击力
        attack_icon = pygame.transform.scale(loader.ATTACK, (45, 40))
        loader.screen.blit(attack_icon, (500, 90))
        loader.screen.blit(loader.VALUE_EMPTY, (550, 90))
        for sb in range(0, cr_attack):
            loader.screen.blit(loader.VALUE_GET, (550 + sb * 34, 90))

        hrattack = loader.BAIKE_FONT.render(str(cr_attack), True, color_rgb.BLACK,
                                            None)
        loader.screen.blit(hrattack, (895, 90))
        # 防御力
        defend_icon = pygame.transform.scale(loader.DEFEND, (45, 40))
        loader.screen.blit(defend_icon, (500, 130))
        loader.screen.blit(loader.VALUE_EMPTY, (550, 130))
        for sb in range(0, cr_defend):
            loader.screen.blit(loader.VALUE_GET, (550 + sb * 34, 130))

        hrattack = loader.BAIKE_FONT.render(str(cr_defend), True, color_rgb.BLACK,
                                            None)
        loader.screen.blit(hrattack, (895, 130))
        # 初始血量
        hp_icon = pygame.transform.scale(loader.HEART, (45, 40))
        loader.screen.blit(hp_icon, (500, 170))
        loader.screen.blit(loader.VALUE_EMPTY, (550, 170))
        for sb in range(0, cr_hp):
            loader.screen.blit(loader.VALUE_GET, (550 + sb * 34, 170))

        hrattack = loader.BAIKE_FONT.render(str(cr_hp), True, color_rgb.BLACK,
                                            None)
        loader.screen.blit(hrattack, (895, 170))
        # 技能说明
        skill_icon = pygame.transform.scale(loader.SKILL, (45, 40))
        loader.screen.blit(skill_icon, (500, 210))
        # 遍历每行
        cs_index = 0
        for cs in cr_skill:
            if cs_index == 0:
                skill_title = loader.BAIKE_FONT.render(cs, True, color_rgb.BLACK,
                                                       None)
                loader.screen.blit(skill_title, (550, 210))
            else:
                csi = loader.BAIKE_FONT.render(cs, True, color_rgb.BLACK,
                                               None)
                loader.screen.blit(csi, (510, 250 + 40 * (cs_index - 1)))
            cs_index = cs_index + 1

    # 绘制退出按钮
    if x >= 960 and x < 1040 and y >= 320 and y < 360:
        loader.screen.blit(loader.BAIKE_BACK_BUT2, (960, 320))
        if is_mouse_down == True:
            player_runtime.INFO['inbaike'] = False
    else:
        loader.screen.blit(loader.BAIKE_BACK_BUT1, (960, 320))


