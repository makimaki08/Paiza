A = [int(input()) for _ in range(10000)]

ans = [-1] * 100
for i in range(100):
    start, end = 100 * i, 100 * (i + 1)

    ans[i] = max(A[start:end])

for val in ans:
    print(val)