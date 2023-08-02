import numpy as np
n, a, b = map(int, input().split())
arr = np.zeros(n+1)
arr[1] = a

for i in range(2,n+1):
	arr[i] = min(arr[i-1] + a, arr[i-2] + b)

print(int(arr[n]))