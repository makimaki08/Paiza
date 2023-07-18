n, k, q = [int(x) for x in input().split()]
output_arr = []
for i in range(n):
	output_arr.append(int(input()))

output_arr.insert(k,q)

for j in range(len(output_arr)):
	print(output_arr[j])