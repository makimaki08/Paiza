import numpy as np

n = int(input())
humans = [int(input()) for _ in range(n)]
ans = np.ones(n)


for i in range(1,n):
	ans[i] = ans[i-1] + 1 if humans[i-1]<=humans[i] else 1

print(int(max(ans)))