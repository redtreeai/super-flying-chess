# -*- coding: utf-8 -*-
# @Time    : 19-8-29 下午2:43
# @Author  : Redtree
# @File    : s_game_play_stage4.py
# @Desc : 决斗或伤害判定


from logic import loader
from data import player_runtime
import pygame
from data import  color_rgb
import random
from utils import timer


def dojob():
    # 描绘决斗场背景 (刺客专属白色背景)
    if player_runtime.INFO['fight_stage'] == 1 and player_runtime.INFO['fight_list'][0] == 5 and player_runtime.INFO[
        'fight_attack_code'] == 0:
        loader.screen.fill(color_rgb.WHITE)
    elif player_runtime.INFO['fight_stage'] == 1 and player_runtime.INFO['fight_list'][1] == 5 and player_runtime.INFO[
        'fight_attack_code'] == 1:
        loader.screen.fill(color_rgb.WHITE)
    else:
        loader.screen.blit(loader.LEITAI[player_runtime.INFO['fight_bg']], (0, 0))
    HEIGHT = 420
    #攻击速度
    ATS = 12
    #伤害字幕速度
    AVS = 6
    #角色移动速度
    MSP = 6

    # 获取双方英雄形象
    # 攻击阶段的武士、刺客 僵尸 狼人 骑士 怪兽 隐藏身形
    if player_runtime.INFO['fight_stage'] == 1 and player_runtime.INFO['fight_list'][0] in [4,5,7,12,13,15] and player_runtime.INFO['fight_attack_code']==0:
        pass
    else:
        left_img = pygame.transform.scale(loader.RMS[player_runtime.INFO['fight_list'][0]][8], (180, 90))
        loader.screen.blit(left_img, (player_runtime.INFO['left_fighter_px'], HEIGHT))

    #攻击阶段的武士、刺客 僵尸 狼人 骑士 怪兽 隐藏身形
    if player_runtime.INFO['fight_stage']==1 and player_runtime.INFO['fight_list'][1] in [4,5,7,12,13,15] and player_runtime.INFO['fight_attack_code']==1 :
        pass
    else:
        right_img = pygame.transform.scale(loader.RMS[player_runtime.INFO['fight_list'][1]][4], (180, 90))
        loader.screen.blit(right_img, (player_runtime.INFO['right_fighter_px'], HEIGHT))


    #预备阶段
    if player_runtime.INFO['fight_stage'] == 0:
        # 描绘决斗类型
        if player_runtime.INFO['death_fight'] == True:
            loader.screen.blit(loader.SIDOU, (220, 240))
            # 死斗中，双方需要战至一方阵亡
        else :
            loader.screen.blit(loader.JUEDOU, (220, 240))

        # 往舞台中间移动
        player_runtime.INFO['left_fighter_px'] = player_runtime.INFO['left_fighter_px'] + MSP
        player_runtime.INFO['right_fighter_px'] = player_runtime.INFO['right_fighter_px'] - MSP

        if abs(player_runtime.INFO['right_fighter_px'] - player_runtime.INFO['left_fighter_px']) <= 800:
            # 准备结束
            # 重置技能特效位置和伤害值位置
            player_runtime.INFO['attack_show_px']=player_runtime.INFO['right_fighter_px']
            player_runtime.INFO['attack_value_py']=HEIGHT
            #攻击判定 也要 重置
            player_runtime.INFO['jd_atc'] = 0
            player_runtime.INFO['fight_stage'] = 1

    elif player_runtime.INFO['fight_stage']==1:
        #PK阶段
        left_code = (0,0)
        right_code = (0,0)
        #获取决斗英雄实时数据坐标
        c1 = 0
        c2 = 0

        for zz in player_runtime.INFO['zdata']:
            for z in zz:
                if z['code']==player_runtime.INFO['fight_list'][0]:
                    left_code=(c1,c2)
                elif z['code']==player_runtime.INFO['fight_list'][1]:
                    right_code=(c1,c2)
                c2=c2+1

            c2=0
            c1=c1+1

        #绘制回合数
        round_title = 'Round '+str(player_runtime.INFO['fight_round'])
        title_rv = loader.GAME_ROUND_TITLE_FONT.render(round_title, True,
                                                   color_rgb.WHITE,
                                                   None)
        loader.screen.blit(title_rv, (400, 5))

        # 绘制英雄血量
        heart_img = pygame.transform.scale(loader.HEART,(60,60))
        left_hp = player_runtime.INFO['zdata'][left_code[0]][left_code[1]]['hp']
        right_hp = player_runtime.INFO['zdata'][right_code[0]][right_code[1]]['hp']
        left_atv = player_runtime.INFO['zdata'][left_code[0]][left_code[1]]['attack']
        left_def = player_runtime.INFO['zdata'][left_code[0]][left_code[1]]['defend']
        right_atv = player_runtime.INFO['zdata'][right_code[0]][right_code[1]]['attack']
        right_def = player_runtime.INFO['zdata'][right_code[0]][right_code[1]]['defend']

        #奥特曼技能处理  (测试是否攻击力会回调)
        if player_runtime.INFO['fight_list'][0]==15 and player_runtime.INFO['fight_list'][1]==3:
            right_atv=right_atv*5
        elif player_runtime.INFO['fight_list'][0]==3 and player_runtime.INFO['fight_list'][1]==15:
            left_atv=left_atv*5

        #狼人技能 夜王，夜晚攻击力翻倍(测试是否攻击力会回调)
        if not player_runtime.INFO['round'] % 4 in [1, 2] :
            if player_runtime.INFO['fight_list'][0] ==12:
                left_atv=left_atv*2
            elif player_runtime.INFO['fight_list'][1]==12:
                right_atv=right_atv*2

        # 怪兽技能 为什么要打我？  被动决斗或死斗  防御翻倍。
        if player_runtime.INFO['fight_list'][0]==15:
            left_def=left_def*2

        lw = 0
        lh = 0
        rw = 0
        rh = 0
        #左边
        for ll in range(0,left_hp):
            loader.screen.blit(heart_img,(5+lw*65,5+lh*65))
            lw =lw+1
            if lw>4:
                lw=0
                lh=lh+1

        # 右边
        for rr in range(0, right_hp):
            loader.screen.blit(heart_img, (710 + rw * 65, 5 + rh * 65))
            rw = rw + 1
            if rw > 4:
                rw = 0
                rh = rh + 1

        # 绘制攻防
        # 1左边玩家
        # 攻击力图标
        attack_icon = pygame.transform.scale(loader.ATTACK, (45, 40))
        loader.screen.blit(attack_icon, (10, 70+lh*65))
        # 攻击力数值
        l_atv_text = loader.GAME_ROUND_FONT.render(str(left_atv), True,
                                                color_rgb.GREEN,
                                                None)
        loader.screen.blit(l_atv_text, (60,70+lh*65))
        # 防御力图标
        defend_icon = pygame.transform.scale(loader.DEFEND, (45, 40))
        loader.screen.blit(defend_icon, (115, 70 + lh * 65))
        # 防御力数值
        l_def_text = loader.GAME_ROUND_FONT.render(str(left_def), True,
                                                 color_rgb.GREEN,
                                                 None)
        loader.screen.blit(l_def_text, (165, 70 + lh * 65))
        # 2右边玩家
        # 攻击力图标
        loader.screen.blit(attack_icon, (830, 70 + rh * 65))
        # 攻击力数值
        r_atv_text = loader.GAME_ROUND_FONT.render(str(right_atv), True,
                                                   color_rgb.GREEN,
                                                   None)
        loader.screen.blit(r_atv_text, (880, 70 + rh * 65))
        # 防御力图标
        loader.screen.blit(defend_icon, (935, 70 + rh * 65))
        # 防御力数值
        r_def_text = loader.GAME_ROUND_FONT.render(str(right_def), True,
                                                   color_rgb.GREEN,
                                                   None)
        loader.screen.blit(r_def_text, (985, 70 + rh * 65))

        #开始战斗
        #1 右边先进攻
        if player_runtime.INFO['fight_attack_code']==1:
            if player_runtime.INFO['jd_atc']==0:
                # 开始计算伤害
                player_runtime.INFO['jd_dmg'] = right_atv - \
                                                left_def

                # 刺客的攻击无视防御力,但有几率被武僧免疫
                if player_runtime.INFO['fight_list'][0] == 5:
                        player_runtime.INFO['jd_dmg'] = right_atv

                if player_runtime.INFO['jd_dmg'] < 0:
                    player_runtime.INFO['jd_dmg'] = 0

                player_runtime.INFO['jd_htw'] = str(player_runtime.INFO['jd_dmg'])

                # 如果是武僧，百分之20概率免疫
                if player_runtime.INFO['fight_list'][0] == 1:
                    seed = random.random()
                    if seed <= 0.2:
                        player_runtime.INFO['jd_dmg'] = 0
                        player_runtime.INFO['jd_htw'] = '免疫'

                # 如果是国王，伤害最多不超过1
                if player_runtime.INFO['fight_list'][0] == 14:
                    if player_runtime.INFO['jd_dmg'] > 1:
                        player_runtime.INFO['jd_dmg'] = 1
                        player_runtime.INFO['jd_htw'] = '1'

                player_runtime.INFO['jd_atc'] =1
                #赋予特效动画的起始时间点
                player_runtime.FIGHT_ACTION['lstime']=timer.get_clock()
            else:
                # 暂时都用飞剑替代 (不同角色特效制作)
                attack_show(1,player_runtime.INFO['fight_list'][1])
                #loader.screen.blit(loader.ATTACK, (player_runtime.INFO['attack_show_px'], HEIGHT))
                player_runtime.INFO['attack_show_px'] = player_runtime.INFO['attack_show_px'] - ATS
                if abs(player_runtime.INFO['attack_show_px'] - player_runtime.INFO['left_fighter_px']) <= ATS * 2:
                    # 锁定位置
                    player_runtime.INFO['attack_show_px'] = player_runtime.INFO['left_fighter_px']

                    # 显示伤害字符
                    dm_text = loader.GAME_ROUND_FONT.render(player_runtime.INFO['jd_htw'], True,
                                                            color_rgb.RED,
                                                            None)
                    loader.screen.blit(dm_text,
                                       (player_runtime.INFO['left_fighter_px'], player_runtime.INFO['attack_value_py']))
                    player_runtime.INFO['attack_value_py'] = player_runtime.INFO['attack_value_py'] - AVS
                    if player_runtime.INFO['attack_value_py'] <= 240:
                        # 锁定位置
                        player_runtime.INFO['attack_value_py'] = 240
                        # 开始结算伤害
                        player_runtime.INFO['zdata'][left_code[0]][left_code[1]]['hp'] = \
                        player_runtime.INFO['zdata'][left_code[0]][left_code[1]]['hp'] - player_runtime.INFO['jd_dmg']
                        # 跳转到下一个攻击方
                        player_runtime.INFO['fight_attack_code'] = 0
                        # 重置攻击效果初始位置
                        player_runtime.INFO['attack_show_px'] = player_runtime.INFO['left_fighter_px']
                        player_runtime.INFO['attack_value_py'] = HEIGHT

                        # 行动后，若回合数大于5,减去1hp
                        if player_runtime.INFO['fight_round'] > 5:
                            player_runtime.INFO['zdata'][right_code[0]][right_code[1]]['hp'] = \
                            player_runtime.INFO['zdata'][right_code[0]][right_code[1]]['hp'] - 1


        else:

            if player_runtime.INFO['jd_atc'] ==1:
                # 开始计算伤害
                player_runtime.INFO['jd_dmg'] = left_atv - \
                                                right_def

                # 刺客的攻击无视防御力,但有几率被武僧免疫
                if player_runtime.INFO['fight_list'][1] == 5:
                    player_runtime.INFO['jd_dmg'] = left_atv

                if player_runtime.INFO['jd_dmg'] < 0:
                    player_runtime.INFO['jd_dmg'] = 0

                player_runtime.INFO['jd_htw'] = str(player_runtime.INFO['jd_dmg'])

                # 如果是武僧，百分之20概率免疫
                if player_runtime.INFO['fight_list'][1] == 1:
                    seed = random.random()
                    if seed <= 0.2:
                        player_runtime.INFO['jd_dmg'] = 0
                        player_runtime.INFO['jd_htw'] = '免疫'

                # 如果是国王，伤害最多不超过1
                if player_runtime.INFO['fight_list'][1] == 14:
                    if player_runtime.INFO['jd_dmg'] > 1:
                        player_runtime.INFO['jd_dmg'] = 1
                        player_runtime.INFO['jd_htw'] = '1'

                player_runtime.INFO['jd_atc'] =0
                # 赋予特效动画的起始时间点
                player_runtime.FIGHT_ACTION['lstime'] = timer.get_clock()
            else:
                # 暂时都用飞剑替代    (左边角色)
                attack_show(0,player_runtime.INFO['fight_list'][0])
                #loader.screen.blit(loader.ATTACK, (player_runtime.INFO['attack_show_px'], HEIGHT))
                player_runtime.INFO['attack_show_px'] = player_runtime.INFO['attack_show_px'] + ATS
                if abs(player_runtime.INFO['attack_show_px'] - player_runtime.INFO['right_fighter_px']) <= ATS * 2:
                    # 锁定位置
                    player_runtime.INFO['attack_show_px'] = player_runtime.INFO['right_fighter_px']

                    # 显示伤害字符
                    dm_text = loader.GAME_ROUND_FONT.render(player_runtime.INFO['jd_htw'], True,
                                                            color_rgb.RED,
                                                            None)
                    loader.screen.blit(dm_text,
                                       (
                                       player_runtime.INFO['right_fighter_px'], player_runtime.INFO['attack_value_py']))
                    player_runtime.INFO['attack_value_py'] = player_runtime.INFO['attack_value_py'] - AVS
                    if player_runtime.INFO['attack_value_py'] <= 240:
                        # 锁定位置
                        player_runtime.INFO['attack_value_py'] = 240
                        # 开始结算伤害
                        player_runtime.INFO['zdata'][right_code[0]][right_code[1]]['hp'] = \
                        player_runtime.INFO['zdata'][right_code[0]][right_code[1]]['hp'] - player_runtime.INFO['jd_dmg']
                        # 跳转到下一个攻击方
                        player_runtime.INFO['fight_attack_code'] = 1
                        # 重置攻击效果初始位置

                        player_runtime.INFO['attack_show_px'] = player_runtime.INFO['right_fighter_px']
                        player_runtime.INFO['attack_value_py'] = HEIGHT
                        # 一轮结束
                        player_runtime.INFO['fight_round'] = player_runtime.INFO['fight_round'] + 1
                        # 行动后，若回合数大于5,减去1hp
                        if player_runtime.INFO['fight_round'] > 5:
                            player_runtime.INFO['zdata'][left_code[0]][left_code[1]]['hp'] = \
                            player_runtime.INFO['zdata'][left_code[0]][left_code[1]]['hp'] - 1

        #不论哪种决斗模式，一方血量为0则终止
        if player_runtime.INFO['zdata'][left_code[0]][left_code[1]]['hp'] <= 0 or player_runtime.INFO['zdata'][right_code[0]][right_code[1]]['hp'] <= 0:
            # 进入结算阶段
            player_runtime.INFO['death_fight'] = False
            player_runtime.INFO['common_fight'] = False
            player_runtime.INFO['fight_attack_code'] = 1 #如果有角色阵亡，需要重置出手顺序
            player_runtime.INFO['fight_round'] = 1
            player_runtime.INFO['fight_list']=[]
            player_runtime.INFO['stage'] = 5
        else:
            #若都存活，则根据决斗类型判断
            #死斗
            if player_runtime.INFO['death_fight']==True:
                pass
            else:
                #普通决斗，仅一回合
                if player_runtime.INFO['fight_round']>=2:

                    #如果发起的是骑士,则获得阵营额外行动的回合
                    if player_runtime.INFO['moving_code']==13:
                        player_runtime.INFO['is_qs_duel']=True

                    player_runtime.INFO['death_fight'] = False
                    player_runtime.INFO['common_fight'] = False
                    player_runtime.INFO['fight_round'] = 1
                    player_runtime.INFO['fight_list'] = []
                    player_runtime.INFO['stage'] = 5



