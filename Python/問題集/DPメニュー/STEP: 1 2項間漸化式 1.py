import numpy as np
x, d, k = map(int, input().split())
arr = [x] * (k+1)

for i in range(2, k+1):
	arr[i] = arr[i-1] + d

print(int(arr[k]))