import numpy as np
H, W, N = map(int, input().split())

box = []
for h in range(H):
	input_arr = list(map(int, input().split()))
	input_arr.insert(0,0)
	box.append(input_arr)
# print(box)

for n in range(N):
	sum_value = 0
	max_y, max_x = map(int, input().split())
	for y in range(max_y):
		sum_arr = np.cumsum(box[y])
		# tmp = sum_arr[max_x]- sum_arr[0]
		# print(sum_arr)
		# print(sum_arr[max_x], sum_arr[0])
		# print(tmp)

		sum_value += sum_arr[max_x]
	print(sum_value)
	# print("--------------")

# arr = np.zeros((H,W))
# print(arr)
# box = [ list(map(int,input().split(" "))) for i in range(H)]
# print(box[:1][:1])

# for n in range(N):
# 	x, y = map(int, input().split())
# 	