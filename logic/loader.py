# -*- coding: utf-8 -*-
# @Time    : 19-6-17 下午5:w15
# @Author  : Redtree
# @File    : loader.py
# @Desc : 所有预加载资源在此处执行

from data import color_rgb
import config
import sys, pygame
from data import title_page
from data import game_page


print(config.GAME_NAME+config.VERSION+'程序初始化中......')
#初始化pg对象
pygame.init()
print('初始化成功,正在加载游戏资源......')
#窗口标题
pygame.display.set_caption(config.GAME_NAME+':'+config.VERSION)
#窗口大小
WINDOW_SIZE =config.WINDOW_WEIGHT,config.WINDOW_HEIGHT
#是否全屏模式
fullscreen=True
#旧版参数
# screen = pygame.display.set_mode(WINDOW_SIZE)
# if fullscreen==True:
#     pygame.display.toggle_fullscreen()
#新版本参数
if fullscreen==True:
    screen = pygame.display.set_mode(WINDOW_SIZE,pygame.FULLSCREEN,32)
else:
    screen = pygame.display.set_mode(WINDOW_SIZE)

#设置帧数
FPS=60
FPSClock=pygame.time.Clock()
FPSClock.tick(FPS)

#隐藏鼠标
pygame.mouse.set_visible(False)


print('正在加载图片资源')
#默认资源样式
TITLE_PAGE = pygame.image.load('resource/map/title.png')
TITLE_FONT = pygame.font.Font('resource/font/msyh.TTF',title_page.TITLE_PAGE_DATA['font-size'])
TITLE_start_surface = TITLE_FONT.render(title_page.TITLE_PAGE_DATA[0], True, color_rgb.WHITE, None)
TITLE_continue_surface = TITLE_FONT.render(title_page.TITLE_PAGE_DATA[1], True, color_rgb.WHITE, None)
TITLE_achievement_surface = TITLE_FONT.render(title_page.TITLE_PAGE_DATA[2], True, color_rgb.WHITE, None)
TITLE_exit_surface = TITLE_FONT.render(title_page.TITLE_PAGE_DATA[3], True, color_rgb.WHITE, None)
#选中资源样式
TITLE_FONT_pos = pygame.font.Font('resource/font/msyh.TTF',title_page.TITLE_PAGE_DATA['font-size']+10)
TITLE_start_surface_pos = TITLE_FONT_pos.render(title_page.TITLE_PAGE_DATA[0], True, color_rgb.YELLOW, None)
TITLE_continue_surface_pos = TITLE_FONT_pos.render(title_page.TITLE_PAGE_DATA[1], True, color_rgb.YELLOW, None)
TITLE_achievement_surface_pos = TITLE_FONT_pos.render(title_page.TITLE_PAGE_DATA[2], True, color_rgb.YELLOW, None)
TITLE_exit_surface_pos = TITLE_FONT_pos.render(title_page.TITLE_PAGE_DATA[3], True, color_rgb.YELLOW, None)

#游戏内字幕样式
GAME_TEXT_FONT_SM = pygame.font.Font('resource/font/msyh.TTF',8)
GAME_TEXT_FONT_MINI = pygame.font.Font('resource/font/msyh.TTF',10)
GAME_TEXT_FONT = pygame.font.Font('resource/font/msyh.TTF',20)
GAME_ROUND_FONT = pygame.font.Font('resource/font/msyh.TTF',30)
GAME_ROUND_TITLE_FONT = pygame.font.Font('resource/font/msyh.TTF',60)


#地图资源
#BG_CENTER = pygame.image.load('resource/map/bg_center.png')
#BG1 = pygame.image.load('resource/map/pan_bg1.png')
#BG2 = pygame.image.load('resource/map/pan_bg2.png')

#角色资源 （旧的立绘版本）
# R1 = pygame.image.load('resource/heros/r1.png')
# R2 = pygame.image.load('resource/heros/r2.png')
# R3 = pygame.image.load('resource/heros/r3.png')
# R4 = pygame.image.load('resource/heros/r4.png')
# R5 = pygame.image.load('resource/heros/r5.png')
# R6 = pygame.image.load('resource/heros/r6.png')
# R7 = pygame.image.load('resource/heros/r7.png')
# R8 = pygame.image.load('resource/heros/r8.png')
# R9 = pygame.image.load('resource/heros/r9.png')
# R10 = pygame.image.load('resource/heros/r10.png')
# R11 = pygame.image.load('resource/heros/r11.png')
# R12 = pygame.image.load('resource/heros/r12.png')
# R13 = pygame.image.load('resource/heros/r13.png')
# R14 = pygame.image.load('resource/heros/r14.png')
# R15 = pygame.image.load('resource/heros/r15.png')
# R16 = pygame.image.load('resource/heros/r16.png')
# RS = [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16]

