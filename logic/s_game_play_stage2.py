# -*- coding: utf-8 -*-
# @Time    : 19-8-29 上午10:07
# @Author  : Redtree
# @File    : s_game_play_stage2.py
# @Desc :   执行移动逻辑阶段


from data import player_runtime
from data import routes
from logic import loader


def dojob():

    # 开始执行角色移动逻辑
    # 1 获取当前队伍编号
    team = player_runtime.INFO['turn']
    # 2 根据队伍编号获取校验路线
    base_route = routes.DATA['base']
    common_route = routes.DATA['common']
    jp_common_route = routes.DATA['jumps_common']
    team_jump_route = []
    team_special_route = []

    # base-->sepcial--->jump---->common
    if team == 0:
        team_jump_route = routes.DATA['jumps_blue']
        team_special_route = routes.DATA['special_blue']
    elif team == 1:
        team_jump_route = routes.DATA['jumps_green']
        team_special_route = routes.DATA['special_green']
    elif team == 2:
        team_jump_route = routes.DATA['jumps_yellow']
        team_special_route = routes.DATA['special_yellow']
    elif team == 3:
        team_jump_route = routes.DATA['jumps_red']
        team_special_route = routes.DATA['special_red']

    # print(player_runtime.INFO['is_moving'],player_runtime.INFO['is_jumping'])

    # 3 开始执行行走逻辑
    # 31 获取当前角色 、位置、方向
    cc_index = 0
    c_index = 0
    for cc in player_runtime.INFO['zdata']:
        for c in cc:
            # 定位英雄
            if c['code'] == player_runtime.INFO['moving_code']:
                if player_runtime.INFO['is_jumping'] == True:
                    # 保持移动
                    SPD = 0.1
                    if c['px'] > player_runtime.INFO['aim_point'][0]:
                        c['px'] = c['px'] - SPD
                    elif c['px'] < player_runtime.INFO['aim_point'][0]:
                        c['px'] = c['px'] + SPD

                    if c['py'] > player_runtime.INFO['aim_point'][1]:
                        c['py'] = c['py'] - SPD
                    elif c['py'] < player_runtime.INFO['aim_point'][1]:
                        c['py'] = c['py'] + SPD

                    if abs(c['px'] - player_runtime.INFO['aim_point'][0]) <= SPD * 2 and abs(
                            c['py'] - player_runtime.INFO['aim_point'][1]) <= SPD * 2:
                        # 强行矫正位置
                        c['px'] = player_runtime.INFO['aim_point'][0]
                        c['py'] = player_runtime.INFO['aim_point'][1]
                        player_runtime.INFO['is_jumping'] = False
                        player_runtime.MUSIC['walk'] = False
                        player_runtime.INFO['stage'] = 3

                elif player_runtime.INFO['is_moving'] == True:
                    # 保持移动
                    SPD = 0.04
                    if c['px'] > player_runtime.INFO['aim_point'][0]:
                        c['px'] = c['px'] - SPD
                        c['faceto']=1
                    elif c['px'] < player_runtime.INFO['aim_point'][0]:
                        c['px'] = c['px'] + SPD
                        c['faceto']=2
                    if c['py'] > player_runtime.INFO['aim_point'][1]:
                        c['py'] = c['py'] - SPD
                        c['faceto']=3
                    elif c['py'] < player_runtime.INFO['aim_point'][1]:
                        c['py'] = c['py'] + SPD
                        c['faceto']=0

                    if abs(c['px'] - player_runtime.INFO['aim_point'][0]) <= SPD * 2 and abs(
                            c['py'] - player_runtime.INFO['aim_point'][1]) <= SPD * 2:
                        # 强行矫正位置
                        c['px'] = player_runtime.INFO['aim_point'][0]
                        c['py'] = player_runtime.INFO['aim_point'][1]

                        #强行矫正方向 (0,2),(10,0),(2,12),(12,10)
                        if (c['px'],c['py']) == (0,2):
                            c['faceto']=0
                        elif (c['px'],c['py']) == (10,0):
                            c['faceto']=1
                        elif (c['px'],c['py']) == (2,12):
                            c['faceto']=2
                        elif (c['px'],c['py']) == (12,10):
                            c['faceto']=3

                        player_runtime.INFO['is_moving'] = False
                        player_runtime.INFO['left_steps'] = player_runtime.INFO['left_steps'] - 1
                        if player_runtime.INFO['left_steps'] < 1:
                            # 执行最后的跳跃逻辑

                            # 1 先校验飞机
                            jump_flag = False
                            for rt in jp_common_route:
                                if (c['px'],c['py']) == rt[0]:
                                    player_runtime.INFO['is_jumping'] = True
                                    player_runtime.INFO['aim_point'] = rt[1]
                                    jump_flag = True
                                    # break
                                    break

                            # 2 校验阵营飞跃
                            for rt in team_jump_route:
                                if (c['px'],c['py']) == rt[0]:
                                    player_runtime.INFO['is_jumping'] = True
                                    player_runtime.INFO['aim_point'] = rt[1]
                                    jump_flag = True
                                    # break
                                    break

                            if jump_flag == False:
                                player_runtime.INFO['stage'] = 3
                else:
                    # (关于方向的修改可能会有bug)
                    # 32 出战验证
                    if c['in_war'] == False:
                        # 未出战角色仅走一步
                        player_runtime.INFO['left_steps'] = 1
                        for rt in base_route:
                            # 行走前确认目标
                            if (c['px'], c['py']) == rt[0]:
                                player_runtime.INFO['aim_point'] = rt[1]
                                player_runtime.INFO['is_moving'] = True
                                # 跳出循环,且出战后改变出战状态
                                c['in_war']=True
                                break

                    else:
                        # 33 已出战后，校验特殊模块
                        special_flag = False

                        # 当前处于特殊路线起点的时候，方向一定要矫正为正向
                        if (c['px'], c['py']) == team_special_route[0]:
                            player_runtime.INFO['zdata'][cc_index][c_index]['direct'] = 1

                        rt_index = 0
                        for rt in team_special_route:
                            # 行走前确认目标
                            if (c['px'], c['py']) == rt:

                                special_flag = True
                                # 如果英雄为正向行进
                                if c['direct'] == 1:
                                    player_runtime.INFO['aim_point'] = team_special_route[rt_index + 1]
                                    player_runtime.INFO['is_moving'] = True

                                    # 位于终点位置
                                    if rt_index + 1 == len(team_special_route) - 1:
                                        c['direct'] = 0
                                else:
                                    player_runtime.INFO['aim_point'] = team_special_route[rt_index - 1]
                                    player_runtime.INFO['is_moving'] = True

                                    # 位于起点位置
                                    if rt_index - 1 == 0:
                                        c['direct'] = 1

                                break
                            rt_index = rt_index +1

                        # 如果触发特殊条件则不进行普通路线校验
                        if special_flag == True:
                            pass
                        else:
                            # 普通路径校验
                            for rt in common_route:
                                # 如果正向行走
                                if c['direct'] == 1:
                                    if (c['px'], c['py']) == rt[0]:
                                        player_runtime.INFO['aim_point'] = rt[1]
                                        player_runtime.INFO['is_moving'] = True
                                        # 跳出
                                        break
                                else:
                                    if (c['px'], c['py']) == rt[1]:
                                        player_runtime.INFO['aim_point'] = rt[0]
                                        player_runtime.INFO['is_moving'] = True
                                        #
                                        break

                # 处理完就跳出循环，增加游戏运行效率
                break
            c_index=c_index+1

        c_index=0
        cc_index=cc_index+1


