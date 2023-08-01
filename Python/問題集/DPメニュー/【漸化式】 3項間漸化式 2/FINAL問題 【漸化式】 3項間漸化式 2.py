import numpy as np
arr = np.ones(40+1)

for i in range(3,40+1):
	arr[i] = arr[i-2] + arr[i-1]

Q = int(input())
for _ in range(Q):
	index = int(input())
	print(int(arr[index]))