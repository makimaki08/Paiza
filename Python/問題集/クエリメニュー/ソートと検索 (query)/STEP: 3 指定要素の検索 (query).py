N, Q = map(int, input().split())
A = [int(input()) for _ in range(N)]
K = [int(input()) for _ in range(Q)]

for k in K:
	print("YES" if k in A else "NO")