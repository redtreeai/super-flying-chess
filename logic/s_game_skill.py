# -*- coding: utf-8 -*-
# @Time    : 19-9-9 下午5:09
# @Author  : Redtree
# @File    : s_game_skill.py
# @Desc : 技能操作


from logic import loader
from data import player_runtime
from data import color_rgb
from utils import timer
import pygame
import random

def dojob(x,y,is_mouse_down,keys):
    '''

    :param x:
    :param y:
    :param is_mouse_down:
    :param keys:
    :param event: 技能事件，特殊标注
    :return:
    '''

    '''
    优先处理event，后处理个别英雄技能事件
    '''

    if player_runtime.INFO['event']=='angel_back':
        if player_runtime.INFO['act_skill'] == True:
            loader.screen.blit(loader.BACK_ANGS[player_runtime.INFO['ts_back_index']],
                               (500, player_runtime.INFO['ts_back_y']))

            player_runtime.INFO['ts_back_y'] = player_runtime.INFO['ts_back_y'] - 5
            if player_runtime.INFO['ts_back_y'] < -120:
                zz_index = 0
                z_index = 0
                for zz in player_runtime.INFO['zdata']:
                    for z in zz:
                        if z['code'] == 9:
                            # 关闭in_skill
                            player_runtime.INFO['zdata'][zz_index][z_index]['hp'] = 0
                            player_runtime.INFO['in_skill'] = False
                            player_runtime.INFO['act_skill'] = False
                            player_runtime.INFO['event']='nothing'
                            player_runtime.INFO['stage'] = 5
                            break
                        z_index = z_index + 1
                    z_index = 0
                    zz_index = zz_index + 1

        else:
            player_runtime.INFO['in_skill']=True
            zz_index = 0
            z_index = 0
            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['code'] == 9:
                        # 先离开界面
                        player_runtime.INFO['ts_back_y'] = 340
                        # 开启动画
                        player_runtime.INFO['act_skill'] = True
                        break
                    z_index = z_index + 1
                z_index = 0
                zz_index = zz_index + 1
    #狙击手
    elif player_runtime.INFO['moving_code']==6:

        if player_runtime.INFO['act_skill']==True:
            # 显示伤害字符
            dm_text = loader.GAME_ROUND_FONT.render('1', True,
                                                    color_rgb.RED,
                                                    None)
            loader.screen.blit(dm_text,(player_runtime.INFO['hit_sk_px'],player_runtime.INFO['hit_sk_py']))
            player_runtime.INFO['hit_sk_py']= player_runtime.INFO['hit_sk_py']-1

            if player_runtime.INFO['hit_sk_py']<= player_runtime.INFO['hit_sk_pya']:
               #伤害结算
               player_runtime.INFO['zdata'][player_runtime.INFO['shr_index'][0]][player_runtime.INFO['shr_index'][1]]['hp']= player_runtime.INFO['zdata'][player_runtime.INFO['shr_index'][0]][player_runtime.INFO['shr_index'][1]]['hp']-1
               #进入下个阶段
               #关闭in_skill
               player_runtime.INFO['in_skill']=False
               player_runtime.INFO['act_skill']=False
               player_runtime.INFO['stage']=5

        else:
            #遮盖基地
            loader.screen.blit(loader.WUYUN,(118,56))
            loader.screen.blit(loader.WUYUN,(646,56))
            loader.screen.blit(loader.WUYUN,(118,584))
            loader.screen.blit(loader.WUYUN,(646,584))

            # 要攻击的目标是
            hit_code = -1

            #捕获棋子坐标
            map_sx = 118
            map_sy = 56

            cpx = int((x-map_sx)/48)
            cpy = int((y-map_sy)/48)

            #
            zz_index = 0
            z_index = 0
            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['in_war']==True and z['gowin']==False and z['px']==cpx and z['py']==cpy:
                        hit_code=z['code']
                        loader.screen.blit(loader.SK7, (map_sx-23 + cpx * 48, map_sy-22 + cpy * 48))
                        player_runtime.INFO['shr_index'] = (zz_index,z_index)

                    z_index = z_index + 1
                z_index = 0
                zz_index = zz_index + 1

            if is_mouse_down==True:
                if hit_code<0:
                    player_runtime.INFO['in_skill']=False
                else:
                    #狙杀效果播放
                    player_runtime.INFO['act_skill']=True
                    player_runtime.INFO['hit_sk_px']=map_sx+12 + cpx * 48
                    player_runtime.INFO['hit_sk_py']=map_sy-22 + cpy * 48
                    player_runtime.INFO['hit_sk_pya'] = map_sy - 62 + cpy * 48

                    #开枪后进入冷却
                    player_runtime.INFO['lr_power']= -1


    #天使
    elif player_runtime.INFO['moving_code']==9:
        if player_runtime.INFO['act_skill'] == True:
            # 显示伤害字符
            dm_text = loader.GAME_ROUND_FONT.render('2', True,
                                                    color_rgb.GREEN,
                                                    None)
            loader.screen.blit(dm_text, (player_runtime.INFO['hit_sk_px'], player_runtime.INFO['hit_sk_py']))
            player_runtime.INFO['hit_sk_py'] = player_runtime.INFO['hit_sk_py'] - 1

            if player_runtime.INFO['hit_sk_py'] <= player_runtime.INFO['hit_sk_pya']:
                # 伤害结算
                player_runtime.INFO['zdata'][player_runtime.INFO['shr_index'][0]][player_runtime.INFO['shr_index'][1]][
                    'hp'] = \
                player_runtime.INFO['zdata'][player_runtime.INFO['shr_index'][0]][player_runtime.INFO['shr_index'][1]][
                    'hp'] + 2
                # 关闭in_skill
                player_runtime.INFO['in_skill'] = False
                player_runtime.INFO['act_skill'] = False
                player_runtime.INFO['stage'] = 5

        else:
            # 遮盖基地
            loader.screen.blit(loader.AIXIN, (118, 56))
            loader.screen.blit(loader.AIXIN, (646, 56))
            loader.screen.blit(loader.AIXIN, (118, 584))
            loader.screen.blit(loader.AIXIN, (646, 584))

            # 要攻击的目标是
            hit_code = -1

            # 捕获棋子坐标
            map_sx = 118
            map_sy = 56

            cpx = int((x - map_sx) / 48)
            cpy = int((y - map_sy) / 48)

            zz_index = 0
            z_index = 0
            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['in_war'] == True and z['gowin'] == False and z['px'] == cpx and z['py'] == cpy:
                        hit_code = z['code']
                        loader.screen.blit(loader.XIANNVBANG, (map_sx - 23 + cpx * 48, map_sy - 22 + cpy * 48))
                        player_runtime.INFO['shr_index'] = (zz_index, z_index)

                    z_index = z_index + 1
                z_index = 0
                zz_index = zz_index + 1

            if is_mouse_down == True:
                if hit_code < 0:
                    player_runtime.INFO['in_skill'] = False
                else:
                    # 狙杀效果播放
                    player_runtime.INFO['act_skill'] = True
                    player_runtime.INFO['hit_sk_px'] = map_sx + 12 + cpx * 48
                    player_runtime.INFO['hit_sk_py'] = map_sy - 22 + cpy * 48
                    player_runtime.INFO['hit_sk_pya'] = map_sy - 62 + cpy * 48

                    # 治疗后进入冷却
                    player_runtime.INFO['ts_power'] = -1

    #屠夫
    elif player_runtime.INFO['moving_code'] == 10:
        if player_runtime.INFO['act_skill'] == True:

            # 遮盖基地
            loader.screen.blit(loader.WUDICAIDAO, (118, 56))
            loader.screen.blit(loader.WUDICAIDAO, (646, 56))
            loader.screen.blit(loader.WUDICAIDAO, (118, 584))
            loader.screen.blit(loader.WUDICAIDAO, (646, 584))

            #先播放飞刀动画，再结算伤害(四向飞刀)
            caidao_img1 = pygame.transform.rotate(loader.CAIDAO,30)
            caidao_img2 = pygame.transform.rotate(loader.CAIDAO,120)
            caidao_img3 = pygame.transform.rotate(loader.CAIDAO,210)
            caidao_img4 = pygame.transform.rotate(loader.CAIDAO,-60)

            #速度后面再调看看 4/7
            wtime = (timer.get_clock()-player_runtime.INFO['tf_lstime'])*6
            loader.screen.blit(caidao_img1,(player_runtime.INFO['tf_spx']-wtime,player_runtime.INFO['tf_spy']))
            loader.screen.blit(caidao_img2,(player_runtime.INFO['tf_spx'],player_runtime.INFO['tf_spy']+wtime))
            loader.screen.blit(caidao_img3,(player_runtime.INFO['tf_spx']+wtime,player_runtime.INFO['tf_spy']))
            loader.screen.blit(caidao_img4,(player_runtime.INFO['tf_spx'],player_runtime.INFO['tf_spy']-wtime))

            #标准坐标
            map_sx = 118
            map_sy = 56
            #提前标血
            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['code'] in player_runtime.INFO['tfl_code']:
                        cspx =map_sx+48* z['px']+12
                        cspy =map_sy+48* z['py']-22

                        #国王伤害为1
                        if z['code']==14:
                         dm_text = loader.GAME_ROUND_FONT.render('1', True,
                                                                color_rgb.RED,
                                                                None)
                        else:
                            dm_text = loader.GAME_ROUND_FONT.render('2', True,
                                                                    color_rgb.RED,
                                                                    None)
                        loader.screen.blit(dm_text,(cspx,cspy))


            #飞刀飞过，hp掉落
            if wtime>1040:
                zz_index = 0
                z_index = 0
                for zz in player_runtime.INFO['zdata']:
                    for z in zz:
                        #伤害结算
                        if z['code'] in player_runtime.INFO['tfl_code']:
                            #国王伤害恒为1
                            if z['code']==14:
                                player_runtime.INFO['zdata'][zz_index][z_index]['hp']= player_runtime.INFO['zdata'][zz_index][z_index]['hp']-1
                            else:
                                player_runtime.INFO['zdata'][zz_index][z_index]['hp']= player_runtime.INFO['zdata'][zz_index][z_index]['hp']-2

                        z_index = z_index + 1
                    z_index = 0
                    zz_index = zz_index + 1
                # 关闭in_skill
                #重置
                player_runtime.INFO['tfl_code'] = []
                player_runtime.INFO['in_skill'] = False
                player_runtime.INFO['act_skill'] = False
                player_runtime.INFO['stage'] = 5

        else:
            #屠夫的逻辑稍微复杂点，要先确定屠夫的坐标，再找出所有攻击对象

            tfx = 0
            tfy = 0
            map_sx = 118
            map_sy = 56
            #1 先获取屠夫坐标
            zz_index = 0
            z_index = 0
            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    #
                    if z['code']==10:
                        #获取屠夫坐标
                        tfx = z['px']
                        tfy = z['py']
                        player_runtime.INFO['tf_spx']=map_sx+48*tfx
                        player_runtime.INFO['tf_spy']=map_sy+48*tfy
                        break

                    z_index = z_index + 1
                z_index = 0
                zz_index = zz_index + 1

            #2 获取攻击对象代码

            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    #十字线坐标上
                    if (z['px']==tfx or z['py']==tfy) and not z['code']==10 and z['in_war']==True and z['gowin']==False:
                        player_runtime.INFO['tfl_code'].append(z['code'])

            #时间定位
            player_runtime.INFO['tf_lstime']=timer.get_clock()
            player_runtime.INFO['tf_power'] = player_runtime.INFO['tf_power']-1
            player_runtime.INFO['act_skill'] = True

    # 女巫
    elif player_runtime.INFO['moving_code'] == 11:
        if player_runtime.INFO['act_skill'] == True:

            # 遮盖基地
            loader.screen.blit(loader.EDUZZ, (118, 56))
            loader.screen.blit(loader.EDUZZ, (646, 56))
            loader.screen.blit(loader.EDUZZ, (118, 584))
            loader.screen.blit(loader.EDUZZ, (646, 584))

            # 先播放诅咒动画，再结算诅咒伤害
            loader.screen.blit(loader.ZUZHOU[player_runtime.INFO['nwzz_index']],(player_runtime.INFO['nw_spx']-100,player_runtime.INFO['nw_spy']-100))

            wtime = (timer.get_clock() - player_runtime.INFO['nwzz_lstime']) * 10

            # 标准坐标
            map_sx = 118
            map_sy = 56
            # 提前标血 (--------------写到这，伤害的随机最好提前在 rinfo里生成)
            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['code'] ==player_runtime.INFO['nw_code']:
                        cspx = map_sx + 48 * z['px'] + 12
                        cspy = map_sy + 48 * z['py'] - 22

                        dm_text = loader.GAME_ROUND_FONT.render(str(player_runtime.INFO['nw_damage']), True,
                                                                    color_rgb.RED,
                                                                    None)
                        loader.screen.blit(dm_text, (cspx, cspy))

            player_runtime.INFO['nwzz_index']=player_runtime.INFO['nwzz_index']+1
            if player_runtime.INFO['nwzz_index']>3:
                player_runtime.INFO['nwzz_index']=0

            # 播放一秒钟后结算伤害
            if wtime > 1040:
                zz_index = 0
                z_index = 0
                for zz in player_runtime.INFO['zdata']:
                    for z in zz:
                        # 伤害结算
                        if z['code'] ==player_runtime.INFO['nw_code']:
                                player_runtime.INFO['zdata'][zz_index][z_index]['hp'] = \
                                player_runtime.INFO['zdata'][zz_index][z_index]['hp'] - player_runtime.INFO['nw_damage']

                        z_index = z_index + 1
                    z_index = 0
                    zz_index = zz_index + 1
                # 关闭in_skill
                # 重置
                player_runtime.INFO['tfl_code'] = []
                player_runtime.INFO['in_skill'] = False
                player_runtime.INFO['act_skill'] = False
                player_runtime.INFO['stage'] = 5

        else:
            # 女巫直接从战场上随机出一个攻击对象即可
            # 1 获取攻击对象
            hit_codes = []
            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['in_war'] == True and z['gowin']==False:
                       hit_codes.append(z['code'])

            player_runtime.INFO['nw_code']=random.choice(hit_codes)

            #2 获取攻击对象坐标
            map_sx = 118
            map_sy = 56
            for zz in player_runtime.INFO['zdata']:
                for z in zz:
                    if z['code'] == player_runtime.INFO['nw_code']:
                        player_runtime.INFO['nw_spx'] = map_sx + 48 *  z['px']
                        player_runtime.INFO['nw_spy'] = map_sy + 48 * z['py']
                        break

            # 时间定位
            player_runtime.INFO['nw_damage']=random.randint(1,3)
            # 国王伤害固定为1
            if player_runtime.INFO['nw_code']==14:
                player_runtime.INFO['nw_damage']=1
            player_runtime.INFO['nwzz_lstime'] = timer.get_clock()
            player_runtime.INFO['act_skill'] = True