#程序员的移动资源
R1_1 = pygame.image.load('resource/heros/r1/r1_0.png')
R1_2 = pygame.image.load('resource/heros/r1/r1_1.png')
R1_3 = pygame.image.load('resource/heros/r1/r1_2.png')
R1_4 = pygame.image.load('resource/heros/r1/r1_3.png')
R1_5 = pygame.image.load('resource/heros/r1/r1_4.png')
R1_6 = pygame.image.load('resource/heros/r1/r1_5.png')
R1_7 = pygame.image.load('resource/heros/r1/r1_6.png')
R1_8 = pygame.image.load('resource/heros/r1/r1_7.png')
R1_9 = pygame.image.load('resource/heros/r1/r1_8.png')
R1_10 = pygame.image.load('resource/heros/r1/r1_9.png')
R1_11 = pygame.image.load('resource/heros/r1/r1_10.png')
R1_12 = pygame.image.load('resource/heros/r1/r1_11.png')
R1_13 = pygame.image.load('resource/heros/r1/r1_12.png')
R1_14 = pygame.image.load('resource/heros/r1/r1_13.png')
R1_15 = pygame.image.load('resource/heros/r1/r1_14.png')
R1_16 = pygame.image.load('resource/heros/r1/r1_15.png')
R1_S = [R1_1,R1_2,R1_3,R1_4,R1_5,R1_6,R1_7,R1_8,R1_9,R1_10,R1_11,R1_12,R1_13,R1_14,R1_15,R1_16]


#小甜心的移动资源
R2_1 = pygame.image.load('resource/heros/r2/r2_0.png')
R2_2 = pygame.image.load('resource/heros/r2/r2_1.png')
R2_3 = pygame.image.load('resource/heros/r2/r2_2.png')
R2_4 = pygame.image.load('resource/heros/r2/r2_3.png')
R2_5 = pygame.image.load('resource/heros/r2/r2_4.png')
R2_6 = pygame.image.load('resource/heros/r2/r2_5.png')
R2_7 = pygame.image.load('resource/heros/r2/r2_6.png')
R2_8 = pygame.image.load('resource/heros/r2/r2_7.png')
R2_9 = pygame.image.load('resource/heros/r2/r2_8.png')
R2_10 = pygame.image.load('resource/heros/r2/r2_9.png')
R2_11 = pygame.image.load('resource/heros/r2/r2_10.png')
R2_12 = pygame.image.load('resource/heros/r2/r2_11.png')
R2_13 = pygame.image.load('resource/heros/r2/r2_12.png')
R2_14 = pygame.image.load('resource/heros/r2/r2_13.png')
R2_15 = pygame.image.load('resource/heros/r2/r2_14.png')
R2_16 = pygame.image.load('resource/heros/r2/r2_15.png')
R2_S = [R2_1,R2_2,R2_3,R2_4,R2_5,R2_6,R2_7,R2_8,R2_9,R2_10,R2_11,R2_12,R2_13,R2_14,R2_15,R2_16]

#科学家的移动资源
R3_1 = pygame.image.load('resource/heros/r3/r3_0.png')
R3_2 = pygame.image.load('resource/heros/r3/r3_1.png')
R3_3 = pygame.image.load('resource/heros/r3/r3_2.png')
R3_4 = pygame.image.load('resource/heros/r3/r3_3.png')
R3_5 = pygame.image.load('resource/heros/r3/r3_4.png')
R3_6 = pygame.image.load('resource/heros/r3/r3_5.png')
R3_7 = pygame.image.load('resource/heros/r3/r3_6.png')
R3_8 = pygame.image.load('resource/heros/r3/r3_7.png')
R3_9 = pygame.image.load('resource/heros/r3/r3_8.png')
R3_10 = pygame.image.load('resource/heros/r3/r3_9.png')
R3_11 = pygame.image.load('resource/heros/r3/r3_10.png')
R3_12 = pygame.image.load('resource/heros/r3/r3_11.png')
R3_13 = pygame.image.load('resource/heros/r3/r3_12.png')
R3_14 = pygame.image.load('resource/heros/r3/r3_13.png')
R3_15 = pygame.image.load('resource/heros/r3/r3_14.png')
R3_16 = pygame.image.load('resource/heros/r3/r3_15.png')
R3_S = [R3_1,R3_2,R3_3,R3_4,R3_5,R3_6,R3_7,R3_8,R3_9,R3_10,R3_11,R3_12,R3_13,R3_14,R3_15,R3_16]

#孩子王的移动资源
R4_1 = pygame.image.load('resource/heros/r4/r4_0.png')
R4_2 = pygame.image.load('resource/heros/r4/r4_1.png')
R4_3 = pygame.image.load('resource/heros/r4/r4_2.png')
R4_4 = pygame.image.load('resource/heros/r4/r4_3.png')
R4_5 = pygame.image.load('resource/heros/r4/r4_4.png')
R4_6 = pygame.image.load('resource/heros/r4/r4_5.png')
R4_7 = pygame.image.load('resource/heros/r4/r4_6.png')
R4_8 = pygame.image.load('resource/heros/r4/r4_7.png')
R4_9 = pygame.image.load('resource/heros/r4/r4_8.png')
R4_10 = pygame.image.load('resource/heros/r4/r4_9.png')
R4_11 = pygame.image.load('resource/heros/r4/r4_10.png')
R4_12 = pygame.image.load('resource/heros/r4/r4_11.png')
R4_13 = pygame.image.load('resource/heros/r4/r4_12.png')
R4_14 = pygame.image.load('resource/heros/r4/r4_13.png')
R4_15 = pygame.image.load('resource/heros/r4/r4_14.png')
R4_16 = pygame.image.load('resource/heros/r4/r4_15.png')
R4_S = [R4_1,R4_2,R4_3,R4_4,R4_5,R4_6,R4_7,R4_8,R4_9,R4_10,R4_11,R4_12,R4_13,R4_14,R4_15,R4_16]

