# -*- coding: utf-8 -*-
# @Time    : 19-6-18 上午10:48
# @Author  : Redtree
# @File    : player_runtime.py
# @Desc : 游戏进行时的实时数据,存档时基于此文件

'''
基本操作信息
wasd 移动
j 普通攻击/特殊攻击 默认普通攻击
u 切换攻击模式
k 特技使用
i 切换特技
m 地图
o 角色信息面板
l 交配
esc 打开设置面板 保存/读取/设置/退出等

space 飞翔/降落

'''
INFO = {
    #玩家数量
    'player_num':1,
    #玩家/AI 轮次
    'pa_turn':[0,0,0,0],
    #选择音频声
    'select_sound':False,
    #首页英雄序号
    'title_r_index':0,
    #首页英雄位置
    'title_rx':-100,
    #首页英雄方向
    'title_rlr':0,
    # 游戏界时钟,根据帧数统计
    'gclock': 0,
    #选择游戏人数中
    'player_selected':False,
    #回合数  1/2 白天 3/4 黑夜
    'round':1,
    #是否有存档数据
    'has_save':False,
    #是否校验过存档
    'save_checked':False,
    #是否在战况中
    'inzhankuang':False,
    #是否在百科中
    'inbaike':False,
    #战况数据
    'zdata':[],
    #英雄池
    'heros_pool':[],

    ###下面是游戏过程中的参数
    #轮次  按照  蓝/绿/黄/红/的顺序 0/1/2/3
    'turn':0,
    #阶段  分为 扔筛子/选择移动角色/移动/死斗、决斗或发动技能/结算
    #  0/1/2/3/4/5
    'stage':0,
    #是否黑夜,根据回合变化
    'is_night':False,
    #当前筛子数字
    'sz_num':0,
    #是否处于提示状态
    'is_mention':False,
    #提示内容
    'mention_text':'',
    #控制面板可操作英雄代码
    'ctb_codes':[],
    #游戏结束
    'gameover':False,
    #获胜军团代码
    'win_code':0,
    #当前行动角色代码
    'moving_code':0,
    #当前行进目标
    'aim_point':(0,0),
    #角色是否行进中
    'is_moving':False,
    #本次行走剩余部署
    'left_steps':0,
    #是否跳跃中
    'is_jumping':False,
    #是否死斗中
    'death_fight':False,
    #决斗名单:
    'fight_list':[],
    #预备攻击中:
    'to_attack':False,
    #可攻击对象
    'to_attack_codes':[],
    #是否决斗中
    'common_fight':False,

    #决斗场景
    'fight_bg':0,
    #决斗阶段  预备/战斗中/结束 0/1/2
    'fight_stage':0,
    #左边角色位置
    'left_fighter_px':-180,
    #右边角色位置
    'right_fighter_px':1080,
    #决斗回合数
    'fight_round':1,
    #决斗进攻放   1右边先 然后0左边
    'fight_attack_code':1,
    #技能特效位置
    'attack_show_px':0,
    #伤害数字位置
    'attack_value_py':0,

    #技能场景中:
    'in_skill':False,
    #技能动画中:
    'act_skill':False,
    #技能命中伤害数值位置:
    'hit_sk_px':0,
    'hit_sk_py':0,
    #目标位置
    'hit_sk_pya':0,
    #技能命中对象队列
    'shr_index':(-1,-1),
    #屠夫技能命中对象队列
    'tfl_code':[],
    #猎人技能充能 2可用，行动两次后恢复:
    'lr_power':2,
    #天使技能充能 3可用，行动三次后恢复:
    'ts_power':3,
    # 屠夫技能 两次可用，回基地重置:
    'tf_power': 2,
    #天使回家动画实时位置
    'ts_back_y':0,
    #播放哪一帧图片
    'ts_back_index':0,
    #决斗伤害确认
    'jd_dmg':0,
    #当前攻击方
    'jd_atc':0,
    #展示数值
    'jd_htw':'',
    #事件
    'event':'nothing',
    #屠夫技能发动时间
    'tf_lstime':0,
    #屠夫技能坐标位置
    'tf_spx':0,
    'tf_spy':0,
    #女巫诅咒动画标签
    'nwzz_index':0,
    #女巫施法时间
    'nwzz_lstime':0,
    #女巫技能坐标位置
    'nw_spx':0,
    'nw_spy':0,
    # 女巫技能命中对象编码
    'nw_code': -1,
    #女巫本次技能伤害
    'nw_damage':0,
    #骑士是否发起决斗
    'is_qs_duel':False,
    #是否位于角色奖励结算
    'gowinr':False,
    #角色奖励阶段
    'gowinr_stage':0,
    #本次奖励类型
    'gowinr_type':0,
    #奖励执行时间
    'gowinr_lstime':0,
    #待奖励角色
    'gowinr_codes':[],

    #是否位于存档页面
    'saving':False,
    # 是否位于读档页面
    'loading': False,
    #提示是否覆盖存档
    'checksover':False,
    #当前操作存档编号 0/1/2
    'cslot':0,
}

#临时存档数据纪录
SDATA = {}

#决斗场面中的特效参数
FIGHT_ACTION = {
    #本次启动时间
    'lstime':0
}

#场景音乐控制
MUSIC = {
    'title':False,
}


#AI行为时间点记录
AITP = {
    #扔筛子
    'st0':0,
    #无法行动提示
    'st11':0,
    #女神祝福流程1
    'gw1':0,
    'gw2':0,
}