
import pygame.font

# 显示得分信息的类
class Scoreboard():
	
	def __init__(self, sets, window):
		
		
		# 初始化显示得分涉及的属性
		self.window = window
		self.window_rect = window.get_rect()
		
		# 显示得分信息时使用的字体设置
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 30)
		self.font2 = pygame.font.SysFont(None, 35)
		
		# 准备初始得分图像
		self.prep_score(sets)
	
	def prep_score(self, sets):
		# 将得分转换为一幅渲染的图像
		s1_score = int(len(sets.snake1))-3
		s1_str = "{:,}".format(s1_score)
		self.s1_image = self.font.render('Blue Guy:'+s1_str, True, self.text_color, (230, 255, 230))
		# 将得分放在屏幕右上角
		self.s1_rect = self.s1_image.get_rect()
		self.s1_rect.left = 0
		self.s1_rect.top = 0
		
		# Snake2
		s2_score = int(len(sets.snake2))-3
		s2_str = "{:,}".format(s2_score)
		self.s2_image = self.font.render('Red Guy:'+s2_str, True, self.text_color, (230, 255, 230))
		# 将得分放在屏幕右上角
		self.s2_rect = self.s2_image.get_rect()
		self.s2_rect.left = sets.width - 110
		self.s2_rect.top = 0
	
	def show_score(self):
		# 在屏幕上显示得分
		self.window.blit(self.s1_image, self.s1_rect)
		self.window.blit(self.s2_image, self.s2_rect)
		



