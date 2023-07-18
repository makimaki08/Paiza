student_num,attendance = map(int, input().split())
student_arr = {}

for _ in range(student_num):
	input_arr = input().split()
	student_arr[int(input_arr[0])] = input_arr[1]

for _ in range(attendance):
	print(student_arr.get(int(input())))