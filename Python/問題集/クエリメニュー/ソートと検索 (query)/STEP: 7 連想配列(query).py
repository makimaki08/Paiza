student_num,event_num = map(int, input().split())
students = {}

for i in range(student_num):
	input_arr = input().split()
	students[int(input_arr[0])] = input_arr[1]

for j in range(event_num):
	input_arr = input().split()
	command = input_arr[0]
	if(command == "join"):
		students[int(input_arr[1])] = input_arr[2]

	elif(command == "leave"):
		students.pop(int(input_arr[1]))

	elif(command == "call"):
		print(students.get(int(input_arr[1])))