#武士的移动资源
R5_1 = pygame.image.load('resource/heros/r5/r5_0.png')
R5_2 = pygame.image.load('resource/heros/r5/r5_1.png')
R5_3 = pygame.image.load('resource/heros/r5/r5_2.png')
R5_4 = pygame.image.load('resource/heros/r5/r5_3.png')
R5_5 = pygame.image.load('resource/heros/r5/r5_4.png')
R5_6 = pygame.image.load('resource/heros/r5/r5_5.png')
R5_7 = pygame.image.load('resource/heros/r5/r5_6.png')
R5_8 = pygame.image.load('resource/heros/r5/r5_7.png')
R5_9 = pygame.image.load('resource/heros/r5/r5_8.png')
R5_10 = pygame.image.load('resource/heros/r5/r5_9.png')
R5_11 = pygame.image.load('resource/heros/r5/r5_10.png')
R5_12 = pygame.image.load('resource/heros/r5/r5_11.png')
R5_13 = pygame.image.load('resource/heros/r5/r5_12.png')
R5_14 = pygame.image.load('resource/heros/r5/r5_13.png')
R5_15 = pygame.image.load('resource/heros/r5/r5_14.png')
R5_16 = pygame.image.load('resource/heros/r5/r5_15.png')
R5_S = [R5_1,R5_2,R5_3,R5_4,R5_5,R5_6,R5_7,R5_8,R5_9,R5_10,R5_11,R5_12,R5_13,R5_14,R5_15,R5_16]

#刺客的移动资源
R6_1 = pygame.image.load('resource/heros/r6/r6_0.png')
R6_2 = pygame.image.load('resource/heros/r6/r6_1.png')
R6_3 = pygame.image.load('resource/heros/r6/r6_2.png')
R6_4 = pygame.image.load('resource/heros/r6/r6_3.png')
R6_5 = pygame.image.load('resource/heros/r6/r6_4.png')
R6_6 = pygame.image.load('resource/heros/r6/r6_5.png')
R6_7 = pygame.image.load('resource/heros/r6/r6_6.png')
R6_8 = pygame.image.load('resource/heros/r6/r6_7.png')
R6_9 = pygame.image.load('resource/heros/r6/r6_8.png')
R6_10 = pygame.image.load('resource/heros/r6/r6_9.png')
R6_11 = pygame.image.load('resource/heros/r6/r6_10.png')
R6_12 = pygame.image.load('resource/heros/r6/r6_11.png')
R6_13 = pygame.image.load('resource/heros/r6/r6_12.png')
R6_14 = pygame.image.load('resource/heros/r6/r6_13.png')
R6_15 = pygame.image.load('resource/heros/r6/r6_14.png')
R6_16 = pygame.image.load('resource/heros/r6/r6_15.png')
R6_S = [R6_1,R6_2,R6_3,R6_4,R6_5,R6_6,R6_7,R6_8,R6_9,R6_10,R6_11,R6_12,R6_13,R6_14,R6_15,R6_16]

#猎人的移动资源
R7_1 = pygame.image.load('resource/heros/r7/r7_0.png')
R7_2 = pygame.image.load('resource/heros/r7/r7_1.png')
R7_3 = pygame.image.load('resource/heros/r7/r7_2.png')
R7_4 = pygame.image.load('resource/heros/r7/r7_3.png')
R7_5 = pygame.image.load('resource/heros/r7/r7_4.png')
R7_6 = pygame.image.load('resource/heros/r7/r7_5.png')
R7_7 = pygame.image.load('resource/heros/r7/r7_6.png')
R7_8 = pygame.image.load('resource/heros/r7/r7_7.png')
R7_9 = pygame.image.load('resource/heros/r7/r7_8.png')
R7_10 = pygame.image.load('resource/heros/r7/r7_9.png')
R7_11 = pygame.image.load('resource/heros/r7/r7_10.png')
R7_12 = pygame.image.load('resource/heros/r7/r7_11.png')
R7_13 = pygame.image.load('resource/heros/r7/r7_12.png')
R7_14 = pygame.image.load('resource/heros/r7/r7_13.png')
R7_15 = pygame.image.load('resource/heros/r7/r7_14.png')
R7_16 = pygame.image.load('resource/heros/r7/r7_15.png')
R7_S = [R7_1,R7_2,R7_3,R7_4,R7_5,R7_6,R7_7,R7_8,R7_9,R7_10,R7_11,R7_12,R7_13,R7_14,R7_15,R7_16]

#僵尸的移动资源
R8_1 = pygame.image.load('resource/heros/r8/r8_0.png')
R8_2 = pygame.image.load('resource/heros/r8/r8_1.png')
R8_3 = pygame.image.load('resource/heros/r8/r8_2.png')
R8_4 = pygame.image.load('resource/heros/r8/r8_3.png')
R8_5 = pygame.image.load('resource/heros/r8/r8_4.png')
R8_6 = pygame.image.load('resource/heros/r8/r8_5.png')
R8_7 = pygame.image.load('resource/heros/r8/r8_6.png')
R8_8 = pygame.image.load('resource/heros/r8/r8_7.png')
R8_9 = pygame.image.load('resource/heros/r8/r8_8.png')
R8_10 = pygame.image.load('resource/heros/r8/r8_9.png')
R8_11 = pygame.image.load('resource/heros/r8/r8_10.png')
R8_12 = pygame.image.load('resource/heros/r8/r8_11.png')
R8_13 = pygame.image.load('resource/heros/r8/r8_12.png')
R8_14 = pygame.image.load('resource/heros/r8/r8_13.png')
R8_15 = pygame.image.load('resource/heros/r8/r8_14.png')
R8_16 = pygame.image.load('resource/heros/r8/r8_15.png')
R8_S = [R8_1,R8_2,R8_3,R8_4,R8_5,R8_6,R8_7,R8_8,R8_9,R8_10,R8_11,R8_12,R8_13,R8_14,R8_15,R8_16]

