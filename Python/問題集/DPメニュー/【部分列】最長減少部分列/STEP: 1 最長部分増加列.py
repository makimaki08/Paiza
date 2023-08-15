import numpy as np

N = int(input())
arr = [int(input()) for _ in range(N)]
ans = np.zeros(N)
ans[0] = 1

# for文を1つで実施しようとすると、前DPの値をうまく利用することができない
for i in range(1,N):
	if arr[i-1]<=arr[i]:
		ans[i] = max(1,ans[i-1] + 1)
	else:
		ans[i] = 1
	print(i, ans[i])

# print(ans)
print(int(max(ans)))
