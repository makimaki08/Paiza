import numpy as np
n, a, b = map(int, input().split())

arr = np.zeros((3,n+5))
for i in range(1,3):
	for j in range(1,n+5):
		if i==1:
			arr[i][j] = max(arr[i][j], arr[i][j-2] + a)

		else:
			arr[i][j] = min(arr[i-1][j], arr[i][j-5] + b)

# print(arr)
print(int(arr[2][n]))