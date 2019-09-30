# -*- coding: utf-8 -*-
# @Time    : 19-8-29 上午10:56
# @Author  : Redtree
# @File    : s_game_play_stage3.py
# @Desc :  移动结束后选择执行命令阶段


from logic import loader
from logic import s_game_skill
from logic import s_game_gowin
from data import player_runtime
from data import color_rgb
import pygame
import random
from data import routes


def dojob(x,y,is_mouse_down,keys):

    if keys['tab']==1:
        player_runtime.INFO['inzhankuang'] = True

    if player_runtime.INFO['gowinr']==True:
        s_game_gowin.dojob(x,y,is_mouse_down)
    elif player_runtime.INFO['in_skill']==True:
        s_game_skill.dojob(x,y,is_mouse_down,keys)
    else:
        # 1 判断是否处于死斗状态
        death_fight_flag = False
        for zz in player_runtime.INFO['zdata']:
            for z in zz:
                # 1 不与自己死斗，2与他人重叠触发死斗 3 死斗双方需在战场上
                if player_runtime.INFO['aim_point'] == (z['px'], z['py']) and not z['code'] == player_runtime.INFO[
                    'moving_code'] and z['in_war'] == True:
                    #天使直接返回基地并重置
                    if z['code'] == 9 or player_runtime.INFO['moving_code']==9:
                        #触发天使返回基地的动作
                        player_runtime.INFO['event']='angel_back'
                        s_game_skill.dojob(x, y, is_mouse_down,keys)
                    else:
                        # 开启死斗
                        player_runtime.INFO['death_fight'] = True
                        player_runtime.INFO['common_fight'] = False
                        # 添加死斗名单
                        player_runtime.INFO['fight_list'].append(z['code'])
                        player_runtime.INFO['fight_list'].append(player_runtime.INFO['moving_code'])
                        # 强制跳转到死斗结算环节
                        death_fight_flag = True
                        # 随机选择死斗场景
                        player_runtime.INFO['fight_bg'] = random.randint(0, 2)
                        player_runtime.INFO['fight_stage'] = 0
                        player_runtime.INFO['to_attack_codes'] = []

                        # 如果有剑客，剑客先攻击永远
                        if player_runtime.INFO['fight_list'][0] == 4:
                            tmp_code = player_runtime.INFO['fight_list'][0]
                            player_runtime.INFO['fight_list'][0] = player_runtime.INFO['fight_list'][1]
                            player_runtime.INFO['fight_list'][1] = tmp_code

                        player_runtime.INFO['right_fighter_px'] = 1040
                        player_runtime.INFO['left_fighter_px'] = -180
                        player_runtime.INFO['stage'] = 4
                        break

        # 2 非死斗，则选择正常攻击或释放技能
        if death_fight_flag == False:

            # 是否位于选择攻击对象的页面
            if player_runtime.INFO['to_attack'] == True:
                # 绘制可攻击对象

                t_index = 0
                for tac in player_runtime.INFO['to_attack_codes']:
                    ct = pygame.transform.scale(loader.RMS[tac][0], (90, 85))
                    if t_index == 0:
                        loader.screen.blit(ct, (860, 510))
                    elif t_index == 1:
                        loader.screen.blit(ct, (950, 510))
                    elif t_index == 2:
                        loader.screen.blit(ct, (860, 595))
                    elif t_index == 3:
                        loader.screen.blit(ct, (950, 595))

                    t_index = t_index + 1

                # 额外绘制返回按钮
                loader.screen.blit(loader.BACK, (950, 595))

                # 绘制选择框
                # 1
                if x >= 860 and x < 950 and y >= 510 and y < 595 and len(player_runtime.INFO['to_attack_codes']) > 0:
                    show_help(['选择决斗对象'])
                    loader.screen.blit(loader.SELECT_MENU, (860, 510))
                    if is_mouse_down == True:
                        # 开启普通决斗
                        player_runtime.INFO['common_fight'] = True
                        player_runtime.INFO['death_fight'] = False
                        # 添加决斗名单
                        player_runtime.INFO['fight_list'].append(player_runtime.INFO['to_attack_codes'][0])
                        player_runtime.INFO['fight_list'].append(player_runtime.INFO['moving_code'])
                        # 随机选择决斗场景
                        player_runtime.INFO['fight_bg'] = random.randint(0, 2)
                        player_runtime.INFO['left_fighter_px'] = -180
                        player_runtime.INFO['right_fighter_px'] = 1040
                        player_runtime.INFO['fight_stage'] = 0
                        # 如果有剑客，剑客先攻击永远
                        if player_runtime.INFO['fight_list'][0] == 4:
                            tmp_code = player_runtime.INFO['fight_list'][0]
                            player_runtime.INFO['fight_list'][0] = player_runtime.INFO['fight_list'][1]
                            player_runtime.INFO['fight_list'][1] = tmp_code
                        player_runtime.INFO['right_fighter_px'] = 1040
                        player_runtime.INFO['left_fighter_px'] = -180
                        player_runtime.INFO['stage'] = 4
                        player_runtime.INFO['to_attack_codes'] = []

                # 2
                elif x >= 950 and x < 1040 and y >= 510 and y < 595 and len(player_runtime.INFO['to_attack_codes']) > 1:
                    show_help(['选择决斗对象'])
                    loader.screen.blit(loader.SELECT_MENU, (950, 510))
                    if is_mouse_down == True:
                        # 开启普通决斗
                        player_runtime.INFO['common_fight'] = True
                        player_runtime.INFO['death_fight'] = False
                        # 添加决斗名单
                        player_runtime.INFO['fight_list'].append(player_runtime.INFO['to_attack_codes'][1])
                        player_runtime.INFO['fight_list'].append(player_runtime.INFO['moving_code'])
                        # 随机选择决斗场景
                        player_runtime.INFO['fight_bg'] = random.randint(0, 2)
                        player_runtime.INFO['left_fighter_px'] = -180
                        player_runtime.INFO['right_fighter_px'] = 1040
                        player_runtime.INFO['fight_stage'] = 0
                        # 如果有剑客，剑客先攻击永远
                        if player_runtime.INFO['fight_list'][0] == 4:
                            tmp_code = player_runtime.INFO['fight_list'][0]
                            player_runtime.INFO['fight_list'][0] = player_runtime.INFO['fight_list'][1]
                            player_runtime.INFO['fight_list'][1] = tmp_code
                        player_runtime.INFO['right_fighter_px'] = 1040
                        player_runtime.INFO['left_fighter_px'] = -180
                        player_runtime.INFO['stage'] = 4
                        player_runtime.INFO['to_attack_codes'] = []

                # 3 最多3个物理攻击对象
                elif x >= 860 and x < 950 and y >= 595 and y < 680 and len(player_runtime.INFO['to_attack_codes']) > 2:
                    show_help(['选择决斗对象'])
                    loader.screen.blit(loader.SELECT_MENU, (860, 595))
                    if is_mouse_down == True:
                        # 开启普通决斗
                        player_runtime.INFO['common_fight'] = True
                        player_runtime.INFO['death_fight'] = False
                        # 添加决斗名单
                        player_runtime.INFO['fight_list'].append(player_runtime.INFO['to_attack_codes'][2])
                        player_runtime.INFO['fight_list'].append(player_runtime.INFO['moving_code'])
                        # 随机选择决斗场景
                        player_runtime.INFO['fight_bg'] = random.randint(0, 2)
                        player_runtime.INFO['left_fighter_px'] = -180
                        player_runtime.INFO['right_fighter_px'] = 1040
                        player_runtime.INFO['fight_stage'] = 0
                        # 如果有剑客，剑客先攻击永远
                        if player_runtime.INFO['fight_list'][0] == 4:
                            tmp_code = player_runtime.INFO['fight_list'][0]
                            player_runtime.INFO['fight_list'][0] = player_runtime.INFO['fight_list'][1]
                            player_runtime.INFO['fight_list'][1] = tmp_code
                        player_runtime.INFO['right_fighter_px'] = 1040
                        player_runtime.INFO['left_fighter_px'] = -180
                        player_runtime.INFO['stage'] = 4
                        player_runtime.INFO['to_attack_codes'] = []
                # 4 返回图标
                elif x >= 950 and x < 1040 and y >= 595 and y < 680:
                    loader.screen.blit(loader.SELECT_MENU, (950, 595))
                    show_help(['返回'])
                    if is_mouse_down == True:
                        # 返回攻击选择
                        player_runtime.INFO['to_attack'] = False

            else:
                # 绘制操作菜单
                ## 1 攻击(仅当附近存在攻击对象时)

                # 获取当前玩家位置
                cpx = player_runtime.INFO['aim_point'][0]
                cpy = player_runtime.INFO['aim_point'][1]

                #如果位于终点
                if (cpx,cpy)==(6, 6):
                    #进入奖励结算
                    player_runtime.INFO['gowinr']=True
                else:
                    # 重置攻击玩家名单
                    player_runtime.INFO['to_attack_codes'] = []

                    # 天使无法攻击
                    if not player_runtime.INFO['moving_code'] == 9:
                        for zz in player_runtime.INFO['zdata']:
                            for z in zz:
                                # 校验附近玩家的存在
                                # print(z['px'],z['py'],cpx,cpy)

                                if abs(z['px'] - cpx) + abs(z['py'] - cpy) == 1 and z['in_war'] == True and z[
                                    'gowin'] == False and not z['code'] == 9:
                                    player_runtime.INFO['to_attack_codes'].append(z['code'])

                    if len(player_runtime.INFO['to_attack_codes']) > 0:
                        loader.screen.blit(loader.ATTACK, (860, 510))
                    ## 2 技能
                    ski = check_skill_icon()
                    loader.screen.blit(ski, (950, 510))
                    ## 3 防守 跳过回合
                    loader.screen.blit(loader.DEFEND, (860, 595))

                    # 绘制选中框(英雄行为交互)
                    # 1
                    if x >= 860 and x < 950 and y >= 510 and y < 595 and len(
                            player_runtime.INFO['to_attack_codes']) > 0:
                        loader.screen.blit(loader.SELECT_MENU, (860, 510))
                        show_help(['发起决斗'])
                        if is_mouse_down == True:
                            player_runtime.INFO['to_attack'] = True
                    # 2
                    elif x >= 950 and x < 1040 and y >= 510 and y < 595:
                        loader.screen.blit(loader.SELECT_MENU, (950, 510))
                        skill_help()
                        if is_mouse_down == True:
                            # 清算技能效果
                            check_skill_action()
                    # 3
                    elif x >= 860 and x < 950 and y >= 595 and y < 680:
                        loader.screen.blit(loader.SELECT_MENU, (860, 595))
                        show_help(['行动结束'])
                        if is_mouse_down == True:
                            # 技能不结算，直接跳到5
                            player_runtime.INFO['to_attack_codes'] = []
                            player_runtime.INFO['stage'] = 5


