import numpy as np

N = int(input())
humans = [int(input()) for _ in range(N)]
ans = np.ones(N)

# print(humans)
# print(ans)

for i in range(1,N):
	ans[i] = ans[i-1]+1 if humans[i-1]>=humans[i] else 1

print(int(max(ans)))