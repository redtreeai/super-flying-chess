# -*- coding: utf-8 -*-
# @Time    : 19-9-17 上午11:43
# @Author  : Redtree
# @File    : s_game_gowin.py
# @Desc :  角色获胜处理


from data import player_runtime
from logic import loader
import random
from data import color_rgb
from utils import timer
import pygame


'''
    1 我方一角色攻击力永久+2
    2 阵营所有英雄血量+2
    3 立即对场上一个指定角色造成2点伤害.
'''


def dojob(x,y,is_mouse_down):

    # 1 选择奖励阶段
    if player_runtime.INFO['gowinr_stage'] == 0:
        # 显示女神板
        loader.screen.blit(loader.WISH1, (90, 170))
        # 350350480490
        if x >= 350 and x <= 480 and y >= 350 and y <= 490 and is_mouse_down == True:
            # 抽取奖励类型
            player_runtime.INFO['gowinr_type'] = random.randint(0, 2)
            # 跳转到显示奖励阶段
            player_runtime.INFO['gowinr_stage'] = 1

    # 2 查看奖励阶段
    elif player_runtime.INFO['gowinr_stage'] == 1:
        # 显示具体祝福内容
        loader.screen.blit(loader.WISHBOARD, (90, 170))
        WORDS = ['使随机一名我方角色攻击力永久+2', '使阵营所有角色血量+2', '对战场上的随机一名敌方角色造成3点伤害']
        word = WORDS[player_runtime.INFO['gowinr_type']]
        cw = loader.GAME_ROUND_FONT.render(word, True, color_rgb.BLACK,
                                           None)
        loader.screen.blit(cw, (140, 300))

        if is_mouse_down==True:
            player_runtime.INFO['gowinr_lstime']=timer.get_clock()
            player_runtime.INFO['gowinr_stage'] = 2
    # 3确认奖励
    elif player_runtime.INFO['gowinr_stage']==2:

        #重置奖励组
        player_runtime.INFO['gowinr_codes']=[]

        #判断奖励类型
        if player_runtime.INFO['gowinr_type']==0:
            #使随机一名我方角色攻击力永久+2

            #获取当前阵营
            cturn = player_runtime.INFO['turn']
            #获取阵营英雄数据
            pzc = player_runtime.INFO['zdata'][cturn]

            #待奖励角色
            c_index = 0
            for p in pzc:
                if p['code']==player_runtime.INFO['moving_code']:
                    #当前角色进入核心
                    player_runtime.INFO['zdata'][cturn][c_index]['gowin']=True
                    #位置重置
                    player_runtime.INFO['zdata'][cturn][c_index]['px']=-5
                    player_runtime.INFO['zdata'][cturn][c_index]['py']=-5
                else:
                    # 添加
                    if p['gowin'] == False:
                        player_runtime.INFO['gowinr_codes'].append(p['code'])

                c_index=c_index+1

            cp = random.choice(player_runtime.INFO['gowinr_codes'])

            #实现效果
            cd_index = 0
            for p in pzc:
                if p['code']==cp:
                    player_runtime.INFO['zdata'][cturn][cd_index]['attack']=player_runtime.INFO['zdata'][cturn][cd_index]['attack']+2
                    break
                cd_index=cd_index+1

            player_runtime.INFO['gowinr_codes']=[]
            player_runtime.INFO['gowinr_codes'].append(cp)
            player_runtime.INFO['gowinr_stage'] = 3

        elif player_runtime.INFO['gowinr_type']==1:
           #使阵营所有角色血量+2
           # 获取当前阵营
           cturn = player_runtime.INFO['turn']
           # 获取阵营英雄数据
           pzc = player_runtime.INFO['zdata'][cturn]

           # 待奖励角色
           c_index = 0
           for p in pzc:
               if p['code'] == player_runtime.INFO['moving_code']:
                   # 当前角色进入核心
                   player_runtime.INFO['zdata'][cturn][c_index]['gowin'] = True
                   # 位置重置
                   player_runtime.INFO['zdata'][cturn][c_index]['px'] = -5
                   player_runtime.INFO['zdata'][cturn][c_index]['py'] = -5
               else:
                   # 添加
                   if p['gowin'] == False:
                       player_runtime.INFO['gowinr_codes'].append(p['code'])

               c_index = c_index + 1

           # 实现效果
           cd_index = 0
           for p in pzc:
                player_runtime.INFO['zdata'][cturn][cd_index]['hp'] = \
                    player_runtime.INFO['zdata'][cturn][cd_index]['hp'] + 2
                cd_index = cd_index + 1

           player_runtime.INFO['gowinr_stage'] = 3

        elif player_runtime.INFO['gowinr_type']==2:
           #对战场上的随机一名敌方角色造成3点伤害

           cc_index = 0
           c_index = 0

           # 获取当前阵营
           cturn = player_runtime.INFO['turn']

           for zz in player_runtime.INFO['zdata']:
               for z in zz:
                   if z['code']==player_runtime.INFO['moving_code']:
                       # 当前角色进入核心
                       player_runtime.INFO['zdata'][cc_index][c_index]['gowin'] = True
                       # 位置重置
                       player_runtime.INFO['zdata'][cc_index][c_index]['px'] = -5
                       player_runtime.INFO['zdata'][cc_index][c_index]['py'] = -5

                   elif not cc_index==cturn and z['in_war']==True and z['gowin']==False:
                       player_runtime.INFO['gowinr_codes'].append(z['code'])

           cp = random.choice(player_runtime.INFO['gowinr_codes'])

           # 实现效果
           cd_index = 0
           c_index = 0
           for zz in player_runtime.INFO['zdata']:
               for z in zz:
                   if z['code'] == player_runtime.INFO['gowinr_codes'][0]:
                       player_runtime.INFO['zdata'][cd_index][c_index]['hp'] = \
                       player_runtime.INFO['zdata'][cd_index][c_index]['attack'] - 3
                       break
                   c_index = c_index + 1
               c_index=0
               cd_index=cd_index+1

           player_runtime.INFO['gowinr_codes'] = []
           player_runtime.INFO['gowinr_codes'].append(cp)
           player_runtime.INFO['gowinr_stage'] = 3

    #4执行奖励
    elif player_runtime.INFO['gowinr_stage']==3:

        # 判断奖励类型
        if player_runtime.INFO['gowinr_type'] == 0:
            # 使随机一名我方角色攻击力永久+2
            # 捕获棋子坐标
            map_sx = 118
            map_sy = 56

            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['code'] ==player_runtime.INFO['gowinr_codes'][0]:
                        v_text = loader.GAME_ROUND_FONT.render('+2', True,
                                                                color_rgb.BLACK,
                                                                None)
                        loader.screen.blit(v_text,(map_sx+z['px']*48+12,map_sy+z['py']*48-24))
                        la = pygame.transform.scale(loader.ATTACK,(12,12))
                        loader.screen.blit(la, (map_sx+z['px']*48,map_sy+z['py']*48-24))

            wtime = (timer.get_clock()-player_runtime.INFO['gowinr_lstime'])*15

            if wtime>1040:
                #演示完毕 结束奖励
                player_runtime.INFO['gowinr']=False
                player_runtime.INFO['stage'] = 5


        elif player_runtime.INFO['gowinr_type'] == 1:
            # 使阵营所有角色血量+2
            # 捕获棋子坐标
            map_sx = 118
            map_sy = 56

            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['code'] in player_runtime.INFO['gowinr_codes']:
                        v_text = loader.GAME_ROUND_FONT.render('+2', True,
                                                               color_rgb.GREEN,
                                                               None)
                        loader.screen.blit(v_text, (map_sx + z['px'] * 48 + 12, map_sy + z['py'] * 48 - 24))
                        lh = pygame.transform.scale(loader.HEART,(12,12))
                        loader.screen.blit(lh, (map_sx + z['px'] * 48, map_sy + z['py'] * 48 - 24))

            wtime = (timer.get_clock()-player_runtime.INFO['gowinr_lstime'])*15

            if wtime > 1040:
                # 演示完毕 结束奖励
                player_runtime.INFO['gowinr'] = False
                player_runtime.INFO['stage'] = 5

        elif player_runtime.INFO['gowinr_type'] == 2:
            # 对战场上的随机一名敌方角色造成3点伤害
            map_sx = 118
            map_sy = 56

            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['code'] == player_runtime.INFO['gowinr_codes'][0]:
                        v_text = loader.GAME_ROUND_FONT.render('-3', True,
                                                               color_rgb.RED,
                                                               None)
                        loader.screen.blit(v_text, (map_sx + z['px'] * 48 + 12, map_sy + z['py'] * 48 - 24))
                        lh = pygame.transform.scale(loader.HEART, (12, 12))
                        loader.screen.blit(lh, (map_sx + z['px'] * 48, map_sy + z['py'] * 48 - 24))
                        break
            wtime = (timer.get_clock()-player_runtime.INFO['gowinr_lstime'])*15

            if wtime > 1040:
                # 演示完毕 结束奖励
                player_runtime.INFO['gowinr'] = False
                player_runtime.INFO['stage'] = 5
