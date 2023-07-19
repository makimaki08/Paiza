height, width = [int(x) for x in input().split()]
pazz_arr = []

for _ in range(height):
	pazz_arr.append(list(input()))
cur_h = 0
cur_w = 0

for h in range(height):
	for w in range(width):
		if(pazz_arr[h][w] == "S"):
			cur_h = h
			cur_w = w


output_line = "NO"
while True:
	# 高さと横が、1~上限内である場合
	if(0<cur_h<height-1 and 0<cur_w<width-1):
		# 通過ずみではない場合
		if(pazz_arr[cur_h][cur_w] != "P"):
			# 通過した箇所は、PassのPを追記
			pazz_arr[cur_h][cur_w] = "P"

			# 上に移動する→"・"であれば、移動してcur_h,cur_wを変更
			if(pazz_arr[cur_h-1][cur_w] == "."):
				cur_h -= 1

			# 右に移動する→"・"であれば、移動してcur_h,cur_wを変更
			elif(pazz_arr[cur_h][cur_w+1] == "."):
				cur_w += 1

			# 左に移動する→"・"であれば、移動してcur_h,cur_wを変更
			elif(pazz_arr[cur_h][cur_w-1] == "."):
				cur_w -= 1

			# 下に移動する→"・"であれば、移動してcur_h,cur_wを変更
			elif(pazz_arr[cur_h+1][cur_w] == "."):
				cur_h += 1


		# 全てが通過ずみの場合
		else:
			break

	# 高さと横が、1~上限内ではない場合->出口発見！
	else:
		output_line = "YES"
		break




# print(pazz_arr[5])
# print(cur_h, cur_w)

# for pazz in pazz_arr:
# 	print(pazz)
print(output_line)