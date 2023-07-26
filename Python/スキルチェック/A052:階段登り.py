import numpy as np
N = int(input())
arr = np.ones(N+1)
A, B = map(int, input().split())
# print(N//A)
# print(N//B)

# N個に先頭の0を合わせた、N+1回ループ
for i in range(N//A+1):
	for j in range(N//B+1):
		AB = A*i + B*j
		# print(AB)
		if(AB>N):
			arr[N] = 0
		else:
			arr[AB] = 0


ans = int(sum(arr))
print(ans)