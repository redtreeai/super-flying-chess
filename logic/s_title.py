# -*- coding: utf-8 -*-
# @Time    : 19-6-17 下午5:34
# @Author  : Redtree
# @File    : s_title.py
# @Desc :  位于title场景下的游戏业务逻辑


from logic import loader
from utils import saver
from data import player_runtime
from data import game_page
from logic import s_game_loading
import config
import pygame
import sys
import copy
from data import color_rgb

def dojob(x,y,is_mouse_down,keys):
    if player_runtime.INFO['loading'] == True:
        loader.screen.fill(color_rgb.BROWN)

        s_game_loading.dojob(x, y, is_mouse_down, keys)
        # 鼠标最后画
        loader.screen.blit(loader.MOUSE, (x - 18, y - 18))
    else:
        loader.screen.blit(loader.TITLE_PAGE, (0, 0))

        x0, y0 = config.WINDOW_WEIGHT / 3, config.WINDOW_HEIGHT / 4
        x1, y1 = config.WINDOW_WEIGHT / 3, config.WINDOW_HEIGHT / 4 + 60
        x2, y2 = config.WINDOW_WEIGHT / 3, config.WINDOW_HEIGHT / 4 + 120
        x3, y3 = config.WINDOW_WEIGHT / 3, config.WINDOW_HEIGHT / 4 + 180

        if player_runtime.INFO['save_checked'] == False:
            save_res = check_save()
            player_runtime.INFO['has_save'] =save_res
            player_runtime.INFO['save_checked'] = True

        select_sound_flag = False

        if x0 + 160 > x >= x0 and y0 + 40 >= y >= y0 and  player_runtime.INFO['has_save'] == True:
            select_sound_flag = True
            check_play_sound()
            loader.screen.blit(loader.TITLE_continue_surface_pos, (x0, y0))
            if is_mouse_down == True:
                continue_game_event()
        elif  player_runtime.INFO['has_save'] == True:
            loader.screen.blit(loader.TITLE_continue_surface, (x0, y0))
        if x1 + 160 > x >= x1 and y1 + 40 >= y >= y1:
            select_sound_flag = True
            check_play_sound()
            loader.screen.blit(loader.TITLE_start_surface_pos, (x1, y1))
            if is_mouse_down == True:
                start_game_event()
        else:
            loader.screen.blit(loader.TITLE_start_surface, (x1, y1))
        if x2 + 160 > x >= x2 and y2 + 40 >= y >= y2:
            select_sound_flag = True
            check_play_sound()
            loader.screen.blit(loader.TITLE_achievement_surface_pos, (x2, y2))
        else:
            loader.screen.blit(loader.TITLE_achievement_surface, (x2, y2))
        if x3 + 160 > x >= x3 and y3 + 40 >= y >= y3:
            select_sound_flag = True
            check_play_sound()
            loader.screen.blit(loader.TITLE_exit_surface_pos, (x3, y3))
            if is_mouse_down == True:
                sys.exit()
        else:
            loader.screen.blit(loader.TITLE_exit_surface, (x3, y3))

        if select_sound_flag == False:
            player_runtime.INFO['select_sound'] = False

        sk = loader.RMS
        cobj = sk[player_runtime.INFO['title_r_index']][0]
        cobj = pygame.transform.scale(cobj, (100, 130))
        if player_runtime.INFO['title_rlr'] == 0:
            loader.screen.blit(cobj, (player_runtime.INFO['title_rx'], 540))
            player_runtime.INFO['title_rx'] = player_runtime.INFO['title_rx'] + 5
            if player_runtime.INFO['title_rx'] > 470:
                player_runtime.INFO['title_rx'] = 1040
                player_runtime.INFO['title_rlr'] = 1
                player_runtime.INFO['title_r_index'] = player_runtime.INFO['title_r_index'] + 1
                if player_runtime.INFO['title_r_index'] > 15:
                    player_runtime.INFO['title_r_index'] = 0
        else:
            loader.screen.blit(cobj, (player_runtime.INFO['title_rx'], 540))
            player_runtime.INFO['title_rx'] = player_runtime.INFO['title_rx'] - 5
            if player_runtime.INFO['title_rx'] < 470:
                player_runtime.INFO['title_rx'] = -100
                player_runtime.INFO['title_rlr'] = 0
                player_runtime.INFO['title_r_index'] = player_runtime.INFO['title_r_index'] + 1
                if player_runtime.INFO['title_r_index'] > 15:
                    player_runtime.INFO['title_r_index'] = 0

        #鼠标最后画
        loader.screen.blit(loader.MOUSE,(x-18,y-18))


#点击开始游戏的事件
def start_game_event():

   player_runtime.INFO = copy.deepcopy(reset_data())
   #切换场景
   loader.curs_code = game_page.SCODE
   print('进入游戏')



#检查存档文件
def check_save():
    try:
        save_path = config.SAVE_PATH
        res = saver.load(save_path)
        if res == False:
            # 追加提示
            print('未发现存档文件')
            return False
        else:
            if res['slot1']=='null' and res['slot2']=='null' and res['slot3']=='null':
                return False
            return True
    except Exception as err:
        return False



