n, x, a, y, b = map(int, input().split())

dp = [10000000] * (n + y)

dp[0] = 0

for i in range(1, n + y):
    if i >= x:
        dp[i] = min(dp[i], dp[i - x] + a)
    if i >= y:
        dp[i] = min(dp[i], dp[i - y] + b)

print(min(dp[n:]))