class Robot:
	def __init__(self, x, y, level):
		self.x = x
		self.y = y
		self.level = level

max_column, max_row, robot_num, move_num = [int(x) for x in input().split()]

space = [[0]*max_row]*max_column
for s in space:
	print(s)

print(s)
# 工具箱が置かれたマスのx,yは、10個で固定
for i in range(10):
	y, x = [int(z) for z in input().split()]
	print(x,y)
	space[y][x] = 1


for s in space:
	print(s)