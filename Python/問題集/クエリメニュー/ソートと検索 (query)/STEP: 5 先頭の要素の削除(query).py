input_num, action_num = map(int, input().split())
input_arr = [int(input()) for _ in range(input_num)]

for i in range(action_num):
	if input() == "pop":
		input_arr.pop(0)
	else:
		for input_value in input_arr:
			print(input_value)
