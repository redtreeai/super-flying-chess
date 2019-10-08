# -*- coding: utf-8 -*-
# @Time    : 19-8-28 上午9:56
# @Author  : Redtree
# @File    : s_game_play_stage0.py
# @Desc :  投掷筛子阶段


from logic import loader
from logic import s_game_saving
from logic import s_game_loading
from data import player_runtime
from data import color_rgb
import pygame
import random
from utils import saver


def dojob(x,y,is_mouse_down,keys):

    #位于存档交互页面
    if player_runtime.INFO['saving']==True:
        s_game_saving.dojob(x,y,is_mouse_down,keys)
    elif player_runtime.INFO['loading']==True:
        s_game_loading.dojob(x,y,is_mouse_down,keys)
    else:
        # 数据菜单交互 仅在阶段0可以操作数据菜单
        # 1 百科
        if x >= 860 and x < 950 and y >= 170 and y < 255:
            loader.screen.blit(loader.SELECT_MENU, (860, 170))
            if is_mouse_down == True:
                player_runtime.INFO['inbaike'] = True
        # 2 战况
        elif x >= 950 and x < 1040 and y >= 170 and y < 255:
            loader.screen.blit(loader.SELECT_MENU, (950, 170))
            if is_mouse_down == True:
                player_runtime.INFO['inzhankuang'] = True
        # 3 存档
        elif x >= 860 and x < 950 and y >= 255 and y < 340:
            loader.screen.blit(loader.SELECT_MENU, (860, 255))
            if is_mouse_down == True:
                pygame.image.save(loader.screen, 'save/tmp.jpg')
                #读取存档数据
                sdata = saver.read_sd()
                player_runtime.SDATA=sdata
                player_runtime.INFO['saving']=True
        # 4 读档
        elif x >= 950 and x < 1040 and y >= 255 and y < 340:
            loader.screen.blit(loader.SELECT_MENU, (950, 255))
            if is_mouse_down == True:
                # 读取存档数据
                sdata = saver.read_sd()
                player_runtime.SDATA = sdata
                player_runtime.INFO['loading'] = True

        if keys['tab'] == 1:
            player_runtime.INFO['inzhankuang'] = True

        # 筛子提示
        tag_blue = loader.GAME_ROUND_FONT.render('点我->', True,
                                                 color_rgb.BLACK,
                                                 None)
        loader.screen.blit(tag_blue, (770, 600))

        # 投掷筛子
        csz = pygame.transform.scale(loader.SZ[player_runtime.INFO['sz_num']], (180, 170))
        loader.screen.blit(csz, (860, 510))


        #操作角色判断 (玩家)
        if player_runtime.INFO['pa_turn'][player_runtime.INFO['turn']]==0:
            # 随机产生1到6的一个位数
            if x >= 860 and x < 1040 and y >= 510 and y < 680:
                loader.SEZI_SOUND.play(0)
                player_runtime.INFO['sz_num'] = random.randint(0, 5)
                if is_mouse_down == True:
                    # 进入选择移动角色的阶段
                    player_runtime.INFO['left_steps'] = player_runtime.INFO['sz_num'] + 1
                    player_runtime.INFO['stage'] = 1

                # 作弊按钮
                elif keys['1'] == 1:
                    # 进入选择移动角色的阶段
                    player_runtime.INFO['sz_num'] = 0
                    player_runtime.INFO['left_steps'] = player_runtime.INFO['sz_num'] + 1
                    player_runtime.INFO['stage'] = 1
                elif keys['2'] == 1:
                    # 进入选择移动角色的阶段
                    player_runtime.INFO['sz_num'] = 1
                    player_runtime.INFO['left_steps'] = player_runtime.INFO['sz_num'] + 1
                    player_runtime.INFO['stage'] = 1
                elif keys['3'] == 1:
                    # 进入选择移动角色的阶段
                    player_runtime.INFO['sz_num'] = 2
                    player_runtime.INFO['left_steps'] = player_runtime.INFO['sz_num'] + 1
                    player_runtime.INFO['stage'] = 1
                elif keys['4'] == 1:
                    # 进入选择移动角色的阶段
                    player_runtime.INFO['sz_num'] = 3
                    player_runtime.INFO['left_steps'] = player_runtime.INFO['sz_num'] + 1
                    player_runtime.INFO['stage'] = 1
                elif keys['5'] == 1:
                    # 进入选择移动角色的阶段
                    player_runtime.INFO['sz_num'] = 4
                    player_runtime.INFO['left_steps'] = player_runtime.INFO['sz_num'] + 1
                    player_runtime.INFO['stage'] = 1
                elif keys['6'] == 1:
                    # 进入选择移动角色的阶段
                    player_runtime.INFO['sz_num'] = 5
                    player_runtime.INFO['left_steps'] = player_runtime.INFO['sz_num'] + 1
                    player_runtime.INFO['stage'] = 1

        else: #AI
            if player_runtime.STAGE_0['lstime']<60:
                loader.SEZI_SOUND.play(0)
                player_runtime.STAGE_0['lstime']= player_runtime.STAGE_0['lstime']+1
            else:
                player_runtime.INFO['sz_num'] = random.randint(0, 5)
                player_runtime.INFO['left_steps'] = player_runtime.INFO['sz_num'] + 1
                player_runtime.INFO['stage'] = 1
                player_runtime.STAGE_0['lstime'] = 0