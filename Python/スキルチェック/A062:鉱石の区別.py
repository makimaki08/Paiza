import numpy as np
N, L = map(int, input().split())
arr = []
for _ in range(N):
	arr.append(list(map(int,input().split())))


print(N, L)
print(arr)
print(np.sum(arr,axis=0))
print(ans)