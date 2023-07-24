H, W, N = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(H)]

ans = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    ans[i] = [0] + A[i - 1][:]
    for j in range(1, W + 1):
        ans[i][j] += ans[i - 1][j] + ans[i][j - 1] - ans[i - 1][j - 1]

for _ in range(N):
    a, b, c, d = map(int, input().split())

    val = ans[c][d]
    if 0 < a and 0 < b:
        val += ans[a - 1][b - 1]
    if 0 < a:
        val -= ans[a - 1][d]
    if 0 < b:
        val -= ans[c][b - 1]

    print(val)