#吸血鬼的移动资源
R9_1 = pygame.image.load('resource/heros/r9/r9_0.png')
R9_2 = pygame.image.load('resource/heros/r9/r9_1.png')
R9_3 = pygame.image.load('resource/heros/r9/r9_2.png')
R9_4 = pygame.image.load('resource/heros/r9/r9_3.png')
R9_5 = pygame.image.load('resource/heros/r9/r9_4.png')
R9_6 = pygame.image.load('resource/heros/r9/r9_5.png')
R9_7 = pygame.image.load('resource/heros/r9/r9_6.png')
R9_8 = pygame.image.load('resource/heros/r9/r9_7.png')
R9_9 = pygame.image.load('resource/heros/r9/r9_8.png')
R9_10 = pygame.image.load('resource/heros/r9/r9_9.png')
R9_11 = pygame.image.load('resource/heros/r9/r9_10.png')
R9_12 = pygame.image.load('resource/heros/r9/r9_11.png')
R9_13 = pygame.image.load('resource/heros/r9/r9_12.png')
R9_14 = pygame.image.load('resource/heros/r9/r9_13.png')
R9_15 = pygame.image.load('resource/heros/r9/r9_14.png')
R9_16 = pygame.image.load('resource/heros/r9/r9_15.png')
R9_S = [R9_1,R9_2,R9_3,R9_4,R9_5,R9_6,R9_7,R9_8,R9_9,R9_10,R9_11,R9_12,R9_13,R9_14,R9_15,R9_16]

#精灵的移动资源
R10_1 = pygame.image.load('resource/heros/r10/r10_0.png')
R10_2 = pygame.image.load('resource/heros/r10/r10_1.png')
R10_3 = pygame.image.load('resource/heros/r10/r10_2.png')
R10_4 = pygame.image.load('resource/heros/r10/r10_3.png')
R10_5 = pygame.image.load('resource/heros/r10/r10_4.png')
R10_6 = pygame.image.load('resource/heros/r10/r10_5.png')
R10_7 = pygame.image.load('resource/heros/r10/r10_6.png')
R10_8 = pygame.image.load('resource/heros/r10/r10_7.png')
R10_9 = pygame.image.load('resource/heros/r10/r10_8.png')
R10_10 = pygame.image.load('resource/heros/r10/r10_9.png')
R10_11 = pygame.image.load('resource/heros/r10/r10_10.png')
R10_12 = pygame.image.load('resource/heros/r10/r10_11.png')
R10_13 = pygame.image.load('resource/heros/r10/r10_12.png')
R10_14 = pygame.image.load('resource/heros/r10/r10_13.png')
R10_15 = pygame.image.load('resource/heros/r10/r10_14.png')
R10_16 = pygame.image.load('resource/heros/r10/r10_15.png')
R10_S = [R10_1,R10_2,R10_3,R10_4,R10_5,R10_6,R10_7,R10_8,R10_9,R10_10,R10_11,R10_12,R10_13,R10_14,R10_15,R10_16]

#屠夫的移动资源
R11_1 = pygame.image.load('resource/heros/r11/r11_0.png')
R11_2 = pygame.image.load('resource/heros/r11/r11_1.png')
R11_3 = pygame.image.load('resource/heros/r11/r11_2.png')
R11_4 = pygame.image.load('resource/heros/r11/r11_3.png')
R11_5 = pygame.image.load('resource/heros/r11/r11_4.png')
R11_6 = pygame.image.load('resource/heros/r11/r11_5.png')
R11_7 = pygame.image.load('resource/heros/r11/r11_6.png')
R11_8 = pygame.image.load('resource/heros/r11/r11_7.png')
R11_9 = pygame.image.load('resource/heros/r11/r11_8.png')
R11_10 = pygame.image.load('resource/heros/r11/r11_9.png')
R11_11 = pygame.image.load('resource/heros/r11/r11_10.png')
R11_12 = pygame.image.load('resource/heros/r11/r11_11.png')
R11_13 = pygame.image.load('resource/heros/r11/r11_12.png')
R11_14 = pygame.image.load('resource/heros/r11/r11_13.png')
R11_15 = pygame.image.load('resource/heros/r11/r11_14.png')
R11_16 = pygame.image.load('resource/heros/r11/r11_15.png')
R11_S = [R11_1,R11_2,R11_3,R11_4,R11_5,R11_6,R11_7,R11_8,R11_9,R11_10,R11_11,R11_12,R11_13,R11_14,R11_15,R11_16]

