import numpy as np

N, max_weight = map(int, input().split())
weights = [0] + [int(input()) for i in range(N)]

dp = np.zeros((N+1, max_weight+1))
dp[0][0] = 1

for i in range(1,N+1):
	for j in range(max_weight+1):
		if j>=weights[i]:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]])
		else:
			dp[i][j] = dp[i-1][j]
if dp[N][max_weight]==1:
	print("yes")
else:
	print("no")