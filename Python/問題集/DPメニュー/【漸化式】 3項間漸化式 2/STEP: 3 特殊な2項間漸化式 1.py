import numpy as np
x, d_1, d_2, k = map(int, input().split())
arr = np.zeros(k+1)
arr[1] = x

for n in range(2,k+1):
	if n%2==1:
		arr[n] = int(arr[n-1] + d_1)
	else:
		arr[n] = int(arr[n-1] + d_2)

print(int(arr[k]))

