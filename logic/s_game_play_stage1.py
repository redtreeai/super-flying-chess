# -*- coding: utf-8 -*-
# @Time    : 19-8-28 上午9:59
# @Author  : Redtree
# @File    : s_game_play_stage1.py
# @Desc : 选择移动对象阶段


from logic import loader
from data import player_runtime
from data import color_rgb
import pygame
import random


def dojob(x,y,is_mouse_down,cheros,keys):

    # 结果显示在左下角
    csz = pygame.transform.scale(loader.SZ[player_runtime.INFO['sz_num']], (60, 60))
    loader.screen.blit(csz, (770, 600))
    # 重置角色控制面板
    player_runtime.INFO['ctb_codes'] = []
    # 如果结果不为6,且阵营没有出战角色，则跳过回合
    #测试的时候先都允许起飞

    cheros = player_runtime.INFO['zdata'][player_runtime.INFO['turn']]

    if not player_runtime.INFO['sz_num'] in [4, 5]:
        in_war_flag = False
        for cr in cheros:
            if cr['in_war'] == True and cr['gowin']==False:
                #白天僵尸无法行动
                if player_runtime.INFO['round'] % 4 in [1, 2] and cr['code']==7:
                    pass
                else:
                    player_runtime.INFO['ctb_codes'].append(cr['code'])
                    in_war_flag = True

        if in_war_flag == False:
            mention_words = ['提示', '无法行动，需掷出点数','大于5']
            do_mention(mention_words)
            #如果是玩家，手动点击跳过，如果是AI，1秒后跳过
            if player_runtime.INFO['pa_turn'][player_runtime.INFO['turn']] == 0:
                if player_runtime.INFO['is_mention'] == True and is_mouse_down == True:
                    player_runtime.INFO['is_mention'] = False
                    player_runtime.INFO['ctb_codes']=[]
                    # 跳到结算步骤b
                    player_runtime.INFO['stage'] = 5
            else:
                #实际的AI操作时间待调整反馈
                if player_runtime.AITP['st11'] < 60:
                    player_runtime.AITP['st11'] = player_runtime.AITP['st11'] + 1
                else:
                    player_runtime.INFO['is_mention'] = False
                    player_runtime.INFO['ctb_codes'] = []
                    # 跳到结算步骤b
                    player_runtime.AITP['st11'] = 0
                    player_runtime.INFO['stage'] = 5

        else:
            # 正常执行其他战场角色
            control_heros_index = 0
            for code in player_runtime.INFO['ctb_codes']:
                chr = pygame.transform.scale(loader.RMS[code][0], (90, 85))
                if control_heros_index == 0:
                    loader.screen.blit(chr, (860, 510))
                elif control_heros_index == 1:
                    loader.screen.blit(chr, (950, 510))
                elif control_heros_index == 2:
                    loader.screen.blit(chr, (860, 595))
                elif control_heros_index == 3:
                    loader.screen.blit(chr, (950, 595))

                control_heros_index = control_heros_index + 1

    else:
        # 选择要移动的角色
        control_heros_index = 0
        for c in cheros:
            if c['gowin']==True:
                pass
            elif player_runtime.INFO['round'] % 4 in [1, 2] and c['code']==7 :
                pass
            else:
                player_runtime.INFO['ctb_codes'].append(c['code'])
                chr = pygame.transform.scale(loader.RMS[c['code']][0], (90, 85))
                if control_heros_index == 0:
                    loader.screen.blit(chr, (860, 510))
                elif control_heros_index == 1:
                    loader.screen.blit(chr, (950, 510))
                elif control_heros_index == 2:
                    loader.screen.blit(chr, (860, 595))
                elif control_heros_index == 3:
                    loader.screen.blit(chr, (950, 595))

                control_heros_index = control_heros_index + 1

    # 如果是玩家，手动选择操作英雄，如果是AI，随机选择
    if player_runtime.INFO['pa_turn'][player_runtime.INFO['turn']] == 0:

        # 英雄菜单交互 仅在阶段1可以选择英雄
        # 1
        if x >= 860 and x < 950 and y >= 510 and y < 595 and len(player_runtime.INFO['ctb_codes'])>0:
            loader.screen.blit(loader.SELECT_MENU, (860, 510))
            if is_mouse_down == True:
                player_runtime.INFO['moving_code'] = player_runtime.INFO['ctb_codes'][0]
                player_runtime.INFO['stage'] = 2
        # 2
        elif x >= 950 and x < 1040 and y >= 510 and y < 595 and len(player_runtime.INFO['ctb_codes'])>1:
            loader.screen.blit(loader.SELECT_MENU, (950, 510))
            if is_mouse_down == True:
                player_runtime.INFO['moving_code'] = player_runtime.INFO['ctb_codes'][1]
                player_runtime.INFO['stage'] = 2
        # 3
        elif x >= 860 and x < 950 and y >= 595 and y < 680 and len(player_runtime.INFO['ctb_codes'])>2:
            loader.screen.blit(loader.SELECT_MENU, (860, 595))
            if is_mouse_down == True:
                player_runtime.INFO['moving_code'] = player_runtime.INFO['ctb_codes'][2]
                player_runtime.INFO['stage'] = 2
        # 4
        elif x >= 950 and x < 1040 and y >= 595 and y < 680 and len(player_runtime.INFO['ctb_codes'])>3:
            loader.screen.blit(loader.SELECT_MENU, (950, 595))
            if is_mouse_down == True:
                player_runtime.INFO['moving_code'] = player_runtime.INFO['ctb_codes'][3]
                player_runtime.INFO['stage'] = 2

        if keys['tab'] == 1:
            player_runtime.INFO['inzhankuang'] = True

    else:
        clen = len(player_runtime.INFO['ctb_codes'])
        if clen<1:
            player_runtime.INFO['is_mention'] = False
            player_runtime.INFO['ctb_codes'] = []
            # 跳到结算步骤b
            player_runtime.INFO['stage'] = 5
        else:
            ai_choice = random.randint(1,len(player_runtime.INFO['ctb_codes']))
            if ai_choice==1:
                player_runtime.INFO['moving_code'] = player_runtime.INFO['ctb_codes'][0]
                player_runtime.INFO['stage'] = 2
            elif ai_choice==2:
                player_runtime.INFO['moving_code'] = player_runtime.INFO['ctb_codes'][1]
                player_runtime.INFO['stage'] = 2
            elif ai_choice == 3:
                player_runtime.INFO['moving_code'] = player_runtime.INFO['ctb_codes'][2]
                player_runtime.INFO['stage'] = 2
            elif ai_choice == 4:
                player_runtime.INFO['moving_code'] = player_runtime.INFO['ctb_codes'][3]
                player_runtime.INFO['stage'] = 2



#创造提示
def do_mention(text):
    mx = 300
    my = 200

    loader.screen.blit(loader.MENTION,(mx,my))
    t_index = 1
    for t in text:
        mtext = loader.GAME_ROUND_FONT.render(t, True,
                                                 color_rgb.BLACK,
                                                 None)
        loader.screen.blit(mtext, (mx+50, my+50*t_index))
        t_index = t_index+1


    player_runtime.INFO['is_mention']=True