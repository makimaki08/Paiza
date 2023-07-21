student_num, event_num, paiza = map(int, input().split())
student_arr = [paiza]
for _ in range(student_num):
	student_arr.append(int(input()))

for i in range(event_num):
	input_arr = input().split()
	if(input_arr[0] == "join"):
		student_arr.append(int(input_arr[1]))

	elif(input_arr[0] == "sorting"):
		student_arr.sort()
		for j in range(len(student_arr)):
			if(student_arr[j] == paiza):
				print(j+1)