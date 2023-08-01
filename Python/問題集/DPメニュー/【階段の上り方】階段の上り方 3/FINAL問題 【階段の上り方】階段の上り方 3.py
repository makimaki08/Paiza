import numpy as np
n, a, b, c = map(int, input().split())
arr = np.zeros(n+1)
arr[0] = 1

for i in range(1,n+1):
	if i>=a:
		arr[i]+= arr[i-a]
	if i>=b:
		arr[i]+= arr[i-b]
	if i>=c:
		arr[i]+= arr[i-c]

print(int(arr[n]))
