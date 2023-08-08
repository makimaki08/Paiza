import numpy as np
n, x, a, y, b, z, c = map(int, input().split())

# print(n, x, a, y, b, z, c)
index = max(x, y, z)
arr = np.zeros((4,n+index))

for i in range(1,4):
	for	j in range(n+index):
		if i==1:
			arr[i][j] = max(arr[i][j], arr[i][j-x] + a)

		elif i == 2:
			arr[i][j] = min(arr[i-1][j], arr[i][j-y] + b)

		elif i==3:
			arr[i][j] = min(arr[i-1][j], arr[i][j-z] + c)

# print(arr)
print(int(arr[3][n-1]))