#执行攻击动画的函数
def attack_show(attack_turn,attack_code):
    '''
    :param attack_turn: 攻击方,1右边，0左边
    :param attack_code: 发动攻击角色代码
    :return:
    '''

    HEIGHT = 420
    lstime = player_runtime.FIGHT_ACTION['lstime']
    #程序员
    if attack_code==0:
        '''
        分为5个键盘，然后一起砸过去(为什么只显示了4个)
        '''
        va = (timer.get_clock() - lstime) * 2
        rot = (timer.get_clock() - lstime) * 6
        bb_text = loader.GAME_ROUND_FONT.render('万键归宗！！', True,
                                                color_rgb.BLACK,
                                                None)
        if attack_turn==1:
            loader.screen.blit(bb_text,(player_runtime.INFO['right_fighter_px'], HEIGHT-60))
        else:
            loader.screen.blit(bb_text,(player_runtime.INFO['left_fighter_px'], HEIGHT-60))
        for x in range(1,6):
                cheight = HEIGHT-300+x*100
                cimg = pygame.transform.rotate(loader.W1,rot)
                if cheight>HEIGHT:
                    loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], cheight - va))
                elif cheight<HEIGHT:
                    loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], cheight + va))
    #小甜心
    elif attack_code == 1:
        '''
        天上掉下好几个LV包砸对面
        '''
        va = (timer.get_clock() - lstime) * 20
        bb_text = loader.GAME_ROUND_FONT.render('要很多包包！！', True,
                                                color_rgb.BLACK,
                                                None)

        if attack_turn == 1:
            loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT - 60))
        else:
            loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 60))

        for x in range(1, 6):
            cheight = HEIGHT - 1200 + x * 200
            if cheight < HEIGHT:
                if attack_turn==1:
                    loader.screen.blit(loader.W2, (player_runtime.INFO['left_fighter_px'], cheight + va))
                else:
                    loader.screen.blit(loader.W2, (player_runtime.INFO['right_fighter_px'], cheight + va))


    #科学家
    elif attack_code == 2:
        '''
        播放钢铁侠动画
        '''
        bb_text = loader.GAME_ROUND_FONT.render('科技之光', True,
                                                color_rgb.BLACK,
                                                None)

        if attack_turn == 1:
            loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT - 180))
            loader.screen.blit(loader.W3_BSR, (player_runtime.INFO['right_fighter_px']-15, HEIGHT-120 ))
        else:
            loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 180))
            loader.screen.blit(loader.W3_BSL, (player_runtime.INFO['left_fighter_px']-15, HEIGHT-120 ))

        va = (timer.get_clock() - lstime)
        v = va%9

        if va<9:
            loader.screen.blit(loader.W3[v], (0,0))
        else:
            if attack_turn == 1:
                cimg = pygame.transform.scale(loader.W3_BOR,(767,200+v*3))
                loader.screen.blit(cimg,(player_runtime.INFO['left_fighter_px'], HEIGHT-60))
            else:
                cimg = pygame.transform.scale(loader.W3_BOL,(767,200+v*3))
                loader.screen.blit(cimg,(player_runtime.INFO['right_fighter_px']-687, HEIGHT-60))

    # 孩子王
    elif attack_code == 3:
        '''
        播放奥特曼动画并释放动感光波
        '''
        va = (timer.get_clock() - lstime)//10
        vb = (timer.get_clock() - lstime)//10
        v1 = vb % 6
        v2 = va % 3
        if attack_turn == 1:
                #光波
                cimg = loader.W4_BOS[v2]
                loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px']-200, HEIGHT))
                if vb<3:
                    # gif
                    dimg = loader.W4_KS[v1]
                    loader.screen.blit(dimg, (player_runtime.INFO['right_fighter_px']-60, HEIGHT - 100))
        else:
                #光波
                cimg = loader.W4_BOS[v2]
                loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], HEIGHT))
                if vb<3:
                    #gif
                    dimg = loader.W4_KS[v1]
                    loader.screen.blit(dimg, (player_runtime.INFO['left_fighter_px'], HEIGHT-100))

    # 武士
    elif attack_code == 4:
        '''
        回旋跳劈,需要隐藏初始角色
        '''

        va = (timer.get_clock() - lstime) * 12
        rot = (timer.get_clock() - lstime) * 36
        bb_text = loader.GAME_ROUND_FONT.render('一刀两断！', True,
                                                color_rgb.BLACK,
                                                None)

        cimg = pygame.transform.rotate(loader.W5_AR, rot)
        if player_runtime.INFO['attack_show_px']-player_runtime.INFO['left_fighter_px']>400:
            loader.screen.blit(cimg,(player_runtime.INFO['attack_show_px'], HEIGHT-va))
            loader.screen.blit(bb_text, (player_runtime.INFO['attack_show_px'],  HEIGHT-va - 120))
        else:
            loader.screen.blit(cimg,(player_runtime.INFO['attack_show_px'], HEIGHT-900+va))
            loader.screen.blit(bb_text, (player_runtime.INFO['attack_show_px'],  HEIGHT-900+va-120))

    # 刺客
    elif attack_code == 5:
        '''
        化为黑影，瞬移背刺。 两个阶段，先旋转缩小，然后背刺回斩。
        '''

        va = (timer.get_clock() - lstime)
        rot = (timer.get_clock() - lstime) * 36
        bb_text = loader.GAME_ROUND_FONT.render('献出心脏吧！', True,
                                                color_rgb.BLACK,
                                                None)
        loader.screen.blit(bb_text, (350, HEIGHT - 120))

        #先设计右边
        if attack_turn==1:
            #第一阶段 边旋转边缩小
            if va<30:
                cimg = pygame.transform.scale(loader.W6_AR,(181-va*6,361-va*12))
                cimg = pygame.transform.rotate(cimg, rot)
                loader.screen.blit(loader.W6_SD, (player_runtime.INFO['left_fighter_px']+80, HEIGHT+50))
                loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px']-80, HEIGHT))
            elif va>=30 and va < 60 :
                va=va-30
                #第二阶段1 瞬移背刺
                loader.screen.blit(loader.W6_AL, (player_runtime.INFO['left_fighter_px']-100+va, HEIGHT-60))
                #剑影
                loader.screen.blit(loader.W6_G1, (0, HEIGHT))
            else:
                va=va-60
                # 第二阶段2 瞬移背刺
                loader.screen.blit(loader.W6_AL, (player_runtime.INFO['left_fighter_px']+va*va, HEIGHT-60))
                # 血光
                loader.screen.blit(loader.W6_G2R, (0, HEIGHT ))
        else:
            # 第一阶段 边旋转边缩小
            if va < 30:
                cimg = pygame.transform.scale(loader.W6_AL, (181 - va * 6, 361 - va * 12))
                cimg = pygame.transform.rotate(cimg, rot)
                loader.screen.blit(loader.W6_SD, (player_runtime.INFO['left_fighter_px']+80, HEIGHT+50))
                loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'] +30, HEIGHT))
            elif va >= 30 and va < 60:
                va = va - 30
                # 第二阶段1 瞬移背刺
                loader.screen.blit(loader.W6_AR, (player_runtime.INFO['right_fighter_px']+100 -va, HEIGHT - 60))
                # 剑影
                loader.screen.blit(loader.W6_G1, (0, HEIGHT))
            else:
                va = va - 60
                # 第二阶段2 瞬移背刺
                loader.screen.blit(loader.W6_AR, (player_runtime.INFO['right_fighter_px'] - va * va, HEIGHT - 60))
                # 血光
                loader.screen.blit(loader.W6_G2L, (0, HEIGHT))

    # 猎人
    elif attack_code == 6:
        '''
        射个光箭就好
        '''
        va = (timer.get_clock() - lstime) * 20
        vb = (timer.get_clock() - lstime) // 3
        vc = vb%5


        bb_text = loader.GAME_ROUND_FONT.render('哼哼，猎物', True,
                                                color_rgb.BLACK,
                                                None)

        if attack_turn == 1:
            loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT - 60))
        else:
            loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 60))

        for x in range(1, 6):
            if attack_turn == 1:
                cimg = pygame.transform.rotate(loader.W7_GS[vc],90)
                loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px']+x*140-va, HEIGHT+20))
            else:
                cimg = pygame.transform.rotate(loader.W7_GS[vc], -90)
                loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'] - x * 140 + va, HEIGHT + 20))
    # 僵尸
    elif attack_code == 7:
        '''
        跳过去抓一下 就好  简单点
        '''
        va = (timer.get_clock() - lstime) * 16
        bb_text = loader.GAME_ROUND_FONT.render('小葵陪我玩 ！', True,
                                                color_rgb.BLACK,
                                                None)

        if attack_turn==1:
            cimg = pygame.transform.scale(loader.R8_5,(96,182))
            if player_runtime.INFO['attack_show_px'] - player_runtime.INFO['left_fighter_px'] > 400:
                loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], HEIGHT - va))
                loader.screen.blit(bb_text, (player_runtime.INFO['attack_show_px'], HEIGHT - va - 120))
            elif player_runtime.INFO['attack_show_px'] - player_runtime.INFO['left_fighter_px'] > 250 and player_runtime.INFO['attack_show_px'] - player_runtime.INFO['left_fighter_px'] <=400:
                loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], HEIGHT - 900 + va))
                loader.screen.blit(bb_text, (player_runtime.INFO['attack_show_px'], HEIGHT - 900 + va - 120))
            else:
                loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], HEIGHT - 900 + va))
                loader.screen.blit(bb_text, (player_runtime.INFO['attack_show_px'], HEIGHT - 900 + va - 120))
                loader.screen.blit(loader.W8_GR,(player_runtime.INFO['left_fighter_px'],HEIGHT))
        else:
            cimg = pygame.transform.scale(loader.R8_9,(96,182))
            if player_runtime.INFO['right_fighter_px'] - player_runtime.INFO['attack_show_px'] > 400:
                loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], HEIGHT - va))
                loader.screen.blit(bb_text, (player_runtime.INFO['attack_show_px'], HEIGHT - va - 120))
            elif player_runtime.INFO['right_fighter_px'] - player_runtime.INFO['attack_show_px'] > 250 and \
                    player_runtime.INFO['right_fighter_px'] - player_runtime.INFO['attack_show_px'] <= 400:
                loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], HEIGHT - 900 + va))
                loader.screen.blit(bb_text, (player_runtime.INFO['attack_show_px'], HEIGHT - 900 + va - 120))
            else:
                loader.screen.blit(cimg, (player_runtime.INFO['attack_show_px'], HEIGHT - 900 + va))
                loader.screen.blit(bb_text, (player_runtime.INFO['attack_show_px'], HEIGHT - 900 + va - 120))
                loader.screen.blit(loader.W8_GL, (player_runtime.INFO['right_fighter_px'], HEIGHT))

    # 吸血鬼
    elif attack_code == 8:
        '''
        吸血特效
        '''
        va = (timer.get_clock() - lstime)//5
        v = va % 3

        bb_text = loader.GAME_ROUND_FONT.render('嘻嘻，榨干你', True,
                                                color_rgb.BLACK,
                                                None)
        if attack_turn == 1:
            loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT - 60))
            cimg = loader.W9S[v]
            loader.screen.blit(cimg, (80, HEIGHT -200))
        else:
            loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 60))
            cimg = loader.W9SB[v]
            loader.screen.blit(cimg, (80, HEIGHT - 200))
    #屠夫 菜刀斩
    elif attack_code==10:
         '''
         菜刀变大，然后劈下去 
         '''
         va = (timer.get_clock() - lstime)
         bb_text = loader.GAME_ROUND_FONT.render('小猪崽子', True,
                                                 color_rgb.BLACK,
                                                 None)
         if attack_turn == 1:
             loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT - 60))
             if va < 45:
                 cimg = pygame.transform.rotate(loader.CAIDAO, -90)
                 cimg = pygame.transform.scale(cimg, (va * 10, va * 10))
                 loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'], HEIGHT - va * 8))
             else:
                 cimg = pygame.transform.rotate(loader.CAIDAO, -90+(va-45)*20)
                 cimg = pygame.transform.scale(cimg, (600, 600))
                 loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'], 60))
         else:
             loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 60))
             if va < 45:
                 cimg = pygame.transform.rotate(loader.CAIDAOL, 90)
                 cimg = pygame.transform.scale(cimg, (va * 10, va * 10))
                 loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px']-300, HEIGHT - va * 8))
             else:
                 cimg = pygame.transform.rotate(loader.CAIDAOL, 90-(va-45)*20)
                 cimg = pygame.transform.scale(cimg, (600, 600))
                 loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px']-300, 60))

    #女巫
    elif attack_code ==11:
        '''
        陨石术
        '''
        va = (timer.get_clock() - lstime)
        vb = va//4
        vc = vb%6

        bb_text = loader.GAME_ROUND_FONT.render('寸草不生！', True,
                                                color_rgb.BLACK,
                                                None)
        if attack_turn == 1:
            cimg = loader.W12S[vc]
            loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT - 60))
            loader.screen.blit(cimg,(800-va*12,va*5))
        else:
            cimg = pygame.transform.flip(loader.W12S[vc],True,False)
            loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 60))
            loader.screen.blit(cimg,(va*12-40,va*5))

    # 狼人
    elif attack_code == 12:
        '''
        变身 冲过去抓一下 
        '''
        v = (timer.get_clock() - lstime)
        va = v // 8
        vb = va%2
        bb_text = loader.GAME_ROUND_FONT.render('尝尝利爪 ！', True,
                                                color_rgb.BLACK,
                                                None)
        if attack_turn == 1:
            cimg = loader.W13
            loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px']+100, HEIGHT-200))
            loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 240))
            if vb == 0:
                loader.screen.blit(loader.W8_GL, (player_runtime.INFO['left_fighter_px'], HEIGHT))
            else:
                loader.screen.blit(loader.W8_GR, (player_runtime.INFO['left_fighter_px'], HEIGHT))
        else:
            cimg = pygame.transform.flip(loader.W13, True,False)
            loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px']-260, HEIGHT-260))
            loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT  - 240))
            if vb==0:
                loader.screen.blit(loader.W8_GL, (player_runtime.INFO['right_fighter_px'], HEIGHT))
            else:
                loader.screen.blit(loader.W8_GR, (player_runtime.INFO['right_fighter_px'], HEIGHT))

    # 骑士
    elif attack_code == 13:
        '''
        变身 冲过去戳一下 
        '''
        v = (timer.get_clock() - lstime)//4
        bb_text = loader.GAME_ROUND_FONT.render('冲锋！', True,
                                                color_rgb.BLACK,
                                                None)
        if attack_turn == 1:
            loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 240))
            cimg = loader.W14
            loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'] + 100-v*v, HEIGHT-150 ))

        else:
            loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT - 240))
            cimg = pygame.transform.flip(loader.W14, True, False)
            loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px']-700+v*v, HEIGHT-150 ))

    # 国王 炮火掩护
    elif attack_code == 14:
        '''
        一群大炮
        '''
        v = (timer.get_clock() - lstime)
        bb_text = loader.GAME_ROUND_FONT.render('王之怒火', True,
                                                color_rgb.BLACK,
                                                None)
        if attack_turn == 1:
            loader.screen.blit(bb_text, (player_runtime.INFO['right_fighter_px'], HEIGHT - 60))
            if v<45:
                cimg = loader.W151
                loader.screen.blit(cimg, (120,0))
            else:
                cimg = loader.W152
                loader.screen.blit(cimg, (120, 0))
        else:
            loader.screen.blit(bb_text, (player_runtime.INFO['left_fighter_px'], HEIGHT - 60))
            if v<45:
                cimg = pygame.transform.flip(loader.W151,True,False)
                loader.screen.blit(cimg, (120,0))
            else:
                cimg = pygame.transform.flip(loader.W152,True,False)
                loader.screen.blit(cimg, (120, 0))

    # 怪兽基多拉
    elif attack_code == 15:
        '''
        化身三头基多拉，破坏死光
        '''
        v = (timer.get_clock() - lstime)
        bb_text = loader.GAME_ROUND_FONT.render('破坏死光', True,
                                                color_rgb.BLACK,
                                                None)
        loader.screen.blit(bb_text, (400, 200))
        if attack_turn == 1:
            if v < 8:
                cimg = loader.W161
                loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px']-300, HEIGHT-200))
            elif v>=10 and v<48:
                vc = v%2
                cimg = loader.W16S[vc]
                loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px']-300, HEIGHT-200))
            elif v>=48 and v<56:
                cimg = loader.W164
                loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px'] - 300, HEIGHT-200))
            elif v >= 56 and v < 62:
                cimg = loader.W165
                loader.screen.blit(cimg, (player_runtime.INFO['right_fighter_px'] - 300, HEIGHT-200))
            elif v > 62:
                vc = v%2
                cimg = loader.W166
                loader.screen.blit(cimg, (120 ,vc*50))
        else:
            if v < 8:
                cimg = pygame.transform.flip(loader.W161,True,False)
                loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'], HEIGHT-200))
            elif v>=10 and v<48:
                vc = v%2
                cimg = pygame.transform.flip(loader.W16S[vc],True,False)
                loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'], HEIGHT-200))
            elif v>=48 and v<56:
                cimg = pygame.transform.flip(loader.W164,True,False)
                loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'] , HEIGHT-200))
            elif v >= 56 and v < 62:
                cimg = pygame.transform.flip(loader.W165,True,False)
                loader.screen.blit(cimg, (player_runtime.INFO['left_fighter_px'] , HEIGHT-200))
            elif v > 62:
                vc = v%2
                cimg = pygame.transform.flip(loader.W166,True,False)
                loader.screen.blit(cimg, (120, vc*50))
    else:
        loader.screen.blit(loader.ATTACK, (player_runtime.INFO['attack_show_px'], HEIGHT))



