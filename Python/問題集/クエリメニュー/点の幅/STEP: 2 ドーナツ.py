import numpy as np
H, W, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(H)]
print(box)
np.pad(box, ((1, 0), (1, 0)))

for n in range(N):
	y, x, b, s = map(int, input().split())
	print(y, x, b, s)