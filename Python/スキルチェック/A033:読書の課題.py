import numpy as np
N, max_days = map(int,input().split())
pages = [] # 総ページ数
days = [] # 読むのにかかる日数

for _ in range(N):
    p,d = map(int,input().split())
    pages.append(p)
    days.append(d)

# 次使用する配列に今回の結果を残すので+1している
dp = [[0]*(max_days+1) for i in range(N+1)] # DPの配列作成


for i in range(N):
	for j in range(max_days+1):
		if j < days[i]:
			dp[i+1][j] = dp[i][j]
		else:
			dp[i+1][j] = max(dp[i][j], dp[i][j-days[i]]+pages[i])

print(dp[N][max_days])