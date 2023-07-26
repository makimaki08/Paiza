def calc_min_and_max_in_divisioned_area(X, range_min, range_max, sqrt, left, right):
    rst_min, rst_max = X[left], X[left]
    now = left
    while now <= right:
        if now % sqrt == 0 and now + sqrt <= right:
            rst_min = min(rst_min, range_min[now // sqrt])
            rst_max = max(rst_max, range_max[now // sqrt])
            now += sqrt
        else:
            rst_min = min(rst_min, X[now])
            rst_max = max(rst_max, X[now])
            now += 1

    return rst_min, rst_max


N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

sqrt = int(pow(N, 0.5))
if sqrt ** 2 < N:
    sqrt += 1

range_max = [-1] * N
range_min = [-1] * N
for i in range(sqrt):
    start, end = sqrt * i, sqrt * (i + 1)
    range_max[i] = max(S[start:end])
    range_min[i] = min(S[start:end])

for _ in range(K):
    a_left, a_right, b_left, b_right = map(lambda x: int(x) - 1, input().split())

    a_rg = a_right - a_left + 1
    b_rg = b_right - b_left + 1

    a_rg_min, a_rg_max = calc_min_and_max_in_divisioned_area(
        S, range_min, range_max, sqrt, a_left, a_right
    )
    b_rg_min, b_rg_max = calc_min_and_max_in_divisioned_area(
        S, range_min, range_max, sqrt, b_left, b_right
    )

    a_score = a_rg_max - a_rg_min
    b_score = b_rg_max - b_rg_min

    if a_score == b_score:
        print("DRAW")
    elif a_score > b_score:
        print("A")
    else:
        print("B")