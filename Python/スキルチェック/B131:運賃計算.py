n,m = map(int, input().split()) # 路線の数を表す整数 N と、駅の数を表す整数 M 

# 路線の交通費を格納する配列
station_arr = []
for i in range(n):
	# 路線とその交通費を追加
	station_arr.append([int(x) for x in input().split()])

station_count = int(input())
total_fare = 0
cur_row = 0
cur_column = 0
for _ in range(station_count):
	input_arr = [int(x) for x in input().split()]
	tar_row = input_arr[0] - 1
	tar_column = input_arr[1] - 1
	# 同じ路線の場合
	if(cur_row==tar_row):
		total_fare += abs(station_arr[tar_row][tar_column] - station_arr[cur_row][cur_column])

	# 異なる路線の場合
	else:
		total_fare += abs(station_arr[tar_row][tar_column] - station_arr[tar_row][cur_column])

	cur_row = tar_row
	cur_column = tar_column

print(total_fare)
