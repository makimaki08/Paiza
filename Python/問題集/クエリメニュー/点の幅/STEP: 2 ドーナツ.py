import numpy as np
def calc_circle(y,x,value):
	top = y - value
	bottom = y + value
	left = x - value
	right = x + value
	return top,bottom,left,right


H, W, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(H)]
box = np.pad(box, ((1, 0), (1, 0)))
# print(box)

for n in range(N):
	y, x, b, s = map(int, input().split())
	in_top, in_bottom, in_left, in_right = calc_circle(y,x,b//2)
	out_top, out_bottom, out_left, out_right = calc_circle(y,x,s//2)
	in_circle_sum = np.sum(box[in_top:in_bottom+1,in_left:in_right+1])
	out_circle_sum = np.sum(box[out_top:out_bottom+1,out_left:out_right+1])
	print(in_circle_sum - out_circle_sum)
