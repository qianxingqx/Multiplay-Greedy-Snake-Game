import random
import pygame

# 设置一个initial模块，让self.snake撞墙后是重置到初始位置
class Point():
    row = 0
    col = 0
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(row=self.row, col=self.col)


# 生成食物并且不让食物生成在蛇的身体里面
def gen_food(sets):
    while 1:
        position = Point(row=random.randint(0, sets.ROW - 1), col=random.randint(0, sets.COL - 1)) # 生成一个随机方块点
        is_coll = False
        if sets.head1.row == position.row and sets.head1.col == position.col: # 如果随机生成的方块点不与头重合，则退出
            is_coll = True
        for body in sets.snake1:
            if body.row == position.row and body.col == position.col:
                is_coll = True
                break
        if not is_coll:
            break
    return position

# 需要执行很多步画图操作 所以定义一个函数
def rects(window, sets, point, color):
    # 定位 画图需要left和top
    left = point.col * sets.width / sets.COL
    top = point.row * sets.hight / sets.ROW
    # 将方块涂色
    pygame.draw.rect(window, color, (left, top, sets.width / sets.COL, sets.hight / sets.ROW))

# 检测事件响应
def check_events(sets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sets.quit = False
		# 检测是否按下鼠标
		#elif event.type == pygame.MOUSEBUTTONDOWN:
		#	mouse_x, mouse_y = pygame.mouse.get_pos()
		# 检测键盘是否按下
		elif event.type == pygame.KEYDOWN:
			check_keydown(sets, event)

# 检测按键按下
def check_keydown(sets, event):
	# 这里小细节,蛇不可以直接左右上下 要判断当前是在什么状态下前行
	if event.key == pygame.K_w: # 当想要向上移动时，只有当目前的方向是左右是才执行
		#sets.snake1_direct = 'top'
		if sets.snake1_direct == 'left' or sets.snake1_direct == 'right':
			sets.snake1_direct = 'top'
	if event.key == pygame.K_s:
		if sets.snake1_direct == 'left' or sets.snake1_direct == 'right':
			sets.snake1_direct = 'bottom'
	if event.key == pygame.K_a:
		if sets.snake1_direct == 'top' or sets.snake1_direct == 'bottom':
			sets.snake1_direct = 'left'
	if event.key == pygame.K_d:
		if sets.snake1_direct == 'top' or sets.snake1_direct == 'bottom':
			sets.snake1_direct = 'right'
	# sets.snake2
	if event.key == pygame.K_UP: # 当想要向上移动时，只有当目前的方向是左右是才执行
		#sets.snake2_direct = 'top'
		if sets.snake2_direct == 'left' or sets.snake2_direct == 'right':
			sets.snake2_direct = 'top'
	if event.key == pygame.K_DOWN:
		if sets.snake2_direct == 'left' or sets.snake2_direct == 'right':
			sets.snake2_direct = 'bottom'
	if event.key == pygame.K_LEFT:
		if sets.snake2_direct == 'top' or sets.snake2_direct == 'bottom':
			sets.snake2_direct = 'left'
	if event.key == pygame.K_RIGHT:
		if sets.snake2_direct == 'top' or sets.snake2_direct == 'bottom':
			sets.snake2_direct = 'right'
