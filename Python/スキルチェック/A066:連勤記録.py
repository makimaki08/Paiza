jobs = int(input())

input_arr = [] # 出勤回数を記録
max_num = 0
for _ in range(jobs):
	input_arr.append([int(x)-1 for x in input().split()])


for x,y in input_arr:
	if(max_num<y):
		max_num = y

schedule_arr = [[0]*max_num]*jobs
for j in range(jobs):
	start_day = input_arr[j][0]
	end_day = input_arr[j][1]
	for n in range(max_num):
		if(start_day<=n and n<=end_day)
		schedule_arr[j][n] = 1

for schedule in schedule_arr:
	print(schedule)