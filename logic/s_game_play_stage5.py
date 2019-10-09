# -*- coding: utf-8 -*-
# @Time    : 19-8-30 下午5:00
# @Author  : Redtree
# @File    : s_game_play_stage5.py
# @Desc : 结算阶段


from data.heros import hrs
from data import player_runtime
import copy


def dojob():

   zd_index = 0
   z_index = 0

   for zz in player_runtime.INFO['zdata']:
       win_list = []
       for z in zz:
           # 1 阵亡角色回到基地
           if z['hp'] <= 0:
               #继续执行剩下的结算
               player_runtime.INFO['zdata'][zd_index][z_index]['hp'] = 0
               player_runtime.INFO['zdata'][zd_index][z_index]['in_war'] = False

               #重置角色数据
               cod =  player_runtime.INFO['zdata'][zd_index][z_index]['code']
               player_runtime.INFO['zdata'][zd_index][z_index]= copy.deepcopy(hrs.DATA)[cod]
               # 是否出征状态，默认否
               player_runtime.INFO['zdata'][zd_index][z_index]['in_war'] = False
               # 行进方向 0倒退 1前进 默认前进
               player_runtime.INFO['zdata'][zd_index][z_index]['direct'] = 1
               # 是否胜利到达终点的判定
               player_runtime.INFO['zdata'][zd_index][z_index]['gowin'] = False
               # 朝向重置
               player_runtime.INFO['zdata'][zd_index][z_index]['faceto'] = 0
               # 重置位置
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

               #重置特殊角色充能
               #1 猎人
               if z['code']==6:
                   player_runtime.INFO['lr_power']=2
               #2 天使
               elif z['code']==9:
                   player_runtime.INFO['ts_power']=3
               #3 屠夫
               elif z['code'] == 10:
                   player_runtime.INFO['tf_power'] = 2

           #爱哭鬼行动结束后增加一点血量
           elif z['code']==8 and player_runtime.INFO['moving_code']==8:
               player_runtime.INFO['zdata'][zd_index][z_index]['hp'] =  player_runtime.INFO['zdata'][zd_index][z_index]['hp']+1

           #猎人技能充能
           elif z['code'] == 6 and player_runtime.INFO['moving_code'] == 6:
               player_runtime.INFO['lr_power']=player_runtime.INFO['lr_power']+1
               if player_runtime.INFO['lr_power']>2:
                    player_runtime.INFO['lr_power']=2
           # 天使技能充能
           elif z['code'] == 9 and player_runtime.INFO['moving_code'] == 9:
                player_runtime.INFO['ts_power'] = player_runtime.INFO['ts_power'] + 1
                if player_runtime.INFO['ts_power'] > 3:
                    player_runtime.INFO['ts_power'] = 3


           #胜利判定
           if z['gowin']==True:
               win_list.append(z['code'])

           z_index = z_index + 1

       #4个角色都胜利了
       if len(win_list)>=4:
           player_runtime.INFO['win_code']=zd_index
           player_runtime.INFO['gameover']=True
           break

       z_index = 0
       zd_index = zd_index + 1

   #非提示状态下继续操作
   if player_runtime.INFO['is_mention']==False:
       # 重置步骤状态
       player_runtime.INFO['stage'] = 0

       #骑士技能，阵营额外行动一次
       if player_runtime.INFO['is_qs_duel']==True:
            player_runtime.INFO['is_qs_duel']=False
       else:
           # 切换执行阵营
           player_runtime.INFO['turn'] = player_runtime.INFO['turn'] + 1
           if player_runtime.INFO['turn'] > 3:
               #回合数+1
               player_runtime.INFO['round']= player_runtime.INFO['round']+1
               player_runtime.INFO['turn'] = 0


