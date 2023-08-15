import numpy as np

N = int(input())
arr = [int(input()) for _ in range(N)]
ans = np.zeros((N+1,N))


for i in range(1,N):
	ans[i][0] = 1
	for j in range(1,N):
		if arr[j-1]<=arr[j]:
			ans[i][j] = max(1, ans[i][j-1]+1)
		else:
			ans[i][j] = ans[i][j-1]

# print(int(max(ans)))
print(ans)

"""
5
100
102
101
91
199

3
"""