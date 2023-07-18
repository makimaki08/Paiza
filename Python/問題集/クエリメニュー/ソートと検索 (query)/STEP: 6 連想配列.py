student_num,attendance_num = map(int, input().split())
student_arr = {(x, y) for x, y in [input().split() for _ in range(student_num)]}

for _ in range(attendance_num):
	input_line = input()
	for num, ID in student_arr:
		if num == input_line:
			print(ID)