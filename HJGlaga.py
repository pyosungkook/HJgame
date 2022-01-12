#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import random

# 게임에 사용되는 전역 변수 정의
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640
fight_width = 36
fight_height = 38
enemy_width = 26
enemy_height = 20

# 게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
   global gamepad
   gamepad.blit(obj, (x,y))

# 게임 실행 메인 함수
def runGame():
   global gamepad, clock, fighter, enemy, bullet

   bullet_xy=[]

   # 전투기 초기 위치 (x, y) 설정
   x = pad_width*0.45
   y = pad_height*0.9
   x_change = 0

   enemy_x = random.randrange(0, pad_width-enemy_width)
   enemy_y = 0
   enemy_speed = 5

   ongame = False
   while not ongame:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            ongame = True
         
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               x_change -= 5
                    
            elif event.key == pygame.K_RIGHT:
               x_change += 5

            elif event.key == pygame.K_SPACE:
                if len(bullet_xy)<4:
                    bullet_x = x + fight_width/2
                    bullet_y = y - fight_height
                    bullet_xy.append([bullet_x, bullet_y])   

         if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               x_change = 0

      gamepad.fill(BLACK)

      # 전투기의 위치를 재조정
      x += x_change
      if x < 0:
         x = 0
      elif x > pad_width - fight_width:
         x = pad_width - fight_width

      drawObject(fighter, x, y)
       
     
      drawObject(enemy, enemy_x, enemy_y)

      if len(bullet_xy)!=0:
          for i, bxy in enumerate(bullet_xy):
              bxy[1]-=10
              bullet_xy[i][1]=bxy[1]

              if bxy[1] <= 0:
                  try:
                      bullet_xy.remove(bxy)
                  except:
                      pass

      if len(bullet_xy)!=0:
           for bx, by in bullet_xy:
               drawObject(bullet,bx,by)            

      enemy_y +=enemy_speed
      if enemy_y > pad_height:
          enemy_y =0
          enemy_x = random.randrange(0, pad_width-enemy_width)
      pygame.display.update()
      clock.tick(60)

   pygame.quit()

# 게임 초기화 함수
def initGame():
   global gamepad, clock, fighter, enemy, bullet

   pygame.init()
   gamepad = pygame.display.set_mode((pad_width, pad_height))
   pygame.display.set_caption('HJGalaga')
   fighter = pygame.image.load('C:\\Users\\user\\Desktop\\fighter.png')
   enemy = pygame.image.load('C:\\Users\\user\\Desktop\\enemy.png')
   bullet = pygame.image.load('C:\\Users\\user\\Desktop\\bullet.png')
   clock = pygame.time.Clock()

initGame()
runGame()


# In[ ]:




