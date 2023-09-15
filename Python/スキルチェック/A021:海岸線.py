import numpy as np
H, W = map(int, input().split())
# arr = np.zeros((H+1, W+1))
arr = [["."]*(H+1) for i in range(W+1)]
for i in range(1,H+1):
	input_line = input()
	for j in range(1,W+1):
		arr[i][j] = input_line[j-1]
arr.append(["."]*(W+1))
ans_arr = [] # 面積, 境界線

for i in range(1,H+1):
	area = 0
	border = 0	
	for j in range(1,W+1):
		target = arr[i][j]
		top = arr[i-1][j]
		bottom = arr[i+1][j]
		left = arr[i][j-1]
		right = arr[i][j+1]
		
		if target=="#":
			area+=1
