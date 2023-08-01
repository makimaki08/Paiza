x, d = map(int, input().split())
arr = [x] * (1000+1)

for i in range(2,1000+1):
	arr[i] = arr[i-1] + d

q = int(input())
for _ in range(q):
	index = int(input())
	print(arr[index])
