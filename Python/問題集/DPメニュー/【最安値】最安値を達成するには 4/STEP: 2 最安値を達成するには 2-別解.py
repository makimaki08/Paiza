import numpy as np

n, a, b = map(int, input().split())
weights = [0, 2, 5]
values = [0, a, b]
arr = np.zeros((len(weights), n+1))

for i in range(1, len(weights)):
	for j in range(1, n+1):
		# 配列の初期設定
		if i==1:
			arr[i][j] = max(values[i], arr[i][j-weights[i]] + values[i])

		else:
			arr[i][j] = min(arr[i-1][j], arr[i][j-weights[i]] + values[i])

# print(arr)
print(int(arr[len(weights)-1][n]))