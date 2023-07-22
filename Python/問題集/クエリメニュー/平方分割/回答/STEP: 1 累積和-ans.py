N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = [0] + A[:]
for i in range(1, N + 1):
    ans[i] += ans[i - 1]

for _ in range(K):
    q = int(input())
    print(ans[q])