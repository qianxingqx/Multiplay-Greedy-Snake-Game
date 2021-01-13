"""
双人贪吃蛇游戏
Created on Fri Oct 30 2020
@author: qianxingdu
"""
import pygame
import random
from sys import exit
from settings import Settings, Point
from score_board import Scoreboard
from functions import *

sets = Settings()

# 初始化，屏幕宽度和高度
pygame.init()
window = pygame.display.set_mode((sets.width, sets.hight))
pygame.display.set_caption('Multiplay Greedy Snake_qxd')


score = Scoreboard(sets,window)

sfoods = []
for i in range(10): # 食物的数量
    sfoods.append(gen_food(sets))


# 设置帧频率
clock = pygame.time.Clock()
while sets.quit:
    # 处理帧频 锁帧
    clock.tick(10) # 设置该项可以改变游戏速度，值越大速度越快
    
    check_events(sets)
                    
    # 吃东西，当头目前的位置和食物的坐标相同时
    snake1_eat = False
    snake2_eat = False
    for index, food in enumerate(sfoods):
        if (sets.head1.row == food.row and sets.head1.col == food.col):
            snake1_eat = True
            sfoods[index] = Point(row=random.randint(0, sets.ROW - 1), col=random.randint(0, sets.COL - 1))
        if (sets.head2.row == food.row and sets.head2.col == food.col):
            snake2_eat = True
            sfoods[index] = Point(row=random.randint(0, sets.ROW - 1), col=random.randint(0, sets.COL - 1))
    # 处理蛇的身子    # 1.把原来的头插入到sets.snake1的头上    # 2.把最后一个sets.snake1删掉
    
    sets.snake1.insert(0, sets.head1.copy()) # 每一次从头部增加了一个块，所以当没有吃东西的时候，需要每次删除掉一个模块来抵消，否则就会是拖尾的效果
    if not snake1_eat: # 没有吃东西的时候
        sets.snake1.pop() # 必须pop掉末尾的模块
    
    sets.snake2.insert(0, sets.head2.copy())
    if not snake2_eat:
        sets.snake2.pop()

    # sets.snake 1 移动一下
    if sets.snake1_direct == 'left':
        sets.head1.col -= sets.s1_speed
    if sets.snake1_direct == 'right':
        sets.head1.col += sets.s1_speed
    if sets.snake1_direct == 'top':
        sets.head1.row -= sets.s1_speed
    if sets.snake1_direct == 'bottom':
        sets.head1.row += sets.s1_speed
        
    if sets.snake2_direct == 'left':
        sets.head2.col -= sets.s2_speed
    if sets.snake2_direct == 'right':
        sets.head2.col += sets.s2_speed
    if sets.snake2_direct == 'top':
        sets.head2.row -= sets.s2_speed
    if sets.snake2_direct == 'bottom':
        sets.head2.row += sets.s2_speed 
        
    # 判断s1身体是否撞到边缘或撞到自身
    s1dead = False
    if sets.head1.col < 0 or sets.head1.row < 0 or sets.head1.col >= sets.COL or sets.head1.row >= sets.ROW:
        s1dead = True
    for body in sets.snake1: # s1头部碰撞到s1身体
        if sets.head1.col == body.col and sets.head1.row == body.row:
            s1dead = True
            break
    for body in sets.snake2: # s1头部碰撞到s2身体
        if sets.head1.col == body.col and sets.head1.row == body.row:
            s1dead = True
            break
    if s1dead:
        sets.init_s1()
        s1dead = False
        #sets.head1.row, sets.head1.col = int(sets.ROW/2 -10), int(sets.COL/2)
        #sets.snake1 = []
        #print('Game Over')
        #quit = False
    
    # 判断s2碰撞
    s2dead = False
    if sets.head2.col < 0 or sets.head2.row < 0 or sets.head2.col >= sets.COL or sets.head2.row >= sets.ROW:
        s2dead = True
    for body in sets.snake2:
        if sets.head2.col == body.col and sets.head2.row == body.row:
            s2dead = True
            break
    for body in sets.snake1:
        if sets.head2.col == body.col and sets.head2.row == body.row:
            s2dead = True
            break
    if s2dead:
        sets.init_s2()
        s2dead = False
        
    # 背景画图
    pygame.draw.rect(window, (230, 255, 230), (0, 0, sets.width, sets.hight))

    # 蛇头
    rects(window, sets, sets.head1, sets.head1_color)
    rects(window, sets, sets.head2, sets.head2_color)
    # 绘制食物
    for food in sfoods:
        rects(window, sets, food, sets.snake1Food_color)
    # 绘制蛇的身子
    for body1 in sets.snake1:
        rects(window, sets, body1, sets.snake1_color)
    for body2 in sets.snake2:
	    rects(window, sets, body2, sets.snake2_color)
    # 绘制得分
    score.prep_score(sets)
    score.show_score()

    # 交还控制权
    pygame.display.flip()

