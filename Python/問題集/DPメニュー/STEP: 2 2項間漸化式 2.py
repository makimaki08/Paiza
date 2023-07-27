x, d = map(int, input().split())
q = int(input())
arr = [x] * (q+1)

for i in range(2,q+1):
	arr[i] = arr[i-1] + d

for _ in range(q):
	index = int(input())
	print(arr[index])
