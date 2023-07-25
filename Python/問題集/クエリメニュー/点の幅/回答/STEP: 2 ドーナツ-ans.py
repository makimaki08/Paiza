def calc_interval_sum(X, a, b, c, d):
    rst = X[c][d]
    if 0 < a and 0 < b:
        rst += X[a - 1][b - 1]
    if 0 < a:
        rst -= X[a - 1][d]
    if 0 < b:
        rst -= X[c][b - 1]

    return rst


H, W, N = map(int, input().split())
C = [[int(x) for x in input().split()] for _ in range(H)]

ans = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    ans[i] = [0] + C[i - 1][:]
    for j in range(1, W + 1):
        ans[i][j] += ans[i - 1][j] + ans[i][j - 1] - ans[i - 1][j - 1]

for _ in range(N):
    y, x, b, s = map(int, input().split())

    bm, sm = b // 2, s // 2

    outer = calc_interval_sum(ans, y - bm, x - bm, y + bm, x + bm)
    inner = calc_interval_sum(ans, y - sm, x - sm, y + sm, x + sm)
    print(outer - inner)