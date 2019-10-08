# -*- coding: utf-8 -*-
# @Time    : 19-8-28 上午9:53
# @Author  : Redtree
# @File    : s_game_play_base.py
# @Desc : 每帧游戏的基础绘制方案（玩家操作逻辑前）


from logic import loader
from data import map_set
from data import color_rgb
import pygame
from data import player_runtime
from utils import timer


def dojob():
    # 游戏过程
    # 绘制基础底板
    loader.screen.fill(color_rgb.WHITE)
    #loader.screen.blit(loader.BG2, (0,0))

    loader.screen.blit(loader.BOARD4, (860, 0))
    loader.screen.blit(loader.BOARD3, (860, 170))
    loader.screen.blit(loader.BOARD2, (860, 340))
    loader.screen.blit(loader.BOARD1, (860, 510))

    # 绘制地图  118  56   624
    map_sx = 118
    map_sy = 56

    map_data = map_set.DATA
    mx = 0
    my = 0
    for md in map_data:
        if md == 0:
            pass
        else:
            loader.screen.blit(loader.MAPS[md], (map_sx + mx * 48, map_sy + my * 48))

        mx = mx + 1
        if mx > 12:
            mx = 0
            my = my + 1

    # 判断当前玩家队伍,绘制操纵区的边框
    if player_runtime.INFO['turn'] == 0:
        loader.screen.blit(loader.CONTROL_BLUE, (860, 510))
        if player_runtime.INFO['pa_turn'][0]==0:
            turn_text = '玩家'
        else:
            turn_text = 'AI'
        tag_blue = loader.GAME_ROUND_FONT.render(turn_text, True,
                                                 color_rgb.BLUE,
                                                 None)
        loader.screen.blit(tag_blue, (10, 48))
    elif player_runtime.INFO['turn'] == 1:
        loader.screen.blit(loader.CONTROL_GREEN, (860, 510))
        if player_runtime.INFO['pa_turn'][1] == 0:
            turn_text = '玩家'
        else:
            turn_text = 'AI'
        tag_blue = loader.GAME_ROUND_FONT.render(turn_text, True,
                                                 color_rgb.GREEN,
                                                 None)
        loader.screen.blit(tag_blue, (10, 48))
    elif player_runtime.INFO['turn'] == 2:
        loader.screen.blit(loader.CONTROL_YELLOW, (860, 510))
        if player_runtime.INFO['pa_turn'][2] == 0:
            turn_text = '玩家'
        else:
            turn_text = 'AI'
        tag_blue = loader.GAME_ROUND_FONT.render(turn_text, True,
                                                 color_rgb.YELLOW,
                                                 None)
        loader.screen.blit(tag_blue, (10, 48))
    elif player_runtime.INFO['turn'] == 3:
        loader.screen.blit(loader.CONTROL_RED, (860, 510))
        if player_runtime.INFO['pa_turn'][3] == 0:
            turn_text = '玩家'
        else:
            turn_text = 'AI'
        tag_blue = loader.GAME_ROUND_FONT.render(turn_text, True,
                                                 color_rgb.RED,
                                                 None)
        loader.screen.blit(tag_blue, (10, 48))


    '''
    绘制完地图绘制棋子,目前没添加AI，所以根据玩家数量填充棋子(后续根据移动方向绘制动作和和朝向)
    '''

    zdata = player_runtime.INFO['zdata']
    zsd = reset_role_list(zdata)

    for z in zsd:
        if z['gowin'] == True:
            pass
        else:
            z_px = z['px']
            z_py = z['py']

            # 如果是移动状态，则根据朝向播放帧序列图片,目前测试猎人
            if player_runtime.INFO['stage'] == 2 and z['code'] == player_runtime.INFO['moving_code']:
                # 获取猎人的移动资源
                cres = check_tik(z['code'], z['faceto'])
                c_img = pygame.transform.scale(cres, (48, 96))
                loader.screen.blit(c_img, (map_sx + int(z_px * 48), map_sy + int((z_py - 1) * 48)))

            else:
                # 绘制人物
                z_res = check_tik(z['code'], z['faceto'], 1)
                z_img = pygame.transform.scale(z_res, (48, 96))
                loader.screen.blit(z_img, (map_sx + int(z_px * 48), map_sy + int((z_py - 1) * 48)))

            #######################这部分暂时保留
            # 绘制基础信息
            chp = str(z['hp'])
            cat = str(z['attack'])
            cdf = str(z['defend'])

            chp_i = pygame.transform.scale(loader.HEART, (8, 8))
            cat_i = pygame.transform.scale(loader.ATTACK, (8, 8))
            cdf_i = pygame.transform.scale(loader.DEFEND, (8, 8))

            loader.screen.blit(chp_i, (map_sx + int(z_px * 48), map_sy + int((z_py - 1) * 48) - 8))
            loader.screen.blit(cat_i, (map_sx + int(z_px * 48) + 16, map_sy + int((z_py - 1) * 48) - 8))
            loader.screen.blit(cdf_i, (map_sx + int(z_px * 48) + 32, map_sy + int((z_py - 1) * 48) - 8))

            chp_w = loader.GAME_TEXT_FONT_SM.render(chp, True,
                                                    color_rgb.BLACK,
                                                    None)
            cat_w = loader.GAME_TEXT_FONT_SM.render(cat, True,
                                                    color_rgb.BLACK,
                                                    None)
            cdf_w = loader.GAME_TEXT_FONT_SM.render(cdf, True,
                                                    color_rgb.BLACK,
                                                    None)
            loader.screen.blit(chp_w, (map_sx + int(z_px * 48) + 8, map_sy + int((z_py - 1) * 48) - 8))
            loader.screen.blit(cat_w, (map_sx + int(z_px * 48) + 24, map_sy + int((z_py - 1) * 48) - 8))
            loader.screen.blit(cdf_w, (map_sx + int(z_px * 48) + 40, map_sy + int((z_py - 1) * 48) - 8))

    # zdata = player_runtime.INFO['zdata']
    # for zd in zdata:
    #     if len(zd) == 0:
    #         pass
    #     else:
    #         for z in zd:
    #             if z['gowin']==True:
    #                 pass
    #             else:
    #                 z_px = z['px']
    #                 z_py = z['py']
    #
    #                 #如果是移动状态，则根据朝向播放帧序列图片,目前测试猎人
    #                 if player_runtime.INFO['stage']==2 and z['code']==player_runtime.INFO['moving_code'] :
    #                     #获取猎人的移动资源
    #                     cres = check_tik(z['code'],z['faceto'])
    #                     c_img = pygame.transform.scale(cres, (48, 96))
    #                     loader.screen.blit(c_img, (map_sx + int(z_px * 48), map_sy + int((z_py - 1) * 48)))
    #
    #                 else:
    #                     #绘制人物
    #                     z_res = check_tik(z['code'],z['faceto'],1)
    #                     z_img = pygame.transform.scale(z_res, (48, 96))
    #                     loader.screen.blit(z_img, (map_sx + int(z_px * 48), map_sy + int((z_py - 1) * 48)))
    #
    #                 #######################这部分暂时保留
    #                 #绘制基础信息
    #                 chp = str(z['hp'])
    #                 cat = str(z['attack'])
    #                 cdf = str(z['defend'])
    #
    #                 chp_i = pygame.transform.scale(loader.HEART,(8,8))
    #                 cat_i = pygame.transform.scale(loader.ATTACK,(8,8))
    #                 cdf_i = pygame.transform.scale(loader.DEFEND,(8,8))
    #
    #                 loader.screen.blit(chp_i,(map_sx + int(z_px * 48), map_sy + int((z_py - 1) * 48)-8))
    #                 loader.screen.blit(cat_i,(map_sx + int(z_px * 48)+w16, map_sy + int((z_py - 1) * 48)-8))
    #                 loader.screen.blit(cdf_i,(map_sx + int(z_px * 48)+32, map_sy + int((z_py - 1) * 48)-8))
    #
    #                 chp_w = loader.GAME_TEXT_FONT_SM.render(chp, True,
    #                                                          color_rgb.BLACK,
    #                                                          None)
    #                 cat_w = loader.GAME_TEXT_FONT_SM.render(cat, True,
    #                                                         color_rgb.BLACK,
    #                                                         None)
    #                 cdf_w = loader.GAME_TEXT_FONT_SM.render(cdf, True,
    #                                                         color_rgb.BLACK,
    #                                                         None)
    #                 loader.screen.blit(chp_w, (map_sx + int(z_px * 48)+8, map_sy + int((z_py - 1) * 48)-8))
    #                 loader.screen.blit(cat_w, (map_sx + int(z_px * 48)+24, map_sy + int((z_py - 1) * 48)-8))
    #                 loader.screen.blit(cdf_w, (map_sx + int(z_px * 48)+40, map_sy + int((z_py - 1) * 48)-8))
    #                 #######################这部分暂时保留


    # 绘制回合数和时间
    if player_runtime.INFO['round'] % 4 in [1, 2]:
        sun = pygame.transform.scale(loader.SUN, (180, 130))
        loader.screen.blit(sun, (860, 0))
    else:
        moon = pygame.transform.scale(loader.MOON, (180, 130))
        loader.screen.blit(moon, (860, 0))

    round_obj = loader.GAME_ROUND_FONT.render('第' + str(player_runtime.INFO['round']) + '回合', True, color_rgb.BLACK,
                                              None)
    loader.screen.blit(round_obj, (860, 120))

    # 绘制数据菜单
    loader.screen.blit(loader.BAIKE, (860, 170))
    loader.screen.blit(loader.ZHANKUANG, (950, 170))
    loader.screen.blit(loader.CUNDANG, (860, 255))
    loader.screen.blit(loader.DUDANG, (950, 255))


