# -*- coding: utf-8 -*-
# @Time    : 19-8-26 上午10:57
# @Author  : Redtree
# @File    : s_game_select_player.py
# @Desc :  游戏前选择玩家数量的操作逻辑


from logic import loader
from data import player_runtime
from data.heros import hrs
import random
import copy


def dojob(x,y,is_mouse_down):
    loader.screen.blit(loader.SELECT_HELP, (120, 0))
    loader.screen.blit(loader.SELECT_PLAYER, (400, 220))

    if x >= 400 and x < 520 and y >= 220 and y < 340:
        player_runtime.INFO['player_num'] = 1
        loader.screen.blit(loader.SELECT, (400, 220))
    elif x >= 520 and x < 640 and y >= 220 and y < 340:
        loader.screen.blit(loader.SELECT, (520, 220))
        player_runtime.INFO['player_num'] = 2
    elif x >= 400 and x < 520 and y >= 340 and y < 460:
        loader.screen.blit(loader.SELECT, (400, 340))
        player_runtime.INFO['player_num'] = 3
    elif x >= 520 and x < 640 and y >= 340 and y < 460:
        loader.screen.blit(loader.SELECT, (520, 340))
        player_runtime.INFO['player_num'] = 4
    else:
        player_runtime.INFO['player_num'] = 0

    #暂时没有AI，取消单人游戏
    if player_runtime.INFO['player_num'] in [2, 3, 4] and is_mouse_down == True:
        # 构造游戏初始数据
        '''
        由于现在还没有AI，所以仅添加玩家阵营
        '''

        # 1 读取英雄池(深度拷贝)
        player_runtime.INFO['heros_pool'] = copy.deepcopy(hrs.DATA)
        cplayers = []
        # 2 初始化玩家位置
        for num in range(0, player_runtime.INFO['player_num']):
            # 构建当前玩家英雄组
            cplayer = []
            while len(cplayer) < 4:
                # 获取本局游戏当前英雄池数量
                hrplen = len(player_runtime.INFO['heros_pool'])
                # 随机从获取英雄,直到4员
                c_index = random.randint(0, hrplen - 1)
                #添加出战状态
                chero = player_runtime.INFO['heros_pool'][c_index]
                #是否出征状态，默认否
                chero['in_war']=False
                #行进方向 0倒退 1前进 默认前进
                chero['direct']=1
                #是否胜利到达终点的判定
                chero['gowin']=False
                # 面部朝向  0/1/2/3 下左右上 默认0
                chero['faceto'] = 0
                cplayer.append(chero)
                player_runtime.INFO['heros_pool'].pop(c_index)

            cplayers.append(cplayer)

        while len(cplayers) < 4:
            # 补足四个角色数据
            cplayers.append([])
        # 打乱顺序
        random.shuffle(cplayers)

        # 分配角色初始化位置
        player_runtime.INFO['zdata'] = cplayers
        zd_index = 0
        for zd in player_runtime.INFO['zdata']:
            if len(zd) == 0:
                pass
            else:
                z_index = 0
                for z in zd:
                    if zd_index == 0:
                        if z_index == 0:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 0
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 11
                        elif z_index == 1:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 1
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 11
                        elif z_index == 2:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 0
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 12
                        elif z_index == 3:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 1
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 12
                    elif zd_index == 1:
                        if z_index == 0:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 11
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 11
                        elif z_index == 1:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 12
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 11
                        elif z_index == 2:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 11
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 12
                        elif z_index == 3:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 12
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 12
                    elif zd_index == 2:
                        if z_index == 0:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 11
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 0
                        elif z_index == 1:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 12
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 0
                        elif z_index == 2:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 11
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 1
                        elif z_index == 3:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 12
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 1
                    elif zd_index == 3:
                        if z_index == 0:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 0
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 0
                        elif z_index == 1:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 1
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 0
                        elif z_index == 2:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 0
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 1
                        elif z_index == 3:
                            player_runtime.INFO['zdata'][zd_index][z_index]['px'] = 1
                            player_runtime.INFO['zdata'][zd_index][z_index]['py'] = 1

                    z_index = z_index + 1

            zd_index = zd_index + 1

        # 开始游戏
        player_runtime.INFO['player_selected'] = True