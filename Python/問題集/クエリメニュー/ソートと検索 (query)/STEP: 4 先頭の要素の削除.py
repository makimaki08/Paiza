index = int(input())
input_arr = [int(input()) for i in range(index)]
input_arr.pop(0)

for input_value in input_arr:
	print(input_value)