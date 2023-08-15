import numpy as np

N = int(input())
arr = [int(input()) for _ in range(N)]
ans = np.zeros(N)
ans[0] = 1

for i in range(1,N):
	if arr[i-1]<=arr[i]:
		ans[i] = ans[i-1] + 1
	else:
		ans[i] = ans[i-1]

# print(ans)
print(int(ans[N-1]))

"""
5
100　→ 1
102　→ 2
101　→ 2
91　→ 2
199　→ 3

3
"""