#女巫的移动资源
R12_1 = pygame.image.load('resource/heros/r12/r12_0.png')
R12_2 = pygame.image.load('resource/heros/r12/r12_1.png')
R12_3 = pygame.image.load('resource/heros/r12/r12_2.png')
R12_4 = pygame.image.load('resource/heros/r12/r12_3.png')
R12_5 = pygame.image.load('resource/heros/r12/r12_4.png')
R12_6 = pygame.image.load('resource/heros/r12/r12_5.png')
R12_7 = pygame.image.load('resource/heros/r12/r12_6.png')
R12_8 = pygame.image.load('resource/heros/r12/r12_7.png')
R12_9 = pygame.image.load('resource/heros/r12/r12_8.png')
R12_10 = pygame.image.load('resource/heros/r12/r12_9.png')
R12_11 = pygame.image.load('resource/heros/r12/r12_10.png')
R12_12 = pygame.image.load('resource/heros/r12/r12_11.png')
R12_13 = pygame.image.load('resource/heros/r12/r12_12.png')
R12_14 = pygame.image.load('resource/heros/r12/r12_13.png')
R12_15 = pygame.image.load('resource/heros/r12/r12_14.png')
R12_16 = pygame.image.load('resource/heros/r12/r12_15.png')
R12_S = [R12_1,R12_2,R12_3,R12_4,R12_5,R12_6,R12_7,R12_8,R12_9,R12_10,R12_11,R12_12,R12_13,R12_14,R12_15,R12_16]

#狼人的移动资源
R13_1 = pygame.image.load('resource/heros/r13/r13_0.png')
R13_2 = pygame.image.load('resource/heros/r13/r13_1.png')
R13_3 = pygame.image.load('resource/heros/r13/r13_2.png')
R13_4 = pygame.image.load('resource/heros/r13/r13_3.png')
R13_5 = pygame.image.load('resource/heros/r13/r13_4.png')
R13_6 = pygame.image.load('resource/heros/r13/r13_5.png')
R13_7 = pygame.image.load('resource/heros/r13/r13_6.png')
R13_8 = pygame.image.load('resource/heros/r13/r13_7.png')
R13_9 = pygame.image.load('resource/heros/r13/r13_8.png')
R13_10 = pygame.image.load('resource/heros/r13/r13_9.png')
R13_11 = pygame.image.load('resource/heros/r13/r13_10.png')
R13_12 = pygame.image.load('resource/heros/r13/r13_11.png')
R13_13 = pygame.image.load('resource/heros/r13/r13_12.png')
R13_14 = pygame.image.load('resource/heros/r13/r13_13.png')
R13_15 = pygame.image.load('resource/heros/r13/r13_14.png')
R13_16 = pygame.image.load('resource/heros/r13/r13_15.png')
R13_S = [R13_1,R13_2,R13_3,R13_4,R13_5,R13_6,R13_7,R13_8,R13_9,R13_10,R13_11,R13_12,R13_13,R13_14,R13_15,R13_16]

#骑士的移动资源
R14_1 = pygame.image.load('resource/heros/r14/r14_0.png')
R14_2 = pygame.image.load('resource/heros/r14/r14_1.png')
R14_3 = pygame.image.load('resource/heros/r14/r14_2.png')
R14_4 = pygame.image.load('resource/heros/r14/r14_3.png')
R14_5 = pygame.image.load('resource/heros/r14/r14_4.png')
R14_6 = pygame.image.load('resource/heros/r14/r14_5.png')
R14_7 = pygame.image.load('resource/heros/r14/r14_6.png')
R14_8 = pygame.image.load('resource/heros/r14/r14_7.png')
R14_9 = pygame.image.load('resource/heros/r14/r14_8.png')
R14_10 = pygame.image.load('resource/heros/r14/r14_9.png')
R14_11 = pygame.image.load('resource/heros/r14/r14_10.png')
R14_12 = pygame.image.load('resource/heros/r14/r14_11.png')
R14_13 = pygame.image.load('resource/heros/r14/r14_12.png')
R14_14 = pygame.image.load('resource/heros/r14/r14_13.png')
R14_15 = pygame.image.load('resource/heros/r14/r14_14.png')
R14_16 = pygame.image.load('resource/heros/r14/r14_15.png')
R14_S = [R14_1,R14_2,R14_3,R14_4,R14_5,R14_6,R14_7,R14_8,R14_9,R14_10,R14_11,R14_12,R14_13,R14_14,R14_15,R14_16]

#国王的移动资源
R15_1 = pygame.image.load('resource/heros/r15/r15_0.png')
R15_2 = pygame.image.load('resource/heros/r15/r15_1.png')
R15_3 = pygame.image.load('resource/heros/r15/r15_2.png')
R15_4 = pygame.image.load('resource/heros/r15/r15_3.png')
R15_5 = pygame.image.load('resource/heros/r15/r15_4.png')
R15_6 = pygame.image.load('resource/heros/r15/r15_5.png')
R15_7 = pygame.image.load('resource/heros/r15/r15_6.png')
R15_8 = pygame.image.load('resource/heros/r15/r15_7.png')
R15_9 = pygame.image.load('resource/heros/r15/r15_8.png')
R15_10 = pygame.image.load('resource/heros/r15/r15_9.png')
R15_11 = pygame.image.load('resource/heros/r15/r15_10.png')
R15_12 = pygame.image.load('resource/heros/r15/r15_11.png')
R15_13 = pygame.image.load('resource/heros/r15/r15_12.png')
R15_14 = pygame.image.load('resource/heros/r15/r15_13.png')
R15_15 = pygame.image.load('resource/heros/r15/r15_14.png')
R15_16 = pygame.image.load('resource/heros/r15/r15_15.png')
R15_S = [R15_1,R15_2,R15_3,R15_4,R15_5,R15_6,R15_7,R15_8,R15_9,R15_10,R15_11,R15_12,R15_13,R15_14,R15_15,R15_16]

