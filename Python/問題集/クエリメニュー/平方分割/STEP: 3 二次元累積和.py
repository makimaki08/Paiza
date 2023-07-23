import numpy as np
H, W, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(H)]
box = np.pad(box, ((1, 0), (1, 0)))

for n in range(N):
	y, x = map(int, input().split())
	print(np.sum(box[:y+1,:x+1]))