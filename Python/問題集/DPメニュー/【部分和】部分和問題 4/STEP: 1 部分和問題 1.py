import numpy as np

input_arr = input().split()
N = int(input_arr[0])
max_weight = int(input_arr[1])
weights = [int(input()) for i in range(N)]
weights.insert(0,0)
# print(weights)

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