#怪兽的移动资源
R16_1 = pygame.image.load('resource/heros/r16/r16_0.png')
R16_2 = pygame.image.load('resource/heros/r16/r16_1.png')
R16_3 = pygame.image.load('resource/heros/r16/r16_2.png')
R16_4 = pygame.image.load('resource/heros/r16/r16_3.png')
R16_5 = pygame.image.load('resource/heros/r16/r16_4.png')
R16_6 = pygame.image.load('resource/heros/r16/r16_5.png')
R16_7 = pygame.image.load('resource/heros/r16/r16_6.png')
R16_8 = pygame.image.load('resource/heros/r16/r16_7.png')
R16_9 = pygame.image.load('resource/heros/r16/r16_8.png')
R16_10 = pygame.image.load('resource/heros/r16/r16_9.png')
R16_11 = pygame.image.load('resource/heros/r16/r16_10.png')
R16_12 = pygame.image.load('resource/heros/r16/r16_11.png')
R16_13 = pygame.image.load('resource/heros/r16/r16_12.png')
R16_14 = pygame.image.load('resource/heros/r16/r16_13.png')
R16_15 = pygame.image.load('resource/heros/r16/r16_14.png')
R16_16 = pygame.image.load('resource/heros/r16/r16_15.png')
R16_S = [R16_1,R16_2,R16_3,R16_4,R16_5,R16_6,R16_7,R16_8,R16_9,R16_10,R16_11,R16_12,R16_13,R16_14,R16_15,R16_16]

#新版本携带角色移动资源
RMS = [R1_S,R2_S,R3_S,R4_S,R5_S,R6_S,R7_S,R8_S,R9_S,R10_S,R11_S,R12_S,R13_S,R14_S,R15_S,R16_S]


#游戏菜单资源
BOARD1 = pygame.image.load('resource/map/board1.png')
BOARD2 = pygame.image.load('resource/map/board2.png')
BOARD3 = pygame.image.load('resource/map/board3.png')
BOARD4 = pygame.image.load('resource/map/board4.png')
MOON = pygame.image.load('resource/map/moon.png')
SELECT_PLAYER = pygame.image.load('resource/map/select_player.png')
SELECT_HELP = pygame.image.load('resource/map/select_help.png')
SUN = pygame.image.load('resource/map/sun.png')
SELECT =  pygame.image.load('resource/map/select.png')
MOUSE = pygame.image.load('resource/map/mouse.png')
MOUSE_WIN = pygame.image.load('resource/map/mouse_win.png')
BAIKE = pygame.image.load('resource/map/baike.png')
ZHANKUANG = pygame.image.load('resource/map/zhankuang.png')
CUNDANG = pygame.image.load('resource/map/cundang.png')
DUDANG = pygame.image.load('resource/map/dudang.png')
SELECT_MENU = pygame.image.load('resource/map/select_menu.png')
SAVE_BOARD_TITLE = pygame.image.load('resource/map/save_board_title.png')
SAVE_BOARD_LOT = pygame.image.load('resource/map/save_board_lot.png')
SAVE_BOARD_LOTA = pygame.image.load('resource/map/save_board_lota.png')
SAVE_BOARD_TITLE_BACK1 = pygame.image.load('resource/map/save_board_title_back1.png')
SAVE_BOARD_TITLE_BACK2 = pygame.image.load('resource/map/save_board_title_back2.png')

#保存页面
#确认保存吗
CHECK_SAVE = pygame.image.load('resource/map/check_save.png')
#确认覆盖存档吗
CHECK_SAVEOVER = pygame.image.load('resource/map/check_saveover.png')
#确认读档
CHECK_LOAD = pygame.image.load('resource/map/check_load.png')
#确认按钮
SURE = pygame.image.load('resource/map/sure.png')
#取消按钮
SURENO = pygame.image.load('resource/map/sureno.png')
#选中提示
SELECT_SAVE = pygame.image.load('resource/map/select_save.png')

#百科菜单资源
BAIKE_FONT = pygame.font.Font('resource/font/msyh.TTF',24)
BAIKE_SHOW =pygame.image.load('resource/map/baike_show.png')
BAIKE_SELECT =pygame.image.load('resource/map/baike_select.png')
BAIKE_BACK = pygame.image.load('resource/map/baike_back.png')
BAIKE_BACK_BUT1 = pygame.image.load('resource/map/baike_back_but1.png')
BAIKE_BACK_BUT2 = pygame.image.load('resource/map/baike_back_but2.png')
SELECT_FIRE =  pygame.image.load('resource/map/select_fire.png')
VALUE_EMPTY = pygame.image.load('resource/map/value_empty.png')
VALUE_GET = pygame.image.load('resource/map/value_get.png')

#战况
ZKS = pygame.image.load('resource/map/zks.png')

#菜单通用资源
ATTACK =  pygame.image.load('resource/map/attack.png')
DEFEND =  pygame.image.load('resource/map/defend.png')
HEART =  pygame.image.load('resource/map/heart.png')
SKILL =  pygame.image.load('resource/map/skill.png')
BACK = pygame.image.load('resource/map/back.png')