def check_skill_icon():
    return loader.SKI[player_runtime.INFO['moving_code']]



def check_skill_action():
    #直接触发程序员调转方向
    if player_runtime.INFO['moving_code']==0:
        bflag = False
        zz_index = 0
        z_index = 0
        for zz in player_runtime.INFO['zdata']:
            for z in zz:
                if z['code']==0 and not (z['px'],z['py']) in [(0,2),(10,0),(2,12),(12,10)]:
                    bflag=True
                    if z['direct']==1:
                        player_runtime.INFO['zdata'][zz_index][z_index]['direct']=0
                    else:
                        player_runtime.INFO['zdata'][zz_index][z_index]['direct']=1

                    if z['faceto']==0:
                        player_runtime.INFO['zdata'][zz_index][z_index]['faceto']=3
                    elif z['faceto']==1:
                        player_runtime.INFO['zdata'][zz_index][z_index]['faceto']=2
                    elif z['faceto'] == 2:
                        player_runtime.INFO['zdata'][zz_index][z_index]['faceto'] = 1
                    elif z['faceto'] == 3:
                        player_runtime.INFO['zdata'][zz_index][z_index]['faceto'] = 0

                    break
                z_index = z_index + 1
            z_index = 0
            zz_index = zz_index + 1

            if bflag==True:
                break

        # 技能不结算，直接跳到5
        player_runtime.INFO['to_attack_codes'] = []
        player_runtime.INFO['stage'] = 5

    #科学家
    elif player_runtime.INFO['moving_code']==2:
        bflag = False
        zz_index = 0
        z_index = 0
        for zz in player_runtime.INFO['zdata']:
            for z in zz:
                if z['code'] == 2 :
                    bflag = True
                    player_runtime.INFO['zdata'][zz_index][z_index]['hp'] = player_runtime.INFO['zdata'][zz_index][z_index]['hp']-1
                    rdp = random.choice(routes.DATA['common'])[0]
                    player_runtime.INFO['zdata'][zz_index][z_index]['px']=rdp[0]
                    player_runtime.INFO['zdata'][zz_index][z_index]['py']=rdp[1]
                    break
                z_index = z_index + 1
            z_index = 0
            zz_index = zz_index + 1

            if bflag == True:
                break

        # 技能不结算，直接跳到5
        player_runtime.INFO['to_attack_codes'] = []
        player_runtime.INFO['stage'] = 5
    elif player_runtime.INFO['moving_code']==6 and player_runtime.INFO['lr_power']==2:
        #猎人，跳转到专属页面
        player_runtime.INFO['in_skill']=True
    elif player_runtime.INFO['moving_code']==9 and player_runtime.INFO['ts_power']==3:
        #天使，跳转到专属页面
        player_runtime.INFO['in_skill']=True
    elif player_runtime.INFO['moving_code'] == 10 and player_runtime.INFO['tf_power'] > 0:
        # 屠夫，跳转到专属页面
        player_runtime.INFO['in_skill'] = True
    elif player_runtime.INFO['moving_code'] == 11 :
        # 女巫，跳转到专属页面
        player_runtime.INFO['in_skill'] = True
    else:
        pass

