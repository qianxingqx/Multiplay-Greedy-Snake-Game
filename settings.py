# 存储一些初始设置参数
import pygame
from functions import *

class Settings():
	
	def __init__(self):

		self.quit = True
		
		self.width = 500
		self.hight = 500

		# ROW和col是将整个屏幕分块，整个屏幕共有多少个行块和多少列块
		self.ROW = 50
		self.COL = 50	

		# snake 头颜色可以自定义
		self.head1_color = (0, 0, 153)
		self.head2_color = (200, 0, 0)
		# 身体的颜色
		self.snake1_color = (0, 204, 255)
		self.snake2_color = (255, 204, 0)
		# 食物颜色
		self.snake1Food_color = (255, 255, 0)
		
		# snake的移动速度
		self.s1_speed = 1
		self.s2_speed = 1
		
		self.init_s1()
		self.init_s2()
		# 食物坐标
		#self.snake1Food = gen_food(self)

	
	def init_s1(self):
		self.snake1_direct = 'left'
		# 蛇头坐标定在中间
		self.head1 = Point(row=int(self.ROW/2 -10), col=int(self.COL/2))
		# 初始化蛇身的元素数量
		self.snake1 = [
			Point(row=self.head1.row, col=self.head1.col + 1),
			Point(row=self.head1.row, col=self.head1.col + 2),
			Point(row=self.head1.row, col=self.head1.col + 3)
				]
	def init_s2(self):
		self.snake2_direct = 'left'
		self.head2 = Point(row=int(self.ROW/2 +10), col=int(self.COL/2))
		self.snake2 = [Point(row=self.head2.row, col=self.head2.col + 1),
			Point(row=self.head2.row, col=self.head2.col + 2),
			Point(row=self.head2.row, col=self.head2.col + 3)]
		
		
