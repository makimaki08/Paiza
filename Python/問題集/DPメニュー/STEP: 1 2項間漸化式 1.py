import numpy as np
x, d, k = map(int, input().split())
arr = np.zeros(k+1)
arr[0] = x

for i in range(1,k+1):
	arr[i] = arr[i-1] + d

print(int(arr[k]))