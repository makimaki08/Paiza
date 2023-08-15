import numpy as np

N = int(input())
arr = [int(input()) for _ in range(N)]
ans = np.ones(N)

# for文を1つで実施しようとすると、前DPの値をうまく利用することができない
for i in range(1,N):
	# ここでforループをもう一度回す必要あり
	for j in range(i):
		if arr[j]<=arr[i]:
			ans[i] = max(ans[i],ans[j] + 1)

# print(ans)
print(int(max(ans)))
