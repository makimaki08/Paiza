n, x = map(int, input().split())
A = [int(input()) for i in range(n)]

# n * x の２次元配列を作成
dp = [[0]*(x + 1) for _ in range(n)]

# 0列目はすべて1
for i in range(n):
    dp[i][0] = 1

dp[0][A[0]] = 1
    
for i in range(1,n):
    for j in range(x + 1):
        if A[i] <= j:
            dp[i][j] += dp[i - 1][j - A[i]] + dp[i -1][j]
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n-1][x]%(10 ** 9 + 7))