N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = [0] + A[:]
for i in range(1, N + 1):
    ans[i] += ans[i - 1]

for _ in range(K):
    a_left, a_right, b_left, b_right = map(int, input().split())

    a = ans[a_right] - ans[a_left - 1]
    b = ans[b_right] - ans[b_left - 1]

    if a_right - a_left + 1 >= N / 3:
        a = -1
    if b_right - b_left + 1 >= N / 3:
        b = -1

    if a == b:
        print("DRAW")
    elif a > b:
        print("A")
    else:
        print("B")