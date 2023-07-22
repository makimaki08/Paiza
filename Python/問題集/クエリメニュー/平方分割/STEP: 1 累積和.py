import numpy
N, K = map(int, input().split())
input_arr = [int(input()) for _ in range(N)]

sum_arr = numpy.cumsum(input_arr)

for _ in range(K):
	index = int(input())
	print(sum_arr[index-1])