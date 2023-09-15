import numpy as np
N, durability = map(int,input().split())
points = [] # 各金魚の美しさ
weights = [] # 各金魚の重量

for _ in range(N):
    w, p = map(int,input().split())
    weights.append(w)
    points.append(p)

# print(N,durability)
# print(points)
# print(weights)

# 次使用する配列に今回の結果を残すので+1している
dp = [[0]*(durability) for i in range(N+1)] # DPの配列作成

for i in range(N):
    for j in range(durability):
        if j < weights[i]: # この時点では許容量を超えていないので選択しない
            dp[i+1][j] = dp[i][j] # ただ選択はしていないが、今回の情報をそのままi+1の方へ移す
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-weights[i]]+points[i])

print(dp[N][durability-1])