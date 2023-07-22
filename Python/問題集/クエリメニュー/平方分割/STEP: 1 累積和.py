N, K = map(int, input().split())
input_arr = [int(input()) for _ in range(N)]
output_arr = [int(input()) for _ in range(K)]


for output_i in output_arr:
	sum_value = 0
	for input_i in range(output_i):
		sum_value += input_arr[input_i]
	print(sum_value)