#地图资源
MAP_GREEN =  pygame.image.load('resource/map/map_green.png')
MAP_RED =  pygame.image.load('resource/map/map_red.png')
MAP_YELLOW =  pygame.image.load('resource/map/map_yellow.png')
MAP_BLUE =  pygame.image.load('resource/map/map_blue.png')
MAP_GREEN_GO =  pygame.image.load('resource/map/map_green_go.png')
MAP_RED_GO =  pygame.image.load('resource/map/map_red_go.png')
MAP_YELLOW_GO =  pygame.image.load('resource/map/map_yellow_go.png')
MAP_BLUE_GO =  pygame.image.load('resource/map/map_blue_go.png')
MAP_WIN =  pygame.image.load('resource/map/map_win.png')
MAP_START =  pygame.image.load('resource/map/map_start.png')
MAP_FLY = pygame.image.load('resource/map/map_fly.png')
MAPS= [False,MAP_BLUE,MAP_GREEN,MAP_YELLOW,MAP_RED,MAP_START,MAP_WIN,MAP_FLY,MAP_BLUE_GO,MAP_GREEN_GO,MAP_YELLOW_GO,MAP_RED_GO]

#控制面板
CONTROL_YELLOW = pygame.image.load('resource/map/control_yellow.png')
CONTROL_BLUE = pygame.image.load('resource/map/control_blue.png')
CONTROL_GREEN = pygame.image.load('resource/map/control_green.png')
CONTROL_RED = pygame.image.load('resource/map/control_red.png')

#
SZ1 = pygame.image.load('resource/map/sz1.png')
SZ2 = pygame.image.load('resource/map/sz2.png')
SZ3 = pygame.image.load('resource/map/sz3.png')
SZ4 = pygame.image.load('resource/map/sz4.png')
SZ5 = pygame.image.load('resource/map/sz5.png')
SZ6 = pygame.image.load('resource/map/sz6.png')
SZ = [SZ1,SZ2,SZ3,SZ4,SZ5,SZ6]


#擂台背景
JUEDOU = pygame.image.load('resource/map/juedou.png')
SIDOU = pygame.image.load('resource/map/sidou.png')
LEITAI1 = pygame.image.load('resource/map/leitai1.png')
LEITAI2 = pygame.image.load('resource/map/leitai2.png')
LEITAI3 = pygame.image.load('resource/map/leitai3.png')
LEITAI = [LEITAI1,LEITAI2,LEITAI3]

#角色技能图标
SK1 = pygame.image.load('resource/skill/sk1.png')
SK2 = pygame.image.load('resource/skill/sk2.png')
SK3 = pygame.image.load('resource/skill/sk3.png')
SK4 = pygame.image.load('resource/skill/sk4.png')
SK5 = pygame.image.load('resource/skill/sk5.png')
SK6 = pygame.image.load('resource/skill/sk6.png')
SK7 = pygame.image.load('resource/skill/sk7.png')
SK8 = pygame.image.load('resource/skill/sk8.png')
SK9 = pygame.image.load('resource/skill/sk9.png')
SK10 = pygame.image.load('resource/skill/sk10.png')
SK11= pygame.image.load('resource/skill/sk11.png')
SK12 = pygame.image.load('resource/skill/sk12.png')
SK13 = pygame.image.load('resource/skill/sk13.png')
SK14 = pygame.image.load('resource/skill/sk14.png')
SK15 = pygame.image.load('resource/skill/sk15.png')
SK16 = pygame.image.load('resource/skill/sk16.png')
SKI = [SK1,SK2,SK3,SK4,SK5,SK6,SK7,SK8,SK9,SK10,SK11,SK12,SK13,SK14,SK15,SK16]

#特殊图标
#猎人狙击面板
WUYUN = pygame.image.load('resource/skill/wuyun.png')
AIXIN = pygame.image.load('resource/skill/aixin.png')
XIANNVBANG = pygame.image.load('resource/skill/xiannvbang.png')
CAIDAO = pygame.image.load('resource/action/caidao.png')
CAIDAOL = pygame.image.load('resource/action/caidaol.png')
WUDICAIDAO = pygame.image.load('resource/skill/wudicaidao.png')
EDUZZ =  pygame.image.load('resource/skill/eduzz.png')

#提示板
MENTION =  pygame.image.load('resource/map/mention.png')

###动作资源

