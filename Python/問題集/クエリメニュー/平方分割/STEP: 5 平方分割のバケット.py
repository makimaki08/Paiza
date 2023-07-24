import numpy as np
N = 10000
sqrt_N = np.sqrt(N)
A = np.array([int(input()) for _ in range(N)])
A = np.split(A, sqrt_N)

for a in A:
	print(max(a))
