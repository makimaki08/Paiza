import numpy as np
arr = np.ones(41)

for i in range(3,41):
	arr[i] = arr[i-2] + arr[i-1]

index = int(input())
print(int(arr[index]))