#程序员键盘
W1 = pygame.image.load('resource/weapon/w1/w1.png')
#小姐姐的lv包
W2 = pygame.image.load('resource/weapon/w2/w2.png')
#科学家过场
W3_0 = pygame.image.load('resource/weapon/w3/w31_0.png')
W3_1 = pygame.image.load('resource/weapon/w3/w31_1.png')
W3_2 = pygame.image.load('resource/weapon/w3/w31_2.png')
W3_3 = pygame.image.load('resource/weapon/w3/w31_3.png')
W3_4 = pygame.image.load('resource/weapon/w3/w31_4.png')
W3_5 = pygame.image.load('resource/weapon/w3/w31_5.png')
W3_6 = pygame.image.load('resource/weapon/w3/w31_6.png')
W3_7 = pygame.image.load('resource/weapon/w3/w31_7.png')
W3_8 = pygame.image.load('resource/weapon/w3/w31_8.png')
W3 = [W3_0,W3_1,W3_2,W3_3,W3_4,W3_5,W3_6,W3_7,W3_8,]
#科学家变身钢铁侠
W3_BSR =  pygame.image.load('resource/weapon/w3/r3s_right.png')
W3_BSL =  pygame.image.load('resource/weapon/w3/r3s_left.png')
W3_BOR = pygame.image.load('resource/weapon/w3/w3_bor.png')
W3_BOL= pygame.image.load('resource/weapon/w3/w3_bol.png')
#孩子王的动感光波
W4_BO1= pygame.image.load('resource/weapon/w4/w4_bo1.png')
W4_BO2= pygame.image.load('resource/weapon/w4/w4_bo2.png')
W4_BO3= pygame.image.load('resource/weapon/w4/w4_bo3.png')
W4_BOS = [W4_BO1,W4_BO2,W4_BO3]
W4_K1= pygame.image.load('resource/weapon/w4/w4k1.png')
W4_K2= pygame.image.load('resource/weapon/w4/w4k2.png')
W4_K3= pygame.image.load('resource/weapon/w4/w4k3.png')
W4_K4= pygame.image.load('resource/weapon/w4/w4k4.png')
W4_K5= pygame.image.load('resource/weapon/w4/w4k5.png')
W4_K6= pygame.image.load('resource/weapon/w4/w4k6.png')
W4_KS = [W4_K1,W4_K2,W4_K3,W4_K4,W4_K5,W4_K6]
#武士跳劈
W5_AR= pygame.image.load('resource/weapon/w5/w5_ar.png')
#刺客瞬移背刺
W6_AR = pygame.image.load('resource/weapon/w6/w6_ar.png')
W6_AL = pygame.image.load('resource/weapon/w6/w6_al.png')
W6_G1 = pygame.image.load('resource/weapon/w6/w6_g1.png')
W6_G2R = pygame.image.load('resource/weapon/w6/w6_g2r.png')
W6_G2L = pygame.image.load('resource/weapon/w6/w6_g2l.png')
W6_SD = pygame.image.load('resource/weapon/w6/w6_sd.png')
#猎人射光箭
W7_G1 =pygame.image.load('resource/weapon/w7/w7_g1.png')
W7_G2 =pygame.image.load('resource/weapon/w7/w7_g2.png')
W7_G3 =pygame.image.load('resource/weapon/w7/w7_g3.png')
W7_G4 =pygame.image.load('resource/weapon/w7/w7_g4.png')
W7_G5 =pygame.image.load('resource/weapon/w7/w7_g5.png')
W7_GS = [W7_G1,W7_G2,W7_G3,W7_G4,W7_G5]
#僵尸爪击
W8_GR =pygame.image.load('resource/weapon/w8/w8_gr.png')
W8_GL =pygame.image.load('resource/weapon/w8/w8_gl.png')
#吸血鬼 吸
W91 =pygame.image.load('resource/weapon/w9/w91.png')
W92=pygame.image.load('resource/weapon/w9/w92.png')
W93 =pygame.image.load('resource/weapon/w9/w93.png')
W9S =[W91,W92,W93]
W9SB =[W93,W92,W91]

#女巫 陨石火球
W1201 = pygame.image.load('resource/weapon/w12/w1201.png')
W1202 = pygame.image.load('resource/weapon/w12/w1202.png')
W1203 = pygame.image.load('resource/weapon/w12/w1203.png')
W1204 = pygame.image.load('resource/weapon/w12/w1204.png')
W1205 = pygame.image.load('resource/weapon/w12/w1205.png')
W1206 = pygame.image.load('resource/weapon/w12/w1206.png')
W12S = [W1201,W1202,W1203,W1204,W1205,W1206]

#狼人 变身爪击
W13 =pygame.image.load('resource/weapon/w13/w13.png')
#骑士 变身冲锋
W14 = pygame.image.load('resource/weapon/w14/w14.png')
#国王 炮阵
W151 = pygame.image.load('resource/weapon/w15/w151.png')
W152 = pygame.image.load('resource/weapon/w15/w152.png')
#怪兽 化身基多拉
W161 = pygame.image.load('resource/weapon/w16/w161.png')
W162 = pygame.image.load('resource/weapon/w16/w162.png')
W163 = pygame.image.load('resource/weapon/w16/w163.png')
W164 = pygame.image.load('resource/weapon/w16/w164.png')
W165 = pygame.image.load('resource/weapon/w16/w165.png')
W166 = pygame.image.load('resource/weapon/w16/w166.png')
W16S = [W162,W163]

#天使回家
BACK_ANG1 =  pygame.image.load('resource/action/back_ang1.png')
BACK_ANG2 =  pygame.image.load('resource/action/back_ang2.png')
BACK_ANGS = [BACK_ANG1,BACK_ANG2]

#女巫诅咒
ZUZHOU1 =  pygame.image.load('resource/action/zuzhou1.png')
ZUZHOU2 =  pygame.image.load('resource/action/zuzhou2.png')
ZUZHOU3 =  pygame.image.load('resource/action/zuzhou3.png')
ZUZHOU4 =  pygame.image.load('resource/action/zuzhou4.png')
ZUZHOU = [ZUZHOU1,ZUZHOU2,ZUZHOU3,ZUZHOU4]

#胜利女神的祝福
WISH1 =  pygame.image.load('resource/action/wish1.png')
WISHBOARD =  pygame.image.load('resource/action/wishboard.png')

print('正在加载音频资源')
#音效
SELECT_SOUND = pygame.mixer.Sound('resource/music/select.wav')
SEZI_SOUND = pygame.mixer.Sound('resource/music/sezi.wav')
TITLE_SOUND =  pygame.mixer.Sound('resource/music/title.wav')

#初始场景为title
curs_code = title_page.SCODE
print('加载完毕，开始游戏')
