import numpy as np
H, W, N = map(int, input().split())
box = np.array([list(map(int, input().split())) for _ in range(H)])
box = np.pad(box, ((1, 0), (1, 0)))

for _ in range(N):
	min_y, min_x, max_y, max_x = map(int, input().split())
	max_y+=1
	max_x+=1
	print(np.sum(box[min_y:max_y,min_x:max_x]))

# https://paiza.jp/works/mondai/reviews/show/f98621fac444f9b894195e0967def4de