class Point:
	def __init__(self, alphabet ,path_a, path_b):
		self.alphabet = alphabet
		self.path_a = path_a
		self.path_b = path_b


# 地点の数 N と、移動の回数 K、開始点S
point_num, move_num, start_point = map(int, input().split())
point_arr = [None]*point_num

# 地点を記録
for i in range(point_num):
	input_arr = input().split()
	alphabet = input_arr[0]
	path_a = int(input_arr[1])
	path_b = int(input_arr[2])

	point_arr[i] = Point(alphabet, path_a, path_b)
	# print(alphabet, path_a, path_b)

# 経路
current = start_point-1
route = point_arr[current].alphabet


for j in range(move_num):
	direction = int(input())

	if(direction==1):
		current = point_arr[current].path_a-1
		route += point_arr[current].alphabet

	else:
		current = point_arr[current].path_b-1
		route += point_arr[current].alphabet

print(route)