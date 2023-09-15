N = int(input())
input_line = list(map(int, input().split()))
# print(input_line)

pre_vacation = 0
pre_day_of_week = 0
sum_work_day = 0

for i in range(N):
	if input_line[i]==0:
		pre_vacation = i

	if i+1<7:
		sum_work_day+=1
	else:
		diff_vacation = i - pre_vacation
		if diff_vacation>=7:
			sum_work_day=0
		else:
			sum_work_day+=1

print(sum_work_day)
