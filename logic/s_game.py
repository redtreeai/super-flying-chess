# -*- coding: utf-8 -*-
# @Time    : 19-8-20 下午4:35
# @Author  : Redtree
# @File    : s_game.py
# @Desc :


from logic import loader
from logic import s_game_select_player
from logic import s_game_baike
from logic import s_game_play
from logic import s_game_zhankuang
from data import player_runtime
from data import color_rgb


def dojob(x,y,is_mouse_down,keys):

    loader.screen.fill(color_rgb.BROWN)

    #数据测试在这边打印

    #位于玩家数量选择页面
    if player_runtime.INFO['player_selected']==False:
        s_game_select_player.dojob(x,y,is_mouse_down)

    #位于百科页面
    elif player_runtime.INFO['inbaike']==True:
        s_game_baike.dojob(x,y,is_mouse_down)

    # 位于战况页面
    elif player_runtime.INFO['inzhankuang'] == True or player_runtime.INFO['gameover']:
        s_game_zhankuang.dojob(x, y, is_mouse_down,keys)

    #位于正常游戏界面
    else:
        s_game_play.dojob(x,y,is_mouse_down,keys)

    if x >= 350 and x <= 480 and y >= 350 and y <= 490 and player_runtime.INFO['gowinr_stage']==0 and player_runtime.INFO['gowinr']==True:
        loader.screen.blit(loader.MOUSE_WIN, (x - 40, y - 18))
    else:
        #鼠标最后画
        loader.screen.blit(loader.MOUSE,(x-18,y-18))