#确认帧数序列
def check_tik(hcode,faceto,mode=0):
    '''
    :param hcode: 英雄编号
    :param faceto: 朝向
    :return:
    '''

    #移动模式
    if mode==0:
        ct = timer.get_clock()

        #取商
        v = ct//15
        #取余
        t = v%4

        #向下
        if faceto ==0:
            return loader.RMS[hcode][t]
        #左
        elif faceto==1:
            return loader.RMS[hcode][t+4]
        #右
        elif faceto==2:
            return loader.RMS[hcode][t+8]
        #上
        elif faceto==3:
            return loader.RMS[hcode][t+12]
    else:
        # 向下
        if faceto == 0:
            return loader.RMS[hcode][0]
        # 左
        elif faceto == 1:
            return loader.RMS[hcode][4]
        # 右
        elif faceto == 2:
            return loader.RMS[hcode][8]
        # 上
        elif faceto == 3:
            return loader.RMS[hcode][12]


#通过冒泡排序重置数组
def reset_role_list(zdata):
    L = []
    for zd in zdata:
        if len(zd) == 0:
            pass
        else:
            for z in zd:
                L.append(z)

    length = len(L)
    # 序列长度为length，需要执行length-1轮交换
    for x in range(1, length):
        # 对于每一轮交换，都将序列当中的左右元素进行比较
        # 每轮交换当中，由于序列最后的元素一定是最大的，因此每轮循环到序列未排序的位置即可
        for i in range(0, length - x):
            if L[i]['py'] > L[i + 1]['py']:
                temp = L[i]
                L[i] = L[i + 1]
                L[i + 1] = temp

    return L