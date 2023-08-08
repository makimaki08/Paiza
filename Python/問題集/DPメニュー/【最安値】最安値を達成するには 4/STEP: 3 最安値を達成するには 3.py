import numpy as np
n, x, a, y, b = map(int, input().split())

arr = np.zeros((3, n+y))

for i in range(1,3):
	for j in range(n+y):
		if i==1:
			arr[i][j] = max(arr[i][j], arr[i][j-x] + a)
		else:
			arr[i][j] = min(arr[i-1][j], arr[i][j-y] + b)

print(int(arr[2][n]))