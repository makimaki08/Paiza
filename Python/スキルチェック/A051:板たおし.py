def get_min_w(cur_w):
	if(cur_w - 1 < 0):
		return 0
	else:
		return cur_w - 1

def get_max_w(cur_w, width):
	if(cur_w + 2 >= width):
		return width
	else:
		return cur_w + 2



height, width = [int(x) for x in input().split()]
input_arr = []
for h in range(height):
	input_arr.append([int(x) for x in input().split()])

max_x = max(input_arr[0])
cur_w = 0
min_width = 0
max_width = width
for w in range(width):
	if(max_x == input_arr[0][w]):
		cur_w = w
		min_width = get_min_w(cur_w)
		max_width = get_max_w(cur_w, width)
score = 0
# print("max_x, cur_w, min_width, max_width")
# print(max_x, cur_w, min_width, max_width)

for h in range(height):
	for w in range(min_width,max_width):
		max_x = max(input_arr[h][min_width:max_width])
		if(max_x == input_arr[h][w]):
			score += input_arr[h][w]
			cur_w = w
			min_width = get_min_w(cur_w)
			max_width = get_max_w(cur_w, width)
			break

	# print("score, max_x, cur_w, min_width, max_width")
	# print(score, max_x, cur_w, min_width, max_width)

print(score)