#读取存档，继续游戏
def continue_game_event():
    sdata = saver.read_sd()
    player_runtime.SDATA = sdata
    player_runtime.INFO['loading'] = True


#校验是否播放音频
def check_play_sound():
    if player_runtime.INFO['select_sound'] == False:
        loader.SELECT_SOUND.play(0)
        player_runtime.INFO['select_sound'] = True



#数据重置
def reset_data():
    info = {
        # 玩家数量
        'player_num': 1,
        # 选择音频声
        'select_sound': False,
        # 首页英雄序号
        'title_r_index': 0,
        # 首页英雄位置
        'title_rx': -100,
        # 首页英雄方向
        'title_rlr': 0,
        # 游戏界时钟,根据帧数统计
        'gclock': 0,
        # 选择游戏人数中
        'player_selected': False,
        # 回合数  1/2 白天 3/4 黑夜
        'round': 1,
        # 是否有存档数据
        'has_save': False,
        # 是否校验过存档
        'save_checked': False,
        # 是否在战况中
        'inzhankuang': False,
        # 是否在百科中
        'inbaike': False,
        # 战况数据
        'zdata': [],
        # 英雄池
        'heros_pool': [],

        ###下面是游戏过程中的参数
        # 轮次  按照  蓝/绿/黄/红/的顺序 0/1/2/3
        'turn': 0,
        # 阶段  分为 扔筛子/选择移动角色/移动/死斗、决斗或发动技能/结算
        #  0/1/2/3/4/5
        'stage': 0,
        # 是否黑夜,根据回合变化
        'is_night': False,
        # 当前筛子数字
        'sz_num': 0,
        # 是否处于提示状态
        'is_mention': False,
        # 提示内容
        'mention_text': '',
        # 控制面板可操作英雄代码
        'ctb_codes': [],
        # 游戏结束
        'gameover': False,
        # 获胜军团代码
        'win_code': 0,
        # 当前行动角色代码
        'moving_code': 0,
        # 当前行进目标
        'aim_point': (0, 0),
        # 角色是否行进中
        'is_moving': False,
        # 本次行走剩余部署
        'left_steps': 0,
        # 是否跳跃中
        'is_jumping': False,
        # 是否死斗中
        'death_fight': False,
        # 决斗名单:
        'fight_list': [],
        # 预备攻击中:
        'to_attack': False,
        # 可攻击对象
        'to_attack_codes': [],
        # 是否决斗中
        'common_fight': False,

        # 决斗场景
        'fight_bg': 0,
        # 决斗阶段  预备/战斗中/结束 0/1/2
        'fight_stage': 0,
        # 左边角色位置
        'left_fighter_px': -180,
        # 右边角色位置
        'right_fighter_px': 1080,
        # 决斗回合数
        'fight_round': 1,
        # 决斗进攻放   1右边先 然后0左边
        'fight_attack_code': 1,
        # 技能特效位置
        'attack_show_px': 0,
        # 伤害数字位置
        'attack_value_py': 0,

        # 技能场景中:
        'in_skill': False,
        # 技能动画中:
        'act_skill': False,
        # 技能命中伤害数值位置:
        'hit_sk_px': 0,
        'hit_sk_py': 0,
        # 目标位置
        'hit_sk_pya': 0,
        # 技能命中对象队列
        'shr_index': (-1, -1),
        # 屠夫技能命中对象队列
        'tfl_code': [],
        # 猎人技能充能 2可用，行动两次后恢复:
        'lr_power': 2,
        # 天使技能充能 3可用，行动三次后恢复:
        'ts_power': 3,
        # 屠夫技能 两次可用，回基地重置:
        'tf_power': 2,
        # 天使回家动画实时位置
        'ts_back_y': 0,
        # 播放哪一帧图片
        'ts_back_index': 0,
        # 决斗伤害确认
        'jd_dmg': 0,
        # 当前攻击方
        'jd_atc': 0,
        # 展示数值
        'jd_htw': '',
        # 事件
        'event': 'nothing',
        # 屠夫技能发动时间
        'tf_lstime': 0,
        # 屠夫技能坐标位置
        'tf_spx': 0,
        'tf_spy': 0,
        # 女巫诅咒动画标签
        'nwzz_index': 0,
        # 女巫施法时间
        'nwzz_lstime': 0,
        # 女巫技能坐标位置
        'nw_spx': 0,
        'nw_spy': 0,
        # 女巫技能命中对象编码
        'nw_code': -1,
        # 女巫本次技能伤害
        'nw_damage': 0,
        # 骑士是否发起决斗
        'is_qs_duel': False,
        # 是否位于角色奖励结算
        'gowinr': False,
        # 角色奖励阶段
        'gowinr_stage': 0,
        # 本次奖励类型
        'gowinr_type': 0,
        # 奖励执行时间
        'gowinr_lstime': 0,
        # 待奖励角色
        'gowinr_codes': [],

        # 是否位于存档页面
        'saving': False,
        # 是否位于读档页面
        'loading': False,
        # 提示是否覆盖存档
        'checksover': False,
        # 当前操作存档编号 0/1/2
        'cslot': 0,
    }

    return info