#创造提示  每行8个字
def show_help(text):
    mx = 860
    my = 340

    t_index = 1
    for t in text:
        mtext = loader.GAME_TEXT_FONT.render(t, True,
                                                 color_rgb.BLACK,
                                                 None)
        loader.screen.blit(mtext, (mx+10, my+20*t_index))
        t_index = t_index+1

#技能描述
def skill_help():
    cd = player_runtime.INFO['moving_code']
    if cd==0:
        show_help(['逆向思维','调整移动方向为反','方向'])
    elif cd==1:
        show_help(['被动:无敌可爱','决斗或死斗过程中','每次受到伤害结算','前百分之20概率','免疫本次伤害'])
    elif cd == 2:
        show_help(['伟大发明', '对自己造成1点伤', '害然后移动到随机','位置'])
    elif cd == 3:
        show_help(['被动:幸福追求', '与怪兽决斗时', '攻击力*5'])
    elif cd == 4:
        show_help(['被动:决斗大师', '决斗或死斗中','永远先手攻击'])
    elif cd == 5:
        show_help(['被动：心眼爆破', '刺客的攻击无视','防御力'])
    elif cd == 6:
        if player_runtime.INFO['lr_power']==2:
            show_help(['狙击(充能完毕)','对战场上任意角色','造成1点伤害'])
        elif player_runtime.INFO['lr_power']==1:
            show_help(['狙击（充能中）', '对战场上任意角色', '造成1点伤害,行动', '1次后重置技能'])
        elif player_runtime.INFO['lr_power'] == 0:
            show_help(['狙击（充能中）', '对战场上任意角色', '造成1点伤害,行动', '2次后重置技能'])
    elif cd == 7:
        show_help(['见不得光','僵尸白天无法行动'])
    elif cd == 8:
        show_help(['血源秘法','每次移动结束后','增加自身血量1'])
    elif cd == 9:
        if player_runtime.INFO['ts_power']==3:
            show_help(['隐形守护者','（被动）无法触发战','斗,触发死斗前','在基地重生（主动）','回复战场任一角色','2hp'])
        elif player_runtime.INFO['ts_power'] == 2:
            show_help(['隐形守护者','（被动）无法触发战','斗,触发死斗前','在基地重生（主动）','回复战场任一角色','2hp,1次行动','后充能'])
        elif player_runtime.INFO['ts_power'] == 1:
            show_help(['隐形守护者','（被动）无法触发战','斗,触发死斗前','在基地重生（主动）','回复战场任一角色','2hp,2次行动','后充能'])
        elif player_runtime.INFO['ts_power'] == 0:
            show_help(['隐形守护者','（被动）无法触发战','斗,触发死斗前','在基地重生（主动）','回复战场任一角色','2hp,3次行动','后充能'])
    elif cd == 10:
        #补充说明
        if player_runtime.INFO['tf_power']==2:
            show_help(['小胖飞刀','对以自己为中心的','十字线上角色造成','2点伤害,可用2次','，复活重置次数'])
        elif player_runtime.INFO['tf_power']==1:
            show_help(['小胖飞刀','对以自己为中心的','十字线上角色造成','2点伤害,可用1次','，复活重置次数'])
        elif player_runtime.INFO['tf_power'] == 0:
            show_help(['小胖飞刀', '对以自己为中心的', '十字线上角色造成', '2点伤害,可用0次', '，复活重置次数'])
    elif cd == 11:
        show_help(['死亡诅咒', '对战场上随机角色','造成1~3点伤害,','可能击中自己'])
    elif cd ==12:
        show_help(['黑夜王者','夜晚攻击力翻倍'])
    elif cd == 13:
        show_help(['战术迂回', '骑士发起决斗后，','阵营额外行动一次'])
    elif cd == 14:
        show_help(['权利庇护', '国王每次受到伤害不超过1点'])
    elif cd ==15:
        show_help(['天生仇恨','被动决斗或死斗','时防御翻倍'])