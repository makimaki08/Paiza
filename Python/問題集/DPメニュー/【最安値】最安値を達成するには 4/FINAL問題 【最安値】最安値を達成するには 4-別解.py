import numpy as np

n, x, a, y, b, z, c = map(int, input().split())
height = 4
weights = [0, x, y, z]
values = [0, a, b, c]

arr = np.zeros((height, n+1))
for i in range(1,height):
	for j in range(1,n+1):
		if i==1:
			arr[i][j] = max(values[i], arr[i][j-weights[i]] + values[i])

		else:
			arr[i][j] = min(arr[i-1][j], arr[i][j-weights[i]] + values[i])

# print(arr)
print(int(arr[height-1][n]))