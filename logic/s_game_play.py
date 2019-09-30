# -*- coding: utf-8 -*-
# @Time    : 19-8-26 上午11:00
# @Author  : Redtree
# @File    : s_game_play.py
# @Desc : 位于正常游戏过程中


from data import player_runtime
from logic import s_game_play_base
from logic import s_game_play_stage0
from logic import s_game_play_stage1
from logic import s_game_play_stage2
from logic import s_game_play_stage3
from logic import s_game_play_stage4
from logic import s_game_play_stage5

def dojob(x,y,is_mouse_down,keys):

    #执行非玩家操作逻辑的部分
    s_game_play_base.dojob()
    #开始玩家操作逻辑
    # 1 判断游戏是否结束

    live_index = 0
    win_index = 0
    z_index = 0
    for zd in player_runtime.INFO['zdata'] :
        if len(zd)>0:
            live_index=live_index+1
            win_index = z_index
        z_index=z_index+1

    # 仅剩一个军团
    if live_index <= 1:
        player_runtime.INFO['win_code'] = win_index
        player_runtime.INFO['gameover'] = True
    else:

        #print(player_runtime.INFO['turn'],player_runtime.INFO['stage'])
        #print(player_runtime.INFO['is_moving'],player_runtime.INFO['is_jumping'])
        #继续游戏
        # 2 获取当前阵营英雄
        cheros = player_runtime.INFO['zdata'][player_runtime.INFO['turn']]
        # 3  判断操作要求
        if len(cheros) == 0:
            player_runtime.INFO['turn'] = player_runtime.INFO['turn'] + 1
            if player_runtime.INFO['turn'] > 3:
                player_runtime.INFO['turn'] = 0
                # 回合数+1
                player_runtime.INFO['round'] = player_runtime.INFO['round'] + 1
        else:
            if player_runtime.INFO['stage'] == 0:
                #筛子投掷或菜单操作
                s_game_play_stage0.dojob(x,y,is_mouse_down,keys)
            elif player_runtime.INFO['stage'] == 1:
                #选择移动角色
                s_game_play_stage1.dojob(x,y,is_mouse_down,cheros,keys)
            elif player_runtime.INFO['stage'] == 2:
                #角色移动过程
                s_game_play_stage2.dojob()
            elif player_runtime.INFO['stage'] == 3:
                #角色技能选择
                s_game_play_stage3.dojob(x,y,is_mouse_down,keys)
            elif player_runtime.INFO['stage'] == 4:
                #决斗/死斗/或其他角色技能的伤害/效果结算
                s_game_play_stage4.dojob()
            elif player_runtime.INFO['stage'] == 5:
                #整体结算
                s_game_play_stage5.dojob()

