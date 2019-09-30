# -*- coding: utf-8 -*-
# @Time    : 19-9-23 上午9:58
# @Author  : Redtree
# @File    : s_game_loading.py
# @Desc : 游戏加载页面


from logic import loader
from data import player_runtime
from utils import saver
from data import game_page
from data import color_rgb


def dojob(x,y,is_mouse_down,keys):

      #显示底版
      loader.screen.blit(loader.SAVE_BOARD_TITLE,(0,0))
      a0 = (x>=20 and x<100 and y>=20 and y<60)
      a1 = (x>=0 and x<=860 and y>=80 and y<280)
      a2 = (x>=0 and x<=860 and y>=280 and y<480)
      a3 = (x>=0 and x<=860 and y>=480 and y<680)

      if a0:
        loader.screen.blit(loader.SAVE_BOARD_TITLE_BACK2,(20,20))
        if is_mouse_down == True:
            player_runtime.INFO['loading'] = False
      else:
        loader.screen.blit(loader.SAVE_BOARD_TITLE_BACK1, (20,20))

      if player_runtime.INFO['checksover']==True:
          loader.screen.blit(loader.SAVE_BOARD_LOT, (0, 80))
          loader.screen.blit(loader.SAVE_BOARD_LOT, (0, 280))
          loader.screen.blit(loader.SAVE_BOARD_LOT, (0, 480))

          s = 90
          for sd in player_runtime.SDATA:
              try:
                  img_url = sd['img_path']
                  if not img_url == '':
                      img_res = sd['img_res']
                      cr = sd['round']
                      cd = sd['date']
                      loader.screen.blit(img_res, (15, s))
                      crt = loader.BAIKE_FONT.render(cr, True, color_rgb.WHITE,
                                                     None)
                      cdt = loader.BAIKE_FONT.render(cd, True, color_rgb.WHITE,
                                                     None)

                      loader.screen.blit(crt, (450, s + 35))
                      loader.screen.blit(cdt, (450, s + 90))
              except Exception as err:
                  print('save read err')
                  print(err)
              s = s + 200


          #执行读档逻辑
          #先提示
          loader.screen.blit(loader.CHECK_LOAD, (230, 200))
          # 确认按钮
          loader.screen.blit(loader.SURE, (300, 370))
          # 取消按钮
          loader.screen.blit(loader.SURENO, (460, 370))

          #点击确认
          if x>=300 and x<=380 and y>=370 and y<=410 :
              loader.screen.blit(loader.SELECT_SAVE, (300, 370))
              if is_mouse_down==True:
                  try:
                      cslot = player_runtime.INFO['cslot']+1
                      cslot_path = 'save/slot'+str(cslot)+'.pkl'
                      res = saver.load(cslot_path)
                      if res == False:
                          print('存档异常')
                      else:
                          player_runtime.INFO = res
                          player_runtime.INFO['checksover']=False
                          player_runtime.INFO['saving']=False
                          loader.curs_code = game_page.SCODE
                  except Exception as err:
                      print('load error')
                      print(err)

          elif x>=460 and x<=540 and y>=370 and y<=410 :
              loader.screen.blit(loader.SELECT_SAVE, (460, 370))
              if is_mouse_down==True:
                  #取消的话就返回到界面浏览状态就行了
                  player_runtime.INFO['checksover']=False

      else:
          #执行选择存档逻辑
          if a1:
            loader.screen.blit(loader.SAVE_BOARD_LOTA, (0, 80))
            if is_mouse_down == True and not player_runtime.SDATA[0]['img_path']=='':
                    player_runtime.INFO['checksover']=True
                    player_runtime.INFO['cslot']=0
          else:
            loader.screen.blit(loader.SAVE_BOARD_LOT, (0, 80))

          if a2:
            loader.screen.blit(loader.SAVE_BOARD_LOTA, (0, 280))
            if is_mouse_down == True and not player_runtime.SDATA[1]['img_path']=='':
                    player_runtime.INFO['checksover']=True
                    player_runtime.INFO['cslot']=1
          else:
            loader.screen.blit(loader.SAVE_BOARD_LOT, (0, 280))

          if a3:
            loader.screen.blit(loader.SAVE_BOARD_LOTA, (0, 480))
            if is_mouse_down == True and not player_runtime.SDATA[2]['img_path']=='':
                    player_runtime.INFO['checksover']=True
                    player_runtime.INFO['cslot']=2
          else:
            loader.screen.blit(loader.SAVE_BOARD_LOT, (0, 480))

          #绘制存档截图
          s = 90
          for sd in player_runtime.SDATA:
              try:
                  img_url = sd['img_path']
                  if not img_url == '':
                      img_res = sd['img_res']
                      cr = sd['round']
                      cd = sd['date']
                      loader.screen.blit(img_res, (15, s))
                      crt = loader.BAIKE_FONT.render(cr, True, color_rgb.WHITE,
                                                     None)
                      cdt = loader.BAIKE_FONT.render(cd, True, color_rgb.WHITE,
                                                     None)

                      loader.screen.blit(crt, (450, s + 35))
                      loader.screen.blit(cdt, (450, s + 90))
              except Exception as err:
                  print('save read err')
                  print(err)
              s = s + 200


