N, K = map(int, input().split())
flag = False
for _ in range(N):
	A = int(input())
	flag = True if A==K else False

if flag:
	print("YES")
else:
	print("NO")
