import numpy as np
n, a, b = map(int, input().split())
weights = [0,1,2]
values = [0,a,b]

arr = np.zeros((len(weights), n+1))


for i in range(1,len(weights)):
	for j in range(1,n+1):
		# i==1の時は、値の初期化を行う
		if i==1:
			if j<weights[i]:
				arr[i][j] = values[i]
			else:
				arr[i][j] = arr[i][j-weights[i]] + values[i]
		# i>1の時は、前の配列と比較して値を更新する。
		else:
			arr[i][j] = min(arr[i-1][j], arr[i][j-weights[i]] + values[i])


print(int(arr[len(weights)-1][n]))