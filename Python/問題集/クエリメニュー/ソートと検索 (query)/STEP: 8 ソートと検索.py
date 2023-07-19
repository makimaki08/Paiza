students = []
student_num, x, paiza = map(int, input().split())
for _ in range(student_num):
	students.append(int(input()))

students.append(x)
students.append(paiza)
students.sort()

count = 0

for student in students:
	count+=1
	if(student == paiza):
		break


print(count)