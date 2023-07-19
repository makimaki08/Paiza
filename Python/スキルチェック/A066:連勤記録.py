jobs = int(input())

input_arr = [] # 出勤回数を記録
max_num = 0
for _ in range(jobs):
	input_arr.append([int(x)-1 for x in input().split()])


for x,y in input_arr:
	if(max_num<y):
		max_num = y + 1

schedule_arr = [[0]*max_num]*jobs
for j in range(jobs):
	start_day = input_arr[j][0]
	end_day = input_arr[j][1]
	for n in range(max_num):
		# print(n, start_day, end_day, start_day<=n, n<=end_day, start_day<=n and n<=end_day)
		if(start_day<=n and n<=end_day):
			schedule_arr[j][n] = 1
		else:
			schedule_arr[j][n] = 0
	# for n in range(start_day,end_day):
	# 	print(n, start_day, end_day, start_day<=n, n<=end_day)
	# 	schedule_arr[j][n] = 1

for schedule in schedule_arr:
	print(schedule)

# 0 0 3 True True True
# 1 0 3 True True True
# 2 0 3 True True True
# 3 0 3 True True True
# 4 0 3 True False False
# 5 0 3 True False False
# 6 0 3 True False False
# 0 4 6 False True False
# 1 4 6 False True False
# 2 4 6 False True False
# 3 4 6 False True False
# 4 4 6 True True True
# 5 4 6 True True True
# 6 4 6 True True True
# [0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0]

