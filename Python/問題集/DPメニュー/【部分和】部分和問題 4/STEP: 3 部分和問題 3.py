import numpy as np

N, max_weight = map(int, input().split())
weights = [0] + [int(input()) for _ in range(N)] 
dp = np.zeros((N+1, max_weight+1))

for i in range(N+1):
	dp[i][0] = 1

for i in range(1,N+1):
	for j in range(max_weight+1):
		if weights[i]<=j:
			# dp[i][j] = dp[i-1][j-weights[i]] + dp[i][j-weights[i]]
			dp[i][j] = min(dp[i-1][j-weights[i]] + 1, dp[i-1][j])
		else:
			dp[i][j] = dp[i-1][j]

print(int(dp[N][max_weight]))
