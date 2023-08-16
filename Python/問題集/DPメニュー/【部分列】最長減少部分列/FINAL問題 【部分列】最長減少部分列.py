import numpy as np
N = int(input())
trees = [int(input()) for _ in range(N)]
dp = np.ones(N)

for i in range(1, N):
	for j in range(i):
		if trees[i]<=trees[j]:
			dp[i] = max(dp[i], dp[j]+1)

print(int(max(dp)))