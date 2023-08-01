import numpy as np
x, d_1, d_2 = map(int, input().split())
Q = int(input())

arr = np.zeros(1001)
arr[1] = x
for i in range(2,1001):
	if i%2==1:
		arr[i] = arr[i-1] + d_1
	else:
		arr[i] = arr[i-1] + d_2


for _ in range(Q):
	index = int(input())
	print(int(arr[index]))